from tkinter import *
from tkinter import messagebox
import ast

def on_entry_focus_in(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, "end")

def on_entry_focus_out(event, entry, default_text):
    if entry.get() == "":
        entry.insert(0, default_text)

def main():
    window = Tk()
    window.title("Sign Up")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    def signup():
        password = code.get()
        confirm_password = confirm_code.get()
        email_address = email.get()

        if password == "" or confirm_password == "" or email_address == "":
            messagebox.showerror("Error", "Please fill in all the fields")
        elif password != confirm_password:
            messagebox.showerror("Error", "Password does not match")
        else:
            users = {}
            try:
                with open("data/users.txt", "r") as file:
                    users = ast.literal_eval(file.read())
            except FileNotFoundError:
                pass

            users = {"first_name": first_name.get(), "last_name": last_name.get(), "email": email_address}
            with open("data/users.txt", "w") as file:
                file.write(str(users))
            messagebox.showinfo("Success", "Account created successfully")

    image = PhotoImage(file="image/signin.png")
    image = image.subsample(2, 2)
    Label(window, image=image, bg="white").place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="Sign Up", fg="#57a1f8", font=("Microsoft YaHei UI Light", 23, "bold"), bg="white")
    heading.place(x=130, y=-10)

    default_first_name = "First Name"
    first_name = Entry(frame, width=14, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    first_name.place(x=30, y=40)
    first_name.insert(0, default_first_name)
    first_name.bind("<FocusIn>", lambda event: on_entry_focus_in(event, first_name, default_first_name))
    first_name.bind("<FocusOut>", lambda event: on_entry_focus_out(event, first_name, default_first_name))

    Frame(frame, width=5, height=1, bg="white").place(x=160, y=40)  # Adding a small space between the fields

    default_last_name = "Last Name"
    last_name = Entry(frame, width=14, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    last_name.place(x=175, y=40)
    last_name.insert(0, default_last_name)
    last_name.bind("<FocusIn>", lambda event: on_entry_focus_in(event, last_name, default_last_name))
    last_name.bind("<FocusOut>", lambda event: on_entry_focus_out(event, last_name, default_last_name))

    Frame(frame, width=120, height=1, bg="black").place(x=25, y=67)

    default_password = "Password"
    code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    code.place(x=30, y=120)
    code.insert(0, default_password)
    code.bind("<FocusIn>", lambda event: on_entry_focus_in(event, code, default_password))
    code.bind("<FocusOut>", lambda event: on_entry_focus_out(event, code, default_password))

    Frame(frame, width=295, height=1, bg="black").place(x=25, y=145)

    default_confirm_password = "Confirm Password"
    confirm_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    confirm_code.place(x=30, y=160)
    confirm_code.insert(0, default_confirm_password)
    confirm_code.bind("<FocusIn>", lambda event: on_entry_focus_in(event, confirm_code, default_confirm_password))
    confirm_code.bind("<FocusOut>", lambda event: on_entry_focus_out(event, confirm_code, default_confirm_password))

    Frame(frame, width=295, height=1, bg="black").place(x=25, y=185)

    default_email = "Email"
    email = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    email.place(x=30, y=200)
    email.insert(0, default_email)
    email.bind("<FocusIn>", lambda event: on_entry_focus_in(event, email, default_email))
    email.bind("<FocusOut>", lambda event: on_entry_focus_out(event, email, default_email))

    Frame(frame, width=295, height=1, bg="black").place(x=25, y=225)

    Button(frame, width=20, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=signup).place(x=110, y=280)

    label = Label(frame, text="Already have an account?", fg="black", font=("Microsoft YaHei UI Light", 9), bg="white")
    label.place(x=60, y=320)

    signin = Button(frame, width=6, text="Sign in", bg="white", fg="#57a1f8", border=0, cursor="hand2")
    signin.place(x=220, y=320)

    window.mainloop()

if __name__ == "__main__":
    main()
