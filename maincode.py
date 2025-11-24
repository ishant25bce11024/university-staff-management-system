import sqlite3

def connect():
    return sqlite3.connect("university.db")

def add_teacher(empid, name, post, subjects, cabinnum, salary):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO teachers (empid, name, post, subjects, cabinnum, salary) VALUES (?, ?, ?, ?, ?, ?)",
        (empid, name, post, subjects, cabinnum, salary)
    )
    conn.commit()
    conn.close()

def delete_teacher(empid):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teachers WHERE empid=?", (empid,))
    conn.commit()
    conn.close()

def promote_teacher(empid, new_post, salary_increment):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE teachers SET post=?, salary=salary + ? WHERE empid=?",
        (new_post, salary_increment, empid)
    )
    conn.commit()
    conn.close()

def edit_teacher(empid, name, post, subjects, cabinnum, salary):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE teachers SET name=?, post=?, subjects=?, cabinnum=?, salary=? WHERE empid=?",
        (name, post, subjects, cabinnum, salary, empid)
    )
    conn.commit()
    conn.close()

def show_teacher(empid):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers WHERE empid=?", (empid,))
    teacher = cursor.fetchone()
    conn.close()
    return teacher

def display_all_teachers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers")
    teachers = cursor.fetchall()
    conn.close()
    return teachers

def menu1():
    while True:
        print("\nMenu:")
        print("1. Add Teacher")
        print("2. Delete Teacher")
        print("3. Promote Teacher")
        print("4. Edit Teacher Details")
        print("5. Show Teacher by Employee ID")
        print("6. Display All Teachers")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            empid = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            post = input("Enter Post: ")
            subjects = input("Enter Subjects (comma separated): ")
            cabinnum = input("Enter Cabin Number: ")
            salary = float(input("Enter Salary: "))
            add_teacher(empid, name, post, subjects, cabinnum, salary)
            print("Teacher added successfully.")

        elif choice == "2":
            empid = int(input("Enter Employee ID to delete: "))
            delete_teacher(empid)
            print("Teacher deleted successfully.")

        elif choice == "3":
            empid = int(input("Enter Employee ID to promote: "))
            new_post = input("Enter New Post: ")
            salary_increment = float(input("Enter Salary Increment: "))
            promote_teacher(empid, new_post, salary_increment)
            print("Teacher promoted successfully.")

        elif choice == "4":
            empid = int(input("Enter Employee ID to edit: "))
            if show_teacher(empid):
                name = input("Enter New Name: ")
                post = input("Enter New Post: ")
                subjects = input("Enter New Subjects (comma separated): ")
                cabinnum = input("Enter New Cabin Number: ")
                salary = float(input("Enter New Salary: "))
                edit_teacher(empid, name, post, subjects, cabinnum, salary)
                print("Teacher details updated successfully.")
            else:
                print("Teacher not found.")

        elif choice == "5":
            empid = int(input("Enter Employee ID to show: "))
            teacher = show_teacher(empid)
            if teacher:
                print(f"Employee ID: {teacher[0]}, Name: {teacher[1]}, Post: {teacher[2]}, Subjects: {teacher[3]}, Cabin No: {teacher[4]}, Salary: {teacher[5]}")
            else:
                print("Teacher not found.")

        elif choice == "6":
            teachers = display_all_teachers()
            if teachers:
                print("All Teachers:")
                for t in teachers:
                    print(f"Employee ID: {t[0]}, Name: {t[1]}, Post: {t[2]}, Subjects: {t[3]}, Cabin No: {t[4]}, Salary: {t[5]}")
            else:
                print("No teachers found.")

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
            
#students code start here

def connect():
    return sqlite3.connect("university.db")

def admit_student(registrationno, name, dob, programme, year, feeperannum, address):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (registrationno, name, dob, programme, year, feeperannum, address)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (registrationno, name, dob, programme, year, feeperannum, address))
    conn.commit()
    conn.close()

def delete_student(registrationno):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE registrationno=?", (registrationno,))
    conn.commit()
    conn.close()

