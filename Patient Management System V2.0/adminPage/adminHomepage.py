from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def mainPage(win, frame, usrN):
    frame.destroy()
    color ="#8e9db2"
    _font = ("Comic Sans MS", 12, "bold")

    menuFrame = Frame(win, bg='#b9cce8', borderwidth="2", relief="groove")
    menuFrame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

    submenuFrame = Frame(menuFrame, bg='#b9cce8')
    submenuFrame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    def profileclick(event):
        profileLabel.config(bg='light grey')
        for child in submenuFrame.winfo_children():
            child.destroy()

        def upClick(event):
            usernamePassLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            usernameLabel = Label(contentFrame, text="Username:", font =("Comic Sans MS", 15, "bold"), bg=color)
            usernameLabel.place(relx=0.35, rely=0.3)

            usernameContent = Label(contentFrame, text=usrN, bg=color, font=("Comic Sans MS", 15, "normal"))
            usernameContent.place(relx=0.5 , rely=0.3)

            def changePass():
                for child in contentFrame.winfo_children():
                    child.destroy()

                enterPLabel = Label(contentFrame, text="Existing Password:", font =("Comic Sans MS", 10, "bold"), bg=color)
                enterPLabel.place(relx=0.35, rely=0.3)

                enterPEntry = Entry(contentFrame,  show="*")
                enterPEntry.place(relx=0.5 , rely=0.3)

                enterNewPLabel = Label(contentFrame, text="New Password:",font =("Comic Sans MS", 10, "bold"), bg=color)
                enterNewPLabel.place(relx=0.35, rely=0.35)

                enterNewPEntry = Entry(contentFrame,  show="*")
                enterNewPEntry.place(relx=0.5, rely=0.35)

                reNewPLabel = Label(contentFrame, text="Retype New Password:",font =("Comic Sans MS", 10, "bold"), bg=color)
                reNewPLabel.place(relx=0.35, rely=0.4)

                reNewPEntry = Entry(contentFrame, show="*")
                reNewPEntry.place(relx=0.5, rely=0.4)

                def saveChange():
                    if p == enterPEntry.get():
                        if enterNewPEntry.get() == reNewPEntry.get():
                            database.changeApass(usrN, enterNewPEntry.get())
                            messagebox.showinfo('Success', 'Password updated')
                            contentFrame.destroy()
                            mainPage(win, menuFrame, usrN)
                        else:
                            messagebox.showerror("Error", "Retyped Password Dont Match the New Password")
                    else:
                        messagebox.showerror("Error", "Password Doesnt Match")

                saveChButton = Button(contentFrame, text="Save Changes", command=saveChange)
                saveChButton.place(relx=0.4, rely=0.45)

                def cancel():
                    contentFrame.destroy()
                    mainPage(win, menuFrame, usrN)

                cancelButton = Button(contentFrame, text="Cancel", command=cancel)
                cancelButton.place(relx=0.5, rely=0.45)

                p = database.adminPass(usrN)


            changePass = Button(contentFrame, text="Change Password", command=changePass)
            changePass.place(relx=0.4, rely=0.4)

        def buttoneffectUP(event):
            usernamePassLabel.config(bg='#b9cce8')
        
        usernamePassLabel = Label(submenuFrame, text='Account Details', bg='#b9cce8')
        usernamePassLabel.place(relx=0, rely=0.07, relwidth=1)
        usernamePassLabel.bind("<Button>", upClick)
        usernamePassLabel.bind("<ButtonRelease>", buttoneffectUP)

    def buttoneffectP(event):
        profileLabel.config(bg='#b9cce8')
        for child in contentFrame.winfo_children():
                child.destroy()


    profileLabel = Label(menuFrame, text='PROFILE', font=("Comic Sans MS", 10, "bold"), bg='#b9cce8')
    profileLabel.place(relx=0, rely=0.05, relwidth=0.5)
    profileLabel.bind("<Button>",profileclick)
    profileLabel.bind("<ButtonRelease>", buttoneffectP)


    def hospitalclick(event):
        HospitalLabel.config(bg='light grey')
        for child in submenuFrame.winfo_children():
            child.destroy()
        
        def hospital_reg(event):
            regHLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            hdata = database.getHospDet()

            if hdata == []:
                noRecordLabel = Label(contentFrame, text="No Hospital Registered", font =("Comic Sans MS", 40, "bold"), fg='dark grey', bg=color)
                noRecordLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
            else:
                noOfRec = len(hdata)
                HId_label = Label(contentFrame, text="Hospital Id",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                HId_label.place(relx=0, rely = 0.2)

                Hname_label = Label(contentFrame, text="Hospital Name",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                Hname_label.place(relx=0.3, rely=0.2)

                add_label = Label(contentFrame, text="Address",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                add_label.place(relx=0.6, rely=0.2)

                ph_label = Label(contentFrame, text="Phone Number",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                ph_label.place(relx=0.85, rely=0.2)

                y = 0.4
                if (noOfRec * 0.1 > 1):
                    d = 1/noOfRec
                else:
                    d = 0.1

                for i in range(noOfRec):
            
                    HId_val = Label(contentFrame, text=hdata[i]['_id'], width=25, bg=color, font =("Comic Sans MS", 10, "italic"))
                    HId_val.place(relx=0, rely=y)

                    Hname_val = Label(contentFrame, text=hdata[i]['name'], width=26, bg=color, wraplength =175  ,font =("Comic Sans MS", 10, "italic"))
                    Hname_val.place(relx=0.3, rely=y)

                    add_val = Label(contentFrame, text=hdata[i]['address'], width =25, bg=color,  wraplength =175 ,font =("Comic Sans MS", 10, "italic"))
                    add_val.place(relx=0.6, rely=y)

                    ph_val = Label(contentFrame, text=hdata[i]['phone'], width =25, bg=color, font =("Comic Sans MS", 10, "italic"))
                    ph_val.place(relx=0.8, rely=y)

                    y += d
 
        def buttoneffectHR(event):
            regHLabel.config(bg='#b9cce8')


        regHLabel = Label(submenuFrame, text='View Hospitals', bg='#b9cce8')
        regHLabel.place(relx=0, rely=0.12, relwidth=0.7)
        regHLabel.bind("<Button>", hospital_reg)
        regHLabel.bind("<ButtonRelease>", buttoneffectHR)

        def hospital_add(event):
            addHLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            hdataC = len(database.getHospDet())

            id = hdataC + 1

            headingLabel = Label(contentFrame, text="Register The Hospital: ", font =("Comic Sans MS", 15, "underline"), bg=color)
            headingLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
            HIdLabel = Label(contentFrame, text="Hospital Id: ", font =('Arial',12,'normal'), bg=color)
            HIdLabel.place(relx=0.3, rely=0.3)
            HIdData =Label(contentFrame, text=id , font =('Arial',12,'italic'), bg=color)
            HIdData.place(relx=0.5, rely=0.3)

            HNameLabel = Label(contentFrame, text="Hospital Name: ", font =('Arial',12,'normal'), bg=color)
            HNameLabel.place(relx=0.3, rely=0.45)
            HNameData = Entry(contentFrame, font =('Arial',12,'italic'))
            HNameData.place(relx=0.5, rely=0.45)

            HAddLabel = Label(contentFrame, text="Hospital Address: ", font =('Arial',12,'normal'), bg=color)
            HAddLabel.place(relx=0.3, rely=0.6)
            HAddData = Entry(contentFrame, font =('Arial',12,'italic'))
            HAddData.place(relx=0.5, rely=0.6)

            HPhoneLabel = Label(contentFrame, text="Hospital Phone Number: ", font =('Arial',12,'normal'), bg=color)
            HPhoneLabel.place(relx=0.3, rely=0.75)
            HPhoneData = Entry(contentFrame, font =('Arial',12,'italic'))
            HPhoneData.place(relx=0.5, rely=0.75)

            def cont():
                n = HNameData.get()
                a = HAddData.get()
                p = HPhoneData.get()

                if n=='' or a == '' or p == '':
                    messagebox.showerror("Fill Details", "Fill all the fields")
                        
                else:
                    for child in contentFrame.winfo_children():
                        child.destroy()
                    
                    userPFrame = LabelFrame(contentFrame, text="Create Username", bg= color)
                    userPFrame.grid(row=0, column=0)

                    username_label = Label(userPFrame, text='User Name', bg= color, width=44 )
                    username_label.grid(row=0, column=0)

                    username_entry = Entry(userPFrame,  width=44)
                    username_entry.grid(row=1, column=0, padx=5, pady=10)

                    import database
                
                    usernames = database.adminAuth()

                    def pass_entry():
                        
                        newUsername = username_entry.get()

                        for vals in usernames:
                            if newUsername == vals:
                                messagebox.showerror("Username Exists", "Try Again, This username exists!")
                                break

                        else:
                            username_entry.config(state='disabled')
                            username_entry.config({'background':color})
                            continueButton.destroy()

                            pass_label = Label(userPFrame, text='Create Password:',  bg= color, width=44 )
                            pass_label.grid(row=2, column=0)

                            pass_entry = Entry(userPFrame,show="*", width=44)
                            pass_entry.grid(row=3, column=0, padx=5, pady=10)

                            repass_label = Label(userPFrame, text='Retype Password:', bg= color, width=44 )
                            repass_label.grid(row=4, column=0)

                            repass_entry = Entry(userPFrame,show="*", width=44)
                            repass_entry.grid(row=5, column=0, padx=5, pady=10)

                            def create():
                                pas = pass_entry.get()
                                rpas = repass_entry.get()

                                if pas != rpas:
                                    messagebox.showerror("Error", "Passwords Dont Match")
                                else:
                                    data = {'_id':id, 'name':n,  'phone': p, 'address':a}
                                    userData = {'username': newUsername, 'password': pas, 'hid':id}
                                
                                    database.insertHopAuth(userData)
                                    database.insertHos(data)
                                    messagebox.showinfo("Created", "Account Created")
                                    contentFrame.destroy()
                                    mainPage(win, menuFrame, usrN)

                            createAccountButton = Button(userPFrame, text='Create Account', width=44, command=create)
                            createAccountButton.grid(row=6, column=0, padx=5,pady=10)

                    continueButton = Button(userPFrame, text='Continue', width=44, command=pass_entry)
                    continueButton.grid(row=2, column=0, pady=10, padx=5)

            
            contButton = Button(contentFrame, text="Next", font=_font, command= cont)
            contButton.place(relx=0.35, rely=0.9)

        def buttoneffectHA(event):
            addHLabel.config(bg='#b9cce8')

        addHLabel = Label(submenuFrame, text='New Hospital', bg='#b9cce8')
        addHLabel.place(relx=0, rely=0.17, relwidth=0.7)
        addHLabel.bind("<Button>", hospital_add)
        addHLabel.bind("<ButtonRelease>", buttoneffectHA)
    
    def buttoneffectH(event):
        HospitalLabel.config(bg= '#b9cce8')


    HospitalLabel = Label(menuFrame, text='HOSPITAL',  font=("Comic Sans MS", 10, "bold"), bg='#b9cce8')
    HospitalLabel.place(relx=0, rely=0.1, relwidth=0.5)
    HospitalLabel.bind("<Button>", hospitalclick)
    HospitalLabel.bind("<ButtonRelease>", buttoneffectH)


    def logout(event):
        logoutLabel.config(bg='grey')
        win.destroy()
        import mainPage
    
    def buttonLO(event):
        logoutLabel.config(bg='#b9cce8')

    logoutLabel = Label(menuFrame, text='Log Out', font =  ("Comic Sans MS", 10, "bold"), bg='#b9cce8')
    logoutLabel.place(relx=0, rely=0.95, relwidth=0.5)
    logoutLabel.bind('<Button>', logout)
    logoutLabel.bind('<ButtonRelease>', buttonLO)

    import database

    contentFrame = Frame(win, bg=color, bd=15, relief=RIDGE)
    contentFrame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

    welcomeText = Label(contentFrame, text="WELCOME", font=("Comic Sans MS", 40, "underline","bold"), bg=color)
    welcomeText.place(relx=0.5, rely=0.3, anchor=CENTER)