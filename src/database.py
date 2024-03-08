import sqlite3
import hashlib


def create_database():
    # Connexion ou création de la base de données
    conn = sqlite3.connect('./../database/myDiscord.db')

    # Créez un objet Cursor
    c = conn.cursor()

    # Créez la table des utilisateurs
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Créez la table des channels
    c.execute('''
            CREATE TABLE IF NOT EXISTS channels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')

    # Créez la table des messages
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    # Créez un channel par défaut s'il n'existe pas déjà
    c.execute("INSERT INTO channels (name, user_id) SELECT 'General', NULL WHERE NOT EXISTS(SELECT 1 FROM channels)")

    # Validez les changements
    conn.commit()

    # Fermez la connexion
    conn.close()


def create_user(username, email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
    conn.commit()
    conn.close()


def check_user(identifier, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE (username = ? OR email = ?) AND password = ?",
              (identifier, identifier, hashed_password))
    user = c.fetchone()
    conn.close()
    return user


def get_channels():
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()
    c.execute("SELECT * FROM channels")
    channels = c.fetchall()
    conn.close()
    return channels


def add_channel(name, user_id):
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()
    c.execute("INSERT INTO channels (name, user_id) VALUES (?, ?)", (name, user_id))
    conn.commit()
    conn.close()
