import json
import uuid
from datetime import datetime
from pathlib import Path
from kivy.app import App


def get_events_path() -> Path:
    data_dir = Path(App.get_running_app().user_data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "events.json"


def load_events() -> list:
    path = get_events_path()
    if not path.exists():
        return []
    with open(path) as f:
        return json.load(f)


def save_events(events: list) -> None:
    with open(get_events_path(), "w") as f:
        json.dump(events, f, indent=2)


def create_event(name: str, date: str, location: str, notes: str) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "date": date,
        "location": location,
        "notes": notes,
        "created_at": datetime.now().isoformat(),
        "boards": [],
    }
