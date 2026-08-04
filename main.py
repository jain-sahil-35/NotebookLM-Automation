import os
import time
from playwright.sync_api import sync_playwright
import pyperclip
from yt_dlp import YoutubeDL
import re
import config
import logging

os.makedirs(config.LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(f"{config.LOG_DIR}/run.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def launch_browser(playwright):
    context = playwright.firefox.launch_persistent_context(
        user_data_dir=config.USER_DATA_DIR,
        headless=config.HEADLESS
    )

    page = context.pages[0] if context.pages else context.new_page()

    open_notebooklm(page)

    return context, page

def load_prompt() -> str:
    """Load the NotebookLM prompt from prompt.txt."""
    with open("prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

def get_playlist_videos(url):
    ydl_opts = {
        **config.BASE_YDL_OPTS,
        "extract_flat": True
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    videos = []

    for entry in info.get("entries", []):

        if entry is None:
            continue

        videos.append({
            "url": f"https://www.youtube.com/watch?v={entry['id']}",
            "title": entry.get("title", "Unknown Title")
        })
    
    return videos

def is_playlist(url):
    ydl_opts = {
        **config.BASE_YDL_OPTS,
        "extract_flat": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return "entries" in info

def open_notebooklm(page):
    page.goto(config.NOTEBOOKLM_URL)
    page.wait_for_load_state("domcontentloaded")

def create_notebook(page):
    logger.info("Creating a new notebook...")
    create_card = page.get_by_label("Create new notebook")
    create_card.wait_for(state="visible")
    create_card.click()

def import_youtube(page, url):
    logger.info("Importing YouTube video...")
    dialog = page.get_by_role("dialog", name="Create Audio and Video")
    dialog.wait_for()
    search_box = dialog.get_by_placeholder("Search the web for new sources")
    search_box.fill(url)
    search_box.press("Enter")

def wait_for_summary(page):
    logger.info("Waiting for summary...")
    summary_ready = page.get_by_role("button", name="Good summary")
    summary_ready.wait_for()
    logger.info("✅ Summary generated!")

def send_prompt(page, prompt):
    logger.info("Generating notes...")
    chat_box = page.get_by_role("textbox", name="Query box")
    chat_box.fill(prompt)
    chat_box.press("Enter")

def wait_for_response(page):

    logger.info("Waiting for NotebookLM...")

    copy_button = page.get_by_role(
        "button",
        name=re.compile("Copy model response")
    )

    copy_button.wait_for(state="visible", timeout=600000)

    while not copy_button.is_enabled():
        time.sleep(1)

    stable = 0
    previous = ""

    while stable < config.STABLE_COUNT:

        current = ""

        # Retry copying up to 3 times
        for _ in range(3):
            copy_button.click()
            time.sleep(config.CLIPBOARD_WAIT)

            current = pyperclip.paste().strip()

            if current:
                break

        if current and current == previous:
            stable += 1
        else:
            stable = 0
            previous = current

        time.sleep(config.STABLE_WAIT)

    return current

def get_video_title(url) -> str:
    ydl_opts = {
        **config.BASE_YDL_OPTS,
        "no_warnings": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get('title', 'Unknown Title')

def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', '-', name)
    name = re.sub(r"\s+", " ", name)
    return name.strip()

def save_notes(notes, title):
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)

    title = sanitize_filename(title)

    with open(f"{config.OUTPUT_DIR}/{title}.md", "w", encoding="utf-8") as f:
        f.write(notes)

    logger.info(f"✅ Saved: {title}.md")

def delete_notebook(page):

    logger.info("Returning to homepage...")

    page.goto(config.NOTEBOOKLM_URL)
    page.wait_for_load_state("domcontentloaded")

    logger.info("Waiting for notebook list...")

    page.get_by_role(
        "button",
        name="Project Actions Menu"
    ).wait_for(timeout=60000)

    logger.info("Deleting notebook...")

    page.get_by_role(
        "button",
        name="Project Actions Menu"
    ).click()

    page.get_by_role(
        "menuitem",
        name="Delete"
    ).click()

    page.get_by_role(
        "button",
        name="Delete"
    ).click()

    page.get_by_label(
        "Create new notebook"
    ).wait_for(timeout=60000)

    logger.info("✅ Notebook deleted.")

def process_video(url, title, page, prompt):
    create_notebook(page)
    import_youtube(page, url)
    wait_for_summary(page)
    time.sleep(config.SUMMARY_WAIT)
    send_prompt(page, prompt)
    notes = wait_for_response(page)
    save_notes(notes, title)
    delete_notebook(page)
    logger.info(f"Finished: {title}")

def note_exists(title: str) -> bool:
    title = sanitize_filename(title)
    path = os.path.join(config.OUTPUT_DIR, f"{title}.md")
    return os.path.exists(path)

def main():

    url = pyperclip.paste().strip()

    if not url.startswith("https://"):
        logger.error("Clipboard doesn't contain a valid URL.")
        return

    prompt = load_prompt()

    with sync_playwright() as p:

        context, page = launch_browser(p)

        if is_playlist(url):
        
            playlist = get_playlist_videos(url)
    
            logger.info(f"Found {len(playlist)} videos.")

            processed = 0
    
            for i, video in enumerate(playlist, start=1):
                logger.info(f"\n[{i}/{len(playlist)}] {video['title']}")

                if note_exists(video["title"]):
                    logger.info(f"⏭ Skipping: {video['title']}")
                    continue

                try:
                    process_video(
                        video["url"],
                        video["title"],
                        page,
                        prompt
                    )

                    processed += 1

                    if processed % config.RESTART_INTERVAL == 0:
                        logger.info(
                            f"Restarting browser after {processed} processed videos..."
                        )

                        context.close()

                        context, page = launch_browser(p)

                except Exception as e:
                    logger.error(f"❌ Failed: {video['title']}")
                    logger.exception(e)
                    continue
        
        else:
    
            title = get_video_title(url)
            if note_exists(title):
                logger.info(f"⏭ Skipping: {title}")
            else:
                process_video(url, title, page, prompt)

        context.close()

if __name__ == "__main__":
    main()