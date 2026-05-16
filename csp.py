#purpose :To Build a simple Library Management system
#input:Data 
#output:To store records
#Author:'dheerajkumarsahu827@gmail.com' 

import mysql.connector as sql
from datetime import date

# Connect to MySQL
con = sql.connect(host="localhost", user="root", password="dheeraj@19", database="cs")
cur = con.cursor()

def Admin_login():
    print('Hello Admin Enter your password ! ->')  
    try:
        P_w=input('Enter Password :- ')
        if P_w == 'dk@19':
            print("Hello User Access Granted ✅ ")
            def Book_m ():
                def Add_book1():
                    title = input("Enter book title: ")
                    author = input("Enter author name: ")
                    avail =int(input("Enter availibility(Quantity) of book :- "))
                    bkcd=int(input("Enter Book Code :- "))
                    if avail < 0:
                        print("Input availibility be positive ")
                    else:
                        cur.execute("INSERT INTO books (title, author, available,b_cd) VALUES (%s, %s, %s,%s)", (title, author,avail,bkcd))
                        con.commit()
                        print("✅ Book added successfully!")
                
                def View_books1():
                    print("####### List of all Books in this Library ########")
                    cur.execute("SELECT * FROM books order by book_id")
                    for row in cur.fetchall():
                        print(row)
                def Del_book1():
                    print("///////////////  Drop Book   //////////////////")
                    cur.execute("SELECT title,b_cd FROM books order by book_id")
                    for row in cur.fetchall():
                        print(row)
                    title1= input("Enter the Book-code to Delete it :- ")
                    query='''delete from books where b_cd =%s'''
                    val=(title1,)
                    try:
                        cur.execute(query,val)
                        print(" ! Book Deleted successfully !")
                    except Exception as e:
                        print("Cannot delete a Book until it is fully Returned")
                        print(e)
                    con.commit()
                    
                def V_i():
                    cur.execute("select * from issue as _1 left join students as _2 on _1.admn_no=_2.admn_no where  return_date is null ;")
                    for l__ in cur.fetchall():
                        print("===========Book issued========")
                        print("Name   :    ",l__[6])
                        print("Class  :    ",l__[7])
                        print("book_id:    ",l__[1])
                        print("Admn_no:    ",l__[2])
                        print("Issue_id:   ",l__[0])
                        print("Issue_date: ",l__[3])
                        print("return_date:",l__[4])
                
                def Update_bka():
                    print("####### List of all Books in this Library ########")
                    cur.execute("SELECT book_id,title,available FROM books order by book_id")
                    for row in cur.fetchall():
                        print(row)
                    bid=int(input("Select the Book to Update avalibility :- "))
                    ava=int(input('Update avalibility of the Book :- '))
                    query=("update books set available =%s WHERE book_id =%s ")
                    val=(ava,bid)
                    if ava < 0:
                        print("Avalibility must be Positive")
                    else:
                        cur.execute(query,val)
                        con.commit()
                        print("Avalibility updated")
                def Menu():
                    while True:
                        print("\n========== BOOK MENU ===========")
                        print("1. Add Books")
                        print("2. View Books")
                        print("3. Delete Book")
                        print("4. View Issued Books")
                        print("5. Update avalibility")
                        print("6. Exit")  

                        choice = input("Enter choice: ")       
                        if choice == '1':
                            Add_book1()
                        elif choice == '2':
                            View_books1()
                        elif choice == '3':
                            Del_book1()
                        elif choice == '4':
                            V_i()
                        elif choice == '5':
                            Update_bka()
                        elif choice == '6':
                            print("👋 Exiting...")
                            break
                        else:
                            print("❌ Invalid choice! Try again.")

                Menu()
            def Stu_m():

                def Add_student1():
                    admn_no = int(input("Enter Admission No: "))
                    name = input("Enter Student Name: ")
                    clas = int(input("Enter Class: "))
                    code1= int(input("Enter Student-Code: "))
                    if admn_no and clas and code1 <0:
                        print("Admission Number Must Be Positive")
                    else:
                        cur.execute("INSERT INTO students VALUES (%s, %s, %s,%s)", (admn_no, name, clas,code1))
                        con.commit()
                        print("✅ Student added successfully!")
                
                def View_student1():
                    print("####### List of all Registered Students in this Library ########")
                    cur.execute("SELECT * FROM students ORDER BY admn_no")
                    for stu in cur.fetchall():
                        print(stu)
                
                def Delete_student1():
                    print("////////////    Drop IDs     ///////////////")
                    cur.execute("SELECT name,code FROM students order by admn_no")
                    for row in cur.fetchall():
                        print(row)
                    title2= input("Enter the code to Delete it :- ")
                    query1='''delete from students where code =%s'''
                    val=(title2,)
                    cur.execute(query1,val)
                    con.commit()
                    print(" ! Student ID Deleted successfully !")

                def Menu():
                    while True:
                        print("\n*******Student Menu *******")
                        print("1. Add Student")
                        print("2. View Student ")
                        print("3. Delete Student")
                        print("4. Exit")
                        
                        choice = input("Enter choice: ")       
                        if choice == '1':
                            Add_student1()
                        elif choice == '2':
                            View_student1()
                        elif choice == '3':
                            Delete_student1()
                        elif choice == '4':
                            print("👋 Exiting...")
                            break 
                        else:
                                print("❌ Invalid choice! Try again.")

                Menu()
            def V_i():
                cur.execute("select * from issue as _1 left join students as _2 on _1.admn_no=_2.admn_no where  return_date is null ;")
                print("issue_id,book_id,date of issue,(DOR),Name,Student_id")
                for vissue in cur.fetchall():
                    print(vissue)
            def FEEDBACK():
                File=open("C:\\Users\\User\\OneDrive\\Desktop\\Python program\\Project\\Library management\\Feedback.txt","r")
                print("**********List of Feedbacks **********")
                x=File.readlines()
                print(x)
                File.close()
            def ADD_NOTICE():
                notice=input("Enter the Notice to be added :- ")
                file=open("C:\\Users\\User\\OneDrive\\Desktop\\Python program\\Project\\Library management\\Notice.txt","a")
                file.write(f'{notice} \n on {date.today()} \n') 
                print("✅ Notice added successfully!")
                file.close()
            def Menu():
                while True:
                    print("\n*******Admin Access *******")
                    print("1. Book menu")
                    print("2. Student Menu")
                    print("3. View Issued Book")
                    print("4. View Feedbacks")
                    print("5. Add Notice")
                    print("6. Exit")

                    choice = input("Enter choice: ")       
                    if choice == '1':
                        Book_m()
                    elif choice == '2':
                        Stu_m()
                    elif choice == '3':
                        V_i()
                    elif choice == '4':
                        FEEDBACK()
                    elif choice == '5':
                        ADD_NOTICE()
                    elif choice == '6':
                        print("👋 Exiting...")
                        break
                    else:
                        print("❌ Invalid choice! Try again.")
            Menu()
        else:
           print('Asscess Denied Wrong Password !!!!')
    except Exception as e:
        print(e)
