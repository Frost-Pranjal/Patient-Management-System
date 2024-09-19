from tkinter import *
from PIL import ImageTk, Image, ImageEnhance


     

def patient(window, frame):
    import patientPage.log as login
    login.signOrLog(window, frame)

def hospital(window, frame):
    import hospitalPage.log as loginH
    loginH.mainLog(window, frame)

def admin(window, frame):
    import adminPage.log as loginAd
    loginAd.mainLog(window, frame)

def main():
    mainPage = Tk()
    color ="#697a81"

    mainPage.wm_title("Wellness Record")
    mainPage.state('zoomed') 
    mainPage.configure(bg=color)
    mainPage.update()

    _font = ("Comic Sans MS", 19, "bold")

    img = Image.open("images\mainpageWallpaper.jpg")
    resized_image = img.resize((mainPage.winfo_width(), mainPage.winfo_height()))

    if img.mode != "RGBA":
        img = resized_image.convert("RGBA")
    else:
        img = resized_image.copy()
    alpha = img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.65)
    img.putalpha(alpha)
  
    bg = ImageTk.PhotoImage(img)
    background = Label(mainPage, image=bg)
    background.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
    background.image = bg

    userChoiceFrame = LabelFrame(mainPage, bd=15, relief=RIDGE)
    userChoiceFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    userChoiceFrame.configure(bg=color)

    frame_label = Label(userChoiceFrame, text="SIGN IN AS", font=('Arial',20,'underline') , bg=color)
    frame_label.grid(row=0, column=0, columnspan=2, pady=20)

    patient_icon = ImageTk.PhotoImage(Image.open("images/user icon.png"))
    patient_icon_label = Label(userChoiceFrame, image=patient_icon, bg=color)     # placing image
    patient_icon_label.grid(row=1, column=0)

    patientButton = Button(userChoiceFrame, text="PATIENT",  width=20, font=_font, command=lambda:patient(mainPage, userChoiceFrame))
    patientButton.grid(row=1, column=1, pady=40, padx=20)

    hospital_icon = ImageTk.PhotoImage(Image.open("images/hospital icon.png"))
    hospital_icon_label = Label(userChoiceFrame, image=hospital_icon, bg=color)     # placing image
    hospital_icon_label.grid(row=2, column=0)

    hospitalButton = Button(userChoiceFrame, text="HOSPITAL", width=20, font=_font, command=lambda: hospital(mainPage, userChoiceFrame))
    hospitalButton.grid(row=2, column=1, pady=40)

    admin_icon = ImageTk.PhotoImage(Image.open("images/admin icon.png"))
    admin_icon_label = Label(userChoiceFrame, image=admin_icon, bg=color)     # placing image
    admin_icon_label.grid(row=3, column=0)

    adminButton = Button(userChoiceFrame, text="ADMIN", width=20, font=_font,  command=lambda: admin(mainPage, userChoiceFrame))
    adminButton.grid(row=3, column=1, pady=40)


    mainPage.mainloop()


main()


