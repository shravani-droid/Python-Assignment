import tkinter as tk

def add():
    a = float(entry1.get())
    b = float(entry2.get())
    result.config(text="Addition = " + str(a + b))

root = tk.Tk()
root.title("Addition of Two Numbers")

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", command=add).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()