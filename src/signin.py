from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title("Login")
root.geometry("925x500+500+200")
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    file = open("data.txt", "r")
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        welcome_screen = Toplevel(root)
        welcome_screen.title("Welcome")
        welcome_screen.geometry("925x500+500+300")
        welcome_screen.configure(bg="white")

        Label(welcome_screen, text="Welcome", fg="black", bg="white", font=("Arial", 30, "bold")).pack(expand=True)

    else:
        messagebox.showerror("Error", "Invalid username or password")

def signup_command():
    signup_window = Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("925x500+300+200")  # Keeping the same dimensions
    signup_window.configure(bg="#fff")
    signup_window.resizable(False, False)

    def signup():
        username = user.get()
        password = code.get()
        conform_password = conform_code.get()
        email = email_entry.get()
        first_name = first_name_entry.get()
        family_name = family_name_entry.get()

        if password == conform_password:
            try:
                file = open("datasheet.txt", "r+")
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: {"password": password, "email": email, "first_name": first_name, "family_name": family_name}}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open("datasheet.txt", "w")
                w = file.write(str(r))
                messagebox.showinfo("Success", f"Account created successfully. {w}")
                signup_window.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        else:
            messagebox.showerror("Error", "Password does not match")

    def close_signup_window():
        signup_window.destroy()

    Label(signup_window, text="Sign Up", fg="#57a1f8", bg="white", font=("Arial", 23, "bold")).pack(pady=20)

    email_label = Label(signup_window, text="Email:", bg="white", font=("Arial", 12))
    email_label.pack()
    email_entry = Entry(signup_window, width=40, bg="white", font=("Arial", 12))
    email_entry.pack(pady=5)

    first_name_label = Label(signup_window, text="First Name:", bg="white", font=("Arial", 12))
    first_name_label.pack()
    first_name_entry = Entry(signup_window, width=40, bg="white", font=("Arial", 12))
    first_name_entry.pack(pady=5)

    family_name_label = Label(signup_window, text="Family Name:", bg="white", font=("Arial", 12))
    family_name_label.pack()
    family_name_entry = Entry(signup_window, width=40, bg="white", font=("Arial", 12))
    family_name_entry.pack(pady=5)

    user_label = Label(signup_window, text="Username:", bg="white", font=("Arial", 12))
    user_label.pack()
    user = Entry(signup_window, width=40, bg="white", font=("Arial", 12))
    user.pack(pady=5)

    code_label = Label(signup_window, text="Password:", bg="white", font=("Arial", 12))
    code_label.pack()
    code = Entry(signup_window, width=40, bg="white", font=("Arial", 12))
    code.pack(pady=5)

    conform_code_label = Label(signup_window, text="Confirm Password:", bg="white", font=("Arial", 12))
    conform_code_label.pack()
    conform_code = Entry(signup_window, width=40, bg="white", font=("Arial", 12))
    conform_code.pack(pady=5)

    signup_button = Button(signup_window, text="Sign Up", width=20, bg="#57a1f8", fg="white", font=("Arial", 12), command=signup)
    signup_button.pack(pady=20)

    close_button = Button(signup_window, text="Close", width=20, bg="#57a1f8", fg="white", font=("Arial", 12), command=close_signup_window)
    close_button.pack()

img = PhotoImage(file="image/login.png")
img = img.subsample(2, 2)
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=500, y=100)

Label(frame, text="Sign In", fg="#57a1f8", bg="white", font=("Arial", 23, "bold")).place(x=100, y=5)

def on_enter(e):
    user.delete(0, END)

def on_leave(e):
    if user.get() == "":
        user.insert(0, "Username")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Arial", 11))
user.place(x=30, y=80)
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=259, height=2, bg="grey").place(x=25, y=107)

def on_enter(e):
    code.delete(0, END)

def on_leave(e):
    if code.get() == "":
        code.insert(0, "Password")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Arial", 11))
code.place(x=30, y=150)
code.insert(0,"Password")
code.bind ("<FocusIn>", on_enter)
code.bind ("<FocusOut>", on_leave)

Frame(frame, width=259, height=2, bg="grey").place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command=signin).place(x=35, y=204)

Label(frame, text="Don't have an account?", bg="white", fg="#57a1f8", font=("Arial", 10)).place(x=75, y=270)
Button(frame, width=6, text="Sign Up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=signup_command).place(x=215, y=270)

root.mainloop()
