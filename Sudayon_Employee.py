from tkinter import *
from connection import conn
from tkinter import ttk, messagebox

color1 = "#669900"
color2 = '#BBDEF0'
color3 = 'black'
font1 = ('Calibri (Body)', 25, 'bold')
font2 = ('Calibri (Body)', 15)
font3 = ('Calibri (Body)', 8)

root_FPS = Tk()
root_FPS.title("Sudayon Final Lab Activity")
root_FPS.configure(bg="Antique White")
root_FPS.geometry("1700x750")
root_FPS.resizable(width="false", height="false")


#Header
tops_FPS = Frame(root_FPS, width=1300, height=100, relief="raised", padx=15, pady=15, bg=color1)
lbltitle_FPS = Label(tops_FPS, text='Payroll Department', bg=color1, font=font1, fg=color3, width=100)
lbltitle2_FPS = Label(tops_FPS, text="New Employee Form", bg='#ddd', font=font2, fg=color3, pady=3)

#Search
entsearch_FPS = Entry(root_FPS, font=("Arial", 16), bg="white", relief="raised", width=44)
btnsearch_FPS = Button(root_FPS, text="Search", font=("Arial", 10), bg=color1, fg="white")

#Frame Input
frminput_FPS = Frame(root_FPS, width=800, height=400, padx=25, pady=25, bg=color1)
lblname_FPS = Label(frminput_FPS, text="Full name :", font=("Arial", 10), bg=color1, fg="white")

entLname_FPS = Entry(frminput_FPS, font=("Arial", 10,), bg="white")
lblLname_FPS = Label(frminput_FPS, text="Last Name", font=("Arial", 10,), bg=color1, fg="white")

entfname_FPS = Entry(frminput_FPS, font=("Arial", 10), bg="white",)
lblfname_FPS = Label(frminput_FPS, text="First Name", font=("Arial", 10), bg=color1, fg="white")

entMname_FPS = Entry(frminput_FPS, font=("Arial", 10,), bg="white")
lblMname_FPS = Label(frminput_FPS, text="Middle Initial", font=("Arial", 10), bg=color1, fg="white")

entage_FPS = Entry(frminput_FPS, font=("Arial", 10), bg="white", width=10)
lblage_FPS = Label(frminput_FPS, text="Age :", font=("Arial", 10), bg=color1, fg="white")

lblgender_FPS = Label(frminput_FPS, text="Gender :", bg=color1, fg="White", font=("Arial", 10))
gender_FPS = StringVar()
radgen1 = Radiobutton(frminput_FPS, text="Female", font=("Arial", 10), bg=color1, fg='white', selectcolor=color1, activebackground=color1, activeforeground="black", variable=gender_FPS, value="Female")
radgen2 = Radiobutton(frminput_FPS, text="Male", font=("Arial", 10), bg=color1, fg='white', selectcolor=color1, activebackground=color1, activeforeground="black", variable=gender_FPS, value="Male")
radgen3 = Radiobutton(frminput_FPS, text="Others", font=("Arial", 10), bg=color1, fg='white', selectcolor=color1, activebackground=color1, activeforeground="black", variable=gender_FPS, value="Others")

lbladd_FPS = Label(frminput_FPS, text="Address: ", bg=color1, fg="White", font=("Arial", 10))
lblstreet_FPS = Label(frminput_FPS, text="Street", font=("Arial", 10), bg=color1, fg="white")
entstreet_FPS = Entry(frminput_FPS, font=("Arial", 10), bg="white", width=20)

lblcity_FPS = Label(frminput_FPS, text="City", font=("Arial",10),bg=color1, fg="white")
entcity_FPS = Entry(frminput_FPS, font=("Arial", 10), bg="white", width=20)

lblprov_FPS = Label(frminput_FPS, text="Province", font=("Arial",10),bg=color1, fg="white")
entprov_FPS = Entry(frminput_FPS, font=("Arial", 10,), bg="white", width=20)

lblcoun_FPS = Label(frminput_FPS, text="Country", font=("Arial", 10), bg=color1, fg="white")
cmb_coun_FPS = ttk.Combobox(frminput_FPS, font=("Arial", 10), width=18, values=("Philippines", "Japan", "Indonesia", "USA", "Korea"))

