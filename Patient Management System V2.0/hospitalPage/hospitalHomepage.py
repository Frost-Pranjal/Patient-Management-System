from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import smtplib
from email.message import EmailMessage
import tkinter.filedialog as tkfd
import pyzbar.pyzbar as pyzbar
import cv2

def mainPage(win, frame, usrN):
    frame.destroy()
    color ="#065a78"
    _font = ("Comic Sans MS", 12, "bold")

    

    menuFrame = Frame(win, bg='#87afbe', borderwidth="2", relief="groove")
    menuFrame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

    submenuFrame = Frame(menuFrame, bg='#87afbe')
    submenuFrame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    def profileclick(event):
        profileLabel.config(bg='light grey')
        for child in submenuFrame.winfo_children():
            child.destroy()

        def pdClick(event):
            personalDetailsLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            hid = database.getHospId(usrN)
            hdata = database.getHospitalInfo(hid)

            headingLabel = Label(contentFrame, text="Your Details Are: ", font =("Comic Sans MS", 15, "underline"), bg=color)
            headingLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
            HIdLabel = Label(contentFrame, text="Hospital Id: ", font =('Arial',12,'normal'), bg=color)
            HIdLabel.place(relx=0.3, rely=0.3)
            HIdData = Label(contentFrame, text=hdata["_id"] , font =('Arial',12,'italic'), bg=color)
            HIdData.place(relx=0.5, rely=0.3)

            HNameLabel = Label(contentFrame, text="Hospital Name: ", font =('Arial',12,'normal'), bg=color)
            HNameLabel.place(relx=0.3, rely=0.45)
            HNameData = Label(contentFrame, text=hdata["name"], font =('Arial',12,'italic'), bg=color)
            HNameData.place(relx=0.5, rely=0.45)

            HAddLabel = Label(contentFrame, text="Hospital Address: ", font =('Arial',12,'normal'), bg=color)
            HAddLabel.place(relx=0.3, rely=0.6)
            HAddData = Label(contentFrame, text=hdata["address"], font =('Arial',12,'italic'), bg=color)
            HAddData.place(relx=0.5, rely=0.6)

            HPhoneLabel = Label(contentFrame, text="Hospital Phone Number: ", font =('Arial',12,'normal'), bg=color)
            HPhoneLabel.place(relx=0.3, rely=0.75)
            HPhoneData = Label(contentFrame, text=hdata["phone"], font =('Arial',12,'italic'), bg=color)
            HPhoneData.place(relx=0.5, rely=0.75)

            def edit():

                HNameData.destroy()
                HAddData.destroy()
                HPhoneData.destroy()

                HNameDataE = Entry(contentFrame,  font =('Arial',12,'italic'), bg=color)
                HNameDataE.place(relx=0.5, rely=0.45)
                HNameDataE.insert(0, hdata["name"])

                HAddDataE = Entry(contentFrame,  font =('Arial',12,'italic'), bg=color)
                HAddDataE.place(relx=0.5, rely=0.6)
                HAddDataE.insert(0, hdata["address"])

                HPhoneDataE = Entry(contentFrame, font =('Arial',12,'italic'), bg=color)
                HPhoneDataE.place(relx=0.5, rely=0.75)
                HPhoneDataE.insert(0, hdata['phone'])

                def saveChanges():
                    n = HNameDataE.get()
                    a = HAddDataE.get()
                    p = HPhoneDataE.get()

                    _id = hdata['_id']

                    database.updateHosp(_id, n, a, p)

                    messagebox.showinfo('Updated', 'Changes Updates')
                    contentFrame.destroy()
                    mainPage(win, menuFrame, usrN)


                saveButton = Button(contentFrame, text="Save Changes", bg=color, font=("Comic Sans MS", 12, "bold"), command=saveChanges)
                saveButton.place(relx=0.7, rely=0.1)

                def cancel():
                    contentFrame.destroy()
                    mainPage(win, menuFrame, usrN)
                
                cancelButton = Button(contentFrame, text="Cancel", bg=color, font=("Comic Sans MS", 12, "bold"), command=cancel)
                cancelButton.place(relx=0.85, rely=0.1)

            editButton = Button(contentFrame, text="Edit Details", bg=color, font=("Comic Sans MS", 12, "bold"), command=edit)
            editButton.place(relx=0.7, rely=0.1)

        def buttoneffectPD(event):
            personalDetailsLabel.config(bg='#87afbe')

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

                reNewPLabel = Label(contentFrame, text="Retype New Password:", font =("Comic Sans MS", 10, "bold"), bg=color)
                reNewPLabel.place(relx=0.35, rely=0.4)

                reNewPEntry = Entry(contentFrame, show="*")
                reNewPEntry.place(relx=0.5, rely=0.4)

                def saveChange():
                    if p == enterPEntry.get():
                        if enterNewPEntry.get() == reNewPEntry.get():
                            database.changeHpass(usrN, enterNewPEntry.get())
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

                p = database.getHpass(usrN)



            changePass = Button(contentFrame, text="Change Password", command=changePass)
            changePass.place(relx=0.4, rely=0.4)

        def buttoneffectUP(event):
            usernamePassLabel.config(bg='#87afbe')

        personalDetailsLabel = Label(submenuFrame, text='Hospital Details', bg='#87afbe')
        personalDetailsLabel.place(relx=0, rely=0.07, relwidth=1)
        personalDetailsLabel.bind("<Button>", pdClick)
        personalDetailsLabel.bind("<ButtonRelease>", buttoneffectPD)

        usernamePassLabel = Label(submenuFrame, text='Account Details', bg='#87afbe')
        usernamePassLabel.place(relx=0, rely=0.12, relwidth=1)
        usernamePassLabel.bind("<Button>", upClick)
        usernamePassLabel.bind("<ButtonRelease>", buttoneffectUP)

    def buttoneffectP(event):
        profileLabel.config(bg='#87afbe')
        for child in contentFrame.winfo_children():
                child.destroy()

    profileLabel = Label(menuFrame, text='PROFILE', font=("Comic Sans MS", 10, "bold"), bg='#87afbe')
    profileLabel.place(relx=0, rely=0.05, relwidth=0.5)
    profileLabel.bind("<Button>",profileclick)
    profileLabel.bind("<ButtonRelease>", buttoneffectP)

    def patientclick(event):
        patientLabel.config(bg='light grey')
        for child in submenuFrame.winfo_children():
            child.destroy()


        def view(event):
            ViewLabel.config(bg="light grey")
            for child in contentFrame.winfo_children():
                child.destroy()

            hid = database.getHospId(usrN)
            uids = database.patForHosp(hid)

            if uids == []:
                noRecordLabel = Label(contentFrame, text="No Patient Registered", font =("Comic Sans MS", 40, "bold"), fg='dark grey', bg=color)
                noRecordLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

            else:
                noOfRec = len(uids)
                patId_label = Label(contentFrame, text="Patient Id",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                patId_label.place(relx=0.1, rely = 0.2)

                patname_label = Label(contentFrame, text="Patient Name",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                patname_label.place(relx=0.35, rely=0.2)

                reg_label = Label(contentFrame, text="Registered On",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                reg_label.place(relx=0.6, rely=0.2)


                y = 0.4
                if (noOfRec * 0.1 > 1):
                    d = 1/noOfRec
                else:
                    d = 0.1

                for i in range(noOfRec):
                    name = database.pFullDetails(uids[i][0])
                    patId_val = Label(contentFrame, text=uids[i][0], width=20, bg=color, font =("Comic Sans MS", 10, "italic"))
                    patId_val.place(relx=0.1, rely=y)

                    patname_val = Label(contentFrame, text=name['name'], width=20, bg=color, font =("Comic Sans MS", 10, "italic"))
                    patname_val.place(relx=0.35, rely=y)

                    reg_val = Label(contentFrame, text=uids[i][1], width =20, bg=color, font =("Comic Sans MS", 10, "italic"))
                    reg_val.place(relx=0.6, rely=y)

                    def viewHist(patId):
                        for child in contentFrame.winfo_children():
                            child.destroy()
                        recM = database.getMedRec(patId)
                        noOfRecM = len(recM)
                        med_det_label = Label(contentFrame, text="Details of Illness",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                        med_det_label.place(relx=0.1, rely = 0.2)

                        duration_label = Label(contentFrame, text="Duration of Illness (Mention the years as well)",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                        duration_label.place(relx=0.35, rely=0.2)

                        status_label = Label(contentFrame, text="Status (Under Medication or Cured)",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                        status_label.place(relx=0.6, rely=0.2)

                        global yM 
                        yM = 0.4
                        if (noOfRecM * 0.1 > 1):
                            dM = 1/noOfRecM
                        else:
                            dM = 0.1

                        for aRec in range(noOfRecM):
                            med_det_val = Label(contentFrame, text=recM[aRec][0], width=20, bg=color, font =("Comic Sans MS", 10, "italic"))
                            med_det_val.place(relx=0.1, rely=yM)

                            duration_val = Label(contentFrame, text=recM[aRec][1], width=20, bg=color, font =("Comic Sans MS", 10, "italic"))
                            duration_val.place(relx=0.35, rely=yM)

                            status_val = Label(contentFrame, text=recM[aRec][2], width =20, bg=color, font =("Comic Sans MS", 10, "italic"))
                            status_val.place(relx=0.6, rely=yM)

                            yM += dM 

                        def add():
                            global yM
                            med_det_ent = Entry(contentFrame,  width=20, font =("Comic Sans MS", 10, "italic"))
                            med_det_ent.place(relx=0.1, rely=yM)

                            duration_ent = Entry(contentFrame, width=20,  font =("Comic Sans MS", 10, "italic"))
                            duration_ent.place(relx=0.35, rely=yM)

                            status_ent = Entry(contentFrame,  width =20,  font =("Comic Sans MS", 10, "italic"))
                            status_ent.place(relx=0.6, rely=yM)


                            def remove_rec():     
                                global yM                  
                                med_det_ent.destroy()
                                duration_ent.destroy()
                                status_ent.destroy()
                                rem_button.destroy()
                                yM -= dM
                                next_button.place(relx=0.8, rely=yM)

                            rem_button_image =ImageTk.PhotoImage(Image.open("patientPage/images/minusButton.png"))
                            rem_button = Button(contentFrame, image=rem_button_image,  bg=color, command= remove_rec)
                            rem_button.image = rem_button_image
                            rem_button.place(relx=0.9, rely=yM)

                            next_button.place(relx=0.8, rely=yM)

                            yM += dM

                            def saveChanges():
                                t=[]
                                for child in contentFrame.winfo_children():
                                    if isinstance(child, Entry):
                                        t.append(child.get())
                                rec_num = int(len(t)/3)
                                t_rec=[]
                                index = 0

                                for r in range(rec_num):
                                    t_rec.append([t[index], t[index+1], t[index+2]])
                                    index +=3

                                for r in recM:
                                    t_rec.append(r)
                                
                                database.updateMedHistory(patId, t_rec)
                                messagebox.showinfo("Updated", "Medical History Updated")
                                contentFrame.destroy()
                                mainPage(win, menuFrame, usrN)

                            saveButton = Button(contentFrame, text="Save Changes", bg=color, font=("Comic Sans MS", 12, "bold"), command=saveChanges)
                            saveButton.place(relx=0.7, rely=0.1)

                            def cancel():
                                contentFrame.destroy()
                                mainPage(win, menuFrame, usrN)
                
                            cancelButton = Button(contentFrame, text="Cancel", bg=color, font=("Comic Sans MS", 12, "bold"), command=cancel)
                            cancelButton.place(relx=0.85, rely=0.1)


                        next_button_image =ImageTk.PhotoImage(Image.open("patientPage/images/plusButton.png"))
                        next_button = Button(contentFrame, image=next_button_image, bg=color, command=add)  
                        next_button.image = next_button_image
                        next_button.place(relx=0.8, rely=y-d)                   


                    medHistButton = Button(contentFrame, text="View History", command=lambda: viewHist(uids[i][0]))
                    medHistButton.place(relx=0.85, rely=y)

                    y += d
        
        def buttoneffectV(event):
            ViewLabel.config(bg='#87afbe')

        ViewLabel = Label(submenuFrame, text='Registered Users', bg='#87afbe')
        ViewLabel.place(relx=0, rely=0.12, relwidth=0.7)
        ViewLabel.bind("<Button>", view)
        ViewLabel.bind("<ButtonRelease>", buttoneffectV)

        def addPat(event):
            AddPatLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()
            

            def verify(uid):
                hid = database.getHospId(usrN)
                uids = database.patForHosp(hid)

                uid = int(uid)

        

                for u in uids:
                    if int(uid) == u[0]:
                        messagebox.showerror('Error', 'This Patient is Already Registered under You Hospital')
                        mainPage(win, frame, usrN)
                        break
                else:
                    otp = random.randint(1000, 10000)
                    p ='jowjtbxbbzvkbivp'
                    e = 'wellness.storage.project@gmail.com'
                    usrE = database.pFullDetails(int(uid)) ['email']

                    msg = EmailMessage()
                    msg.set_content("THE VERIFICATION CODE FOR YOUR ACCOUNT "
                                    "IS %s" % str(otp))
                    msg['Subject'] = "Authentication"
                    msg["From"] = p
                    msg["To"] = usrE

                    # email connection server 587
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(e, p)
                    server.send_message(msg)

                    for child in contentFrame.winfo_children():
                        child.destroy()

                    otpLab = Label(contentFrame, text="Enter the OTP", font = ("Comic Sans MS", 10, "bold"))
                    otpLab.place(relx=0.5, rely=0.4, anchor=CENTER)

                    otpVer = Entry(contentFrame)
                    otpVer.place(relx=0.5, rely=0.5, anchor=CENTER)

                    def add():
                        if int(otpVer.get()) == otp:
                            hid = database.getHospId(usrN)
                            database.changeOngoing(uid)
                            database.addHosp(hid, uid)
                            messagebox.showinfo('Added', 'Patient Added')
                            contentFrame.destroy()
                            mainPage(win, menuFrame, usrN)
                        
                        else:
                            messagebox.showerror('Error', 'Incorrect OTP')
                            mainPage(win, frame, usrN)


                    subButton = Button(contentFrame, text="Submit", font=_font, command= add)
                    subButton.place(relx=0.5, rely=0.6, anchor=CENTER)


            def manual():
                for child in contentFrame.winfo_children():
                    child.destroy()

                userId = Label(contentFrame, text="Pateint's ID:", bg=color, font=_font)
                userId.place(relx=0.5, rely=0.3, anchor=CENTER)

                userIDE = Entry(contentFrame)
                userIDE.place(relx=0.5, rely=0.38, anchor=CENTER)

                submit = Button(contentFrame, text='Verify',command=lambda: verify(userIDE.get()), font=_font)
                submit.place(relx=0.5, rely=0.5, anchor=CENTER) 

            def qr():
                for child in contentFrame.winfo_children():
                    child.destroy()
                def decode_qr_code():
                    file_path = tkfd.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
                    if not file_path:
                        return

                    img = cv2.imread(file_path)
                    decoded = pyzbar.decode(img)
                    value = decoded[0].data.decode("utf-8")

                    uid = database.getUidUser(value)

                    submit = Button(contentFrame, text='Verify', width=20, font=_font, command=lambda: verify(uid))
                    submit.place(relx=0.5, rely=0.6, anchor=CENTER)                    

                    
                browse_button =Button(contentFrame, text="Browse", command=decode_qr_code, width=20, font=_font)
                browse_button.place(relx=0.5, rely=0.5, anchor=CENTER)


            manualButton = Button(contentFrame, text="Have the Patient ID?", width=20, font=_font,command=manual)
            manualButton.place(relx=0.2, rely=0.4)

            qrButton = Button(contentFrame, text="Have A QR Code?", width=20, font=_font,command=qr) 
            qrButton.place(relx=0.6, rely=0.4)

        def buttoneffectAP(event):
            AddPatLabel.config(bg='#87afbe')

        AddPatLabel = Label(submenuFrame, text='Add Patient', bg='#87afbe')
        AddPatLabel.place(relx=0, rely=0.17, relwidth=0.7)
        AddPatLabel.bind('<Button>', addPat)
        AddPatLabel.bind('<ButtonRelease>', buttoneffectAP)

        def delPat(event):
            DelPatLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            hid = database.getHospId(usrN)             
            uids = database.patForHosp(hid)

            if uids == []:
                noRecordLabel = Label(contentFrame, text="No Patient Registered", font =("Comic Sans MS", 40, "bold"), fg='dark grey', bg=color)
                noRecordLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

            else:
              
                noOfRec = len(uids)
                patId_label = Label(contentFrame, text="Patient Id",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                patId_label.place(relx=0.3, rely = 0.2)

                patname_label = Label(contentFrame, text="Patient Name",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                patname_label.place(relx=0.5, rely=0.2)

                y = 0.4
                if (noOfRec * 0.1 > 1):
                    d = 1/noOfRec
                else:
                    d = 0.1

                for i in range(noOfRec):
           
                    name = database.pFullDetails(uids[i][0])
                    patId_val = Label(contentFrame, text=uids[i][0], width=20, bg=color, font =("Comic Sans MS", 10, "italic"))
                    patId_val.place(relx=0.3, rely=y)

                    patname_val = Label(contentFrame, text=name['name'], width=20, bg=color, font =("Comic Sans MS", 10, "italic"))
                    patname_val.place(relx=0.5, rely=y)

                    def remove_rec():
                        database.changeOngoing(uids[i][0])
                        mainPage(win, frame, usrN)

                    rem_button_image =ImageTk.PhotoImage(Image.open("patientPage/images/minusButton.png"))
                    rem_button = Button(contentFrame, image=rem_button_image,  bg=color, command= remove_rec)
                    rem_button.image = rem_button_image
                    rem_button.place(relx=0.9, rely=y)

                    y += d

        def buttoneffectD(evel):
            DelPatLabel.config(bg='#87afbe')

        DelPatLabel = Label(submenuFrame, text='Delete Patient', bg='#87afbe')
        DelPatLabel.place(relx=0, rely=0.22, relwidth=0.7)
        DelPatLabel.bind('<Button>', delPat)
        DelPatLabel.bind('<ButtonRelease>', buttoneffectD)

    def buttoneffectPA(event):
        patientLabel.config(bg='#87afbe')

    patientLabel = Label(menuFrame, text='PATIENTS', font=("Comic Sans MS", 10, "bold"), bg='#87afbe')
    patientLabel.place(relx=0, rely=0.1, relwidth=0.5)
    patientLabel.bind("<Button>", patientclick)
    patientLabel.bind("<ButtonRelease>", buttoneffectPA)

    def logout(event):
        logoutLabel.config(bg='grey')
        win.destroy()
        import mainPage
    
    def buttonLO(event):
        logoutLabel.config(bg='#87afbe')

    logoutLabel = Label(menuFrame, text='Log Out', font =  ("Comic Sans MS", 10, "bold"), bg='#87afbe')
    logoutLabel.place(relx=0, rely=0.95, relwidth=0.5)
    logoutLabel.bind('<Button>', logout)
    logoutLabel.bind('<ButtonRelease>', buttonLO)

    import database

    contentFrame = LabelFrame(win, bg=color, bd=15, relief=RIDGE)
    contentFrame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

    

    welcomeText = Label(contentFrame, text="WELCOME", font=("Comic Sans MS", 40, "underline","bold"), bg=color)
    welcomeText.place(relx=0.5, rely=0.3, anchor=CENTER)
    