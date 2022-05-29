from cgitb import text
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student import Student
import tkinter
import os
from train import Train
from recognition import Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #first img
        img=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\fr4.webp")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        #second img
        img1=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\fr3.jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third img

        img2=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\fr5.jfif")
        img2=img2.resize((560,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=560,height=130)


        #bg img
        img3=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="lime")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #student button
        img4=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\stuimg.jfif")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.std_det,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b2=Button(bg_img,text="Student Details",command=self.std_det,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b2.place(x=200,y=300,width=220,height=40)


         #recognition button
        img5=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\fare.gif")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.recog_data,cursor="hand2")
        b1.place(x=600,y=100,width=220,height=220)

        b2=Button(bg_img,text="Recognition",command=self.recog_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b2.place(x=600,y=300,width=220,height=40)

        #attendance
        img6=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\att.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=220)

        b2=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b2.place(x=1000,y=300,width=220,height=40)

        
        #train data
       
        img8=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\trda.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_det)
        b1.place(x=200,y=380,width=220,height=220)

        b2=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_det,font=("times new roman",15,"bold"),bg="white",fg="black")
        b2.place(x=200,y=580,width=220,height=40)

        #photos

        img9=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\fr2.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=380,width=220,height=220)

        b2=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b2.place(x=600,y=580,width=220,height=40)

        

        #exit

        img11=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=380,width=220,height=220)

        b2=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b2.place(x=1000,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return 


        #function buttons
        
    def std_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def recog_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    







        



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()