lblzip_FPS = Label (frminput_FPS, text="Zip", font=("Arial", 10), bg=color1, fg="white")
entzip_FPS = Entry(frminput_FPS, font=("Arial", 10,), bg="white",width=20)

lblnum_FPS = Label (frminput_FPS, text="Number:", font=("Arial", 10), bg=color1, fg="white")
entnum_FPS = Entry(frminput_FPS, font=("Arial", 10), bg="white", width=22)

lblstats_FPS = Label(frminput_FPS, text="Status:", font=("Arial",10),bg=color1, fg="white")
list_stats_FPS = Listbox(frminput_FPS, width=22, font=("Arial", 10), height=0)
list_stats = ["Single", "Married", "Widowed", "Seperated", "Divorced"]

for stat in list_stats:
    list_stats_FPS.insert(END, stat)

#list_stats.insert(1, "Single")
#list_stats.insert(2, "Married")
#list_stats.insert(3, "Widowed")
#list_stats.insert(4, "Separated")
#list_stats.insert(5, "Divorced")

lblemail_FPS = Label(frminput_FPS, text="Email:", font=("Arial", 10), bg=color1, fg="white")
entemail_FPS = Entry(frminput_FPS, font=("Arial", 10), bg="white",  width=22)

lblposi_FPS = Label(frminput_FPS, text="Position", font=("Arial",10),bg=color1, fg="white")
entposi_FPS = Entry(frminput_FPS,font=("Arial", 10,), bg="white",width=22)

lblrate_FPS = Label(frminput_FPS, text="Rate per\nhour:", font=("Arial", 10), bg=color1, fg="white")
entrate_FPS = Entry(frminput_FPS, font=("Arial", 10,), bg="white", width=22)



#Functions
def search(event):
    try:
        table.delete(*table.get_children())
        search = entsearch_FPS.get()
        if search == "":
            messagebox.showerror("Notification","Enter search value!")
            table.delete(*table.get_children())
            show()
        else:
            cursor = conn.cursor()
            sql = "SELECT id,name,age,gender,address,contact,status,email,position,e_type,h_rate,n_hours,d_rate,w_payment,m_payment " \
                  "FROM tbl_employee WHERE id LIKE '%" + search + "%' OR name LIKE '%" + str(search) + "%' OR position LIKE '%" + str(search) + "%' OR gender LIKE '%" + str(search) + "%' OR e_type LIKE '%" + str(search) + "%' "
            cursor.execute(sql)
            rows = cursor.fetchall()

            #display to treeview
            for i, (id, name, age, gender, address, contact, status, email, position, e_type, h_rate, n_hours, d_rate, w_payment, m_payment) in enumerate(rows, start=1):
                table.insert("", "end", values=(id, name, age, gender, address, contact, status, email, position, e_type, h_rate, n_hours, d_rate, w_payment, m_payment))

    except Exception as e:
        messagebox.showerror("error",e)

def leftclick(event):
    emp = "Full Time"
    fname = entfname_FPS.get()
    mname = entMname_FPS.get()
    lname = entLname_FPS.get()
    name = (fname + " " + mname + " " + lname)
    age = entage_FPS.get()
    gen = gender_FPS.get()
    enum = entnum_FPS.get()
    email = entemail_FPS.get()
    posi = entposi_FPS.get()

    st = entstreet_FPS.get()
    ct = entcity_FPS.get()
    prov = entprov_FPS.get()
    zip = entzip_FPS.get()
    coun = cmb_coun_FPS.get()
    add = (st + ", " + ct + ", " + prov + ", " + coun + ", " + zip)
    numhour = int(8)
    rt = int(entrate_FPS.get())
    daily = float(rt * 8)
    weekly = float(daily * 6)
    monthly = float(daily * 24)

    stats = list_stats_FPS.curselection()
    stats1 = list_stats_FPS.get(stats[0])

    try:
        cursor = conn.cursor()
        sql = "Insert into tbl_employee(name,age,gender,address,contact,status,email,position,e_type,h_rate,n_hours,d_rate,w_payment,m_payment) " \
              "values('" + name + "','" + str(age) + "','" + str(gen) + "','" + str(add) + "','" + str(
            enum) + "','" + str(stats1) + "','" + email + "','" + posi + "','" + str(emp) + "','" + str(
            rt) + "','" + str(numhour) + "','" + str(daily) + "','" + str(weekly) + "','" + str(monthly) + "')"
        cursor.execute(sql)
        cursor.execute("commit")
        messagebox.showinfo("Save", "Successfully added Record!")
        table.delete(*table.get_children())
        show()
        cursor.close()
    except Exception as e:
        messagebox.showerror("error", e)

