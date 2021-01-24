from tkinter import*
from pymysql import*


def main_page():
    
    tw=Tk()    
    #tw.state('zoomed')
    tw.geometry('900x720+350+0')
    tw.resizable(width=False,height=False)
    tw.title('Student Information System')
    tw.configure(background='white')

    label_0=Label(tw,bg='darkcyan',fg='white',width=50,height=2,text='Student Information System',font='cursive 20 bold')
    label_0.pack(fill=X)

    label_1=Label(tw,bg='white',text='Username :',width=20,font='cursve 10 bold')
    label_1.place(x=250,y=180)

    e1=Entry(tw,width=40)
    e1.place(x=400,y=180)

    label_2=Label(tw,bg='white',text='Password :',width=20,font='cursve 10 bold')
    label_2.place(x=250,y=230)

    e2=Entry(tw,show='*',width=40)
    e2.place(x=400,y=230)

    Button(tw,command=lambda:login(e1,e2,tw),text='Login',bg='darkcyan',fg='white',).place(x=350,y=280)

    Button(tw,command=lambda:forgot_pswrd(tw),text='Forgot Password ?',bg='white').place(x=450,y=280)


    label_3=Label(tw,text='Not registered yet?',bg='white',width=30,font='cursive 10 bold')
    label_3.place(x=330,y=350)

    Button(tw,command=lambda:signup(tw),text='SignUp',bg='darkcyan',fg='white').place(x=395,y=380)

    tw.mainloop()
  

#................GUI end.................................................................................................................

#................main account............................................................................................................    

def account(tw):
        tw.destroy()
        login1=Tk()
        
        login1.title('Welcome to your account')
        login1.state('zoomed')
        login1.configure(bg='white')
        login1.resizable(width=False,height=False)
        label_14=Label(login1,text='Student Information System',bg='darkcyan',fg='white',width=50,height=2,font='cursive 20 bold').pack(fill=X)
        Button(login1,command=lambda:open_main(login1),text='Logout',bg='darkcyan',fg='white').place(x=1200,y=100)

        #......Entry Section...................................................................................................................
        frame_1=Frame(login1,width=400,height=400)
        frame_1.place(x=50,y=200)

        label_15=Label(frame_1,text='Roll No. :',font='cursive 10 bold')
        label_15.place(x=50,y=100)

        e9=Entry(frame_1,width=40)
        e9.place(x=130,y=100)

        label_16=Label(frame_1,text='Name :',font='cursive 10 bold')
        label_16.place(x=50,y=150)

        e10=Entry(frame_1,width=40)
        e10.place(x=130,y=150)

        label_17=Label(frame_1,text='Marks :',font='cursive 10 bold')
        label_17.place(x=50,y=200)

        e11=Entry(frame_1,width=40)
        e11.place(x=130,y=200)

        label_18=Label(frame_1,text='Entry Section',font='cursive 15 bold')
        label_18.place(x=50,y=30)
        

        

        def submit_entry(e9,e10,e11):
            con=connect(host='localhost',user='root',password='',database='pydb')
            cursor=con.cursor()
            roll=e9.get()
            name=e10.get()
            marks=e11.get()
            print(marks)
            if(cursor.execute("Select roll from entry where roll='"+roll+"'")==1):
               label_19=Label(frame_1,text='Error! Data Already Entered',fg='red',font='cursive 15 bold')
               label_19.place(x=100,y=300)
               con.close()
            else:
               cursor.execute("insert into entry values(%s,%s,%s)",(roll,name,marks))
               con.commit()
               label_19=Label(frame_1,text='Data Entered Successfully',fg='green',font='cursive 15 bold')
               label_19.place(x=100,y=300)
               con.close()

        def update_entry(e9,e10,e11):
            con=connect(host='localhost',user='root',password='',database='pydb')
            cursor=con.cursor()
            roll=e9.get()
            name=e10.get()
            marks=e11.get()
            
            if(cursor.execute("Select roll from entry where roll='"+roll+"'") and len(name)!=0 and len(marks)!=0):
                cursor.execute("update entry set name='"+name+"',marks='"+marks+"' where roll='"+roll+"'")
                con.commit()
                label_20=Label(frame_1,text='Data  Updated  Successfully',fg='green',font='cursive 15 bold')
                label_20.place(x=100,y=300)
                con.close()
            else:
                label_20=Label(frame_1,text='Error!  Unable  to  find  data',fg='red',font='cursive 15 bold')
                label_20.place(x=100,y=300)
                con.close()
                

        def delete_entry(e9,e10,e11):
            con=connect(host='localhost',user='root',password='',database='pydb')
            cursor=con.cursor()
            roll=e9.get()
            name=e10.get()
            marks=e11.get()
            
            if(cursor.execute("Select roll from entry where roll='"+roll+"'")):
                cursor.execute("delete from entry where roll='"+roll+"'")
                con.commit()
                label_20=Label(frame_1,text='Data  Deleted  Successfully',fg='green',font='cursive 15 bold')
                label_20.place(x=100,y=300)
                con.close()
            else:
                label_21=Label(frame_1,text='Error! Unable to find  data',fg='red',font='cursive 15 bold')
                label_21.place(x=100,y=300)
                con.close()
                
                      
               
        Button(frame_1,command=lambda:submit_entry(e9,e10,e11),text='Submit',bg='darkcyan',fg='white',).place(x=130,y=250)
        Button(frame_1,command=lambda:update_entry(e9,e10,e11),text='Update',bg='darkcyan',fg='white',).place(x=210,y=250)
        Button(frame_1,command=lambda:delete_entry(e9,e10,e11),text='Delete',bg='darkcyan',fg='white',).place(x=290,y=250)      

       #...........Student Record Display...............................................................................................     
        
        frame_2=Frame(login1,width=800,height=400)
        frame_2.place(x=500,y=200)

        label_22=Label(frame_2,text='Student Record Display',font='cursive 15 bold')
        label_22.place(x=50,y=30)

        label_23=Label(frame_2,text='Roll No. :',font='cursive 10 bold')
        label_23.place(x=50,y=80)

        e31=Entry(frame_2,width=40)
        e31.place(x=130,y=80)

        Button(frame_2,command=lambda:record_show(e31),text='Search',bg='darkcyan',fg='white').place(x=400,y=75)

        def record_show(e31):
            con=connect(host='localhost',user='root',password='',database='pydb')
            cursor=con.cursor()
            roll=e31.get()
            if(cursor.execute("Select roll from entry where roll='"+roll+"'")):
                cursor.execute("Select * from entry where roll='"+roll+"'")
                data=cursor.fetchone()
                #print(data)
                i=50
                Label(frame_2,text=data[0]).place(x=i,y=120)
                Label(frame_2,text=data[1]).place(x=150,y=120)
                Label(frame_2,text=data[2]).place(x=250,y=120)
                
            
        
            
            
            

       
        
