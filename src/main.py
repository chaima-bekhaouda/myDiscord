from ttkthemes import ThemedTk
from src.database import create_database
from src.frames import Frames

def main():
    # Initialize main window with a theme
    root = ThemedTk(theme="arc", background=True, themebg=True)
    root.title("MyDiscord")

    # Get screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set main window size to half of the screen size
    root.geometry(f"{screen_width // 2}x{screen_height // 2}")

    # Initialize frames
    frames = Frames(root)

    # Display welcome frame
    frames.show_frame(frames.welcome_frame)

    # Start application loop
    root.mainloop()

# Program entry point
if __name__ == "__main__":
    # Create database
    create_database()
    # Run main function
    main()