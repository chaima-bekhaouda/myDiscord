import tkinter as tk
from tkinter import ttk
import sqlite3

def create_database():
    # Connectez-vous à la base de données SQLite, si elle n'existe pas, elle sera créée
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


def show_frame(frame):
    # Cacher tous les cadres
    for f in (welcome_frame, login_frame, registration_frame):
        f.pack_forget()
    # Afficher le cadre demandé
    frame.pack(fill="both", expand=True)


def create_welcome_frame(parent):
    welcome_frame = ttk.Frame(parent)
    ttk.Label(welcome_frame, text="Bienvenue sur MyDiscord!", font=("Arial", 16)).pack(pady=20)

    # Créer un conteneur pour les boutons
    button_container = ttk.Frame(welcome_frame)
    button_container.pack(pady=10)

    # Pack les boutons dans le conteneur avec un espacement uniforme
    ttk.Button(button_container, text="Se connecter", command=lambda: show_frame(login_frame)).pack(side=tk.LEFT,
                                                                                                    padx=10)
    ttk.Button(button_container, text="S'inscrire", command=lambda: show_frame(registration_frame)).pack(side=tk.LEFT,
                                                                                                         padx=10)

    return welcome_frame


def create_login_frame(parent):
    login_frame = ttk.Frame(parent)
    ttk.Label(login_frame, text="Connexion", font=("Arial", 16)).pack(pady=10)
    ttk.Label(login_frame, text="Email/Nom d'utilisateur").pack()
    ttk.Entry(login_frame).pack()  # Champ Email/Nom d'utilisateur
    ttk.Label(login_frame, text="Mot de passe").pack()
    ttk.Entry(login_frame, show="*").pack()  # Champ mot de passe
    ttk.Button(login_frame, text="Connexion").pack(pady=10)
    ttk.Button(login_frame, text="Retour", command=lambda: show_frame(welcome_frame)).pack(pady=10)
    return login_frame


def create_registration_frame(parent):
    registration_frame = ttk.Frame(parent)
    ttk.Label(registration_frame, text="Inscription", font=("Arial", 16)).pack(pady=10)
    ttk.Label(registration_frame, text="Nom d'utilisateur").pack()
    ttk.Entry(registration_frame).pack()  # Champ Nom d'utilisateur
    ttk.Label(registration_frame, text="Email").pack()
    ttk.Entry(registration_frame).pack()  # Champ Email
    ttk.Label(registration_frame, text="Mot de passe").pack()
    ttk.Entry(registration_frame, show="*").pack()  # Champ mot de passe
    ttk.Label(registration_frame, text="Confirmer le mot de passe").pack()
    ttk.Entry(registration_frame, show="*").pack()  # Champ de confirmation du mot de passe
    ttk.Button(registration_frame, text="Inscription").pack(pady=10)
    ttk.Button(registration_frame, text="Retour", command=lambda: show_frame(welcome_frame)).pack(pady=10)
    return registration_frame


def main():
    root = tk.Tk()
    root.title("MyDiscord")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width // 2}x{screen_height // 2}")

    global welcome_frame, login_frame, registration_frame

    # Creation des cadres
    welcome_frame = create_welcome_frame(root)
    login_frame = create_login_frame(root)
    registration_frame = create_registration_frame(root)

    # Afficher initialement le cadre de bienvenue
    show_frame(welcome_frame)

    root.mainloop()


if __name__ == "__main__":
    create_database()
    main()
