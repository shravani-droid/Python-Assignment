
import tkinter as tk

def check_eligibility():
    name = entry1.get()
    age = int(entry2.get())

    if age >= 18:
        result.config(text=name + " is eligible to vote")
    else:
        result.config(text=name + " is not eligible to vote")

root = tk.Tk()
root.title("Voting Eligibility Checker")

tk.Label(root, text="Enter Name").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Age").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Check Eligibility",
          command=check_eligibility).pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()
