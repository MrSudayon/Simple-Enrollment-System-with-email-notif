from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from connection import conn
from tkinter import ttk, messagebox

color1 = "#669900"
color2 = '#BBDEF0'
color3 = 'black'
Anti = 'Antique White'
font1 = ('Arial (Body)', 30, 'bold')
font2 = ('Calibri (Body)', 15)
font3 = ('Calibri (Body)', 10)
font4 = ('Calibri (Body)', 10, 'underline')

login_RS = Tk()
login_RS.title("LOGIN")
login_RS.configure(bg="Antique White")
login_RS.geometry("350x350")
login_RS.resizable(width="false", height="false")



tops_RS = Frame(login_RS, width=500, height=100, bg=Anti)
tops_RS.place(anchor="n", x=200, y=40)

#Image Admin
img = (Image.open("imgs/administrator.png"))
resized_img= img.resize((80,80), Image.Resampling.LANCZOS)
new_img= ImageTk.PhotoImage(resized_img)
labelimg = Label(login_RS, image = new_img, bg=Anti)
labelimg.place(anchor="nw", x=45, y=15)

#Contents
lbltitle_RS = Label(tops_RS, text="LOGIN", bg=Anti, font=font1, fg=color3, width=7, relief=SOLID)
lbltitle_RS.grid(row=0, column=0)

userlbl_RS = Label(login_RS, text="username:", bg=Anti, font=font3, fg=color3).place(anchor="w", relx=.1, rely=.4)
usertxt_RS = Entry(login_RS, bg="#fff1c9", font=font3, fg=color3, width=25)
usertxt_RS.place(anchor="w", relx=.3, rely=.4)

passlbl_RS = Label(login_RS, text="password:", bg=Anti, font=font3, fg=color3).place(anchor="w", relx=.1, rely=.5)
passtxt_RS = Entry(login_RS, bg="#fff1c9", font=font3, fg=color3, width=25, show="*")
passtxt_RS.place(anchor="w", relx=.3, rely=.5)

#Functions
def create():
    create = Tk()
    create.title("Create Account")
    create.configure(bg="Antique White")
    create.geometry("450x450")
    create.resizable(width="false", height="false")
    crt_tops = Frame(create, width=500, height=100, bg=Anti)
    crt_tops.place(anchor="n", x=235, y=55)

    crt_title = Label(crt_tops, text="Register", bg=Anti, font=font1, fg=color3, width=8, relief=SOLID)
    crt_title.grid(column=0, row=0)

    global unametxt
    unamelbl = Label(create, text="username: ", bg=Anti, font=font3, fg=color3).place(anchor="w", relx=.1, rely=.4)
    unametxt = Entry(create, bg="#fff1c9", font=font3, fg=color3, width=30, relief=RAISED)
    unametxt.place(anchor="w", relx=.3, rely=.4)

    global passtxt
    passlbl = Label(create, text="password: ", bg=Anti, font=font3, fg=color3).place(anchor="w", relx=.1, rely=.5)
    passtxt = Entry(create, bg="#fff1c9", show="*", font=font3, fg=color3, width=30, relief=RAISED)
    passtxt.place(anchor="w", relx=.3, rely=.5)

    global cpasstxt
    cpasslbl = Label(create, text="confirm: ", bg=Anti, font=font3, fg=color3).place(anchor="w", relx=.1, rely=.6)
    cpasstxt = Entry(create, bg="#fff1c9", show="*", font=font3, fg=color1, width=30, relief=RAISED)
    cpasstxt.place(anchor="w", relx=.3, rely=.6)

    global emailtxt
    emaillbl = Label(create, text="Email: ", bg=Anti, font=font3, fg=color3).place(anchor="w", relx=.1, rely=.7)
    emailtxt = Entry(create, bg="#fff1c9", font=font3, fg=color3, width=30, relief=RAISED)
    emailtxt.place(anchor="w", relx=.3, rely=.7)

    # Create funtions
    def loginnow():
        create.destroy()

    def register(event):
        clear()
        user = unametxt.get()
        pasw = passtxt.get()
        cpas = cpasstxt.get()
        email = emailtxt.get()

        try:
            if pasw == cpas:
                cursor = conn.cursor()
                sql = "insert into tbl_user (user, password, email) values ('"+ user +"', '"+ pasw +"', '"+ email +"')"
                cursor.execute(sql)
                cursor.execute("commit")
                messagebox.showinfo("Save", "Registered!")
            else:
                messagebox.showinfo("Invalid","Password doesn't match!")

        except Exception as ex:
            messagebox.showerror("error ",ex)

    def clearfield(event):
        clear()

    # Create account Buttons
    rgstrbtn = Button(create, text="Register", bg="#45ff76", font=font2, fg=color3, width=12, cursor="hand2")
    rgstrbtn.place(anchor="s", x=130, y=400)
    rgstrbtn.bind("<Button-1>", register)

    clrbtn = Button(create, text="Clear", bg="#ff5036", font=font2, fg=color3, width=12, cursor="hand2")
    clrbtn.place(anchor="s", x=320, y=400)
    clrbtn.bind("<Button-1>", clearfield)

    Button(create, text="Sign-In? Click here", bg=Anti, font=font4, fg="black", cursor="hand2", command = loginnow, relief = FLAT).place(anchor="s", x=220, y=430)

    create.mainloop()

def logged():
    login_RS.destroy()
    from student_enrollment import displayarr
    displayarr.mainloop()

def clear():
    usertxt_RS.delete(0, END)
    passtxt_RS.delete(0, END)

def login(event):
    try:
        global usern
        usern = usertxt_RS.get()
        passw = passtxt_RS.get()
        msg = "LOGGED-IN AT SYSTEM"

        cursor = conn.cursor()
        sql = "SELECT user,password FROM tbl_user WHERE user = %s and password = %s"
        cursor.execute(sql,[(usern),(passw)])
        rows = cursor.fetchall()

        if rows:
            for i in rows:
                sqllog = "insert into tbl_logs (user, action, timedate)" \
                      "values ('"+ usern +"', '"+ msg +"', NOW())"
                cursor.execute(sqllog)
                cursor.execute("commit")
                messagebox.showinfo("Welcome","Successfully Logged In")

                cursor.close()
                logged()
                break

        elif usern == "" and passw == "":
            messagebox.showinfo("Blank Fields Detected","Please enter Username and Password")

        else:
            messagebox.showinfo("Wrong Credentials","User and Password not matched")

        clear()

    except Exception as ex:
        messagebox.showerror("error", ex)




#User Buttons
loginbtn_RS = Button(login_RS, text="Submit", bg="#ffc82b", font=font2, fg=color3, width=15, cursor="hand2")
loginbtn_RS.place(anchor="s", x=180, y=240)
loginbtn_RS.bind("<Button-1>",login)

Button(login_RS, text="Create account?", bg=Anti, font=font4, fg="blue", cursor="hand2", command= create, relief = FLAT).place(anchor="s", x=180, y=270)


#About Developer
def open_url(url):
   webbrowser.open_new_tab(url)

url = 'https://www.linktr.ee/suu2'
aboutdev = Label(login_RS, text="Developer ©", bg=Anti, font=font3, fg=color3, cursor="hand2")
aboutdev.place(anchor="sw", x=5, y=345)
aboutdev.bind("<Button-1>", lambda event: open_url(url))

login_RS.mainloop()
