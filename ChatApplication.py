#Registration page
from tkinter import *
import tkinter.messagebox as tm
import tkinter.scrolledtext as ScrolledTextObject
from urllib.request import urlopen
import threading
FileName = "RegistrationData.db"
TableName = "RegistrationDetails"
Counter = 0
def RegistrationPage():
	def RegisterButtonClick():	
		if Password.get() == "" or UserId.get() == "":
			tm.showerror("Registration error", "Enter valid details")
		else :
			if Password.get() != RetypePassword.get():
				tm.showerror("Registration error", "Password not matched")
			else:
				CheckRegistration()
	def CheckRegistration():
		print()
	def ClosePage():
		root.destroy()
	root = Tk(className = "Registration Page")
	root.geometry("500x500")
	RegisterLabel = Label(root,text = "Register", font = 30).grid(row = 0, column = 1)
	UserIdLabel = Label(root, text = "User Id:").grid(row = 1, sticky = "w")
	ExampleLabel = Label(root, text = "Example:Jhon123").grid(row = 2, column = 1)
	UserNameLabel = Label(root, text = "User Name:").grid(row = 3, sticky = "w")
	ExampleLabel = Label(root, text = "Example:Jhon Adem").grid(row = 4, column = 1)
	PasswordLabel = Label(root, text = "Password:").grid(row = 5, sticky = "w",pady=5)
	RetypePasswordLabel = Label(root, text = "Re-type Password:").grid(row = 7, sticky = "w",pady=5)
	UserId = Entry(root)
	UserName = Entry(root)
	Password= Entry(root, show = "*")
	RetypePassword = Entry(root, show = "*")
	UserId.grid(row = 1, column = 1)
	UserName.grid(row = 3, column = 1)
	Password.grid(row = 5, column = 1,pady=5)
	RetypePassword.grid(row = 7, column = 1,pady=5)
	RegisterButton = Button(root, text = "Register", fg = "blue", command = RegisterButtonClick).grid(row=8,sticky="w")
	RegisterButton = Button(root, text = "Cancel", fg = "blue", command = ClosePage).grid(row=8,column=1)
	root.mainloop()
def MassageFrame():
	def InsertMessage(event):
			Message = MessageEntry.get()
			textPad.insert(END, Message+"\n")
			MessageEntry.delete(0, END)
			return "break"
	def ReceiveMessage():
		TempVariable = 0
		while True :
			ReadMessageList = []
			Content = urlopen("http://192.241.244.177/MuraliKrishna/SendRecvMessage.php?flag=0&UserID=" + UserIdEntry1.get())
			for Value in Content:
				Text2 = Value.decode()
				for Data in Text2.split("<br>"):
					ReadMessageList.append(Data)
			if len(ReadMessageList) == 0:
				TempVariable = 1 #No Use
			else:
				for List in ReadMessageList:
					textPad.insert(END, "\t\t\t"+List+"\n")
	UserIdKey = ""
	Content = urlopen("http://192.241.244.177/MuraliKrishna/Login.php?UserId=" + UserIdEntry1.get() + "&Password="+ PasswordEntry2.get())
	for Value in Content:
		Text2 = Value.decode()
		for Data in Text2.split("<br>"):
	 		UserIdKey = Data
	if Data == "1" :
		threading.Thread(target=ReceiveMessage).start()
		MessageWindow = Tk()
		MessageWindow.geometry("355x490")
		PasswordEntry2.delete(0, END)
		ReadMessage = StringVar()
		textPad = ScrolledTextObject.ScrolledText(MessageWindow, width=47, height=30, bg="white")
		textPad.place(relx=.0, rely=.0 )
		MessageEntry = Entry(MessageWindow, text=ReadMessage, width=42)
		MessageEntry.place(relx=.0, rely=.89)
		MessageEntry.bind("<Return>", InsertMessage)
		MessageWindow.mainloop()
	else:
	 	tm.showinfo("LoginMessage", UserIdEntry1.get() + "  Invalid UserID or Password")
Root = Tk(className = "e-Chat")
Root.geometry("1200x500")
Loginabel = Label(Root, text = "Login-Page", font = 30).grid(row = 0, column = 1)
UserIdLogin = Label(Root, text = "User Id: ").grid(row = 1, sticky = "w")
PasswordLabel = Label(Root, text = "Password: ").grid(row = 2, sticky = "w")
UserIdEntry1 = Entry(Root)
PasswordEntry2 = Entry(Root, show = "*")
LoginButton = Button(Root, text = "login", fg = "blue", command = MassageFrame).grid(row = 7,pady=23,padx=11)
UserIdEntry1.grid(row = 1, column = 1)
PasswordEntry2.grid(row = 2, column = 1)
RegisterButton = Button(Root, text = "Register", fg = "blue", command = RegistrationPage).grid(row = 7, column = "1",pady=23)
Root.mainloop()