#........Login validation................................................................................................................
    
def login(e1,e2,tw):
    
    #connect with database
    con=connect(host='localhost',user='root',password='',database='pydb')
    cursor=con.cursor()
    username=e1.get()
    password=e2.get()
    
        
    if(cursor.execute("select email,password from projectdb where email='"+username+"' and password='"+password+"'")):
        account(tw)
        

        
    
        
        
        
        #label_4=Label(tw,text='Welcome to your account',bg='white',fg='green',font='cursive 20 normal')
        #label_4.place(x=490,y=450)
    else:
       label_5=Label(tw,text='Invalid Username or Password!',bg='white',fg='red',font='cursive 20 normal')
       label_5.place(x=490,y=450)
       con.close()
       #exit()

#............SignUp........................................................................................................................

        

def signup(tw):
    signup=Tk() 
    signup.title('Registration')
    signup.geometry('600x720+350+0')
    signup.resizable(width=False,height=False)
    signup.configure(background='white')
        
    label_6=Label(signup,text='Student Information System',bg='darkcyan',fg='white',font='cursive 20 bold',height=2)
    label_6.pack(fill=X)

    label_7=Label(signup,text='Registration',bg='white',font='bold 15')
    label_7.place(x=180,y=150)

    label_8=Label(signup,text='Name :',bg='white',width=20,font='cursive 10 bold')
    label_8.place(x=50,y=220)

    e3=Entry(signup,width=40)
    e3.place(x=200,y=220)

    label_9=Label(signup,text='Email :',bg='white',width=20,font='cursive 10 bold')
    label_9.place(x=50,y=270)

    e4=Entry(signup,width=40)
    e4.place(x=200,y=270)

    label_10=Label(signup,text='Password :',bg='white',width=20,font='cursive 10 bold')
    label_10.place(x=50,y=320)

    e5=Entry(signup,show='*',width=40)
    e5.place(x=200,y=320)

    label_11=Label(signup,text='Mobile :',bg='white',width=20,font='cursive 10 bold')
    label_11.place(x=50,y=370)

    e6=Entry(signup,width=40)
    e6.place(x=200,y=370)

    Button(signup,command=lambda:submit(e3,e4,e5,e6,tw),text='Signup',bg='darkcyan',fg='white').place(x=110,y=420)
    

    def submit(e3,e4,e5,e6,tw):
        #connection()
        #connect with database
        con=connect(host='localhost',user='root',password='',database='pydb')
        cursor=con.cursor()
    
        #Take data and store in the given variables
        name=e3.get()
        email=e4.get()
        password=e5.get()
        mobile=e6.get()


        if(cursor.execute("Select email,mobile from projectdb where email='"+email+"' and mobile='"+mobile+"'"))==1:
            label_13=Label(signup,text='Error! User already registered',bg='white',fg='red',font='cursive 20 normal')
            label_13.place(x=110,y=470)
        else:    
            #Store data in database
            cursor.execute("insert into projectdb values(%s,%s,%s,%s)",(name,email,password,mobile))
            con.commit()
            account(tw)
            signup.destroy()
            con.close()
            #label_12=Label(signup,text='Registration Complete successfully',bg='white',fg='green',font='cursive 20 normal')
            #label_12.place(x=110,y=470)