def edit_student(registrationno, name, dob, programme, year, feeperannum, address):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students SET name=?, dob=?, programme=?, year=?, feeperannum=?, address=?
        WHERE registrationno=?""",
        (name, dob, programme, year, feeperannum, address, registrationno))
    conn.commit()
    conn.close()

def display_all_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

def show_student(registrationno):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE registrationno=?", (registrationno,))
    student = cursor.fetchone()
    conn.close()
    return student

def show_students_by_programme(programme):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE programme=?", (programme,))
    students = cursor.fetchall()
    conn.close()
    return students

def menu2():
    while True:
        print("\nStudent Management Menu:")
        print("1. Admit Student")
        print("2. Delete Student")
        print("3. Edit Student Details")
        print("4. Display All Students")
        print("5. Show Student by Registration Number")
        print("6. Show Students by Programme")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            registrationno = int(input("Enter Registration Number: "))
            name = input("Enter Name: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            programme = input("Enter Programme: ")
            year = int(input("Enter Year: "))
            feeperannum = float(input("Enter Fee Per Annum: "))
            address = input("Enter Address: ")
            admit_student(registrationno, name, dob, programme, year, feeperannum, address)
            print("Student admitted successfully.")

        elif choice == "2":
            registrationno = int(input("Enter Registration Number to delete: "))
            delete_student(registrationno)
            print("Student deleted successfully.")

        elif choice == "3":
            registrationno = int(input("Enter Registration Number to edit: "))
            if show_student(registrationno):
                name = input("Enter New Name: ")
                dob = input("Enter New Date of Birth (YYYY-MM-DD): ")
                programme = input("Enter New Programme: ")
                year = int(input("Enter New Year: "))
                feeperannum = float(input("Enter New Fee Per Annum: "))
                address = input("Enter New Address: ")
                edit_student(registrationno, name, dob, programme, year, feeperannum, address)
                print("Student details updated successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            students = display_all_students()
            if students:
                for s in students:
                    print(f"RegNo: {s[0]}, Name: {s[1]}, DOB: {s[2]}, Programme: {s[3]}, Year: {s[4]}, Fee: {s[5]}, Address: {s[6]}")
            else:
                print("No students found.")

        elif choice == "5":
            registrationno = int(input("Enter Registration Number to show: "))
            student = show_student(registrationno)
            if student:
                print(f"RegNo: {student[0]}, Name: {student[1]}, DOB: {student[2]}, Programme: {student[3]}, Year: {student[4]}, Fee: {student[5]}, Address: {student[6]}")
            else:
                print("Student not found.")

        elif choice == "6":
            programme = input("Enter Programme to list students: ")
            students = show_students_by_programme(programme)
            if students:
                for s in students:
                    print(f"RegNo: {s[0]}, Name: {s[1]}, DOB: {s[2]}, Programme: {s[3]}, Year: {s[4]}, Fee: {s[5]}, Address: {s[6]}")
            else:
                print("No students found in this programme.")

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
#emploies
import sqlite3

def connect():
    return sqlite3.connect("university.db")

def add_staff(empid, name, designation, cabinnum, salary):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO emploies (empid, name, designation, cabinnum, salary) VALUES (?, ?, ?, ?, ?)",
        (empid, name, designation, cabinnum, salary)
    )
    conn.commit()
    conn.close()

def delete_staff(empid):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emploies WHERE empid=?", (empid,))
    conn.commit()
    conn.close()

def edit_staff(empid, name, designation, cabinnum, salary):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE emploies SET name=?, designation=?, cabinnum=?, salary=? WHERE empid=?",
        (name, designation, cabinnum, salary, empid)
    )
    conn.commit()
    conn.close()

def display_all_staff():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emploies")
    staff_members = cursor.fetchall()
    conn.close()
    return staff_members

def show_staff(empid):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emploies WHERE empid=?", (empid,))
    staff = cursor.fetchone()
    conn.close()
    return staff

def show_staff_by_designation(designation):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emploies WHERE designation=?", (designation,))
    staff_members = cursor.fetchall()
    conn.close()
    return staff_members

def menu3():
    while True:
        print("\nStaff Management Menu:")
        print("1. Add Staff Member")
        print("2. Delete Staff Member")
        print("3. Edit Staff Details")
        print("4. Display All Staff Members")
        print("5. Show Staff by Employee ID")
        print("6. Show Staff by Designation")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            empid = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            designation = input("Enter Designation: ")
            cabinnum = input("Enter Cabin Number: ")
            salary = float(input("Enter Salary: "))
            add_staff(empid, name, designation, cabinnum, salary)
            print("Staff member added successfully.")

        elif choice == "2":
            empid = int(input("Enter Employee ID to delete: "))
            delete_staff(empid)
            print("Staff member deleted successfully.")

        elif choice == "3":
            empid = int(input("Enter Employee ID to edit: "))
            if show_staff(empid):
                name = input("Enter New Name: ")
                designation = input("Enter New Designation: ")
                cabinnum = input("Enter New Cabin Number: ")
                salary = float(input("Enter New Salary: "))
                edit_staff(empid, name, designation, cabinnum, salary)
                print("Staff details updated successfully.")
            else:
                print("Staff member not found.")

        elif choice == "4":
            staff_members = display_all_staff()
            if staff_members:
                print("All Staff Members:")
                for s in staff_members:
                    print(f"EmpID: {s[0]}, Name: {s[1]}, Designation: {s[2]}, Cabin No: {s[3]}, Salary: {s[4]}")
            else:
                print("No staff members found.")

        elif choice == "5":
            empid = int(input("Enter Employee ID to show: "))
            staff = show_staff(empid)
            if staff:
                print(f"EmpID: {staff[0]}, Name: {staff[1]}, Designation: {staff[2]}, Cabin No: {staff[3]}, Salary: {staff[4]}")
            else:
                print("Staff member not found.")

        elif choice == "6":
            designation = input("Enter Designation to list staff members: ")
            staff_members = show_staff_by_designation(designation)
            if staff_members:
                for s in staff_members:
                    print(f"EmpID: {s[0]}, Name: {s[1]}, Designation: {s[2]}, Cabin No: {s[3]}, Salary: {s[4]}")
            else:
                print("No staff members found with this designation.")

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
ans2='y'
while ans2 in'yY':
    ans=int(input("1.change Teacher\n2.change in students\n3.changes in employees\n4.visitourweb\n5.exit\n"))
    if ans==1:
        menu1()
    elif ans==2:
        menu2()
    elif ans==3:
        menu3()
    elif ans==5:
        exit()
    else:
        print('provide a correct input pleas')
ans2=input('want to continue??y/n')









