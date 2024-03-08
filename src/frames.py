import random
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk

from src.database import create_user, get_channels, get_messages, add_message, get_username
from src.validator import Validator


class Frames:
    def __init__(self, root):
        self.root = root
        # Initialize frame components
        self.username = None
        self.main_frame = None
        self.channel_list = None
        self.logout_button = None
        self.message_scrollbar = None
        self.channel_scrollbar = None
        self.message_area = None
        self.message_container = None
        self.message_entry = None
        self.send_button = None

        # Create initial frames
        self.login_frame = self.create_login_frame()
        self.registration_frame = self.create_registration_frame()
        self.welcome_frame = self.create_welcome_frame()

    # Hide all frames and show the specified one
    def show_frame(self, frame):
        for f in (self.welcome_frame, self.login_frame, self.registration_frame):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    # Create and return the welcome frame
    def create_welcome_frame(self):
        # Create a new frame for the welcome screen
        welcome_frame = ttk.Frame(self.root)

        # Add a welcome label to the frame
        ttk.Label(welcome_frame, text="Bienvenue sur MyDiscord!", font=("Helvetica", 16)).pack(pady=20)

        # Create a container for the buttons
        button_container = ttk.Frame(welcome_frame)
        button_container.pack(pady=10)

        # Add a login button to the button container
        ttk.Button(button_container, text="Se connecter",
                   command=lambda: self.show_frame(self.login_frame)).pack(side=tk.LEFT, padx=10)

        # Add a registration button to the button container
        ttk.Button(button_container, text="S'inscrire",
                   command=lambda: self.show_frame(self.registration_frame)).pack(side=tk.LEFT, padx=10)

        # Get the available themes
        available_themes = self.root.get_themes()

        # Create a variable to hold the selected theme
        theme_var = tk.StringVar()
        theme_var.set(available_themes[0])

        # Create a dropdown menu for the themes
        theme_dropdown = ttk.Combobox(welcome_frame, textvariable=theme_var, values=available_themes)
        theme_dropdown.pack(pady=10)

        # Add a button to change the theme
        theme_button = ttk.Button(welcome_frame, text="Changer le thème",
                                  command=lambda: self.root.set_theme(theme_var.get()))
        theme_button.pack(pady=10)

        # Return the completed welcome frame
        return welcome_frame

    # Change the theme of the root window
    def change_theme(self):
        # Get the list of available themes
        available_themes = self.root.get_themes()

        # Randomly select a theme from the list
        selected_theme = random.choice(available_themes)

        # Apply the selected theme to the root window
        self.root.set_theme(selected_theme)

    # Create and return the login frame
    def create_login_frame(self):
        # Create a new frame for the login screen
        login_frame = ttk.Frame(self.root)

        # Add a title label to the frame
        ttk.Label(login_frame, text="Connexion", font=("Arial", 16)).pack(pady=10)

        # Add a label and entry for the username
        ttk.Label(login_frame, text="Email/Nom d'utilisateur").pack()
        username_entry = ttk.Entry(login_frame)
        username_entry.pack()

        # Add a label and entry for the password
        ttk.Label(login_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(login_frame, show="*")
        password_entry.pack()

        # Add a login button that calls the login method with the entered username and password
        ttk.Button(login_frame, text="Connexion",
                   command=lambda: self.login(username_entry.get(), password_entry.get())).pack(pady=10)

        # Add a back button that shows the welcome frame
        ttk.Button(login_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)

        # Return the completed login frame
        return login_frame

    # Create and return the registration frame
    def create_registration_frame(self):
        # Create a new frame for the registration screen
        registration_frame = ttk.Frame(self.root)

        # Add a title label to the frame
        ttk.Label(registration_frame, text="Inscription", font=("Arial", 16)).pack(pady=10)

        # Add a label and entry for the username
        ttk.Label(registration_frame, text="Nom d'utilisateur").pack()
        username_entry = ttk.Entry(registration_frame)
        username_entry.pack()

        # Add a label and entry for the email
        ttk.Label(registration_frame, text="Email").pack()
        email_entry = ttk.Entry(registration_frame)
        email_entry.pack()

        # Add a label and entry for the password
        ttk.Label(registration_frame, text="Mot de passe").pack()
        password_entry = ttk.Entry(registration_frame, show="*")
        password_entry.pack()

        # Add a label and entry for the password confirmation
        ttk.Label(registration_frame, text="Confirmer le mot de passe").pack()
        confirm_password_entry = ttk.Entry(registration_frame, show="*")
        confirm_password_entry.pack()

        # Add a registration button that calls the register method with the entered details
        ttk.Button(registration_frame, text="Inscription",
                   command=lambda: self.register(username_entry.get(), email_entry.get(), password_entry.get(),
                                                 confirm_password_entry.get())).pack(pady=10)

        # Add a back button that shows the welcome frame
        ttk.Button(registration_frame, text="Retour",
                   command=lambda: self.show_frame(self.welcome_frame)).pack(pady=10)

        # Return the completed registration frame
        return registration_frame

    # Validate registration and create user if valid
    def register(self, username, email, password, confirm_password):
        # Validate the registration details
        if not Validator.validate_registration(username, email, password, confirm_password):
            return

        # If validation is successful, create a new user
        create_user(username, email, password)

        # Show a success message to the user
        msgbox.showinfo("Succès", "Inscription réussie. Vous pouvez maintenant vous connecter.")

        # Show the login frame
        self.show_frame(self.login_frame)

    # Validate login and create main frame if valid
    def login(self, identifier, password):
        # Validate the login details
        if not Validator.validate_login(identifier, password):
            return

        # If validation is successful, get the username
        self.username = get_username(identifier)

        # Hide the root window
        self.root.withdraw()

        # Create the main frame
        self.create_main_frame()

    # Create the main frame after successful login
    def create_main_frame(self):
        # Create a new top-level window for the main frame
        self.main_frame = tk.Toplevel(self.root)
        self.main_frame.title("MyDiscord")

        # Add a logout button to the main frame
        self.logout_button = ttk.Button(self.main_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side=tk.BOTTOM)

        # Add a scrollbar for the channel list
        self.channel_scrollbar = ttk.Scrollbar(self.main_frame)
        self.channel_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Create a treeview for the channel list
        self.channel_list = ttk.Treeview(self.main_frame, yscrollcommand=self.channel_scrollbar.set)
        self.channel_list.pack(side=tk.LEFT, fill=tk.BOTH)

        # Get the list of channels and add them to the treeview
        channels = get_channels()
        for channel in channels:
            self.channel_list.insert('', 'end', text=channel[1], values=(channel[0], channel[2]))

        # Bind the treeview selection event to the select_channel method
        self.channel_list.bind('<<TreeviewSelect>>',
                               lambda event: self.select_channel(self.channel_list.selection()[0]))

        # Configure the channel scrollbar to scroll the channel list
        self.channel_scrollbar.config(command=self.channel_list.yview)

        # Add a scrollbar for the message area
        self.message_scrollbar = ttk.Scrollbar(self.main_frame)
        self.message_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a text widget for the message area
        self.message_area = tk.Text(self.main_frame, bg="white", yscrollcommand=self.message_scrollbar.set)
        self.message_area.pack(side=tk.TOP, fill=tk.BOTH)
        self.message_area.config(state=tk.DISABLED)

        # Configure the message scrollbar to scroll the message area
        self.message_scrollbar.config(command=self.message_area.yview)

        # Create a container for the message entry and send button
        self.message_container = ttk.Frame(self.main_frame)
        self.message_container.pack(side=tk.BOTTOM, fill=tk.X)

        # Add a text entry for the message
        self.message_entry = ttk.Entry(self.message_container)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.message_entry.bind('<Return>', lambda event: self.send_message(self.message_entry.get()))

        # Add a send button that calls the send_message method with the entered message
        self.send_button = ttk.Button(self.message_container, text="SEND",
                                      command=lambda: self.send_message(self.message_entry.get()))
        self.send_button.pack(side=tk.RIGHT)

    # Destroy main frame and show welcome frame
    def logout(self):
        # Destroy the main frame
        self.main_frame.destroy()

        # Show the root window
        self.root.deiconify()

        # Show the welcome frame
        self.show_frame(self.welcome_frame)

    # Fetch and display messages for the selected channel
    def select_channel(self, channel):
        # Get the ID of the selected channel
        channel_id = self.channel_list.item(channel)['values'][0]

        # Get the messages for the selected channel
        messages = get_messages(channel_id)

        # Enable the message area and clear its contents
        self.message_area.config(state=tk.NORMAL)
        self.message_area.delete('1.0', tk.END)

        # Configure the message area tags for user and other messages
        self.message_area.tag_configure("user", justify='right', background='light blue')
        self.message_area.tag_configure("other", justify='left', background='grey')

        # Insert the messages into the message area
        for message in messages:
            message_id, username, message_text, timestamp = message
            formatted_message = f"{timestamp} - {username}: {message_text}\n"
            if username == self.username:
                self.message_area.insert(tk.END, formatted_message, "user")
            else:
                self.message_area.insert(tk.END, formatted_message, "other")

        # Disable the message area
        self.message_area.config(state=tk.DISABLED)

    # Send a message to the selected channel
    def send_message(self, message):
        # Get the selected channel
        selected_channel = self.channel_list.selection()

        # Show an error if no channel is selected
        if not selected_channel:
            msgbox.showerror("Erreur", "Veuillez sélectionner un channel avant d'envoyer un message.")
            return

        # Show an error if the message is empty
        if not message.strip():
            msgbox.showerror("Erreur", "Le message ne peut pas être vide.")
            return

        # Get the ID of the selected channel
        channel_id = self.channel_list.item(selected_channel[0])['values'][0]

        # Add the message to the selected channel
        add_message(self.username, channel_id, message)

        # Insert the message into the message area
        self.message_area.insert(tk.END, message + '\n')

        # Clear the message entry
        self.message_entry.delete(0, tk.END)

        # Refresh the selected channel
        self.select_channel(selected_channel[0])
