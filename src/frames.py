import re
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk

from src.database import create_user, check_user


def validate_registration(username, email, password, confirm_password):
    if password != confirm_password:
        msgbox.showerror("Erreur", "Les mots de passe ne correspondent pas")
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        msgbox.showerror("Erreur", "L'email n'est pas valide")
        return False
    if username.lower() == "admin":
        msgbox.showerror("Erreur", "Le nom d'utilisateur 'admin' n'est pas autorisé")
        return False
    user = check_user(username, password)
    if user:
        user = check_user(email, password)
        if user:
            msgbox.showerror("Erreur", "Un utilisateur avec ce nom d'utilisateur ou email existe déjà")
            return False
    return True


def validate_login(username, password):
    user = check_user(username, password)
    if not user:
        msgbox.showerror("Erreur", "Nom d'utilisateur ou mot de passe invalide")
        return False
    return True


class Frames:
    def __init__(self, root):
        self.root = root
        self.login_frame = self.create_login_frame()
        self.registration_frame = self.create_registration_frame()
        self.welcome_frame = self.create_welcome_frame()

    def show_frame(self, frame):
        # Cacher tous les cadres
        for f in (self.welcome_frame, self.login_frame, self.registration_frame):
            f.pack_forget()
        # Afficher le cadre demandé
        frame.pack(fill="both", expand=True)

    def create_welcome_frame(self):
        welcome_frame = ttk.Frame(self.root)
        ttk.Label(welcome_frame, text="Bienvenue sur MyDiscord!", font=("Arial", 16)).pack(pady=20)

        # Créer un conteneur pour les boutons
        button_container = ttk.Frame(welcome_frame)
        button_container.pack(pady=10)

        # Pack les boutons dans le conteneur avec un espacement uniforme
        ttk.Button(button_container, text="Se connecter",
                   command=lambda: self.show_frame(self.login_frame)).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_container, text="S'inscrire",
                   command=lambda: self.show_frame(self.registration_frame)).pack(side=tk.LEFT, padx=10)

        return welcome_frame

    def create_login_frame(self):
        login_frame = ttk.Frame(self.root)
        ttk.Label(login_frame, text="Connexion", font=("Arial", 16)).pack(pady=10)
        ttk.Label(login_frame, text="Email/Nom d'utilisateur").pack()
        username_entry = ttk.Entry(login_frame)
        username_entry.pack()
        ttk.Label(login_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(login_frame, show="*")
        password_entry.pack()
        ttk.Button(login_frame, text="Connexion",
                   command=lambda: self.login(username_entry.get(), password_entry.get())).pack(pady=10)
        ttk.Button(login_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)
        return login_frame

    def create_registration_frame(self):
        registration_frame = ttk.Frame(self.root)
        ttk.Label(registration_frame, text="Inscription", font=("Arial", 16)).pack(pady=10)
        ttk.Label(registration_frame, text="Nom d'utilisateur").pack()
        username_entry = ttk.Entry(registration_frame)
        username_entry.pack()
        ttk.Label(registration_frame, text="Email").pack()
        email_entry = ttk.Entry(registration_frame)
        email_entry.pack()
        ttk.Label(registration_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(registration_frame, show="*")
        password_entry.pack()
        ttk.Label(registration_frame, text="Confirmer le mot de passe").pack()
        confirm_password_entry = ttk.Entry(registration_frame, show="*")
        confirm_password_entry.pack()
        ttk.Button(registration_frame, text="Inscription",
                   command=lambda: self.register(username_entry.get(), email_entry.get(), password_entry.get(),
                                                 confirm_password_entry.get())).pack(pady=10)
        ttk.Button(registration_frame, text="Retour", command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)
        return registration_frame

    def register(self, username, email, password, confirm_password):
        if not validate_registration(username, email, password, confirm_password):
            return
        create_user(username, email, password)
        msgbox.showinfo("Succès", "Inscription réussie. Vous pouvez maintenant vous connecter.")
        self.show_frame(self.login_frame)

    def login(self, username, password):
        if not validate_login(username, password):
            return
        self.root.withdraw()
        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = tk.Toplevel(self.root)
        self.main_frame.title("MyDiscord")

        self.logout_button = ttk.Button(self.main_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side=tk.BOTTOM)

        self.channel_scrollbar = ttk.Scrollbar(self.main_frame)
        self.channel_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.channel_list = ttk.Treeview(self.main_frame, yscrollcommand=self.channel_scrollbar.set)
        self.channel_list.pack(side=tk.LEFT, fill=tk.BOTH)

        self.channel_scrollbar.config(command=self.channel_list.yview)

        self.message_scrollbar = ttk.Scrollbar(self.main_frame)
        self.message_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_area = tk.Text(self.main_frame, bg="light grey", yscrollcommand=self.message_scrollbar.set)
        self.message_area.pack(side=tk.TOP, fill=tk.BOTH)
        self.message_area.config(state=tk.DISABLED)

        self.message_scrollbar.config(command=self.message_area.yview)

        self.message_container = ttk.Frame(self.main_frame)
        self.message_container.pack(side=tk.BOTTOM, fill=tk.X)

        self.message_entry = ttk.Entry(self.message_container)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.message_entry.bind('<Return>', lambda event: self.send_message(self.message_entry.get()))

        self.send_button = ttk.Button(self.message_container, text="SEND",
                                      command=lambda: self.send_message(self.message_entry.get()))
        self.send_button.pack(side=tk.RIGHT)

    def logout(self):
        self.main_frame.destroy()
        self.root.deiconify()
        self.show_frame(self.welcome_frame)

    def select_channel(self, channel):
        pass

    def send_message(self, message):
        pass
