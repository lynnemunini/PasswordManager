from tkinter import *
import random
# import pyperclip
window = Tk()
GREY = "#F3EFCC"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    new_password = "".join(password_list)
    password.insert(INSERT, new_password)
    # Copy password generated to clipboard
    # pyperclip.copy(my_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def choice(option):
    pop.destroy()
    if option == yes_image:
        my_new_password = f"{my_website} | {my_username_email} | {my_password} | \n"
        with open(f"data.txt", mode="a") as data:
            data.write(my_new_password)
        website.delete('1.0', END)
        email.delete('1.0', END)
        password.delete('1.0', END)
        website.focus()


def clicker():
    global pop
    global yes_image
    pop = Toplevel(window)
    global my_website
    my_website = website.get("1.0", 'end-1c')
    global my_username_email
    my_username_email = email.get("1.0", 'end-1c')
    global my_password
    my_password = password.get("1.0", 'end-1c')
    pop.geometry("510x100")
    pop.config(bg=GREY)

    if len(my_website) == 0 or len(my_password) == 0:
        pop.title("Oops!")
        pop_label = Label(pop, text="Please make sure you haven't left any fields empty", bg=GREY,
                          font=("courier", 12, "normal"))
        pop_label.grid(row=0, column=1, pady=10)
        my_frame = Frame(pop, bg=GREY)
        my_frame.grid(row=1, column=1, pady=5)
        ok_image = PhotoImage(file="ok (1).png")
        ok_image_button = Button(my_frame, image=ok_image, bg=GREY, highlightthickness=0,
                                 command=lambda: choice(ok_image), border=0)
        ok_image_button.grid(row=1, column=2)

    else:
        global pict
        pop.geometry("350x150")
        pop.title(f"{my_website}")
        my_text = f"\nThese are the details you entered\n" \
                  f"Email: {my_username_email}\n" \
                  f"Password: {my_password}\n" \
                  f"is it okay to save?"
        pop_label = Label(pop, text=my_text, bg=GREY, font=("courier", 12, "normal"))
        pop_label.grid(row=0, column=1)
        my_frame = Frame(pop, bg=GREY)
        my_frame.grid(row=1, column=1, pady=5)
        yes_image = PhotoImage(file="yes (1).png")
        yes_image_button = Button(my_frame, image=yes_image, bg=GREY, highlightthickness=0,
                                  command=lambda: choice(yes_image), border=0)
        yes_image_button.grid(row=3, column=1, padx=50)
        no_image = PhotoImage(file="say-no (1).png")
        no_image_button = Button(my_frame, image=no_image, bg=GREY, highlightthickness=0,
                                 command=lambda: choice(no_image), border=0)
        no_image_button.grid(row=3, column=2, padx=50)


# ---------------------------- UI SETUP ------------------------------- #
window.title("Password Manager")
window.config(padx=20, pady=20, bg=GREY)
canvas = Canvas(width=256, height=256, bg=GREY, highlightthickness=0)
logo = PhotoImage(file="Logo1.png")
canvas.create_image(128, 128, image=logo)
canvas.grid(column=1, row=0)

# Labels

# Website
website_label = Label(text="Website:", font=("courier", 13, "bold"))
website_label.grid(column=0, row=1)
website_label.config(bg=GREY)

# Email/Username
email_label = Label(text="Email/Username:", font=("courier", 13, "bold"))
email_label.grid(column=0, row=2)
email_label.config(bg=GREY)

# Password
password_label = Label(text="Password:", font=("courier", 13, "bold"))
password_label.grid(column=0, row=3)
password_label.config(bg=GREY)

# Website Text
website = Text(borderwidth=0, highlightthickness=0, width=45, height=2, insertbackground="orange",
               selectbackground="white", fg="orange", cursor="pencil")
website.focus()
website.grid(column=1, row=1, columnspan=2, pady=5)

# Email Text
email = Text(borderwidth=0, insertbackground="orange", highlightthickness=0, width=45, height=2,
             selectbackground="white", fg="orange", cursor="pencil")
# To set default text for email/username
email.insert(INSERT, "you@you.com")
email.grid(column=1, row=2, columnspan=2)

# Password
password = Text(bg="white", borderwidth=0, highlightthickness=0, width=31, height=2, insertbackground="orange",
                selectbackground="white", fg="orange")
password.grid(column=1, row=3, pady=5)

# Password Generate
generate = Button(text="Generate", font=("courier", 13), width=9, borderwidth=0, highlightthickness=0,
                  command=generate_password)
generate.grid(column=2, padx=0, row=3)
generate.config(bg="orange")

# Generate image
generate = Canvas(width=32, height=32, bg=GREY, highlightthickness=0)
create = PhotoImage(file="creating.png")
generate.create_image(16, 16, image=create)
generate.grid(column=3, row=3)
# Add
add_image = PhotoImage(file="plus-sign.png")
add_image_button = Button(image=add_image, bg=GREY, highlightthickness=0, border=0, command=clicker)
add_image_button.grid(column=1, row=4, padx=0)


window.mainloop()
