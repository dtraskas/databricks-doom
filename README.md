# DOOM — Databricks Edition

The classic 1993 id Software first-person shooter running inside a [Databricks App](https://docs.databricks.com/en/dev-tools/databricks-apps/index.html) via [js-dos](https://js-dos.com) — a DOSBox emulator compiled to WebAssembly.

![DOOM Databricks Edition](https://img.shields.io/badge/Databricks-App-FF3621?style=flat&logo=databricks&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat&logo=flask&logoColor=white)

---

## How it works

```
Browser
  └── Flask app (Databricks App runtime)
        └── index.html
              └── js-dos (DOSBox / WebAssembly)
                    └── DOOM.EXE  ← streamed from public CDN
```

The Flask server has a single job: serve the HTML shell. The DOSBox engine (`js-dos-api.js`, `js-dos-v3.js`) is self-hosted as static assets so the app works without any external CDN dependency for the engine itself. The shareware DOOM WAD is fetched directly by the browser from a public CDN at startup.

---

## Prerequisites

- Python 3.9+
- [Databricks CLI](https://docs.databricks.com/en/dev-tools/cli/install.html) (for deployment)
- A Databricks workspace with Apps enabled

---

## Local development

```bash
# Clone the repo
git clone https://github.com/dtraskas/databricks-doom.git
cd databricks-doom

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

Then open [http://localhost:8000](http://localhost:8000) in your browser. DOOM will load automatically.

---

## Deploy to Databricks

```bash
# Authenticate with your workspace
databricks auth login

# Deploy the app
databricks apps deploy
```

The `manifest.yaml` and `app.yaml` in the repo root define the app name, description, and start command — no additional configuration needed.

---

## Controls

| Key | Action |
|-----|--------|
| `W A S D` / Arrow keys | Move |
| `Ctrl` | Fire |
| `Space` | Open / Use |
| `Shift` | Run |
| `Alt` | Strafe |
| `1` – `7` | Switch weapon |
| `Tab` | Automap |
| `Esc` | Menu |

---

## Project structure

```
databricks-doom/
├── app.py              # Flask app — serves the HTML shell
├── app.yaml            # Databricks App start command
├── manifest.yaml       # Databricks App metadata
├── requirements.txt    # Python dependencies
├── static/
│   ├── js-dos-api.js   # js-dos public API (self-hosted)
│   └── js-dos-v3.js    # DOSBox/WebAssembly engine (self-hosted)
└── templates/
    └── index.html      # Game shell + UI chrome
```

---

## Legal

DOOM © 1993 id Software. This project uses the freely distributable shareware. No commercial WAD files are included or distributed.