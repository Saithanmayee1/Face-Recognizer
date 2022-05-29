from ctypes.wintypes import INT
from distutils.log import debug
from tkinter import *
from tkinter import ttk
from turtle import right
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import insert
import csv
import os
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_attend_id=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dept=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()



        #first img
        img=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\stuimg.jfif")
        img=img.resize((700,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=700,height=200)
        #second img
        img1=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\fr2.png")
        img1=img1.resize((850,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=850,height=200)

        #bg img
        img3=Image.open(r"C:\Users\Jhanu\Documents\Face Recog Images\bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)


        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="lime")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=5,width=740,height=300)


        
        #labels and entries

        #attendance id
        attendanceId_Label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_Label.grid(row=1,column=0,padx=10,pady=20,sticky=W)

        attendanceId_Label=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,width=20,font=("times new roman",12,"bold"))
        attendanceId_Label.grid(row=1,column=2,padx=10,pady=20,sticky=W)

        #name
        name_Label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_Label.grid(row=1,column=5,padx=70,pady=20,sticky=W)

        name_Label=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        name_Label.grid(row=1,column=6,padx=0,pady=20,sticky=W)

        #date
        date_Label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_Label.grid(row=3,column=5,padx=70,pady=20,sticky=W)

        date_Label=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        date_Label.grid(row=3,column=6,padx=0,pady=20,sticky=W)

        #department
        department_Label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_Label.grid(row=3,column=0,padx=10,pady=20,sticky=W)

        department_Label=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dept,font=("times new roman",12,"bold"))
        department_Label.grid(row=3,column=2,padx=10,pady=20,sticky=W)

        #time
        time_Label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        time_Label.grid(row=5,column=0,padx=10,pady=20,sticky=W)

        time_Label=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        time_Label.grid(row=5,column=2,padx=10,pady=20,sticky=W)

        #attendance
        attendance_Label=Label(left_inside_frame,text="Attendance:",font=("times new roman",12,"bold"),bg="white")
        attendance_Label.grid(row=5,column=5,padx=70,pady=20,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_attend_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=5,column=6,pady=8)
        self.atten_status.current(0)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=4,y=230,width=720,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=39,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        save_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=38,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        update_btn.grid(row=0,column=1,padx=1)

        # delete_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        # delete_btn.grid(row=0,column=2,padx=1)

        # reset_btn=Button(btn_frame,text="Reset",width=19,command=self.reset_data,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        # reset_btn.grid(row=0,column=3,padx=1)

        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=445)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()   
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("AL1 File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("AL1 File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_attend_id.set(rows[0]),
        self.var_attend_name.set(rows[1]),
        self.var_attend_dept.set(rows[2]),
        self.var_attend_time.set(rows[3]),
        self.var_attend_date.set(rows[4]),
        self.var_attend_attendance.set(rows[5])

    
                    
       
                
                    
                   

    # def reset_data(self):
    #     self.var_attend_id.set("")
    #     self.var_attend_name.set("")
    #     self.var_attend_dept.set("")
    #     self.var_attend_time.set("")
    #     self.var_attend_date.set("")
    #     self.var_attend_attendance.set("Status")



    






        






if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()

