# NotebookLM Automation

Automate NotebookLM note generation from YouTube videos and playlists using Playwright.

## Features

- Supports both single YouTube videos and playlists
- Automatically imports videos into NotebookLM
- Waits for NotebookLM to generate the source summary
- Sends a custom prompt automatically
- Copies the generated response
- Saves notes as Markdown files
- Automatically skips videos whose notes already exist
- Restarts the browser periodically for long playlists
- Deletes temporary notebooks after processing
- Configurable through `config.py`
- Detailed logging

---

## Project Structure

```
NotebookLM-Automation/
│
├── main.py
├── config.py
├── prompt.txt
├── requirements.txt
├── README.md
├── LICENSE
│
├── output/
├── logs/
└── playwright-profile/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/jain-sahil-35/NotebookLM-Automation.git
cd NotebookLM-Automation
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

## Usage

1. Login to NotebookLM once.
2. Paste a YouTube video or playlist URL into your clipboard.
3. Configure your prompt in `prompt.txt`.
4. Run

```bash
python main.py
```

The generated notes will be saved as Markdown files inside the `output` directory.

---

## Configuration

Most settings can be modified in `config.py`.

Examples include:

- Browser restart interval
- Output directory
- NotebookLM URL
- Logging configuration

---

## Output

Generated notes are saved as

```
output/
    Video Title.md
```

which can be directly opened in Obsidian or any Markdown editor.

---

## Current Features

- Single video support
- Playlist support
- Resume interrupted playlists
- Automatic notebook cleanup
- Browser restart for long playlists
- Markdown export
- Logging

---

## Future Improvements

- Parallel processing
- Automatic folder organization
- GUI version
- PDF export
- CLI arguments
- Docker support

---

## License

MIT License