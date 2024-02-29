from tkinter import *
from tkinter import messagebox

f = ('Times', 14)

def insert_record():
    warn = ""
    if register_name.get() == "":
        warn = "Name can't be empty"

    elif register_email.get() == "":
        warn = "Email can't be empty"

    elif register_mobile.get() == "":
        warn = "Contact can't be empty"

    elif register_pwd.get() == "":
        warn = "Password can't be empty"

    elif pwd_again.get() == "":
        warn = "Re-enter password can't be empty"

    elif register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"

    else:
        messagebox.showinfo('Confirmation', 'Record Saved')
        return

    messagebox.showerror('Error', warn)

def login_response():
    uname = email_tf.get()
    upwd = pwd_tf.get()
    warn = ""
    if uname == "":
        warn = "Username can't be empty"
    elif upwd == "":
        warn = "Password can't be empty"
    else:
        if uname == "admin" and upwd == "admin":
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            return
        else:
            warn = "Invalid username or password"

    messagebox.showerror('Login Status', warn)

ws = Tk()
ws.title('PythonGuides')
ws.geometry('940x500')
ws.config(bg='#0B5A81')

left_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    left_frame,
    text="Enter Email",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame,
    font=f
)

pwd_tf = Entry(
    left_frame,
    font=f,
    show='*'
)

login_btn = Button(
    left_frame,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=login_response
)

right_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    right_frame,
    text="Enter Name",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Email",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Contact Number",
    bg='#CCCCCC',
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Re-Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

register_name = Entry(
    right_frame,
    font=f
)

register_email = Entry(
    right_frame,
    font=f
)

register_mobile = Entry(
    right_frame,
    font=f
)

register_pwd = Entry(
    right_frame,
    font=f,
    show='*'
)

pwd_again = Entry(
    right_frame,
    font=f,
    show='*'
)

register_btn = Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)

email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20)
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_pwd.grid(row=3, column=1, pady=10, padx=20)
pwd_again.grid(row=4, column=1, pady=10, padx=20)
register_btn.grid(row=5, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)

ws.mainloop()