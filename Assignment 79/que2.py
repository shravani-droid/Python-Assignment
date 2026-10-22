
import tkinter as tk

def find_max():
    a = float(entry1.get())
    b = float(entry2.get())
    c = float(entry3.get())
    result.config(text="Largest Number = " + str(max(a, b, c)))

root = tk.Tk()
root.title("Find Largest Number")

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Third Number").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Button(root, text="Find Maximum", command=find_max).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()
