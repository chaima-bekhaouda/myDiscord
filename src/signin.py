from tkinter import  *
from tkinter import messagebox
import ast

root=Tk()
root.title("login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username=user.get()
    password=code.get()

    file=open("data.txt","r")
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    #print(r.keys())
    #print(r.values())

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("Welcome")
        screen.geometry("925x500+300+200")
        screen.configure(bg="white")

        Label(screen,text="Welcome",fg="black",bg="white",font=("arial",50,"bold")).pack(expand=True)

        screen.mainloop()

    else:
        messagebox.showerror("Error","Invalid username or password")

###############____________________________
def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)


    def signup():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()

        if password==conform_password:
            try:
                file = open("datasheet.txt", "r+")  # Open the file "datasheet.txt" in read mode
                d = file.read() # Define the variable "d" and assign it the value of "pp"
                r = ast.literal_eval(d)  # Define the variable "r" by evaluating the string "d" as a literal

                dict2 = {username: password}  # creates a dictionary with user name as
                r.update(dict2)  # updates the dictionary with the new user name and password
                file.truncate(0)
                file.close()

                file = open("datasheet.txt", "w")
                w = file.write(str(r))  # writes the updated data sheet.

                messagebox.showinfo("Success", f"Account created successfully. {w}")
                window.destroy()

            except:
                file=open("datasheet.txt", "w")
                pp=str({username:password})     #if there is no data sheet it creates a new one
                file.write(pp)
                file.close()

        else:
            messagebox.showerror("Error", "Password does not match")

    def sign():
        window.destroy()


    img = PhotoImage(file="image/login1.png")
    img = img.subsample(2, 2)
    Label(window, image=img, border=0, bg="white").place(x=50, y=90)

    frame=Frame(window, width=350, height=400, bg="white")
    frame.place(x=480, y=50)


    heading=Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=("arial",23,"bold"))
    heading.place(x=100,y=5)

    def on_enter(e):
        user.delete(0, "end")
    def on_leave(e):
        if user.get() == "":
            user.insert(0, "Username")

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("arial", 11))
    user.place(x=30, y=80)
    user.insert(0,"Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)


    Frame(frame, width=295, height=2, bg="grey").place(x=25, y=107)

    def on_enter(e):
        code.delete(0, "end")
    def on_leave(e):
        if code.get() == "":
            code.insert(0, "Password")

    code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("arial", 11))
    code.place(x=30, y=150)
    code.insert(0,"Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)


    Frame(frame, width=295, height=2, bg="grey").place(x=25, y=177)

    def on_enter(e):
        conform_code.delete(0, "end")
    def on_leave(e):
        if conform_code.get() == "":
            conform_code.insert(0, "Conform Password")

    conform_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("arial", 11))
    conform_code.place(x=30, y=220)
    conform_code.insert(0,"Conform Password")
    conform_code.bind("<FocusIn>", on_enter)
    conform_code.bind("<FocusOut>", on_leave)


    Frame(frame, width=295, height=2, bg="grey").place(x=25, y=247)


    Button(frame, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0 ,command=signup).place(x=35, y=274)
    label=Label(frame, text="Already have an account?", bg="white", fg="black", font=("arial", 9))
    label.place(x=50, y=340)

    signin=Button(frame, width=6, text="Sign In", border=0, bg="white", cursor="hand2", fg="#57a1f8" , command =sign)
    signin.place(x=200, y=340)


    window.mainloop()
######_____________________________________________



img = PhotoImage(file="image/login.png")
img = img.subsample(2, 2)
Label(root, image=img, bg="white").place(x=50, y=50)


frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)


heading=Label(frame,text="Sign in", fg="#57a1f8", bg="white", font=("arial",23,"bold"))
heading.place(x=100,y=5)

########_________________________________

def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get(0,"end")
    if name=="":
        user.insert(0,"Username")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("arial", 11))
user.place(x=30, y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame, width=259, height=2, bg="grey").place(x=25, y=107)

########_________________________________
def on_enter(e):
    code.delete(0,"end")

def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("arial", 11))
code.place(x=30, y=150)
code.insert(0,"Password")
code.bind ("<FocusIn>",on_enter)
code.bind ("<FocusOut>",on_leave)

Frame(frame, width=259, height=2, bg="grey").place(x=25, y=177)

#################________________
Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=signin).place(x=35, y=204)
label=Label(frame,text="Don't have an account?",bg="white",fg="#57a1f8",font=("arial",10))
label.place(x=75,y=270)

sign_up= Button(frame, width=6, text="Sign Up",border=0, bg="white", cursor="hand2", fg="#57a1f8" , command=signup_command)
sign_up.place(x=215,y=270)










root.mainloop()
