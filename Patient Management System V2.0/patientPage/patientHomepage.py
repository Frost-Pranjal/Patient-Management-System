import qrcode
from pymongo import MongoClient
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

_font = ("Comic Sans MS", 10, "bold")
color ="#d3d4c4"

def mainPage(win, frame, userNm):
    frame.destroy()
    win.wm_title("Patient User")

    def profileclick(event):
        profileLabel.config(bg='light grey')
        for child in submenuFrame.winfo_children():
            child.destroy()

        def pdClick(event):
            personalDetailsLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            def edit():
                nameConL.destroy()
                dobConL.destroy()
                phConL.destroy()
                addConL.destroy()

                nameConE = Entry(contentFrame,  font = ("Comic Sans MS", 10, "normal"), bg=color)
                nameConE.place(relx=0.4, rely=0.35)

                nameConE.insert(0, data["name"])

                dobConE = Entry(contentFrame,  font = ("Comic Sans MS", 10, "normal"), bg=color)
                dobConE.place(relx=0.4, rely=0.5)

                dobConE.insert(0, data["dob"])

                phConE = Entry(contentFrame,  font = ("Comic Sans MS", 10, "normal"), bg=color)
                phConE.place(relx=0.4, rely=0.65)

                phConE.insert(0, data["phoneNumber"])

                addConE = Entry(contentFrame,  font = ("Comic Sans MS", 10, "normal"), bg=color)
                addConE.place(relx=0.4, rely=0.8)

                addConE.insert(0, data["address"])

                emConE = Entry(contentFrame,  font = ("Comic Sans MS", 10, "normal"), bg=color)
                emConE.place(relx=0.4, rely=0.95)

                emConE.insert(0, data["email"])

                editButton.destroy()

                def saveChanges():
                    n = nameConE.get()
                    d = dobConE.get()
                    p = phConE.get()
                    a = addConE.get()
                    e = emConE.get()

                    _id = data["_id"]

                   
                    database.updateProfile(_id, n, d, p, a, e)
                    messagebox.showinfo('Updated', 'Changes Updates')
                    contentFrame.destroy()
                    mainPage(win, menuFrame, userNm)
                  


                saveButton = Button(contentFrame, text="Save Changes", bg=color, font=("Comic Sans MS", 12, "bold"), command=saveChanges)
                saveButton.place(relx=0.7, rely=0.1)

                def cancel():
                    contentFrame.destroy()
                    mainPage(win, menuFrame, userNm)
                
                cancelButton = Button(contentFrame, text="Cancel", bg=color, font=("Comic Sans MS", 12, "bold"), command=cancel)
                cancelButton.place(relx=0.85, rely=0.1)
        
            data = database.pFullDetails(uid)

            patIDLabel = Label(contentFrame, text = "ID: ", font = ("Comic Sans MS", 10, "italic"), bg=color)
            patIDLabel.place(relx=0.2, rely=0.2)

            patIdConL = Label(contentFrame, text = data["_id"], font = ("Comic Sans MS", 10, "normal"), bg=color )
            patIdConL.place(relx=0.4, rely=0.2)

            nameLabel = Label(contentFrame, text="Name: ", font = ("Comic Sans MS", 10, "italic"), bg=color)
            nameLabel.place(relx=0.2, rely=0.35)

            nameConL = Label(contentFrame, text= data["name"], font = ("Comic Sans MS", 10, "normal"), bg=color)
            nameConL.place(relx=0.4, rely=0.35)

            dobLabel = Label(contentFrame, text="Date of Birth: ", font = ("Comic Sans MS", 10, "italic"), bg=color)
            dobLabel.place(relx=0.2, rely=0.5)

            dobConL = Label(contentFrame, text= data["dob"], font = ("Comic Sans MS", 10, "normal"), bg=color)
            dobConL.place(relx=0.4, rely=0.5)

            phLabel = Label(contentFrame, text="Phone Number: ", font = ("Comic Sans MS", 10, "italic"), bg=color)
            phLabel.place(relx=0.2, rely = 0.65)

            phConL = Label(contentFrame, text= data["phoneNumber"], font = ("Comic Sans MS", 10, "normal"), bg=color)
            phConL.place(relx=0.4, rely=0.65)

            addLabel = Label(contentFrame, text="Address: ", font = ("Comic Sans MS", 10, "italic"), bg=color)
            addLabel.place(relx=0.2, rely=0.8)

            addConL = Label(contentFrame, text=data["address"], font = ("Comic Sans MS", 10, "normal"), bg=color)
            addConL.place(relx=0.4, rely=0.8)

            emailLabel = Label(contentFrame, text="Email: ", font = ("Comic Sans MS", 10, "italic"), bg=color)
            emailLabel.place(relx=0.2, rely=0.95)

            emailConL = Label(contentFrame, text=data["email"], font = ("Comic Sans MS", 10, "normal"), bg=color)
            emailConL.place(relx=0.4, rely=0.95)

            editButton = Button(contentFrame, text="Edit Profile", bg=color, font=("Comic Sans MS", 12, "bold"), command=edit)
            editButton.place(relx=0.7, rely=0.1)
        
        def buttoneffectPD(event):
            personalDetailsLabel.config(bg='#d4d4c4')
           

        def mhClick(event):
            medicalHistoryLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            rec = database.getMedRec(uid)

            def editAdd():
                for child in contentFrame.winfo_children():
                    child.destroy()

                global nR
                nR  = noOfRec+1
                if noOfRec ==  0:
                    nR = 1

                def nextRecord():
                    global nR
                    medText = Text(histFrame, width=20, height=2)
                    medText.grid(row=nR, column=0, pady=4)

                    durText = Text(histFrame,  width=20, height=2)
                    durText.grid(row=nR, column=1, pady=4)

                    statusText = Text(histFrame,  width=20, height=2)
                    statusText.grid(row=nR, column=2, pady=4)

                    next_button.grid(row=nR, column=3, padx=3)

                    def remove_rec():
                        global nR
                        medText.destroy()
                        durText.destroy()
                        statusText.destroy()
                        rem_button.destroy()
                        nR -=1

                    rem_button_image =ImageTk.PhotoImage(Image.open("patientPage/images/minusButton.png"))
                    rem_button = Button(histFrame, image=rem_button_image,  bg=color, command= remove_rec)
                    rem_button.image = rem_button_image
                    rem_button.grid(row=nR, column=4, padx=3)
                    nR += 1

                def remove_rec():
                    global nR
                    medText.destroy()
                    durText.destroy()
                    statusText.destroy()
                    rem_button.destroy()
                    nR -=1

                histFrame = Frame(contentFrame, bg=color)
                histFrame.place(relx=0.1, rely=0.2)

                med_det_label = Label(histFrame, text="Details of Illness",  bg= color, wraplength=137, padx=10, width=27)
                med_det_label.grid(row=0, column=0)

                duration_label = Label(histFrame, text="Duration of Illness (Mention the years as well)",  bg= color, wraplength=137, padx=10, width=27)
                duration_label.grid(row=0, column=1)

                status_label = Label(histFrame, text="Status (Under Medication or Cured)",  bg= color, wraplength=137, padx=10, width=27)
                status_label.grid(row=0, column=2)
                
                for records in range(0, noOfRec):
                    medText =Text(histFrame, width=20, height=2)
                    medText.grid(row=records+1, column=0, pady=4)
                    medText.insert(END, rec[records][0])

                    durText = Text(histFrame,  width=20, height=2)
                    durText.grid(row=records+1, column=1, pady=4)
                    durText.insert(END, rec[records][1])

                    statusText = Text(histFrame,  width=20, height=2)
                    statusText.grid(row=records+1, column=2, pady=4)
                    statusText.insert(END, rec[records][2])

                    rem_button_image =ImageTk.PhotoImage(Image.open("patientPage/images/minusButton.png"))
                    rem_button = Button(histFrame, image=rem_button_image,  bg=color)
                    rem_button.image = rem_button_image
                    rem_button.grid(row=records+1, column=4, padx=3)
                    rem_button.config(command=remove_rec)

                next_button_image =ImageTk.PhotoImage(Image.open("patientPage/images/plusButton.png"))
                next_button = Button(histFrame, image=next_button_image, bg=color, command=nextRecord)
                if noOfRec == 0:
                    next_button.grid(row=1, column=3, padx=7)
                    next_button.config(command= nextRecord )
                else:
                    next_button.grid(row=noOfRec, column=3, padx=7)
                next_button.image = next_button_image

                def saveChanges():
                    t=[]
                    for child in histFrame.winfo_children():
                        if isinstance(child, Text):
                            t.append(child.get("1.0",'end-1c'))
                    rec_num = int(len(t)/3)
                    t_rec=[]
                    index = 0

                    for r in range(rec_num):
                        t_rec.append([t[index], t[index+1], t[index+2]])
                        index +=3
                    
                    database.updateMedHistory(uid, t_rec)
                    messagebox.showinfo("Updated", "Medical History Updated")
                    contentFrame.destroy()
                    mainPage(win, menuFrame, userNm)

                saveButton = Button(contentFrame, text="Save Changes", bg=color, font=("Comic Sans MS", 12, "bold"), command=saveChanges)
                saveButton.place(relx=0.7, rely=0.1)

                def cancel():
                    contentFrame.destroy()
                    mainPage(win, menuFrame, userNm)
                
                cancelButton = Button(contentFrame, text="Cancel", bg=color, font=("Comic Sans MS", 12, "bold"), command=cancel)
                cancelButton.place(relx=0.85, rely=0.1)
                        
            if rec == []:
                noRecordLabel = Label(contentFrame, text="No Medical Record Inserted", font =("Comic Sans MS", 40, "bold"), fg='dark grey', bg=color)
                noRecordLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

                addButton = Button(contentFrame, text="Add Record", command=editAdd)
                addButton.place(relx=0.8, rely=0.1)
                noOfRec = 0

            else:
                noOfRec = len(rec)
                med_det_label = Label(contentFrame, text="Details of Illness",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                med_det_label.place(relx=0.1, rely = 0.2)

                duration_label = Label(contentFrame, text="Duration of Illness (Mention the years as well)",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                duration_label.place(relx=0.35, rely=0.2)

                status_label = Label(contentFrame, text="Status (Under Medication or Cured)",  bg= color, wraplength=137, padx=5, width=17, font=('Arial',10,'underline'))
                status_label.place(relx=0.6, rely=0.2)

                y = 0.4
                if (noOfRec * 0.1 > 1):
                    d = 1/noOfRec
                else:
                    d = 0.1

                for aRec in range(noOfRec):
                    med_det_val = Label(contentFrame, text=rec[aRec][0], width=20, bg=color, font =("Comic Sans MS", 10, "italic"))
                    med_det_val.place(relx=0.1, rely=y)

                    duration_val = Label(contentFrame, text=rec[aRec][1], width=20, bg=color, font =("Comic Sans MS", 10, "italic"))
                    duration_val.place(relx=0.35, rely=y)

                    status_val = Label(contentFrame, text=rec[aRec][2], width =20, bg=color, font =("Comic Sans MS", 10, "italic"))
                    status_val.place(relx=0.6, rely=y)

                    y += d

                editButton = Button(contentFrame, text="Edit Record", command=editAdd)
                editButton.place(relx=0.8, rely=0.1)
        
        def buttoneffectMH(event):
            medicalHistoryLabel.config(bg='#d4d4c4')


        def upClick(event):
            usernamePassLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            usernameLabel = Label(contentFrame, text="Username:", font =("Comic Sans MS", 15, "bold"), bg=color)
            usernameLabel.place(relx=0.35, rely=0.3)

            usernameContent = Label(contentFrame, text=userNm, bg=color, font=("Comic Sans MS", 15, "normal"))
            usernameContent.place(relx=0.5 , rely=0.3)

            def changePass():
                for child in contentFrame.winfo_children():
                    child.destroy()

                enterPLabel = Label(contentFrame, text="Existing Password:", font =("Comic Sans MS", 10, "bold"), bg=color)
                enterPLabel.place(relx=0.35, rely=0.3)

                enterPEntry = Entry(contentFrame)
                enterPEntry.place(relx=0.5 , rely=0.3)

                enterNewPLabel = Label(contentFrame, text="New Password:", font =("Comic Sans MS", 10, "bold"), bg=color)
                enterNewPLabel.place(relx=0.35, rely=0.35)

                enterNewPEntry = Entry(contentFrame)
                enterNewPEntry.place(relx=0.5, rely=0.35)

                reNewPLabel = Label(contentFrame, text="Retype New Password:", font =("Comic Sans MS", 10, "bold"), bg=color)
                reNewPLabel.place(relx=0.35, rely=0.4)

                reNewPEntry = Entry(contentFrame)
                reNewPEntry.place(relx=0.5, rely=0.4)

                def saveChange():
                    if p == enterPEntry.get():
                        if enterNewPEntry.get() == reNewPEntry.get():
                            database.changeP(userNm, enterNewPEntry.get())
                            messagebox.showinfo('Success', 'Password updated')
                            contentFrame.destroy()
                            mainPage(win, menuFrame, userNm)
                        else:
                            messagebox.showerror("Error", "Retyped Password Dont Match the New Password")
                    else:
                        messagebox.showerror("Error", "Password Doesnt Match")

                saveChButton = Button(contentFrame, text="Save Changes", command=saveChange)
                saveChButton.place(relx=0.4, rely=0.45)

                def cancel():
                    contentFrame.destroy()
                    mainPage(win, menuFrame, userNm)

                cancelButton = Button(contentFrame, text="Cancel", command=cancel)
                cancelButton.place(relx=0.5, rely=0.45)

                p = database.getPass(userNm)



            changePass = Button(contentFrame, text="Change Password", command=changePass)
            changePass.place(relx=0.4, rely=0.4)

        def buttoneffectUP(event):
            usernamePassLabel.config(bg='#d4d4c4')

        personalDetailsLabel = Label(submenuFrame, text='Personal Details', bg='#d4d4c4')
        personalDetailsLabel.place(relx=0, rely=0.07, relwidth=1)
        personalDetailsLabel.bind("<Button>", pdClick)
        personalDetailsLabel.bind("<ButtonRelease>", buttoneffectPD)

        medicalHistoryLabel = Label(submenuFrame, text='Medical History', bg='#d4d4c4')
        medicalHistoryLabel.place(relx=0, rely=0.12, relwidth=1)
        medicalHistoryLabel.bind("<Button>", mhClick)
        medicalHistoryLabel.bind("<ButtonRelease>", buttoneffectMH)

        usernamePassLabel = Label(submenuFrame, text='Account Details', bg='#d4d4c4')
        usernamePassLabel.place(relx=0, rely=0.17, relwidth=1)
        usernamePassLabel.bind("<Button>", upClick)
        usernamePassLabel.bind("<ButtonRelease>", buttoneffectUP)

    def buttoneffectP(event):
        profileLabel.config(bg= '#d4d4c4')

    def hospitalclick(event):
        HospitalLabel.config(bg='light grey')
        for child in submenuFrame.winfo_children():
            child.destroy()

        def hospital_connected(event):
            ConnectedLabel.config(bg='light grey')
            for child in contentFrame.winfo_children():
                child.destroy()

            hid = database.getHospConIds(uid)
            if hid == '':
                noDataLabel = Label(contentFrame, text="You are Not Under any Hospital At the Moment", font =("Comic Sans MS", 15, "bold"), bg=color)
                noDataLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
            else:
                hdata = database.getHospitalInfo(hid)
        
                headingLabel = Label(contentFrame, text="You are Currently Under: ", font =("Comic Sans MS", 15, "underline"), bg=color)
                headingLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
                HIdLabel = Label(contentFrame, text="Hospital Id: ", font =('Arial',12,'normal'), bg=color)
                HIdLabel.place(relx=0.3, rely=0.3)
                HIdData = Label(contentFrame, text=hdata["_id"] , font =('Arial',12,'italic'), bg=color)
                HIdData.place(relx=0.5, rely=0.3)

                HNameLabel = Label(contentFrame, text="Hospital Name: ",  wraplength=170,font =('Arial',12,'normal'), bg=color)
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

            InfoLabel = Label(contentFrame, text="If You Think There is a Mistake Please Contact the Administrartion at:", font =('Arial',8,'normal') , bg=color, fg='#333333')
            InfoLabel.place(relx=0.5, rely=0.85, anchor=CENTER)
            contactLabel = Label(contentFrame, text='wellness.storage.project@gmailcom', font =('Arial',8,'italic') , bg=color, fg='#333333')
            contactLabel.place(relx=0.5, rely=0.87, anchor=CENTER)

        def buttoneffectHC(event):
            ConnectedLabel.config(bg='#d4d4c4')

        ConnectedLabel = Label(submenuFrame, text='Connected', bg='#d4d4c4')
        ConnectedLabel.place(relx=0, rely=0.12, relwidth=0.7)
        ConnectedLabel.bind("<Button>", hospital_connected)
        ConnectedLabel.bind("<ButtonRelease>", buttoneffectHC)

        def hospitalHistory(event):
            HistoryLabel.config(bg='grey')
            for child in contentFrame.winfo_children():
                child.destroy()
            histData = database.getHospHist(uid)
            noOfHist = len(histData)
            if noOfHist == 0:
                noDataLabel = Label(contentFrame, text="You Dont Have Any History Record", font =("Comic Sans MS", 15, "bold"), bg=color)
                noDataLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
            else:
                hopIdLabel = Label(contentFrame, text="Hospital Id", bg=color, font =('Arial',12,'bold'))
                hopIdLabel.place(relx=0.2, rely=0.2)

                hopNameLabel = Label(contentFrame, text="Hospital Name", bg=color, font =('Arial',12,'bold'))
                hopNameLabel.place(relx=0.4, rely=0.2)

                hopStartingLabel = Label(contentFrame, text="File Openes On", bg=color, font =('Arial',12,'bold'))
                hopStartingLabel.place(relx=0.6, rely=0.2)

                hopEndingLabel = Label(contentFrame, text="File Closed On", bg=color, font =('Arial',12,'bold'))
                hopEndingLabel.place(relx=0.8, rely=0.2)

                y = 0.4
                for hosp in histData:
                    name = database.getHospitalInfo(int(hosp[0]))['name']
                    Label(contentFrame, text=hosp[0], bg=color, font =('Arial',12,'normal')).place(relx=0.2, rely=y)
                    Label(contentFrame, text=name, bg=color, wraplength=137,font =('Arial',12,'normal')).place(relx=0.4, rely=y)
                    Label(contentFrame, text=hosp[1], bg=color, font =('Arial',12,'normal')).place(relx=0.6, rely=y)
                    Label(contentFrame, text=hosp[2], bg=color, font =('Arial',12,'normal')).place(relx=0.8, rely=y)
                    y+=0.2
                
        def buttoneffectH(event):
            HistoryLabel.config(bg='#d4d4c4')

        HistoryLabel = Label(submenuFrame, text='History', bg='#d4d4c4')
        HistoryLabel.place(relx=0, rely=0.17, relwidth=0.7)
        HistoryLabel.bind('<Button>', hospitalHistory)
        HistoryLabel.bind('<ButtonRelease>', buttoneffectH)

    def buttoneffectH(event):
        HospitalLabel.config(bg= '#d4d4c4')

    def qrclick(event):
        qrLabel.config(bg='light grey')
        for child in submenuFrame.winfo_children():
            child.destroy()

        def qrClick(event):
            generateQrLabel.config(bg="light grey")
            for child in contentFrame.winfo_children():
                child.destroy()

            qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
            qr.add_data(userNm)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="#d4d4c4")


            def download_image():
                file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
                if file_path:
                    img.save(file_path)

            downloadButton = Button(contentFrame, text="Download QR Code", command=download_image, font=_font)
            downloadButton.place(relx=0.5, rely=0.5, relwidth=0.4, anchor=CENTER)

        def buttoneffectQR(event):
            generateQrLabel.config(bg="#d4d4c4")

        generateQrLabel = Label(submenuFrame, text='Create QR', bg='#d4d4c4')
        generateQrLabel.place(relx=0, rely=0.17, relwidth=0.7)
        generateQrLabel.bind("<Button>", qrClick)
        generateQrLabel.bind("<ButtonRelease>", buttoneffectQR)

    def buttoneffectQ(event):
        qrLabel.config(bg= '#d4d4c4')

    import database
    uid = database.getUidUser(userNm)

    menuFrame = Frame(win, bg='#d4d4c4', borderwidth="2", relief="groove")
    menuFrame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

    submenuFrame = Frame(menuFrame, bg='#d4d4c4')
    submenuFrame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    profileLabel = Label(menuFrame, text='PROFILE', font=_font, bg='#d4d4c4')
    profileLabel.place(relx=0, rely=0.05, relwidth=0.5)
    profileLabel.bind("<Button>",profileclick)
    profileLabel.bind("<ButtonRelease>", buttoneffectP)

    HospitalLabel = Label(menuFrame, text='HOSPITAL', font=_font, bg='#d4d4c4')
    HospitalLabel.place(relx=0, rely=0.1, relwidth=0.5)
    HospitalLabel.bind("<Button>", hospitalclick)
    HospitalLabel.bind("<ButtonRelease>", buttoneffectH)

    qrLabel = Label(menuFrame, text='QR CODE', font=_font, bg='#d4d4c4')
    qrLabel.place(relx=0, rely=0.15, relwidth=0.5)
    qrLabel.bind("<Button>", qrclick)
    qrLabel.bind("<ButtonRelease>", buttoneffectQ)

    def logout(event):
        logoutLabel.config(bg='grey')
        win.destroy()
        import mainPage
    
    def buttonLO(event):
        logoutLabel.config(bg='#d4d4c4')

    logoutLabel = Label(menuFrame, text='Log Out', font = _font, bg='#d4d4c4')
    logoutLabel.place(relx=0, rely=0.95, relwidth=0.5)
    logoutLabel.bind('<Button>', logout)
    logoutLabel.bind('<ButtonRelease>', buttonLO)


    contentFrame = Frame(win, bg=color, bd=15, relief=RIDGE)
    contentFrame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)


    welcomeText = Label(contentFrame, text="WELCOME", font=("Comic Sans MS", 40, "underline","bold"), bg=color)
    welcomeText.place(relx=0.5, rely=0.3, anchor=CENTER)
