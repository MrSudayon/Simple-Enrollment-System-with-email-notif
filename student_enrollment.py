from tkinter import *
from connection import conn
from tkinter import messagebox
from tkinter import ttk

displayarr = Tk()
displayarr.geometry("1300x800")
displayarr.title("FINALS UPGRADE")
displayarr.resizable(width="false", height="false")
displayarr.configure(bg="#F5F5DC")

def deletearr(event):
    try:
        msgarr=messagebox.askquestion("Delete Record","Do you want to delete record?")
        if msgarr == 'yes':
            cursorarr=conn.cursor()
            sqlarr="Delete from enrolled where ID='"+str(ID)+"'"
            cursorarr.execute(sqlarr)
            cursorarr.execute("commit")
            messagebox.showinfo("Notification","Deleted Record")

            tablearr.delete(*tablearr.get_children())
            showarr()
            cleararr()
    except Exception as ex:
        messagebox.showerror("error", ex)

def cleararr():
    entFirstarr.delete(0, END)
    entMidarr.delete(0, END)
    entLastarr.delete(0, END)
    radGen1arr.deselect()
    radGen2arr.deselect()
    entStarr.delete(0, END)
    entCityarr.delete(0, END)
    entProvarr.delete(0, END)
    cmbCountryarr.delete(0, END)
    entZiparr.delete(0, END)
    entbday.delete(0, END)
    entcon.delete(0, END)
    cmbentdays.delete(0, END)
    entrate.delete(0, END)
    entstart.delete(0, END)
    entpay.delete(0, END)
    entbal.delete(0, END)

def showarr():
    try:
        cursorarr=conn.cursor()
        sqlarr="select * from enrolled"
        cursorarr.execute(sqlarr)
        rowsarr= cursorarr.fetchall()
        #displaytotreeview
        for i,(ID,FUll_NAME,BIRTHDATE,CONTACT,GENDER,ADDRESS,DAYS,RATE,START_DATE,TUITION,STATUS,PAYMENT,BALANCE) in enumerate(rowsarr, start=1):
            tablearr.insert("",'end',values=(ID,FUll_NAME,BIRTHDATE,CONTACT,GENDER,ADDRESS,DAYS,RATE,START_DATE,TUITION,STATUS,PAYMENT,BALANCE))
            cursorarr.close()
    except Exception as ex:
        messagebox.showerror("error",ex)

def display_selectarr(event):
    cleararr()
    for select in tablearr.selection():
        rowarr=tablearr.item(select)
        global ID
        ID,FUll_NAME,BIRTHDATE,CONTACT,GENDER,ADDRESS,DAYS,RATE,START_DATE,TUITION,STATUS,PAYMENT,BALANCE = rowarr['values'][0:13]
        firstarr,middlearr,lastarr,*a=FUll_NAME.split(" , ")
        starr,ctarr,prarr,cnarr,zparr,*a=ADDRESS.split(" , ")
        entFirstarr.insert(0,"{first}".format(first=firstarr))
        entMidarr.insert(0,"{middle}".format(middle=middlearr))
        entLastarr.insert(0,"{last}".format(last=lastarr))
        entbday.insert(0,BIRTHDATE)
        entcon.insert(0,CONTACT)
        if GENDER == 'Male':
            radGen1arr.select()
            radGen2arr.deselect()
        elif GENDER == 'Female':
            radGen1arr.deselect()
            radGen2arr.select()
        else:
            radGen1arr.deselect()
            radGen2arr.deselect()
        entStarr.insert(0,"{st}".format(st=starr))
        entCityarr.insert(0,"{ct}".format(ct=ctarr))
        entProvarr.insert(0,"{pr}".format(pr=prarr))
        cmbCountryarr.insert(0,"{cn}".format(cn=cnarr))
        entZiparr.insert(0,"{zp}".format(zp=zparr))
        cmbentdays.insert(0,DAYS)
        entrate.insert(0,RATE)
        entstart.insert(0,START_DATE)
        entpay.insert(0,PAYMENT)
        entbal.insert(0,BALANCE)
        return ID

