import tkinter as tk

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "admin" and password == "1234":
        result.config(text="Login Successful")
    else:
        result.config(text="Invalid Username or Password")

root = tk.Tk()
root.title("Basic Login Form")

tk.Label(root, text="Username").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Password").pack()
entry2 = tk.Entry(root, show="*")
entry2.pack()

tk.Button(root, text="Login", command=login).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()
