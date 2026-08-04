# NotebookLM
NOTEBOOKLM_URL = "https://notebooklm.google.com"

# Directories
# OUTPUT_DIR = r"D:\Obsidian\My Vault\100 Days Of Machine Learning"
OUTPUT_DIR = "output"
LOG_DIR = "logs"

# Playwright
USER_DATA_DIR = "playwright-profile"
HEADLESS = False
RESTART_INTERVAL = 25

# Waiting Times (seconds)
SUMMARY_WAIT = 5
CLIPBOARD_WAIT = 1
STABLE_WAIT = 5
STABLE_COUNT = 3

# yt-dlp
BASE_YDL_OPTS = {
    "quiet": True,
    "skip_download": True,
    "cookiesfrombrowser": ("firefox",),
    "js_runtimes": {
        "node": {}
    },
    "remote_components": ["ejs:github"],
}