def updatearr(event):

    firstnarr = entFirstarr.get()
    midarr = entMidarr.get()
    lastnarr = entLastarr.get()

    genderarr = genarr.get()

    starr = entStarr.get()
    cityarr = entCityarr.get()
    provarr = entProvarr.get()
    cnarr = cmbCountryarr.get()
    ziparr = entZiparr.get()

    bday = entbday.get()
    cnumarr = entcon.get()

    cmbdays = cmbentdays.get()
    rate = entrate.get()
    start = entstart.get()
    payment=entpay.get()

    fullnarr = firstnarr + " , " + midarr + " , " + lastnarr
    addarr = starr + " , " + cityarr + " , " + provarr + " , " + cnarr + " , " + ziparr
    tuition = int(rate) * int(cmbdays)
    balance=int(tuition) - int(payment)
    try:
        cursorarr = conn.cursor()

        sqlarr = "Update enrolled set FULL_NAME='" + str(fullnarr) + "',BIRTHDATE='" + str(bday) + "',CONTACT='" + str(cnumarr) + "',\
        GENDER='" + str(genderarr) + "',ADDRESS='" + str(addarr) + "',DAYS='" + str(cmbdays) + "',RATE='" + str(rate) + "',\
        START_DATE='" + str(start) + "',TUITION='" + str(tuition) + "',PAYMENT='" + str(payment) + "',BALANCE='" + str(balance) + "' where ID='" + str(ID) + "' "

        cursorarr.execute(sqlarr)
        cursorarr.execute("commit")
        messagebox.showinfo("Notification","successfully Updated record!")
        tablearr.delete(*tablearr.get_children())
        showarr()
        cleararr()
    except Exception as ex:
        messagebox.showerror("error", ex)

def clearbutarr(event):
    tablearr.delete(*tablearr.get_children())
    showarr()
    cleararr()
def save(event):
    firstnarr = entFirstarr.get()
    midarr = entMidarr.get()
    lastnarr = entLastarr.get()

    genderarr = genarr.get()

    starr = entStarr.get()
    cityarr = entCityarr.get()
    provarr = entProvarr.get()
    cnarr = cmbCountryarr.get()
    ziparr = entZiparr.get()

    bday = entbday.get()
    cnumarr = entcon.get()

    cmbdays = cmbentdays.get()
    rate = entrate.get()
    start = entstart.get()
    payment = entpay.get()
    fullnarr = firstnarr + " , " + midarr + " , " + lastnarr
    addarr = starr + " , " + cityarr + " , " + provarr + " , " + cnarr + " , " + ziparr
    tuition= int(rate) * int(cmbdays)
    status="Enrolled"
    balance=int(tuition) - int(payment)
    try:
        cursorarr = conn.cursor()
        sqlarr = "insert into enrolled (ID,FUll_NAME,BIRTHDATE,CONTACT,GENDER,ADDRESS,DAYS,RATE,START_DATE,TUITION,STATUS,PAYMENT,BALANCE) \
        VALUES ('"+""+"','" + str(fullnarr) + "','" + str(bday) + "','" + str(cnumarr) + "','" + str(genderarr) + "','" + str(addarr) + "',\
        '" + str(cmbdays) + "','" + str(rate) + "','" + str(start) + "','" + str(tuition) + "','" + str(status) + "','" + str(payment) + "','" + str(balance) + "')"

        cursorarr.execute(sqlarr)
        cursorarr.execute("commit")
        messagebox.showinfo("rightClick","successfully added record!")
        tablearr.delete(*tablearr.get_children())
        showarr()
        cleararr()
        cursorarr.close()
    except Exception as ex:
        messagebox.showerror("error",ex)

