import pandas as pd
from tkinter import *

font_s = ("courier", 10, "bold")
font_col = "white"
bg_col = "black"

# -------interal Data -------------
data = pd.read_csv("nato_phonetic_alphabet.csv")
df = data.to_dict()
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
# ------internal operations--------


def op():
    global textbox
    word = entry.get().upper()
    output_list = [dictionary[letter] for letter in word]
    textbox.insert(1.0, str(output_list))


def clear_entry():
    entry.delete(0, END)
    textbox.delete(1.0, END)
# ------window-------


win = Tk()
win.config(bg=bg_col)
win.geometry("620x500")
win.title("NATO phonetics Word GUI by Ranit Sarkar")

ranit = Canvas(height=120, width=610, bg="black", highlightthickness=0)
logo = PhotoImage(file="logo.png")
ranit.create_image(305, 60, image=logo)


label1 = Label(text="Type the word here", font=("courier", 20, "bold"),
               fg=font_col, highlightthickness=0, bg=bg_col)
# by ranit_sarkar
entry = Entry(width=40, font=("Arial", 15))
submit_but = Button(text="SUBMIT", height=2, width=10, command=op, activebackground="green")
clear_but = Button(text="CLEAR", height=2, width=10, command=clear_entry, activebackground="blue")
textbox = Text(width=42, height=12, bg=bg_col, font=("courier", 12), fg=font_col,
               highlightthickness=0, borderwidth=0)
exit_but = Button(text="EXIT", height=2, width=10, command=exit, activebackground="red")


ranit.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label1.grid(row=1, column=0, columnspan=1,)
entry.grid(row=2, column=0, pady=10, columnspan=1)
submit_but.grid(row=2, column=1, pady=10)
clear_but.grid(row=4, column=1, pady=10)
textbox.grid(row=4, column=0, columnspan=1, rowspan=2)
exit_but.grid(row=5, column=1,)

win.mainloop()
