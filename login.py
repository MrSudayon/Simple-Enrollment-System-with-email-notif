from tkinter import *
from PIL import Image, ImageTk
from connection import conn
from tkinter import ttk, messagebox

color1 = "#669900"
color2 = '#BBDEF0'
color3 = 'black'
Anti = 'Antique White'
font1 = ('Arial (Body)', 30, 'bold')
font2 = ('Calibri (Body)', 15)
font3 = ('Calibri (Body)', 10)

login_RS = Tk()
login_RS.title("LOGIN")
login_RS.configure(bg="Antique White")
login_RS.geometry("350x350")
login_RS.resizable(width="false", height="false")

tops_RS = Frame(login_RS, width=500, height=100, bg=Anti)
tops_RS.place(anchor="n", x=200, y=40)

img = (Image.open("imgs/administrator.png"))
resized_img= img.resize((80,80), Image.Resampling.LANCZOS)
new_img= ImageTk.PhotoImage(resized_img)
labelimg = Label(login_RS, image = new_img, bg=Anti)
labelimg.place(anchor="nw", x=45, y=15)

lbltitle_RS = Label(tops_RS, text="LOGIN", bg=Anti, font=font1, fg=color3, width=100)
lbltitle_RS.grid(row=0, column=0)

userlbl_RS = Label(login_RS, text="username:", bg=Anti, font=font3, fg=color3)
userlbl_RS.place(anchor="w", relx=.1, rely=.4)
usertxt_RS = Entry(login_RS, bg="#fff1c9", font=font3, fg=color3, width=25, relief=RAISED)
usertxt_RS.place(anchor="w", relx=.3, rely=.4)

passlbl_RS = Label(login_RS, text="password:", bg=Anti, font=font3, fg=color3)
passlbl_RS.place(anchor="w", relx=.1, rely=.5)
passtxt_RS = Entry(login_RS, bg="#fff1c9", font=font3, fg=color3, width=25, relief=RAISED)
passtxt_RS.place(anchor="w", relx=.3, rely=.5)

loginbtn_RS = Button(login_RS, text="Submit", bg="#ffc82b", font=font2, fg=color3, width=15)
loginbtn_RS.place(anchor="s", x=180, y=240)

createacc_RS = Button(login_RS, text="Create account?", bg=Anti, font=font3, fg=color3)
createacc_RS.place(anchor="s", x=180, y=270)

login_RS.mainloop()