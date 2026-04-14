import sqlite3
import os
from kivy.app import App


def get_db_path():
    return os.path.join(App.get_running_app().user_data_dir, "scorecard.db")


def get_connection():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row  # allows dict-like access
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS events (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            date        TEXT NOT NULL,
            location    TEXT,
            notes       TEXT,
            created_at  TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS boards (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id    INTEGER NOT NULL,
            board_num   INTEGER NOT NULL,
            opps        TEXT,
            contract    TEXT,
            lead        TEXT,
            result      TEXT,
            score       INTEGER,
            notes       TEXT,
            created_at  TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (event_id) REFERENCES events(id)
        );
    """)

    conn.commit()
    conn.close()


# --- Event queries ---


def create_event(name, date, location="", notes=""):
    conn = get_connection()
    conn.execute(
        "INSERT INTO events (name, date, location, notes) VALUES (?, ?, ?, ?)",
        (name, date, location, notes),
    )
    conn.commit()
    conn.close()


def get_events():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM events ORDER BY date DESC").fetchall()
    conn.close()
    return rows


def get_event(event_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    conn.close()
    return row


def update_event(event_id, name, date, location="", notes=""):
    conn = get_connection()
    conn.execute(
        "UPDATE events SET name=?, date=?, location=?, notes=? WHERE id=?",
        (name, date, location, notes, event_id),
    )
    conn.commit()
    conn.close()


def delete_event(event_id):
    conn = get_connection()
    conn.execute("DELETE FROM boards WHERE event_id=?", (event_id,))
    conn.execute("DELETE FROM events WHERE id=?", (event_id,))
    conn.commit()
    conn.close()


# --- Board queries ---


def create_board(
    event_id, board_num, opps="", contract="", lead="", result="", notes=""
):
    conn = get_connection()
    conn.execute(
        "INSERT INTO boards (event_id, board_num, opps, contract, lead, result, notes) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (event_id, board_num, opps, contract, lead, result, notes),
    )
    conn.commit()
    conn.close()


def get_boards(event_id):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM boards WHERE event_id=? ORDER BY board_num", (event_id,)
    ).fetchall()
    conn.close()
    return rows


def get_board(board_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM boards WHERE id=?", (board_id,)).fetchone()
    conn.close()
    return row


def update_board(
    board_id, board_num, opps="", contract="", lead="", result="", notes=""
):
    conn = get_connection()
    conn.execute(
        "UPDATE boards SET board_num=?, opps=?, contract=?, lead=?, result=?, notes=? WHERE id=?",
        (board_num, opps, contract, lead, result, notes, board_id),
    )
    conn.commit()
    conn.close()


def delete_board(board_id):
    conn = get_connection()
    conn.execute("DELETE FROM boards WHERE id=?", (board_id,))
    conn.commit()
    conn.close()