def rightclick(event):
    emp = "Part-Time"
    fname = entfname_FPS.get()
    mname = entMname_FPS.get()
    lname = entLname_FPS.get()
    name = (fname + " " + mname + " " + lname)
    age = entage_FPS.get()
    gen = gender_FPS.get()
    enum = entnum_FPS.get()
    email = entemail_FPS.get()
    posi = entposi_FPS.get()

    st = entstreet_FPS.get()
    ct = entcity_FPS.get()
    prov = entprov_FPS.get()
    zip = entzip_FPS.get()
    coun = cmb_coun_FPS.get()
    add = (st + ", " + ct + ", " + prov + ", " + coun + ", " + zip)
    numhour = int(4)
    rt = int(entrate_FPS.get())
    daily = float(rt * 4)
    weekly = float(daily * 6)
    monthly = float(daily * 24)

    stats = list_stats_FPS.curselection()
    stats1 = list_stats_FPS.get(stats[0])
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO tbl_employee(name,age,gender,address,contact,status,email,position,e_type,h_rate,n_hours,d_rate,w_payment,m_payment) " \
              "VALUES('" + name + "','" + str(age) + "','" + str(gen) + "','" + str(add) + "','" + str(enum) + "','" + str(
            stats1) + "','" + email + "','" + posi + "','" + str(emp) + "','" + str(rt) + "','" + str(
            numhour) + "','" + str(daily) + "','" + str(weekly) + "','" + str(monthly) + "')"
        cursor.execute(sql)
        cursor.execute("commit")
        messagebox.showinfo("Save", "Successfully added Record!")
        table.delete(*table.get_children())
        show()
        cursor.close()
    except Exception as e:
        messagebox.showerror("error", e)

def display_selected(event):
    clear()
    global id
    for select in table.selection():
        row = table.item(select)

    id, name, age, gender, address, contact, status, email, position, e_type, h_rate, n_hours, d_rate = row['values'][0:13]

    fname, mname, lname = name.split()
    st, ct, pr, cn, zp, *a = address.split()
    entfname_FPS.insert(0, "{first}".format(first=fname))
    entMname_FPS.insert(0, "{middle}".format(middle=mname))
    entLname_FPS.insert(0, "{last}".format(last=lname))

    entage_FPS.insert(0, age)

    if gender == 'Female':
        radgen1.select()
        radgen2.deselect()
        radgen3.deselect()
    elif gender == 'Male':
        radgen1.deselect()
        radgen2.select()
        radgen3.deselect()
    elif gender == 'Others':
        radgen1.deselect()
        radgen2.deselect()
        radgen3.select()

    entstreet_FPS.insert(0, "{street}".format(street=st))
    entcity_FPS.insert(0, "{city}".format(city=ct))
    entprov_FPS.insert(0, "{prov}".format(prov=pr))
    cmb_coun_FPS.insert(0, "{coun}".format(coun=cn))
    entzip_FPS.insert(0, "{zip}".format(zip=zp))

    entnum_FPS.insert(0, contact)

    list_stats = ["Single","Married","Widowed","Separated","Divorced"]
    list_stats.insert(0, status)

    for stat_ in list_stats:
        list_stats_FPS.insert(END, stat_)

    entemail_FPS.insert(0, email)
    entposi_FPS.insert(0, position)
    entrate_FPS.insert(0, h_rate)

    return id