#...........Forgot Password.......................................................................................................................................
            
def forgot_pswrd(tw):
    
    
    forgot=Tk()
    forgot.title('Reset Password')
    forgot.geometry('600x720+350+0')
    forgot.configure(background='white')
    forgot.resizable(width=False,height=False)
    
    label_14=Label(forgot,text='Student Information System',bg='darkcyan',fg='white',font='cursive 20 bold',height=2)
    label_14.pack(fill=X)

    label_15=Label(forgot,text='Email :',bg='white',font='cursive 10 bold')
    label_15.place(x=110,y=170)

    e6=Entry(forgot,width=43)
    e6.place(x=180,y=170)

    Button(forgot,command=lambda:check_email(e6,tw),text='Submit',bg='darkcyan',fg='white').place(x=110,y=220)

    def check_email(e6,tw):
        con=connect(host='localhost',user='root',password='',database='pydb')
        cursor=con.cursor()
        
        email=e6.get()
        if(cursor.execute("Select email from projectdb where email='"+email+"'"))==1:
            label_16=Label(forgot,text='New Password :',bg='white',font='cursive 10 bold')
            label_16.place(x=110,y=270)

            e7=Entry(forgot,show='*',width=43)
            e7.place(x=215,y=270)

            label_18=Label(forgot,text='Confirm Password :',bg='white',font='cursive 10 bold')
            label_18.place(x=110,y=320)

            e8=Entry(forgot,show='*',width=40)
            e8.place(x=240,y=320)

           

            Button(forgot,command=lambda:reset(e7,e8,tw),text='Reset Password',bg='darkcyan',fg='white').place(x=110,y=370)
            def reset(e7,e8,tw):
                password=e7.get()
                cpassword=e8.get()
                if(password==cpassword):
                    cursor.execute("Update projectdb set password='"+password+"' where email='"+email+"'")
                    con.commit()
                    forgot.destroy()
                    account(tw)
                    #Destroy page.................
                    
                    
                    label_20=Label(forgot,text='Password  changed  successfully',bg='white',fg='green',font='cursive 10 bold')
                    label_20.place(x=110,y=420)
                    
                    
                else:
                    label_19=Label(forgot,text='Error! Password does not verified',bg='white',fg='red',font='cursive 10 bold')
                    label_19.place(x=110,y=420)
                

            

            
            
        
        else:
            label_17=Label(forgot,text='Error! Invalid Email',bg='white',fg='red',font='cursive 10 bold')
            label_17.place(x=110,y=270)
            
            

#.............To logout and destroy the existing window and then move to new screen...................        
def open_main(login1):
    login1.destroy()
    main_page()

    
    
    
    
    
    

#...........Function calling.......................................................................................................................................


main_page()