def Bk_menu():
    def View_books():
        print("####### List of all Books in this Library ########")
        cur.execute("SELECT book_id,title,author, available FROM books order by book_id")
        for row in cur.fetchall():
            print(row)
    
    def Issue_book():
        try:
            print("=====DISPLAYING ONLY AVAILABLE BOOKS =====")
            cur.execute("SELECT book_id,title,author FROM books WHERE available > 0")
            for b in cur.fetchall():
                print(b)
            book_id = int(input("Enter Book ID From The Above list: "))
            admn_no = int(input("Enter Admission No: "))
            cur.execute("SELECT available FROM books WHERE book_id=%s", (book_id,))
            avail = cur.fetchone()
            if avail and avail[0]:
                cur.execute("INSERT INTO issue (book_id, admn_no, issue_date, return_date) VALUES (%s, %s, %s, NULL)", (book_id, admn_no, date.today()))
                cur.execute("UPDATE books SET available= available-1 WHERE book_id=%s", (book_id,))
                con.commit()
                cur.execute("SELECT * FROM issue ORDER BY issue_id DESC LIMIT 1")
                for k in cur.fetchall():
                    print (k)
                    print("📚 Book issued successfully!")
                    print(f'Your _Issued_ID_={k[0]} for 📚 Book:- {book_id}')
                    print(f'Please Remember you Issued_ID :- {k[0]} At the time of Returning Book')
            else:
                print("❌ Book not available!")
        except Exception as P:
            print(P)

    def Return_book():
        try:
            issue_id = int(input("Enter Issue ID: "))
            cur.execute("SELECT book_id FROM issue WHERE issue_id=%s AND return_date IS NULL", (issue_id,))
            data = cur.fetchone()
            if data:
                cur.execute("UPDATE issue SET return_date=%s WHERE issue_id=%s", (date.today(), issue_id))
                cur.execute("UPDATE books SET available= available +1 WHERE book_id=%s", (data[0],))
                con.commit()
                print("✅ Book returned successfully!")
                cur.execute("SELECT * FROM issue WHERE admn_no = %s",(issue_id,))
            else:
                print("❌ Invalid Issue ID or already returned!")
        except Exception as y:
            print(y)

    def View_fines():
        try:
            x=int(input("Enter your Admission No :- "))
            try:
                query='''SELECT  * FROM issue WHERE admn_no =%s'''
                value=(x,)
                cur.execute(query,value) 
                for l in cur.fetchall():
                    if l[3]==l[4]:
                        print(" No Late Fee ")
                    elif l[4] is None:
                        print("Book not yet returned, Late Fee will be calculated after returning the book")
                    else:
                        print("******Late Fee will be charged****** \n Please contact the library for more details")
            except Exception as f:
                print(f)
        except Exception as c:
            print(c)
    def Menu():
        while True:
            print("\n########## BOOK MENU ############")
            print("1. View Books")
            print("2. Issue Book")
            print("3. Return Book")
            print("4. View Fine ")
            print("5. Exit")  

            choice = input("Enter choice: ")       
            if choice == '1':
                View_books()
            elif choice == '2':
                Issue_book()
            elif choice == '3':
                Return_book()
            elif choice == '4':
                View_fines()
            elif choice == '5':
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice! Try again.")
    Menu()
