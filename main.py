from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# Password Generator


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    psw_entry.delete(0, END)
    psw_entry.insert(0, password)
    pyperclip.copy(password)

# Password Manager


def save_datas():

    website = website_entry.get()
    email = email_entry.get()
    password = psw_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Üres mezők", message="Kérem töltse ki az üres mezőket!")
    else:
        is_ok = messagebox.askokcancel(title="Helyesek az adatok?", message=f"A megadott adatok:\nWeboldal: {website}\nEmail: {email}\nJelszó: {password}\n\nMegfelelőek az adatok?")

        if is_ok:
            with open("data.text", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                psw_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Weboldal:")
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email / Felh.név:")
email_label.grid(row=2, column=0, sticky="e")

psw_label = Label(text="Jelszó:")
psw_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "takacs.barbara97@gmail.com")

psw_entry = Entry(width=30)
psw_entry.grid(row=3, column=1, columnspan=2, sticky="w")

# Buttons
generate_btn = Button(text="Jelszó generálás", width=15, command=generate_password)
generate_btn.grid(row=3, column=2, sticky="e")

add_btn = Button(text="Mentés", width=30, command=save_datas)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
