OctoFit Tracker — Project scaffold

Structure

octofit-tracker/
├── backend/
│   ├── venv/ (Python virtual environment - not committed)
│   └── requirements.txt
└── frontend/

Setup (recommended)

1. Create a Python virtual environment and activate it:

```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
```

2. Install backend dependencies:

```bash
pip install -r octofit-tracker/backend/requirements.txt
```

Ports used by this project (forwarding suggested in devcontainer):
- `8000` (public) — Django dev server
- `3000` (public) — Frontend dev server
- `27017` (private) — MongoDB

Notes
- The `backend/venv` directory is intentionally ignored by `.gitignore`.
- Use Django's ORM for DB operations where possible, per project guidelines.
