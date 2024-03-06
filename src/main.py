import tkinter as tk

from frames import Frames
from src.database import create_database


def main():
    root = tk.Tk()
    root.title("MyDiscord")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width // 2}x{screen_height // 2}")

    frames = Frames(root)

    # Afficher initialement le cadre de bienvenue
    frames.show_frame(frames.welcome_frame)

    root.mainloop()


if __name__ == "__main__":
    create_database()
    main()