def Reg_stu():
        print("####### List of all Registered Students  ########")
        cur.execute("SELECT admn_no,name,class FROM students ORDER BY admn_no")
        for stu in cur.fetchall():
            print(stu)

def Cus_login():
    try: 
        csl=int(input("Enter admn_no :-  "))
        query1="SELECT * FROM students WHERE admn_no =%s"
        val=(csl,)
        cur.execute(query1,val)
        for l in cur.fetchall():
            print("**************Details**************")
            print("admn_no: ",l[0])
            print("Name: ",l[1])
            print("Class: ",l[2])
            print("code: ",l[3])
        
            query2="SELECT * FROM issue WHERE admn_no = %s"
            val1=(csl,)
            cur.execute(query2,val1)
        for l_ in cur.fetchall() :
            print("===========Book issued========")
            print("issue_id: ",l_[0])
            print("book_id: ",l_[1])
            print("admn_no: ",l_[2])
            print("Issue_date: ",l_[3])
            print("return_date: ",l_[4])
            if (l_[3] == l_[4]):
                print(" No Late Fee ")
            else:
                print("******Late Fee will be charged****** \n Please find you Fee by another Menu")
        else:
            print("=========No More Books issued=======")
    except Exception as e :
        print('!!!',e,'try again !!!' )

def Feedback():
    try:
        i=input("Enter your Feedback :- ") 
        y=int(input("Enter your Admission_no :- "))
        z=int(input("Enter your code to Register and finalise the Feedback :-"))
        query='''SELECT * FROM STUDENTS WHERE admn_no =%s AND code =%s'''
        value=(y,z)
        cur.execute(query,value)
        if cur.fetchone():
            file=open("C:\\Users\\User\\OneDrive\\Desktop\\Python program\\Project\\Library management\\Feedback.txt","a")
            file.write(f'Feedback from Student with Admission_No {y} is : {i}\n on {date.today()} \n') 
            print("✅ Feedback recorded successfully! Thank you for your input.")
            file.close()  
        else:
            print("Invalid Admission No or Code. Feedback not recorded.")
    except Exception as e:
        print(e)
 
def Notice():
    file=open("C:\\Users\\User\\OneDrive\\Desktop\\Python program\\Project\\Library management\\Notice.txt","r")
    print("**********List of Notices **********")
    x=file.readlines()
    print(x)
    file.close()

def Menu():
    while True:
        print("\n========== LIBRARY MANAGEMENT MENU ===========")
        print("1. Admin login")
        print("2. Books Menu")
        print("3. List of Regitered Student [ID]")
        print("4. Customer Login(issued Books and Details)")
        print("5. Feedback")
        print("6. Notice")
        print("7. Exit")  

        choice = input("Enter choice: ")       
        if choice == '1':
            Admin_login()
        elif choice == '2':
            Bk_menu()
        elif choice == '3':
            Reg_stu()
        elif choice == '4':
            Cus_login()
        elif choice == '5':
            Feedback()
        elif choice == '6':
            Notice()
        elif choice == '7':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice! Try again.")

Menu()
con.close()