def searcharr(event):
    try:
        tablearr.delete(*tablearr.get_children())
        findarr = entsearch.get()
        if(findarr==""):
            messagebox.showerror("Notification","Enter search value!")
            tablearr.delete(*tablearr.get_children())
            showarr()
        else:
            cursorarr = conn.cursor()
            sqlarr = "select * from enrolled where FULL_NAME like '%"+ findarr +"%' OR ID like '%"+ findarr +"%'"
            cursorarr.execute(sqlarr)
            myresarr=cursorarr.fetchall()

            for i, (ID,FUll_NAME,BIRTHDATE,CONTACT,GENDER,ADDRESS,DAYS,RATE,START_DATE,TUITION,STATUS,PAYMENT,BALANCE) in enumerate(myresarr, start=1):
                tablearr.insert("", 'end', values=(ID,FUll_NAME,BIRTHDATE,CONTACT,GENDER,ADDRESS,DAYS,RATE,START_DATE,TUITION,STATUS,PAYMENT,BALANCE))

    except Exception as e:
        messagebox.showerror("error",e)
def completed(event):
    try:
        cursorarr = conn.cursor()
        status="COMPLETED"
        if ID:
            sqlarr = "Update enrolled set STATUS='" + str(status) + "' where ID='" + str(ID) + "' "
            cursorarr.execute(sqlarr)
            cursorarr.execute("commit")
            messagebox.showinfo("Notification", "successfully Updated record!")
            tablearr.delete(*tablearr.get_children())
            showarr()
            cleararr()
        else:
            messagebox.showinfo("Notification", "No ID Found: Please Select first")
    except Exception as ex:
        messagebox.showerror("error", ex)

def logoutt(event):
    try:
        cursorarr = conn.cursor()
        cursorarr1 = conn.cursor()

        sqllast = "select id, user from tbl_logs ORDER BY id DESC LIMIT 1"
        cursorarr1.execute(sqllast)
        result = cursorarr1.fetchall()
        myres = [result]
        fres = list(myres[id].user())
        msg = "LOGGED-OUT AT SYSTEM"

        sqllog = "insert into tbl_logs (user, action, timedate)" \
                 "values ('"+ fres +"' , '" + msg + "', NOW())"
        cursorarr.execute(sqllog)
        cursorarr.execute("commit")
        #messagebox.showinfo("Welcome", "Successfully Logged uut")

        displayarr.destroy()

    except Exception as ex:
        messagebox.showerror("error", ex)


#frame
frameemployeearr = Frame(displayarr,width=1300,height=150,bg="#E59866",padx=470,pady=20)
frameemployeearr.pack()

frameinarr = Frame(displayarr,width=500,height=800,bg="#C0C0C0",padx=10,pady=10)
frameinarr.pack(anchor="w",pady=10,padx=10)
frameinarr.place(x=30,y=130)



lblheaderarr = Label(frameemployeearr,text="Preschool Enrollment",font=("Helvetica",40),fg="#0a2351",bg="#E59866")
lblheaderarr.grid(row=0, column=0)

lblinfo= Label(frameinarr,text="Child's Information",width=50,height=1,font=("Arial",15),fg="#0a2351",bg="#318CE7")
lblinfo.grid(row=0,column=0,columnspan=3,sticky="w")
lblfullname = Label(frameinarr,text="Child's Name:",font=("Arial",12),fg="#0a2351",bg="#C0C0C0")
lblfullname.grid(row=1,column=0,columnspan=3,sticky="w")
entFirstarr = Entry(frameinarr,font=("Arial",11))
entFirstarr.grid(row=2,column=0,pady=3,padx=3)
entMidarr = Entry(frameinarr,font=("Arial",11))
entMidarr.grid(row=2,column=1,pady=3,padx=3)
entLastarr = Entry(frameinarr,font=("Arial",11))
entLastarr.grid(row=2,column=2,pady=3,padx=3)

lblfn = Label(frameinarr,text="Fist Name",font=("Arial",10),fg="#0a2351",bg="#C0C0C0")
lblfn.grid(row=3,column=0)
lblmn = Label(frameinarr,text="Middle Name",font=("Arial",10),fg="#0a2351",bg="#C0C0C0")
lblmn.grid(row=3,column=1)
lblln = Label(frameinarr,text="Last Name",font=("Arial",10),fg="#0a2351",bg="#C0C0C0")
lblln.grid(row=3,column=2)

