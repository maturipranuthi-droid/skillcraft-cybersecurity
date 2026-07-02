from tkinter import *
from datetime import datetime

def save_text():
    text = text_box.get("1.0", END)
    with open("user_input_log.txt", "a") as file:
        file.write(f"\n[{datetime.now()}]\n")
        file.write(text)
        file.write("\n" + "-" * 30 + "\n")

root = Tk()
root.title("Typing Practice Logger")
root.geometry("500x300")

Label(root, text="Type something below:").pack(pady=5)

text_box = Text(root, height=10, width=50)
text_box.pack(pady=10)

Button(root, text="Save Text", command=save_text).pack()

root.mainloop()