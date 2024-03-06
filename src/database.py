import sqlite3


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

    # Créez la table des messages
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    # Validez les changements
    conn.commit()

    # Fermez la connexion
    conn.close()


def create_user(username, email, password):
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()


def check_user(identifier, password):
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE (username = ? OR email = ?) AND password = ?", (identifier, identifier, password))
    user = c.fetchone()
    conn.close()
    return user