from argparse import FileType
from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os

root = Tk()
root.title("shareP")
root.geometry("450x560+500+200")
root.configure(bg = "#f4fdfe")
root.resizable(False,False)


def send():
    window = Toplevel(root)
    window.title("send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype =(('file_type','*.txt'),('all files','*.*')))
    
    def sender():
        s = socket.socket()
        host=socket.gethostname()
        port = 8080
        s.bind((host,port))
        s.listen(1)
        print('waiting for any incoming connection....')
        conn,addr =s.accept()
        file = open(filename,'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully....")

    #icon
    image_icon1 = PhotoImage(file="images/sendicon.png")
    window.iconphoto(False,image_icon1)
    
    sback_i = Image.open("images/sback.png")
    re = sback_i.resize((448,252), Image.LANCZOS)
    sbackground = ImageTk.PhotoImage(re)
    Label(window,image=sbackground).place(x=-2,y=0)

    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white',fg='black').place(x=140,y=290)

    Button(window,text="+ select file", width=9, height=1, font= 'arial 14 bold', bg="#fff",fg="#000",command=select_file).place(x=71,y=80)
    Button(window, text="SEND", width=8, height=1,font='arial 14 bold', bg="#000",fg="#fff",command=sender).place(x=270,y=80)

    window.mainloop()

def receive():
    main = Toplevel(root)
    main.title("receive")
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
        ID = SenderID.get()
        filename1 =incoming_file.get()

        s = socket.socket()
        port = 8080
        s.connect((ID,port))
        file = open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")

    #icon
    image_icon2 = PhotoImage(file="images/receiveicon.png")
    main.iconphoto(False,image_icon2)

    rback_i = Image.open("images/rback.png")
    re = rback_i.resize((448,252), Image.LANCZOS)
    rbackground = ImageTk.PhotoImage(re)
    Label(main, image=rbackground).place(x=-1,y=0)

    rlogo_i = Image.open("images/rlogo.png")
    rew = rlogo_i.resize((60,60), Image.LANCZOS)
    rlogo = ImageTk.PhotoImage(rew)
    Label(main, image=rlogo,bg="#f4fdfe").place(x=20,y=266)

    Label(main,text="Receive", font=('arial',20),bg="#f4fdfe").place(x=100,y=296)

    Label(main,text="Input sender id",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=340)
    SenderID = Entry(main,width=25,fg="black",border=2,bg="white",font=('arial',15))
    SenderID.place(x=20,y=370)
    SenderID.focus()

    Label(main,text="Filename for the incoming file",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=420)
    incoming_file = Entry(main,width=25,fg="black",border=2,bg="white",font=('arial',15))
    incoming_file.place(x=20,y=450)

    rbu_i = Image.open("images/rarrow.png")
    r = rbu_i.resize((50,50), Image.LANCZOS)
    rbu = ImageTk.PhotoImage(r)
    rr = Button(main,text="Receive",compound=LEFT,image=rbu,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)


    main.mainloop()

    
#icon
image_icon = PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)

Label(root,text = "File Transfer", font=('Acumin Variable Convept', 20, 'bold'), bg="#f4fdfe", fg="#2B1B17").place(x=20, y=30)
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

send_i = Image.open("images/send.png")
resi = send_i.resize((60,60), Image.LANCZOS)
send_image = ImageTk.PhotoImage(resi)
send =Button(root, image=send_image, bg="#f4fdfe", bd=0, command=send)
send.place(x=50, y=100)

receive_i = Image.open("images/receive.png")
resiz = receive_i.resize((60,60), Image.LANCZOS)
recieve_image = ImageTk.PhotoImage(resiz)
send =Button(root, image=recieve_image, bg="#f4fdfe", bd=0, command=receive)
send.place(x=300, y=100)

#labels
Label(root,text = "Send", font=('Acumin Variable Convept', 17, 'bold'), bg="#f4fdfe",fg="#045F5F").place(x=52, y=170)
Label(root,text = "Receive", font=('Acumin Variable Convept', 20, 'bold'), bg="#f4fdfe",fg="#045F5F").place(x=280, y=170)

back_i = Image.open("images/background.png")
res = back_i.resize((448,252), Image.LANCZOS)
background = ImageTk.PhotoImage(res)
Label(root, image=background).place(x=-1,y=308)


root.mainloop()