lblbday = Label(frameinarr,text="Birth date(mm/dd/yy):",font=("Arial",12),fg="#0a2351",bg="#C0C0C0")
lblbday.grid(row=4,column=1,sticky="w")
entbday= Entry(frameinarr,font=("Arial",11))
entbday.grid(row=5,column=1,pady=3,padx=3)
lblcontact = Label(frameinarr,text="Homes Phone #:",font=("Arial",12),fg="#0a2351",bg="#C0C0C0")
lblcontact.grid(row=4,column=2,sticky="w")
entcon= Entry(frameinarr,font=("Arial",11))
entcon.grid(row=5,column=2,pady=3,padx=3)


lblGenarr = Label(frameinarr,text="Gender:",font=("Arial",12),fg="#0a2351",bg="#C0C0C0")
lblGenarr.grid(row=4,column=0,pady=3,padx=3,sticky="w")
genarr = StringVar()
radGen1arr = Radiobutton(frameinarr,text="Male",selectcolor="WHITE",font=("Arial",11),variable=genarr, value="Male",fg="Black",bg="#C0C0C0")
radGen2arr = Radiobutton(frameinarr,text="Female",selectcolor="WHITE",font=("Arial",11),variable=genarr, value="Female",fg="Black",bg="#C0C0C0")

radGen1arr.grid(row=5,column=0,pady=1,padx=1,sticky="w")
radGen2arr.grid(row=6,column=0,pady=1,padx=1,sticky="w")

lbldays = Label(frameinarr,text="Days of Program:",font=("Arial",11),fg="#0a2351",bg="#C0C0C0")
lbldays.grid(row=8,column=0,pady=3,padx=3,sticky="w")

cmbentdays=ttk.Combobox(frameinarr,font=("Arial",11),values=("3","4","5","6","7","8","9","10"))
cmbentdays.grid(row=9,column=0,pady=3,padx=3)

lblstart = Label(frameinarr,text="Start Date (mm/dd/yy):",font=("Arial",11),fg="#0a2351",bg="#C0C0C0")
lblstart.grid(row=10,column=0,pady=3,padx=3,sticky="w")

entstart = Entry(frameinarr,font=("Arial",11))
entstart.grid(row=11,column=0,pady=3,padx=3)

lblAddarr = Label(frameinarr,text="Address:",font=("Arial",12),fg="#0a2351",bg="#C0C0C0")
lblAddarr.grid(row=6,column=1,pady=3,padx=3,sticky="w")

entStarr = Entry(frameinarr,font=("Arial",11))
entStarr.grid(row=7,column=1,pady=3,padx=3)
entCityarr= Entry(frameinarr,font=("Arial",11))
entCityarr.grid(row=7,column=2,pady=3,padx=3)

lblStarr = Label(frameinarr,text="Street",font=("Arial",10),fg="#0a2351",bg="#C0C0C0")
lblStarr.grid(row=8,column=1,pady=3,padx=3)
lblCityarr = Label(frameinarr,text="City",font=("Arial",10),fg="#0a2351",bg="#C0C0C0")
lblCityarr.grid(row=8,column=2,pady=3,padx=3)
entProvarr = Entry(frameinarr,font=("Arial",11))
entProvarr.grid(row=9,column=1,pady=3,padx=3)
cmbCountryarr=ttk.Combobox(frameinarr,font=("Arial",11),values=("Philippines","South korea","China", "Japan","Singgapore"))
cmbCountryarr.grid(row=9,column=2,pady=0,padx=0)

lblProvarr = Label(frameinarr,text="Province",font=("Arial",10),fg="#0a2351",bg="#C0C0C0")
lblProvarr.grid(row=10,column=1,pady=3,padx=3)
lblCountryarr = Label(frameinarr,text="Country",font=("Arial",10),fg="#0a2351",bg="#C0C0C0")
lblCountryarr.grid(row=10,column=2,pady=3,padx=3)

entZiparr = Entry(frameinarr,font=("Arial",11))
entZiparr.grid(row=11,column=1,pady=3,padx=3)

lblZiparr = Label(frameinarr,text="Zip",font=("Arial",10),fg="#0a2351",bg="#C0C0C0")
lblZiparr.grid(row=12,column=1,pady=3,padx=3)