def update(event):
    fname = entfname_FPS.get()
    mname = entMname_FPS.get()
    lname = entLname_FPS.get()
    name = (fname + " " + mname + " " + lname)
    age = entage_FPS.get()
    gen = gender_FPS.get()
    enum = entnum_FPS.get()
    email = entemail_FPS.get()
    posi = entposi_FPS.get()

    st = entstreet_FPS.get()
    ct = entcity_FPS.get()
    prov = entprov_FPS.get()
    zip = entzip_FPS.get()
    coun = cmb_coun_FPS.get()
    add = (st + ", " + ct + ", " + prov + ", " + coun + ", " + zip)
    numhour = entrate_FPS.get()
    rt = int(entrate_FPS.get())
    daily = float(rt * 8)
    weekly = float(daily * 6)
    monthly = float(daily * 24)

    stats = list_stats_FPS.curselection()
    if stats==():
        messagebox.showinfo("Unselected status:","Reselect your current status, If you don't want to change it")

    else:
        stats1 = list_stats_FPS.get(stats[0])

    list_stats_FPS.insert(0, stats1)
    try:
        cursor = conn.cursor()

        sql = "UPDATE tbl_employee SET name='" + name + "',age='" + str(age) + "',gender='" + str(gen) + "',address='" + str(add) + "',contact='" + str(enum) + "'" \
              ",status='" + str(stats1) + "',email='" + email + "',position='" + posi + "',h_rate='" + str(rt) + "',n_hours = '" + str(numhour) + "',d_rate='" + str(daily) + "'" \
              ",w_payment='" + str(weekly) + "',m_payment='" + str(monthly) + "' where id ='" + str(id) + "' "
        cursor.execute(sql)
        cursor.execute("commit")
        messagebox.showinfo("Save", "Successfully Updated Record!")
        table.delete(*table.get_children())
        show()
        clear()
        cursor.close()

    except Exception as ex:
        messagebox.showerror("error", ex)

def delete(event):
    try:
        msg = messagebox.askquestion("Delete Record","Do you want to delete this record?")

        if msg == 'yes':
            cursor = conn.cursor()
            sql = "DELETE FROM tbl_employee WHERE id =  '" + str(id) + "' "
            cursor.execute(sql)
            cursor.execute("commit")
            messagebox.showinfo("Notification","Record Deleted")
            table.delete(*table.get_children())
            show()
            clear()

    except Exception as e:
        messagebox.showerror("error", e)

def clearfields(event):
    table.delete(*table.get_children())
    show()
    clear()
    list_stats = ["Single", "Married", "Widowed", "Seperated", "Divorced"]

    for stat in list_stats:
        list_stats_FPS.insert(END, stat)

def clear1():
    table.delete(*table.get_children())
    show()
    clear()
    list_stats = ["Single", "M_ied", "Widowed", "Seperated", "Divorced"]

    for stats in list_stats:
        list_stats_FPS.insert(END, stats)

def clear():
    entfname_FPS.delete(0, END)
    entMname_FPS.delete(0, END)
    entLname_FPS.delete(0, END)
    entage_FPS.delete(0, END)
    entstreet_FPS.delete(0, END)
    entcity_FPS.delete(0, END)
    entprov_FPS.delete(0, END)
    entzip_FPS.delete(0, END)
    cmb_coun_FPS.delete(0, END)
    entnum_FPS.delete(0, END)
    list_stats_FPS.delete(0, END)
    entemail_FPS.delete(0, END)
    entposi_FPS.delete(0, END)
    entrate_FPS.delete(0, END)

def show():
    try:
        cursor = conn.cursor()
        sql = "SELECT id,name,age,gender,address,contact,status,email,position,e_type,h_rate,n_hours,d_rate,w_payment,m_payment FROM tbl_employee"
        cursor.execute(sql)
        rows = cursor.fetchall()
        radgen1.deselect()
        radgen2.deselect()
        radgen3.deselect()

        for i,(id,name,age,gender,address,contact,status,email,position,e_type,h_rate,n_hours,d_rate,w_payment,m_payment) in enumerate(rows,start=1):
            table.insert("",'end',values=(id,name,age,gender,address,contact,status,email,position,e_type,h_rate,n_hours,d_rate,w_payment,m_payment))
    except Exception as e:
        messagebox.showerror("error", e)


#Table Data View

col_FPS = ('ID','Name','Age','Gender','Address','Number','Status','Email','Position','Emp Type','Rate per hour',
           'Hours','Day Rate','Week Payment','Month Payment')
table = ttk.Treeview(root_FPS,columns=col_FPS,show='headings',height=20)
table.place(x=670,y=200)
table.bind("<<TreeviewSelect>>",display_selected)

for col in col_FPS:
    table.heading(col,text=col)
show()

table.column('ID',width=15,stretch=YES)
table.column('Name',width=120,stretch=YES)
table.column('Age',width=30,stretch=YES)
table.column('Gender',width=45,stretch=YES)
table.column('Address',width=130,stretch=YES)
table.column('Number',width=80,stretch=YES)
table.column('Status',width=45,stretch=YES)
table.column('Email',width=50)
table.column('Position',width=60)
table.column('Emp Type',width=70)
table.column('Rate per hour',width=50)
table.column('Hours',width=40)
table.column('Day Rate',width=70)
table.column('Week Payment',width=90)
table.column('Month Payment',width=100)

