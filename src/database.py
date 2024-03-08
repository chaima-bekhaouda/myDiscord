import sqlite3
import hashlib


def create_database():
    # Connect to the database or create it if it doesn't exist
    conn = sqlite3.connect('./../database/myDiscord.db')

    # Create a cursor object
    c = conn.cursor()

    # Create the users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Create the channels table
    c.execute('''
            CREATE TABLE IF NOT EXISTS channels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')

    # Create the messages table
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            channel_id INTEGER,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(channel_id) REFERENCES channels(id)
        )
    ''')

    # Create a default channel if it doesn't already exist
    c.execute("INSERT INTO channels (name, user_id) SELECT 'General', NULL WHERE NOT EXISTS(SELECT 1 FROM channels)")

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()


def create_user(username, email, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the database
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()

    # Insert the new user into the users table
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()


def check_user(identifier, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the database
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()

    # Select the user from the users table with the given identifier and password
    c.execute("SELECT * FROM users WHERE (username = ? OR email = ?) AND password = ?",
              (identifier, identifier, hashed_password))

    # Fetch the user
    user = c.fetchone()

    # Close the connection
    conn.close()

    # Return the user
    return user


def get_username(identifier):
    # Connect to the database
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()

    # Select the username from the users table with the given identifier
    c.execute("SELECT username FROM users WHERE (username = ? OR email = ?)", (identifier, identifier))

    # Fetch the username
    username = c.fetchone()

    # Close the connection
    conn.close()

    # Return the username
    return username[0]


def get_channels():
    # Connect to the database
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()

    # Select all channels from the channels table
    c.execute("SELECT * FROM channels")

    # Fetch all channels
    channels = c.fetchall()

    # Close the connection
    conn.close()

    # Return the channels
    return channels


def add_channel(name, user_id):
    # Connect to the database
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()

    # Insert the new channel into the channels table
    c.execute("INSERT INTO channels (name, user_id) VALUES (?, ?)", (name, user_id))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()


def get_messages(channel_id):
    # Connect to the database
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()

    # Select all messages from the messages table for the given channel
    c.execute("""
        SELECT messages.id, messages.user_id, messages.message, messages.timestamp
        FROM messages
        WHERE channel_id = ?
    """, (channel_id,))

    # Fetch all messages
    messages = c.fetchall()

    # Close the connection
    conn.close()

    # Return the messages
    return messages


def add_message(user_id, channel_id, message):
    # Connect to the database
    conn = sqlite3.connect('./../database/myDiscord.db')
    c = conn.cursor()

    # Insert the new message into the messages table
    c.execute("INSERT INTO messages (user_id, channel_id, message) VALUES (?, ?, ?)", (user_id, channel_id, message))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