lblrate = Label(frameinarr,text="Rate per Day:",font=("Arial",11),fg="#0a2351",bg="#C0C0C0")
lblrate.grid(row=13,column=0,pady=3,padx=3,sticky="w")

entrate = Entry(frameinarr,font=("Arial",11))
entrate.grid(row=14,column=0,pady=3,padx=3)

lblpay = Label(frameinarr,text="Payment:",font=("Arial",11),fg="#0a2351",bg="#C0C0C0")
lblpay.grid(row=13,column=1,pady=3,padx=3,sticky="w")

entpay = Entry(frameinarr,font=("Arial",11))
entpay.grid(row=14,column=1,pady=3,padx=3)

lblbal = Label(frameinarr,text="Balance:",font=("Arial",11),fg="#0a2351",bg="#C0C0C0")
lblbal.grid(row=13,column=2,pady=3,padx=3,sticky="w")

entbal = Entry(frameinarr,font=("Arial",11),bg="#C0C0C0",fg="red")
entbal.grid(row=14,column=2,pady=3,padx=3)

btnSavearr = Button(frameinarr,text="Save",font=("Arial",10,"bold"),bg="lime",activebackground="lime",activeforeground="white")
btnSavearr.bind("<Button-1>",save)
btnSavearr.grid(row=18,column=2,pady=3,padx=3)
btnclear = Button(frameinarr,text="clear",font=("Arial",10,"bold"),bg="blue",activebackground="blue",activeforeground="white")
btnclear.bind("<Button-1>",clearbutarr)
btnclear.grid(row=18,column=1,pady=3,padx=3)
btnupdate = Button(frameinarr,text="Update",font=("Arial",10,"bold"),bg="YELLOW",activebackground="YELLOW",activeforeground="white")
btnupdate.bind("<Button-1>",updatearr)
btnupdate.grid(row=18,column=0,pady=3,padx=3)

btncom = Button(frameinarr,text="Mark Done",font=("Arial",10,"bold"),bg="orange",activebackground="orange",activeforeground="white")
btncom.bind("<Button-1>",completed)
btncom.grid(row=20,column=0,pady=3,padx=3)

logout = Button(frameinarr, text="Logout", font=("Arial",10,"bold"),fg="#0a2351",bg="#ff2441", relief=RAISED)
logout.bind("<Button-1>",logoutt)
logout.grid(row=20, column=2, pady=3, padx=3)

entsearch= Entry(displayarr,font=("Arial",11),width=40,bg="#F5F5F5")
entsearch.place(x=860,y=160)

btnsearch = Button(displayarr,text="Search",font=("Arial",10,"bold"),bg="lime",activebackground="lime",activeforeground="white")
btnsearch.bind("<Button-1>",searcharr)
btnsearch.place(x=1200,y=160)

colsarr = ("ID","FUll_NAME","BIRTHDATE","CONTACT","GENDER","ADDRESS","DAYS","RATE","START_DATE","TUITION","STATUS","PAYMENT","BALANCE")
tablearr = ttk.Treeview(displayarr,height=12,show="headings",columns=colsarr)
tablearr.place(x=630,y=200)
tablearr.bind("<<TreeviewSelect>>",display_selectarr)

for col in colsarr:
    tablearr.heading(col,text=col)
showarr()
tablearr.column("ID",width=30,stretch=YES)
tablearr.column("FUll_NAME",width=60,stretch=YES)
tablearr.column("BIRTHDATE",width=60,stretch=YES)
tablearr.column("CONTACT",width=60,stretch=YES)
tablearr.column("GENDER",width=50,stretch=YES)
tablearr.column("ADDRESS",width=60,stretch=YES)
tablearr.column("DAYS",width=30,stretch=YES)
tablearr.column("RATE",width=40,stretch=YES)
tablearr.column("START_DATE",width=60,stretch=YES)
tablearr.column("TUITION",width=50,stretch=YES)
tablearr.column("STATUS",width=60,stretch=YES)
tablearr.column("PAYMENT",width=50,stretch=YES)
tablearr.column("BALANCE",width=50,stretch=YES)

displayarr.mainloop()