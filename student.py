from ctypes.wintypes import INT
from distutils.log import debug
from optparse import Values
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import insert




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_yr=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()





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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT DETAILS",font=("times new roman",35,"bold"),bg="white",fg="lime")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        current_course_frame.place(x=15,y=0,width=720,height=150)

        #department label
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),width=19,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science(AI)","Computer Science(DS)","IT","ECE","EEE","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=4,pady=14,sticky=W)

        #course label
        course_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=1,column=2,padx=30,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=19,state="readonly")
        course_combo["values"]=("Select Course","BE","B.Tech")
        course_combo.current(0)
        course_combo.grid(row=1,column=3,padx=25,pady=14,sticky=W)

        #year
        
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=5,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_yr,font=("times new roman",12,"bold"),width=19,state="readonly")
        year_combo["values"]=("Select Year","I","II","III","IV")
        year_combo.current(0)
        year_combo.grid(row=5,column=1,padx=4,pady=30,sticky=W)

        #Semester
        sem_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=5,column=2,padx=30,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=19,state="readonly")
        sem_combo["values"]=("Select Semester","I","II")
        sem_combo.current(0)
        sem_combo.grid(row=5,column=3,padx=25,pady=30,sticky=W)

        #student class info
        stud_cls_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        stud_cls_frame.place(x=10,y=170,width=720,height=380)

        #std id
        std_id_label=Label(stud_cls_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        std_id_label.grid(row=1,column=0,padx=10,pady=20,sticky=W)

        std_id_entry=ttk.Entry(stud_cls_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        std_id_entry.grid(row=1,column=2,padx=10,pady=20,sticky=W)

        #std name
        std_name_label=Label(stud_cls_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        std_name_label.grid(row=1,column=5,padx=30,pady=20,sticky=W)

        std_name_entry=ttk.Entry(stud_cls_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        std_name_entry.grid(row=1,column=7,padx=20,pady=20,sticky=W)

         #class division
        cls_div_label=Label(stud_cls_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        cls_div_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        cls_div_combo=ttk.Combobox(stud_cls_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        cls_div_combo["values"]=("Select Division","A","B","C")
        cls_div_combo.current(0)
        cls_div_combo.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(stud_cls_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=5,padx=30,pady=5,sticky=W)

        gender_combo=ttk.Combobox(stud_cls_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=7,padx=20,pady=5,sticky=W)

        #date of birth
        dob_label=Label(stud_cls_frame,text="Date of Birth:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=3,column=0,padx=10,pady=20,sticky=W)

        dob_entry=ttk.Entry(stud_cls_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=3,column=2,padx=10,pady=20,sticky=W)

        #email
        mail_id_label=Label(stud_cls_frame,text="Email ID:",font=("times new roman",12,"bold"),bg="white")
        mail_id_label.grid(row=3,column=5,padx=30,pady=20,sticky=W)

        mail_id_entry=ttk.Entry(stud_cls_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        mail_id_entry.grid(row=3,column=7,padx=20,pady=20,sticky=W)

        #phone no.
        phone_no_label=Label(stud_cls_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(stud_cls_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        #address
        add_label=Label(stud_cls_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=4,column=5,padx=30,pady=5,sticky=W)

        add_entry=ttk.Entry(stud_cls_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=4,column=7,padx=20,pady=5,sticky=W)

        #teacher
        teacher_label=Label(stud_cls_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=5,column=0,padx=10,pady=15,sticky=W)

        teacher_entry=ttk.Entry(stud_cls_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=5,column=2,padx=10,pady=15,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(stud_cls_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        #self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(stud_cls_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=2)

        #button frame
        btn_frame=Frame(stud_cls_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=4,y=280,width=700,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        save_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        update_btn.grid(row=0,column=1,padx=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.del_data,width=18,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        delete_btn.grid(row=0,column=2,padx=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        reset_btn.grid(row=0,column=3,padx=1)

        #new button frame
        btn_frame1=Frame(stud_cls_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=4,y=315,width=700,height=36)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=38,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        take_photo_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame1,text="Update Photo Sample",width=37,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        update_btn.grid(row=0,column=3,padx=1)

        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="View Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height=580)

        #mini frame
        mini_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        mini_frame.place(x=5,y=15,width=630,height=540)

        #search bar
        search_label=Label(mini_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=30,sticky=W)

        self.var_combo_search=StringVar()
        search_combo=ttk.Combobox(mini_frame,textvariable=self.var_combo_search,font=("times new roman",12,"bold"),width=18,state="readonly")
        search_combo["values"]=("Select","std_id","phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=2,padx=5,pady=30,sticky=W)

        self.var_search=StringVar()
        phone_no_entry=ttk.Entry(mini_frame,textvariable=self.var_search,width=15,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=0,column=3,padx=1,sticky=W)
        

        search_btn=Button(mini_frame,command=self.search_data,text="Search",width=10,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        search_btn.grid(row=0,column=4,padx=3)

        show_all_btn=Button(mini_frame,command=self.fetch_data,text="Show All",width=10,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        show_all_btn.grid(row=0,column=5,padx=3)

        #table frame
        table_frame=Frame(mini_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=90,width=615,height=430)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.stud_table=ttk.Treeview(table_frame,column=("std id","std name","dep","course","year","sem","class div","gender","dob","email","phoneno","address","teacher name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)

        self.stud_table.heading("dep",text="Department")
        self.stud_table.heading("course",text="Course")
        self.stud_table.heading("year",text="Year")
        self.stud_table.heading("sem",text="Semester")
        self.stud_table.heading("std id",text="Student ID")
        self.stud_table.heading("std name",text="Student Name")
        self.stud_table.heading("class div",text="Class Division")
        self.stud_table.heading("gender",text="Gender")
        self.stud_table.heading("dob",text="Date of Birth")
        self.stud_table.heading("email",text="Email")
        self.stud_table.heading("phoneno",text="Phone No")
        self.stud_table.heading("address",text="Address")
        self.stud_table.heading("teacher name",text="Teacher Name")

        self.stud_table["show"]="headings"
        self.stud_table.column("dep",width=200)
        self.stud_table.column("course",width=200)
        self.stud_table.column("year",width=200)
        self.stud_table.column("sem",width=200)
        self.stud_table.column("std id",width=200)
        self.stud_table.column("std name",width=200)
        self.stud_table.column("class div",width=200)
        self.stud_table.column("gender",width=200)
        self.stud_table.column("dob",width=200)
        self.stud_table.column("email",width=200)
        self.stud_table.column("phoneno",width=200)
        self.stud_table.column("address",width=200)
        self.stud_table.column("teacher name",width=200)
        self.stud_table.pack(fil=BOTH,expand=1)
        self.stud_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

        #function declaration

    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_yr.get()=="Select year" or self.var_sem.get()=="Select Semester" or  self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_div.get()=="Select Division" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="saithanmayeepaida",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_dept.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_yr.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                                                    ))
                # my_str="insert into student values('"+self.var_std_id.get()+"','"+self.var_std_name.get()+"','"+self.var_dept.get()+"','"+self.var_course.get()+"','"+self.var_yr.get()+"','"+self.var_sem.get()+"','"+self.var_div.get()+"','"+self.var_gender.get()+"','"+self.var_dob.get()+"','"+self.var_email.get()+"','"+self.var_phone.get()+"','"+self.var_address.get()+"','"+self.var_teacher.get()+"','"+self.var_radio1.get()+"')" 
                # debug
                

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #fetch
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="saithanmayeepaida",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.stud_table.delete(*self.stud_table.get_children())
            for i in data:
                self.stud_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dept.set(data[2]),
        self.var_course.set(data[3]),
        self.var_yr.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13])

    #update function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_yr.get()=="Select year" or self.var_sem.get()=="Select Semester" or  self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_div.get()=="Select Division" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
        else:
            try:
                Up_date=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Up_date>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="saithanmayeepaida",database="face_recogniser")
                    my_cursor=conn.cursor() 
                    debug
                    my_update_Str = "update student set std_name='"+self.var_std_name.get()+"',dept='"+self.var_dept.get()+"',course='"+self.var_course.get()+"',year='"+self.var_yr.get()+"',sem='"+self.var_sem.get()+"',division='"+self.var_div.get()+"',gender='"+self.var_gender.get()+"',dob='"+self.var_dob.get()+"',email_id='"+self.var_email.get()+"',phone_no='"+self.var_phone.get()+"',City='"+self.var_address.get()+"',Teacher_Name='"+self.var_teacher.get()+"',photo_sample='"+self.var_phone.get()+"' where std_id='"+self.var_std_id.get()+"'"

                    #messagebox.showerror("Error",my_update_Str,parent=self.root)
                    
                    my_cursor.execute(my_update_Str)
                else:
                    if not Up_date:
                        return
                messagebox.showinfo("Success","Student details sucessfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    #delete function
    def del_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student details?",parent=self.root)
                if delete > 0 :
                    conn=mysql.connector.connect(host="localhost",username="root",password="saithanmayeepaida",database="face_recogniser")
                    my_cursor=conn.cursor() 
                    sql="delete from student where std_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_yr.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_div.set("Select Division")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")      

    #generate dataset 
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_yr.get()=="Select year" or self.var_sem.get()=="Select Semester" or  self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_div.get()=="Select Division" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="saithanmayeepaida",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_generate_Str = "update student set std_name='"+self.var_std_name.get()+"',dept='"+self.var_dept.get()+"',course='"+self.var_course.get()+"',year='"+self.var_yr.get()+"',sem='"+self.var_sem.get()+"',division='"+self.var_div.get()+"',gender='"+self.var_gender.get()+"',dob='"+self.var_dob.get()+"',email_id='"+self.var_email.get()+"',phone_no='"+self.var_phone.get()+"',City='"+self.var_address.get()+"',Teacher_Name='"+self.var_teacher.get()+"',photo_sample='"+self.var_phone.get()+"' where std_id='"+self.var_std_id.get()+"'"
                my_cursor.execute(my_generate_Str)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                #load predefinied data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed succesfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #search data
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select an option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="saithanmayeepaida",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.stud_table.delete(*self.stud_table.get_children())
                    for i in data:
                        self.stud_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)






        
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()