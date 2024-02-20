import tkinter as tk
from tkinter import ttk
from datetime import datetime
from channel import Channel


class Message:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = datetime.now()

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Discord")
        self.root.geometry("1080x720")
        self.root.minsize(480, 360)
        self.root.config(background='#2B2B2B')
        
        self.channels = [Channel("General"), Channel("Gaming"), Channel("Music", is_voice=True)]
        self.current_channel = self.channels[0]  # Default to General channel
        self.users = []

        # Create GUI elements
        self.message_frame = ttk.Frame(self.root)
        self.message_frame.pack(padx=10, pady=10)

        self.message_listbox = tk.Listbox(self.message_frame, width=50, height=20)
        self.message_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.message_scrollbar = ttk.Scrollbar(self.message_frame, orient=tk.VERTICAL, command=self.message_listbox.yview)
        self.message_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message_listbox.config(yscrollcommand=self.message_scrollbar.set)

        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.pack(padx=10, pady=10)

        self.message_entry = ttk.Entry(self.entry_frame, width=40)
        self.message_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.send_button = ttk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        # Populate initial messages
        self.populate_messages()

    def populate_messages(self):
        self.message_listbox.delete(0, tk.END)
        for message in self.current_channel.messages:
            timestamp_str = message.timestamp.strftime("(%H:%M %d/%m/%Y)")
            self.message_listbox.insert(tk.END, f"{message.author} {timestamp_str}")
            self.message_listbox.insert(tk.END, f"{message.content}")

    def send_message(self):
        content = self.message_entry.get()
        if content:
            message = Message("User", content)  # For simplicity, assume all messages are from the same user
            self.current_channel.messages.append(message)
            self.populate_messages()
            self.message_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
