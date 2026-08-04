# 🚀 NotebookLM Automation

> Automatically generate structured Markdown notes from YouTube videos and playlists using Google NotebookLM.

NotebookLM Automation is a Python-based tool that automates the entire workflow of importing YouTube videos into Google NotebookLM, generating notes using a custom prompt, exporting the response as Markdown, and automatically deleting the created notebook.

The project supports both **single videos** and **entire YouTube playlists**, automatically skips already processed lectures, resumes interrupted runs, and generates notes that are ready to use in **Obsidian** or any Markdown editor.

---

# 🎥 Demo

> 

---

# 📸 Screenshots

## Running the Automation

![Running Automation](assets/Screenshot(75).png)

---

## NotebookLM Generating Notes

![NotebookLM](assets/Screenshot(76).png)

---

## Generated Markdown Notes

![Output Folder](assets/Screenshot(77).png)

---

# ✨ Features

- 📺 Process individual YouTube videos
- 📚 Process complete YouTube playlists
- ⏭ Automatically skip videos whose notes already exist
- 🔄 Resume interrupted playlist processing
- 🤖 Automatically create NotebookLM notebooks
- 📝 Generate notes using a customizable prompt
- 📄 Export notes as Markdown
- 🗑 Automatically delete notebooks after exporting notes
- 📁 Obsidian-compatible Markdown output
- ⚙ Configurable through `config.py`
- 📋 Detailed execution logs
- 🔁 Automatic browser restart after configurable intervals

---

# ⚙️ Requirements

- Python 3.12+
- Firefox
- Node.js
- Playwright
- yt-dlp

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/jain-sahil-35/NotebookLM-Automation.git
cd NotebookLM-Automation
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browser

```bash
playwright install firefox
```

---

# ⚙️ Configuration

Modify the values inside `config.py` according to your preferences.

Example

```python
OUTPUT_DIR = "output"
PLAYWRIGHT_PROFILE = "playwright-profile"
RESTART_INTERVAL = 25
```

You can configure:

- Output directory
- Browser profile
- Restart interval
- Logging settings

---

# 📝 Prompt Customization

The prompt used to generate notes is stored in `prompt.txt`.

Simply edit this file to generate different kinds of notes, such as:

- Revision Notes
- Interview Notes
- Study Notes
- Cheat Sheets
- Flashcards
- Summaries

No code changes are required.

---

# ▶️ Usage

Copy a YouTube video or playlist URL to your clipboard.

Run

```bash
python main.py
```

The automation will automatically:

1. Detect whether the URL is a video or playlist.
2. Open NotebookLM.
3. Create a notebook.
4. Import the YouTube video.
5. Wait for NotebookLM to process the source.
6. Send the prompt.
7. Wait until NotebookLM finishes generating the response.
8. Copy the generated notes.
9. Save them as a Markdown file.
10. Delete the created notebook.
11. Continue with the next lecture (for playlists).

---

# ⚠️ Important Notes

Please read these before running the automation.

## 1. Start with an empty NotebookLM workspace

The automation deletes the notebook it creates after exporting the notes.

If your NotebookLM homepage already contains notebooks, the automation may not be able to reliably identify the notebook it created.

**Recommendation**

- Delete or move existing notebooks before starting.
- Run the automation with an empty NotebookLM homepage.

---

## 2. Do not use your computer while the automation is running

The automation controls Firefox using Playwright.

Any manual interaction can interrupt the workflow.

Examples include:

- Clicking inside Firefox
- Typing on the keyboard
- Switching browser tabs
- Closing browser windows

Doing so may cause:

- Notes not being generated
- Incorrect buttons being clicked
- Incorrect content being copied
- Automation failures

---

## 3. Keep Firefox open

Do not close Firefox while the automation is running.

Closing the browser will terminate the current automation.

---

## 4. Stay logged into NotebookLM

The automation assumes you are already logged into your Google account.

If NotebookLM requests authentication, the automation cannot continue.

---

## 5. Maintain a stable internet connection

NotebookLM processes sources online.

An unstable connection may lead to:

- Import failures
- Longer processing times
- Incomplete responses

---

## 6. Do not modify NotebookLM during execution

Avoid:

- Renaming notebooks
- Deleting notebooks manually
- Opening multiple NotebookLM tabs
- Changing the NotebookLM layout

These actions may interfere with the automation.

---

## 7. Firefox is currently supported

The automation has been tested with Firefox using Playwright.

Support for additional browsers may be added in future releases.

---

## 8. Large playlists may take several hours

NotebookLM processes one lecture at a time.

The automation automatically:

- skips already processed lectures
- resumes interrupted runs
- restarts the browser after a configurable number of videos

---

## 9. NotebookLM interface updates may break the automation

The project relies on Playwright locators.

If Google updates the NotebookLM interface, some locators may need to be updated.

---

# 📂 Project Structure

```
NotebookLM-Automation/
│
├── assets/
├── logs/
├── output/
├── config.py
├── main.py
├── prompt.txt
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📄 Output

Generated notes are saved as Markdown files.

Example

```
output/
│
├── Operating Systems.md
├── Machine Learning.md
├── Computer Networks.md
```

These Markdown files can be opened directly in:

- Obsidian
- VS Code
- Typora
- Any Markdown editor

---

# 🔄 Workflow

```
Clipboard URL
      │
      ▼
Detect Video / Playlist
      │
      ▼
Open NotebookLM
      │
      ▼
Create Notebook
      │
      ▼
Import YouTube Video
      │
      ▼
Wait for Source Processing
      │
      ▼
Send Prompt
      │
      ▼
Generate Notes
      │
      ▼
Copy Response
      │
      ▼
Save Markdown
      │
      ▼
Delete Notebook
      │
      ▼
Next Video
```

---

# 🚧 Known Limitations

- Requires an active Google account logged into NotebookLM.
- Requires Firefox with Playwright.
- NotebookLM interface changes may require locator updates.
- NotebookLM processing speed depends on server load.
- The automation controls the browser and should not be interrupted during execution.

---

# 💡 Future Improvements

- Chrome and Edge support
- Docker support
- Graphical User Interface (GUI)
- Multiple prompt profiles
- Automatic PDF export
- Automatic retry mechanism
- Better notebook identification without requiring an empty workspace

---

# 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# ⭐ Support

If you found this project useful, consider giving it a **Star ⭐** on GitHub.

It helps others discover the project and motivates future development.