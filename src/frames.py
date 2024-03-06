import tkinter as tk
from tkinter import ttk


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
                   command=lambda: self.show_frame(self.registration_frame)).pack(
            side=tk.LEFT, padx=10)

        return welcome_frame

    def create_login_frame(self):
        login_frame = ttk.Frame(self.root)
        ttk.Label(login_frame, text="Connexion", font=("Arial", 16)).pack(pady=10)
        ttk.Label(login_frame, text="Email/Nom d'utilisateur").pack()
        ttk.Entry(login_frame).pack()
        ttk.Label(login_frame, text="Mot de passe").pack()
        ttk.Entry(login_frame, show="*").pack()
        ttk.Button(login_frame, text="Connexion").pack(pady=10)
        ttk.Button(login_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(
            pady=10)
        return login_frame

    def create_registration_frame(self):
        registration_frame = ttk.Frame(self.root)
        ttk.Label(registration_frame, text="Inscription", font=("Arial", 16)).pack(pady=10)
        ttk.Label(registration_frame, text="Nom d'utilisateur").pack()
        ttk.Entry(registration_frame).pack()
        ttk.Label(registration_frame, text="Email").pack()
        ttk.Entry(registration_frame).pack()
        ttk.Label(registration_frame, text="Mot de passe").pack()
        ttk.Entry(registration_frame, show="*").pack()
        ttk.Label(registration_frame, text="Confirmer le mot de passe").pack()
        ttk.Entry(registration_frame, show="*").pack()
        ttk.Button(registration_frame, text="Inscription").pack(pady=10)
        ttk.Button(registration_frame, text="Retour", command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)
        return registration_frame