# BUTTON
btnsave_FPS = Button(frminput_FPS, text="Save Employee Record", font=("Arial", 10), activebackground="gray", activeforeground="white")
btnsave_FPS.bind("<Button-1>",leftclick)
btnsave_FPS.bind("<Button-2>",rightclick)
btnsave_FPS.bind("<Button-3>",rightclick)

btnclear_FPS = Button(frminput_FPS, text="Clear Fields", font=("Arial", 10), activebackground="gray", activeforeground="white")
btnclear_FPS.bind("<Button-1>",clearfields)

btnupdate_FPS = Button(frminput_FPS, text="Update", font=("Arial", 10), activebackground="gray", activeforeground="white")
btnupdate_FPS.bind("<Button-1>",update)
btndelete_FPS = Button(frminput_FPS, text="Delete", font=("Arial", 10), activebackground="gray", activeforeground="white")
btndelete_FPS.bind("<Button-1>",delete)

# POSITION INPUT
tops_FPS.place(anchor="c", x=855, y=60)
lbltitle_FPS.grid(row=0, column=0)
lbltitle2_FPS.grid(row=3, column=0)
frminput_FPS.place(x=35,y=130)

entsearch_FPS.place(x=715, y=150)
btnsearch_FPS.place(x=1250, y=150)
btnsearch_FPS.bind("<Button-1>",search)

lblname_FPS.grid(row=0,column=0,sticky='w')

entLname_FPS.grid(row=0,column=1,sticky='w')
lblLname_FPS.grid(row=1,column=1,sticky='w')

entfname_FPS.grid(row=0,column=2,sticky='w')
lblfname_FPS.grid(row=1,column=2,sticky='w')

entMname_FPS.grid(row=0,column=3,padx=6)
lblMname_FPS.grid(row=1,column=3,padx=5,sticky='w')

lblage_FPS.grid(row=2,column=0,sticky='e')
entage_FPS.grid(row=2,column=1,sticky='w')

lblgender_FPS.grid(row=3,column=0,rowspan=3,sticky='e')
radgen1.grid(row=3,column=1,sticky="w")
radgen2.grid(row=4,column=1,sticky="w")
radgen3.grid(row=5,column=1,sticky="w")

lbladd_FPS.grid(row=6, column=0, rowspan=3, sticky='e')

lblstreet_FPS.grid(row=7,column=1,sticky='w')
entstreet_FPS.grid(row=6,column=1,sticky='w')

lblcity_FPS.grid(row=7,column=2,sticky='w')
entcity_FPS.grid(row=6,column=2,padx=2,sticky='e')

lblprov_FPS.grid(row=7,column=3,padx=7,sticky='w')
entprov_FPS.grid(row=6,column=3,padx=2,sticky='e')

cmb_coun_FPS.grid(row=8,column=1,sticky='w')
lblcoun_FPS.grid(row=9,column=1,sticky='w')

entzip_FPS.grid(row=8,column=2,sticky='e')
lblzip_FPS.grid(row=9,column=2,padx=3,sticky='w')

lblnum_FPS.grid(row=10,column=0,sticky='e')
entnum_FPS.grid(row=10,column=1,pady=5,sticky='w')

lblstats_FPS.grid(row=11,column=0,sticky='e')
list_stats_FPS.grid(row=11,column=1,pady=1)

lblemail_FPS.grid(row=12,column=0,sticky='e')
entemail_FPS.grid(row=12,column=1,pady=5,sticky='w')

lblposi_FPS.grid(row=13,column=0,sticky='e')
entposi_FPS.grid(row=13,column=1,pady=5,sticky='w')

lblrate_FPS.grid(row=14,column=0,sticky='e')
entrate_FPS.grid(row=14,column=1,sticky='w')

btnsave_FPS.grid(row=17,column=0,columnspan=3,pady=15)
btnclear_FPS.grid(row=18,columnspan=5,pady=0)
btnupdate_FPS.grid(row=17,column=1,columnspan=4,pady=15)
btndelete_FPS.grid(row=17,column=2,columnspan=3,pady=15)


root_FPS.mainloop()
