import sqlite3
import datetime
from getpass import getpass



#connection
conn = sqlite3.connect("students_management_system.db")

# ---> students table start here
try:
    conn.execute('''create table `students`(`id` integer not null primary key,
       `first_name` varchar(50) not null,
       `last_name` varchar(50) not null,
       `father_name` varchar(50) not null,
       `address` varchar(100) not null,
       `phone_number` varchar(17) not null,
       `course` integer not null,
       constraint `fk_students_tests_course` FOREIGN KEY(`course`) references `courses`(`id`)
       )''')

except Exception as e:
    print("already exists:"+str(e))
# ---> students table end here

# ---> courses table start here
try:
    conn.execute('''create table `courses`(`id` integer not null primary key,
    `course` varchar(100) not null unique,
    `fee` integer not null)''')

except Exception as e:
    print("already exists:"+str(e))
# ---> courses table end here


# ---> Attendence table start here
try:
    conn.execute('''create table `students_attendence`(`id` integer not null primary key,
    `student_id` integer not null,
    `attendence` varchar(7) not null,
    `date` TIMESTAMP not null,
    constraint `fk_students_attendence_student_id` FOREIGN KEY(`student_id`) references `students`(`id`))''')

except Exception as e:
    print("already exists:"+str(e))
# ---> Attendence table end here


# ---> Exam table start here
try:
    conn.execute('''create table `students_exams`(`id` integer not null primary key,
    `student_id` integer not null,
    `exam` varchar(10) not null,
    `date` TIMESTAMP not null,
    constraint `fk_students_exams_student_id` FOREIGN KEY(`student_id`) references `students`(`id`))''')

except Exception as e:
    print("already exists:"+str(e))
# ---> Exam table end here


# ---> Payments table start here
try:
    conn.execute('''create table `students_Payments`(`id` integer not null primary key,
    `student_id` integer not null,
    `payments` integer not null,
    `date` TIMESTAMP not null,
    constraint `fk_students_Payments_student_id` FOREIGN KEY(`student_id`) references `students`(`id`)
    )''')

except Exception as e:
    print("already exists:"+str(e))
# ---> Payments table end here


# ---> Admin table start here
try:
    conn.execute('''create table `admins`(`id` integer not null primary key,
    `user_name` varchar(10) not null,
    `user_password` varchar(10) not null unique)''')

except Exception as e:
    print("already exists:"+str(e))


user_name = conn.execute("select `user_name` from `admins` where `id` = 1")
user_name = tuple(user_name)

user_password = conn.execute("select `user_password` from `admins` where `id` =1")
user_password = tuple(user_password)


user_name_input = input("Enter USER-NAME:-")
################## settings on please emulate terminal in output console (if you can not change this settings then please comment getpass input and uncomments the simple input)
user_password_input = getpass("Enter USER-PASSWORD:-")
# user_password_input = input("Enter USER-PASSWORD:-")
# ---> Admin table end here

if user_name_input in user_name[0] and user_password_input in user_password[0]:
    print("LOGIN SUCCESSFULLY!")
    while True:
        print('''
            Press 1 For Students.
            Press 2 For Courses.
            Press 3 For Students-Attendence.
            Press 4 For Students-Exams.
            Press 5 For Students-Payments.
            Press 6 Password.
            Press 0 For Exit.
        ''')

        try:
            press = int(input("Press Any Number:-"))

            # ---> Students Start Here
            if press == 1:
                while True:
                    print('''
                        Press 1 For Students-List.
                        Press 2 For Add New Students.
                        Press 3 For Delete Single Student.
                        Press 4 For Delete All Student.
                        Press 5 For Update Single Student.
                        Press 0 For Back.
                        ''')

                    user_input = int(input("Press Any Number:-"))

                    # ---> Students List start here
                    if user_input == 1:
                        while True:
                            print('''
                                Press 1 For All Students-List.
                                Press 2 For Search Student (by ID only).
                                Press 3 For Search Student (by FIRST-NAME only).
                                Press 4 For Search Student (by LAST-NAME only).
                                Press 5 For Search Student (by FATHER-NAME only).
                                Press 6 For Search Student (by ADDRESS only).
                                Press 7 For Search Student (by PHONE-NUMBER only).
                                Press 8 For Search Student (by COURSE-NAME only).
                                Press 0 For Back.
                            ''')
                            press = int(input("Enter A Number:-"))
                            if press == 1:
                                data = conn.execute('''
                                select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,
                                `s`.`address`,`s`.`phone_number`, `c`.`course`
                                from `students` as `s`, `courses` as `c`
                                where `c`.`id` = `s`.`course`;
                                ''')
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Students Not Found.")
                                else:
                                    print("All Students-List")
                                    print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                    for n in data_t:
                                        print(n)

                            elif press == 2:
                                student_id = int(input("Enter STUDENT-ID To Search Student (by ID only):-"))
                                student_id = str(student_id)
                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,`s`.`address`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `s`.`id` = '" + student_id + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                conn.execute(data)
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    print("Student-List")
                                    print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                    for n in data_t:
                                        print(n)

                            elif press == 3:
                                student_name = input(
                                    "Enter STUDENT-FIRST-NAME To Search Student (by FIRST-NAME only):-")
                                student_name = student_name.lower()
                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,`s`.`address`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `s`.`first_name` = '" + student_name + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                conn.execute(data)
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    print("Student-List")
                                    print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                    for n in data_t:
                                        print(n)

                            elif press == 4:
                                student_name = input("Enter STUDENT-LAST-NAME To Search Student (by LAST-NAME only):-")
                                student_name = student_name.lower()
                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,`s`.`address`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `s`.`last_name` = '" + student_name + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                conn.execute(data)
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    print("Student-List")
                                    print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                    for n in data_t:
                                        print(n)

                            elif press == 5:
                                student_name = input("Enter STUDENT-FATHER-NAME To Search Student (by FATHER-NAME only):-")
                                student_name = student_name.lower()
                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,`s`.`address`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `s`.`father_name` = '" + student_name + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                conn.execute(data)
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    print("Student-List")
                                    print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                    for n in data_t:
                                        print(n)

                            elif press == 6:
                                student_address = input("Enter ADDRESS To Search Student (by ADDRESS only):-")
                                student_address = student_address.lower()
                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,`s`.`address`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `s`.`address` = '" + student_address + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                conn.execute(data)
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    print("Student-List")
                                    print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                    for n in data_t:
                                        print(n)

                            elif press == 7:
                                student_phone_number = input("Enter Phone-Number To Search Student (by Phone-Number only):-")
                                student_phone_number = student_phone_number.lower()
                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,`s`.`address`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `s`.`phone_number` = '" + student_phone_number + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                conn.execute(data)
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    print("Student-List")
                                    print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                    for n in data_t:
                                        print(n)

                            elif press == 8:
                                student_course = input("Enter Course To Search Student (by Course only):-")
                                student_course = student_course.lower()
                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,`s`.`address`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`course` = '" + student_course + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                conn.execute(data)
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    print("Student-List")
                                    print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                    for n in data_t:
                                        print(n)

                            elif press == 0:
                                break

                    # ---> Students List end here

                    # ---> Add New Student start here
                    elif user_input == 2:
                        print("Please Enter Correct information....")
                        first_name = input("Enter (Maximum 50 Characters) First-Name:-")
                        first_name = first_name.lower()
                        last_name = input("Enter (Maximum 50 Characters) Last-Name:-")
                        last_name = last_name.lower()
                        father_name = input("Enter (Maximum 50 Characters) Father-Name:-")
                        father_name = father_name.lower()
                        address = input("Enter (Maximum 100 Characters) Address:-")
                        address = address.lower()
                        phone_number = input("Enter (Maximum 17 Characters) Phone-Number:-")
                        phone_number = phone_number.lower()

                        courses_data = "select `id`,`course` from `courses` order by `id` asc"
                        cur = conn.cursor()
                        cur.execute(courses_data)
                        data_fetch = cur.fetchall()
                        data_course = tuple(data_fetch)
                        if len(data_course) == 0:
                            print("You Have No Course! You Can't Add New Students,Please Fisrt Add Course Thanks.")
                            break
                        else:
                            print("All Courses")

                        print("All Courses")
                        print("Curse-ID,Course-Name")

                        for n in data_course:
                            print(n)
                        course = int(input("We Have ABOVE COURSES..Please Enter ABOVE COURSE ID ONLY Thanks:-"))
                        course = str(course)

                        data = "select `c`.`id`,`c`.`course` from `courses` as `c` where `c`.`id` = '" + course + "' order by `c`.`id` asc"
                        cur = conn.cursor()
                        cur.execute(data)
                        data_fetch = cur.fetchall()
                        data_t = tuple(data_fetch)
                        if len(data_t) == 0:
                            print("Course Not Found.")
                        else:
                            data_len = len(data_t)
                            data_len = str(data_len)
                            print("Found " + data_len + " Records")
                            print("You Selected this Course.")
                            for n in data_t:
                                print(n)

                            insert_list = [first_name, last_name, father_name, address, phone_number, course]

                            yes_no = input("Are You Sure Want To Add New Student? (Y/N):-")
                            yes_no = yes_no.lower()
                            if yes_no == 'y':
                                conn.execute('''insert into `students`
                                (`first_name`,`last_name`,`father_name`,`address`,`phone_number`,`course`)
                                values(?,?,?,?,?,?)''',
                                insert_list)

                                conn.commit()
                                print("Student ADDED")
                                data = conn.execute("select * from `students` where `phone_number` = '" + phone_number + "'")
                                for n in data:
                                    print(n)

                            else:
                                print("You Entered (N) For No.")
                    # ---> Add New Student end here

                    # ---> Delete Single Student start here
                    elif user_input == 3:
                        data = conn.execute('''
                            select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,
                            `s`.`address`,`s`.`phone_number`, `c`.`course`
                            from `students` as `s`, `courses` as `c`
                            where `c`.`id` = `s`.`course`;
                        ''')
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Students Not Found.")
                        else:
                            print("Student-List")
                            print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                            for n in data_t:
                                print(n)

                            delete_single_student = input("Enter Student Id For Delete Single Student:-")

                            data = "select * from `students` where `id` = '" + delete_single_student + "'"
                            cur = conn.cursor()
                            cur.execute(data)
                            data_fetch = cur.fetchall()
                            data_t = tuple(data_fetch)
                            if len(data_t) == 0:
                                print("Student Not Found.")
                            else:
                                data_len = len(data_t)
                                data_len = str(data_len)
                                print("Found " + data_len + " Records")
                                print("You Selected this Student.")
                                for n in data_t:
                                    print(n)

                                yes_no = input("Are You Sure Want To Delete Single Student? (Y/N):-")
                                yes_no = yes_no.lower()
                                if yes_no == 'y':
                                    d = "delete from `students` where id='" + delete_single_student + "'"
                                    conn.execute(d)
                                    conn.commit()
                                    print("Student Deleted.")
                                    data = conn.execute('''
                                    select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,
                                    `s`.`address`,`s`.`phone_number`, `c`.`course`
                                    from `students` as `s`, `courses` as `c`
                                    where `c`.`id` = `s`.`course`;
                                    ''')
                                    data_t = tuple(data)
                                    if len(data_t) == 0:
                                        print("Students Not Found.")
                                    else:
                                        print("Student-List")
                                        print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                        for n in data_t:
                                            print(n)

                                else:
                                    print("You Entered (N) For No.")

                    # ---> Delete Single Student end here

                    # ---> Delete All Students start here
                    elif user_input == 4:
                        data = conn.execute('''
                            select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,
                            `s`.`address`,`s`.`phone_number`, `c`.`course`
                            from `students` as `s`, `courses` as `c`
                            where `c`.`id` = `s`.`course`;
                        ''')
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Students Not Found.")
                        else:
                            print("Student-List")
                            print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                            for n in data_t:
                                print(n)

                            yes_no = input("Are You Sure Want To Delete All Student? (Y/N):-")
                            yes_no = yes_no.lower()

                            if yes_no == 'y':
                                d = "delete from `students`"
                                conn.execute(d)
                                conn.commit()
                                print("All Students Deleted.")

                            else:
                                print("You Entered (N) For No.")


                    # ---> Delete All Students end here

                    # ---> Update Single Student Start Here
                    elif user_input == 5:
                        data = conn.execute("select * from `students`")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Stduents Not Found.")
                        else:
                            print("Student-List")
                            print("Student-ID,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                            for n in data_t:
                                print(n)

                            update_single_student_id = input("Enter Student Id For Update Single Student:-")
                            student_update = conn.execute("select * from `students` where id = '" + update_single_student_id + "'")
                            data_t = tuple(student_update)
                            if len(data_t) == 0:
                                print("Student Not Found.")
                            else:
                                print("Student-List")
                                print("Roll-Number,First-Name,Last-Name,Father-Name,Address,Phone-Number,Course")
                                for n in data_t:
                                    print(n)

                                while True:
                                    print("""
                                        Press 1 For First_Name.
                                        Press 2 For Last_Name.
                                        Press 3 For Father_Name.
                                        Press 4 For Address.
                                        Press 5 For Phone_Number.
                                        Press 6 For Course.
                                        Press 0 For Back.
                                    """)
                                    press = int(input("Enter A Number:-"))
                                    if press == 1:
                                        first_name = input("Enter (Maximum 50 Characters) First_Name For Update:-")
                                        first_name = first_name.lower()
                                        yes_no = input("Are You Sure Want To Update Single Student First-Name? (Y/N):-")
                                        yes_no = yes_no.lower()
                                        if yes_no == 'y':
                                            student_update = "update `students` set `first_name`='" + first_name + "' where `id` ='" + update_single_student_id + "'"
                                            conn.execute(student_update)
                                            conn.commit()
                                            print("Student First_Name Updated.")
                                            data = conn.execute("select * from `students` where id = '" + update_single_student_id + "'")
                                            for n in data:
                                                print(n)

                                        else:
                                            print("You Entered (N) For No.")

                                    elif press == 2:
                                        last_name = input("Enter (Maximum 50 Characters) Last_Name For Update:-")
                                        last_name = last_name.lower()
                                        yes_no = input("Are You Sure Want To Update Single Student Last-Name? (Y/N):-")
                                        yes_no = yes_no.lower()
                                        if yes_no == 'y':
                                            student_update = "update `students` set `last_name`='" + last_name + "' where `id` ='" + update_single_student_id + "'"
                                            conn.execute(student_update)
                                            conn.commit()
                                            print("Student Last_Name Updated.")
                                            data = conn.execute("select * from `students` where id = '" + update_single_student_id + "'")
                                            for n in data:
                                                print(n)

                                        else:
                                            print("You Entered (N) For No.")

                                    elif press == 3:
                                        father_name = input("Enter (Maximum 50 Characters) Father_Name For Update:-")
                                        father_name = father_name.lower()
                                        yes_no = input("Are You Sure Want To Update Single Student Father-Name? (Y/N):-")
                                        yes_no = yes_no.lower()
                                        if yes_no == 'y':
                                            student_update = "update `students` set `father_name`='" + father_name + "' where `id` ='" + update_single_student_id + "'"
                                            conn.execute(student_update)
                                            conn.commit()
                                            print("Student Father_Name Updated.")
                                            data = conn.execute("select * from `students` where id = '" + update_single_student_id + "'")
                                            for n in data:
                                                print(n)

                                        else:
                                            print("You Entered (N) For No.")

                                    elif press == 4:
                                        address = input("Enter (Maximum 100 Characters) Address For Update:-")
                                        address = address.lower()
                                        yes_no = input("Are You Sure Want To Update Single Student Address? (Y/N):-")
                                        yes_no = yes_no.lower()
                                        if yes_no == 'y':
                                            student_update = "update `students` set `address`='" + address + "' where `id` ='" + update_single_student_id + "'"
                                            conn.execute(student_update)
                                            conn.commit()
                                            print("Student Address Updated.")
                                            data = conn.execute("select * from `students` where id = '" + update_single_student_id + "'")
                                            for n in data:
                                                print(n)

                                        else:
                                            print("You Entered (N) For No.")

                                    elif press == 5:
                                        phone_number = input("Enter (Maximum 17 Characters) Phone_Number For Update:-")
                                        phone_number = phone_number.lower()
                                        yes_no = input("Are You Sure Want To Update Single Student Phone-Number? (Y/N):-")
                                        yes_no = yes_no.lower()
                                        if yes_no == 'y':
                                            student_update = "update `students` set `phone_number`='" + phone_number + "' where `id` ='" + update_single_student_id + "'"
                                            conn.execute(student_update)
                                            conn.commit()
                                            print("Student Phone_Number Updated.")
                                            data = conn.execute("select * from `students` where id = '" + update_single_student_id + "'")
                                            for n in data:
                                                print(n)

                                        else:
                                            print("You Entered (N) For No.")

                                    elif press == 6:
                                        courses_data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                        cur = conn.cursor()
                                        cur.execute(courses_data)
                                        data_fetch = cur.fetchall()
                                        data_course = tuple(data_fetch)
                                        if len(data_course) == 0:
                                            print("You Have No Course! You Can't Update Students,Please Fisrt Add Course Thanks.")
                                            break
                                        else:
                                            print("All Courses")

                                        print("Course-ID,Course-Name")
                                        for n in courses_data:
                                            print(n)
                                        course = int(input("We Have ABOVE COURSES..Please Enter ABOVE COURSE ID ONLY Thanks:-"))
                                        course = str(course)

                                        data = "select `id`,`course` from `courses` where `id` = '" + course + "' order by `id` asc"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Course Not Found.")
                                        else:
                                            data_len = len(data_t)
                                            data_len = str(data_len)
                                            print("Found " + data_len + " Records")
                                            print("You Selected this Course.")
                                            for n in data_t:
                                                print(n)

                                            yes_no = input("Are You Sure Want To Update Single Student Course? (Y/N):-")
                                            yes_no = yes_no.lower()
                                            if yes_no == 'y':
                                                student_update = "update `students` set `course`='" + course + "' where `id` ='" + update_single_student_id + "'"
                                                conn.execute(student_update)
                                                conn.commit()
                                                print("Student Course Updated.")
                                                data = conn.execute("select * from `students` where id = '" + update_single_student_id + "'")
                                                for n in data:
                                                    print(n)

                                            else:
                                                print("You Entered (N) For No.")

                                    elif press == 0:
                                        break

                    # ---> Update Single Student end Here

                    # ---> Students Back start here
                    elif user_input == 0:
                        break
                    # ---> Students Back end here

            # ---> Students end Here

            # ---> courses start here
            elif press == 2:
                while True:

                    print('''
                            Press 1 For Courses-List.
                            Press 2 For Add New Course.
                            Press 3 For Delete Single Course.
                            Press 4 For Delete All Courses.
                            Press 5 For Update Single Course.
                            Press 0 For Back.
                    ''')

                    user_input = int(input("Press Any Number:-"))

                    # ---> Courses-List start here
                    if user_input == 1:
                        data = conn.execute("select * from `courses`")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Course Not Found.")
                        else:
                            print("Course-ID,Course-Name,Course-Fee")
                            for n in data_t:
                                print(n)
                    # ---> Courses-List end here

                    # ---> Add New Course Start here
                    elif user_input == 2:
                        print("Please Enter Correct information....")
                        course_name = input("Enter (Maximum 50 Characters) Course Name:-")
                        course_name = course_name.lower()
                        course_fee = int(input("Enter (IN NUMBERS) Course fee:-"))
                        insert_list = [course_name, course_fee]

                        yes_no = input("Are You Sure Want To Add New Course? (Y/N):-")
                        yes_no = yes_no.lower()
                        if yes_no == 'y':
                            conn.execute("insert into `courses`(`course`,`fee`)values(?,?)", insert_list)
                            conn.commit()
                            print("Course ADDED")
                            data = conn.execute("select * from `courses` where `course` = '"+course_name+"'")
                            print("Course-ID,Course-Name,Course-Fee")
                            for n in data:
                                print(n)
                        else:
                            print("You Entered (N) For No.")
                    # ---> Add New Course end here

                    # ---> Delete Single Course start here
                    elif user_input == 3:
                        data = conn.execute("select * from `courses`")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Course Not Found.")
                        else:
                            print("Course-ID,Course-Name,Course-Fee")
                            for n in data_t:
                                print(n)

                            delete_single_course = input("Enter Course Id For Delete Single Course:-")

                            data = conn.execute("select * from `courses` where id ='"+delete_single_course+"'")
                            data_t = tuple(data)
                            if len(data_t) == 0:
                                print("Course Not Found.")
                            else:
                                print("Course-ID,Course-Name,Course-Fee")
                                for n in data_t:
                                    print(n)

                                yes_no = input("Are You Sure Want To Delete Single Course? (Y/N):-")
                                yes_no = yes_no.lower()
                                if yes_no == 'y':
                                    d = "delete from `courses` where id='" + delete_single_course + "'"
                                    conn.execute(d)
                                    conn.commit()
                                    print("Course Deleted.")
                                    data = conn.execute("select * from `courses`")
                                    data_t = tuple(data)
                                    if len(data_t) == 0:
                                        print("Course Not Found.")
                                    else:
                                        print("Course-ID,Course-Name,Course-Fee")
                                        for n in data_t:
                                            print(n)

                                else:
                                    print("You Entered (N) For No.")
                    # ---> Delete Single Course end here

                    # ---> Delete All Courses start here
                    elif user_input == 4:
                        data = conn.execute("select * from `courses`")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Course Not Found.")
                        else:
                            print("Course-ID,Course-Name,Course-Fee")
                            for n in data_t:
                                print(n)

                            yes_no = input("Are You Sure Want To Delete All Courses? (Y/N):-")
                            yes_no = yes_no.lower()

                            if yes_no == 'y':
                                d = "delete from `courses`"
                                conn.execute(d)
                                conn.commit()
                                print("All Courses Deleted.")

                            else:
                                print("You Entered (N) For No.")
                    # ---> Delete All Courses end here

                    # ---> Update Single Course Start Here
                    elif user_input == 5:
                        data = conn.execute("select * from `courses`")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Course Not Found.")
                        else:
                            print("Course-ID,Course-Name,Course-Fee")
                            for n in data_t:
                                print(n)

                            update_single_course_id = int(input("Enter Course Id For Update Single course:-"))
                            update_single_course_id = str(update_single_course_id)
                            course_update = conn.execute("select * from `courses` where id = '" + update_single_course_id + "'")
                            data_t = tuple(course_update)
                            if len(data_t) == 0:
                                print("Course Not Found.")
                            else:
                                print("Course-ID,Course-Name,Course-Fee")
                                for n in data_t:
                                    print(n)

                                while True:
                                    print("""
                                        Press 1 For Course_Name.
                                        Press 2 For Fee.
                                        Press 0 For Back.
                                    """)
                                    press = int(input("Enter A Number:-"))
                                    if press == 1:
                                        course_name = input("Enter (Maximum 100 Characters) Course_Name For Update:-")
                                        course_name = course_name.lower()
                                        yes_no = input("Are You Sure Want To Update Single Course-Name? (Y/N):-")
                                        yes_no = yes_no.lower()
                                        if yes_no == 'y':
                                            course_update = "update `courses` set `course`='" + course_name + "' where `id` ='" + update_single_course_id + "'"
                                            conn.execute(course_update)
                                            conn.commit()
                                            print("Course-Name Updated.")
                                            data = conn.execute("select * from `courses` where id = '" + update_single_course_id + "'")
                                            print("Course-ID,Course-Name,Course-Fee")
                                            for n in data:
                                                print(n)
                                        else:
                                            print("You Entered (N) For No.")

                                    elif press == 2:
                                        fee = int(input("Enter (IN NUMBERS) Fee For Update:-"))
                                        fee = str(fee)
                                        yes_no = input("Are You Sure Want To Update Single Course Fee? (Y/N):-")
                                        yes_no = yes_no.lower()
                                        if yes_no == 'y':
                                            fee_update = "update `courses` set `fee`='" + fee + "' where `id` ='" + update_single_course_id + "'"
                                            conn.execute(fee_update)
                                            conn.commit()
                                            print("Course Fee Updated.")
                                            data = conn.execute("select * from `courses` where id = '" + update_single_course_id + "'")
                                            print("Course-ID,Course-Name,Course-Fee")
                                            for n in data:
                                                print(n)
                                        else:
                                            print("You Entered (N) For No.")

                                    elif press == 0:
                                        break

                    # ---> Update Single Course end Here

                    # ---> Courses Back start Here
                    elif user_input == 0:
                        break
                    # ---> Courses  Back end Here

            # ---> courses end here

            # ---> Students-Attendence start here
            elif press == 3:
                while True:
                    print('''
                        Press 1 For Check Attendence-List.
                        Press 2 For Take-Attendence.
                        Press 3 For Delete-All-Attendence.
                        Press 4 For Update-Attendence.
                        Press 0 For Back.
                    ''')
                    press = int(input("Press Any Number:-"))
                    if press == 1:
                        while True:
                            print('''
                                Press 1 For Check ALL Attendence-List.
                                Press 2 For Check Attendence (by Course ONLY).
                                Press 3 For Check Attendence (by Course ONLY with Date).
                                Press 0 For Back.
                            ''')
                            press = int(input("Press Any Number:-"))
                            if press == 1:
                                data = conn.execute('''
                                    select `s`.`id`,`s`.`first_name`,`s`.`last_name`,
                                    `s`.`phone_number`, `c`.`course`,`sa`.`attendence`,STRFTIME('%d/%m/%Y,%H:%M',`sa`.`date`) as `date`
                                    from `students` as `s`, `courses` as `c`,`students_attendence` as `sa`
                                    where `c`.`id` = `s`.`course` and `s`.`id` = `sa`.`student_id`;
                                ''')
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Attendence Not Found.")
                                else:
                                    print("Student-Id,First-Name,Last-Name,Phone-Number,Course-Name,Attendence,Attendence-Time")
                                    for n in data_t:
                                        print(n)

                            elif press == 2:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not Found.")
                                else:
                                    print("Course-ID,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course-ID only To check Attendence (BY COURSE):-"))
                                    course_id = str(course_id)

                                    data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`sa`.`attendence`,STRFTIME('%d/%m/%Y,%H:%M',`sa`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_attendence` as `sa` where `c`.`id` = `s`.`course` and `s`.`id` = `sa`.`student_id` and `c`.`id` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Attendence Not Found.")
                                    else:
                                        print("Student-Id,First-Name,Last-Name,Phone-Number,Course-Name,Attendence,Attendence-Time")
                                        for n in data_t:
                                            print(n)

                            elif press == 3:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not Found.")
                                else:
                                    print("Course-ID,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course-ID only To check Attendence (BY COURSE):-"))
                                    course_id = str(course_id)
                                    data = "select `id`,`course` from `courses` where id = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Course Not Found.")
                                    else:
                                        print("Course-ID,Course-Name")
                                        for n in data_t:
                                            print(n)

                                        data = "select `sa`.`id` from `students_attendence` as `sa`,`students` as `s` where `s`.`id` = `sa`.`student_id` and `s`.`course` = '" + course_id + "'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Attendence Not Found.")
                                        else:
                                            day = int(input("Enter Date only To check Attendence (BY Date) like (01 OR 29):-"))
                                            month = int(input("Enter Month only To check Attendence (BY Date) like(01 OR 11):-"))
                                            year = int(input("Enter Year only To check Attendence (BY Date) like(2010 OR 2022):-"))

                                            if day < 10:
                                                day = str(day)
                                                day = "0"+day
                                            else:
                                                day = str(day)

                                            if month < 10:
                                                month = str(month)
                                                month = "0"+month
                                            else:
                                                month = str(month)

                                            year = str(year)
                                            date = day + "/" + month + "/" + year
                                            course_id = str(course_id)
                                            data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`sa`.`attendence`,STRFTIME('%d/%m/%Y',`sa`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_attendence` as `sa` where `c`.`id` = `s`.`course` and `s`.`id` = `sa`.`student_id` and `c`.`id` = '" + course_id + "' and STRFTIME('%d/%m/%Y',`sa`.`date`) = '" + date + "';"
                                            cur = conn.cursor()
                                            cur.execute(data)
                                            data_fetch = cur.fetchall()
                                            data_std = tuple(data_fetch)
                                            if len(data_std) == 0:
                                                print("Attendence Not Found.")
                                            else:
                                                print("Student-Id,First-Name,Last-Name,Phone-Number,Course-Name,Attendence,Attendence-Time")
                                                for n in data_std:
                                                    print(n)



                            elif press == 0:
                                break

                    elif press == 2:
                        while True:
                            print('''
                                Press 1 For Take Students-Attendence.
                                Press 0 For Back.
                            ''')
                            press = int(input("Press Any Number:-"))
                            if press == 1:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not Found.")
                                else:
                                    data_len = len(data_t)
                                    data_len = str(data_len)
                                    print("Found " + data_len + " Records")
                                    print("Course-ID,course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course ID For Take Attendence (BY COURSE ONLY):-"))
                                    course_id = str(course_id)

                                    data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Students Not Found.")
                                    else:
                                        data_len = len(data_t)
                                        data_len = str(data_len)
                                        print("Found " + data_len + " Records")
                                        print("You Have Follwings Students In this Course.")
                                        print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                        for n in data_t:
                                            print(n)

                                        student_id = int(input("Enter STUDENT-ID only For (TAKE SINGLE STUDENT-ATTENDENCE):-"))
                                        student_id = str(student_id)

                                        data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "' and `s`.`id` = '"+student_id+"'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Student Not Found.")
                                        else:
                                            data_len = len(data_t)
                                            data_len = str(data_len)
                                            print("Found " + data_len + " Records")
                                            print("You Have Follwings Students In this Course.")
                                            print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                            for n in data_t:
                                                print(n)

                                            student_attendence = input("Enter STUDENT-ATTENDENCE Present/Absent (MAXIMUM 7 CHARACTERS):-")
                                            student_attendence = student_attendence.lower()
                                            date = datetime.datetime.now()
                                            insert_list = [student_id, student_attendence, date]

                                            yes_no = input("Are You Sure Want To Add New Student-Attendence? (Y/N):-")
                                            yes_no = yes_no.lower()
                                            if yes_no == 'y':
                                                conn.execute('''insert into `students_attendence`
                                                (`student_id`,`attendence`,`date`)
                                                values(?,?,?)''', insert_list)

                                                conn.commit()
                                                print("1 ATTENDENCE ADDED")
                                                data = conn.execute("select * from `students_attendence` where `id` = (select MAX(id) from `students_attendence`)")
                                                print("Attendence-ID,Student-ID,Attendence,Attendence-Date")
                                                for n in data:
                                                    print(n)

                                            else:
                                                print("You Entered (N) For No.")

                            elif press == 0:
                                break

                    elif press == 3:
                        data = conn.execute("select * from `students_attendence`")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Attendence Not Found.")
                        else:
                            data_t = len(data_t)
                            data_t = str(data_t)
                            print("Found "+data_t+" Records")

                            yes_no = input("Are You Sure Want To Delete All Students-Attendence? (Y/N):-")
                            yes_no = yes_no.lower()

                            if yes_no == 'y':
                                d = "delete from `students_attendence`"
                                conn.execute(d)
                                conn.commit()
                                print("All Students-Attendence Deleted.")

                            else:
                                print("You Entered (N) For No.")

                    elif press == 4:
                        print("You Have Follwings Courses Students.")
                        data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Course Not Found.")
                        else:
                            data_len = len(data_t)
                            data_len = str(data_len)
                            print("Found " + data_len + " Records")
                            print("Course-ID,Course-Name")
                            for n in data_t:
                                print(n)

                            course_id = int(input("Enter Course ID For Update-Attendence (BY COURSE ONLY):-"))
                            course_id = str(course_id)

                            data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "'"
                            cur = conn.cursor()
                            cur.execute(data)
                            data_fetch = cur.fetchall()
                            data_t = tuple(data_fetch)
                            if len(data_t) == 0:
                                print("Student Not Found.")
                            else:
                                data_len = len(data_t)
                                data_len = str(data_len)
                                print("Found " + data_len + " Records")
                                print("You Have Follwings Students In this Course.")
                                print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                for n in data_t:
                                    print(n)

                                student_id = int(input("Enter STUDENT-ID only For (UPDATE SINGLE STUDENT-ATTENDENCE):-"))
                                student_id = str(student_id)

                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "' and `s`.`id` = '"+student_id+"'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    data_len = len(data_t)
                                    data_len = str(data_len)
                                    print("Found " + data_len + " Records")
                                    print("You Have Follwings Students In this Course.")
                                    print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    data = "select `sa`.`id` from `students_attendence` as `sa`,`students` as `s` where `s`.`id` = `sa`.`student_id` and `s`.`course` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Attendence Not Found.")
                                    else:
                                        day = int(input("Enter Date only To Update Attendence (BY Date) like (01 OR 29):-"))
                                        month = int(input("Enter Month only To Update Attendence (BY Date) like(01 OR 11):-"))
                                        year = int(input("Enter Year only To Update Attendence (BY Date) like(2010 OR 2022):-"))

                                        if day < 10:
                                            day = str(day)
                                            day = "0" + day
                                        else:
                                            day = str(day)

                                        if month < 10:
                                            month = str(month)
                                            month = "0" + month
                                        else:
                                            month = str(month)

                                        year = str(year)
                                        date = day + "/" + month + "/" + year

                                        data = "select `sa`.`id`,`s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`sa`.`attendence`,STRFTIME('%d/%m/%Y',`sa`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_attendence` as `sa` where `c`.`id` = `s`.`course` and `s`.`id` = `sa`.`student_id` and `s`.`id` = '" + student_id + "' and STRFTIME('%d/%m/%Y',`sa`.`date`) = '" + date + "'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Attendence Not Found.")
                                        else:
                                            print("Attendence-ID,Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Attendence,Attendence-Date")
                                            for n in data_t:
                                                print(n)

                                            attendence_id = int(input("Enter STUDENT-ATTENDENCE-ID First For Update:-"))
                                            attendence_id = str(attendence_id)
                                            data = "select `sa`.`id`,`s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`sa`.`attendence`,STRFTIME('%d/%m/%Y',`sa`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_attendence` as `sa` where `c`.`id` = `s`.`course` and `s`.`id` = `sa`.`student_id` and `s`.`id` = '" + student_id + "' and STRFTIME('%d/%m/%Y',`sa`.`date`) = '" + date + "' and `sa`.`id` = '" + attendence_id + "'"
                                            cur = conn.cursor()
                                            cur.execute(data)
                                            data_fetch = cur.fetchall()
                                            data_t = tuple(data_fetch)
                                            if len(data_t) == 0:
                                                print("Attendence Not Found.")
                                            else:
                                                print("Attendence-ID,Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Attendence,Attendence-Date")
                                                for n in data_t:
                                                    print(n)

                                                student_attendence = input("Enter STUDENT-ATTENDENCE Present/Absent (MAXIMUM 7 CHARACTERS):-")
                                                student_attendence = student_attendence.lower()

                                                yes_no = input("Are You Sure Want To Update Student-Attendence? (Y/N):-")
                                                yes_no = yes_no.lower()
                                                if yes_no == 'y':
                                                    data = "update `students_attendence` set `attendence`='" + student_attendence + "' where `student_id` ='" + student_id + "' and STRFTIME('%d/%m/%Y',`date`) = '" + date + "' and `id` = '" + attendence_id + "'"
                                                    conn.execute(data)
                                                    conn.commit()
                                                    print("1 ATTENDENCE UPDATED")

                                                else:
                                                    print("You Entered (N) For No.")

                    elif press == 0:
                        break
            # ---> Students-Attendence end here

            # ---> Students-Exams start here
            elif press == 4:
                while True:
                    print('''
                        Press 1 For Check Exam-Results-List.
                        Press 2 For Take-Exam.
                        Press 3 For Delete-All-Exam-Results.
                        Press 4 For Update-Exam-Results.
                        Press 0 For Back.
                    ''')

                    press = int(input("Press Any Number:-"))
                    if press == 1:
                        while True:
                            print('''
                                Press 1 For Check ALL Results-List.
                                Press 2 For Check Results (by Course ONLY).
                                Press 3 For Check Results (by Course ONLY with Date).
                                Press 0 For Back.
                            ''')
                            press = int(input("Press Any Number:-"))
                            if press == 1:
                                data = conn.execute('''
                                select `s`.`id`,`s`.`first_name`,`s`.`last_name`,
                                `s`.`phone_number`, `c`.`course`,`se`.`exam`,STRFTIME('%d/%m/%Y,%H:%M',`se`.`date`) as `date`
                                from `students` as `s`, `courses` as `c`,`students_exams` as `se`
                                where `c`.`id` = `s`.`course` and `s`.`id` = `se`.`student_id`;
                                ''')
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Result Not Found.")
                                else:
                                    print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Exam,Exam-Date")
                                    for n in data_t:
                                        print(n)

                            elif press == 2:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not Found.")
                                else:
                                    print("Course-ID,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course-ID only To check Results (BY COURSE):-"))
                                    course_id = str(course_id)

                                    data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`se`.`exam`,STRFTIME('%d/%m/%Y,%H:%M',`se`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_exams` as `se` where `c`.`id` = `s`.`course` and `s`.`id` = `se`.`student_id` and `c`.`id` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Result Not Found.")
                                    else:
                                        print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Exam,Exam-Date")
                                        for n in data_t:
                                            print(n)

                            elif press == 3:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not Found.")
                                else:
                                    print("Course-ID,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course-ID only To check Results (BY COURSE):-"))
                                    course_id = str(course_id)

                                    data = conn.execute("select `id`,`course` from `courses` where id = '" + course_id + "'")
                                    data_t = tuple(data)
                                    if len(data_t) == 0:
                                        print("Course Not Found.")
                                    else:
                                        print("Course-ID,Course-Name")
                                        for n in data_t:
                                            print(n)

                                        data = "select `se`.`id` from `students_exams` as `se`,`students` as `s` where `s`.`id` = `se`.`student_id` and `s`.`course` = '" + course_id + "'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Result Not Found.")
                                        else:
                                            day = int(input("Enter Date only To check Results (BY Date) like (01 OR 29):-"))
                                            month = int(input("Enter Month only To check Results (BY Date) like(01 OR 11):-"))
                                            year = int(input("Enter Year only To check Results (BY Date) like(2010 OR 2022):-"))

                                            if day < 10:
                                                day = str(day)
                                                day = "0" + day
                                            else:
                                                day = str(day)

                                            if month < 10:
                                                month = str(month)
                                                month = "0" + month
                                            else:
                                                month = str(month)

                                            year = str(year)
                                            date = day + "/" + month + "/" + year

                                            data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`se`.`exam`,STRFTIME('%d/%m/%Y',`se`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_exams` as `se` where `c`.`id` = `s`.`course` and `s`.`id` = `se`.`student_id` and `c`.`id` = '" + course_id + "' and STRFTIME('%d/%m/%Y',`se`.`date`) = '" + date + "'"
                                            cur = conn.cursor()
                                            cur.execute(data)
                                            data_fetch = cur.fetchall()
                                            data_t = tuple(data_fetch)
                                            if len(data_t) == 0:
                                                print("Result Not Found.")
                                            else:
                                                print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Exam,Exam-Date")
                                                for n in data_t:
                                                    print(n)


                            elif press == 0:
                                break

                    elif press == 2:
                        while True:
                            print('''
                                Press 1 For Take Students-Exams.
                                Press 0 For Back.
                            ''')
                            press = int(input("Press Any Number:-"))
                            if press == 1:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not Found.")
                                else:
                                    data_len = len(data_t)
                                    data_len = str(data_len)
                                    print("Found " + data_len + " Records")
                                    print("Course-ID,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course ID For Take Exams (BY COURSE ONLY):-"))
                                    course_id = str(course_id)

                                    data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Student Not Found.")
                                    else:
                                        data_len = len(data_t)
                                        data_len = str(data_len)
                                        print("Found " + data_len + " Records")
                                        print("You Have Follwings Students In this Course.")
                                        print("Student-Id,First-Name,Last-Name,Phone-Number,Course-Name")
                                        for n in data_t:
                                            print(n)

                                        student_id = int(input("Enter STUDENT-ID only For (TAKE SINGLE STUDENT-EXAM):-"))
                                        student_id = str(student_id)
                                        data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "' and `s`.`id` = '"+student_id+"'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Student Not Found.")
                                        else:
                                            data_len = len(data_t)
                                            data_len = str(data_len)
                                            print("Found " + data_len + " Records")
                                            print("Student-Id,First-Name,Last-Name,Phone-Number,Course-Name")
                                            for n in data_t:
                                                print(n)

                                            data = "select `se`.`id` from `students_exams` as `se`,`students` as `s` where `s`.`id` = `se`.`student_id` and `s`.`course` = '" + course_id + "'"
                                            cur = conn.cursor()
                                            cur.execute(data)
                                            data_fetch = cur.fetchall()
                                            data_t = tuple(data_fetch)
                                            if len(data_t) == 0:
                                                print("Exam Not Found.")
                                            else:
                                                student_exam = input("Enter STUDENT-EXAM MARKS/Pass/Fail/Present/Absent (MAXIMUM 10 CHARACTERS):-")
                                                student_exam = student_exam.lower()
                                                date = datetime.datetime.now()
                                                insert_list = [student_id, student_exam, date]

                                                yes_no = input("Are You Sure Want To Add New Student-Result? (Y/N):-")
                                                yes_no = yes_no.lower()
                                                if yes_no == 'y':
                                                    conn.execute('''insert into `students_exams`
                                                    (`student_id`,`exam`,`date`)
                                                    values(?,?,?)''',
                                                    insert_list)

                                                    conn.commit()
                                                    print("1 EXAM ADDED")
                                                    data = conn.execute("select * from `students_exams` where `id` = (select MAX(id) from `students_exams`)")
                                                    print("Exam-ID,Student-ID,Exam,Exam-Date")
                                                    for n in data:
                                                        print(n)

                                                else:
                                                    print("You Entered (N) For No.")



                            elif press == 0:
                                break

                    elif press == 3:
                        data = conn.execute("select * from `students_exams`")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Result Not Found.")
                        else:
                            data_t = len(data_t)
                            data_t = str(data_t)
                            print("Found " + data_t + " Records")

                            yes_no = input("Are You Sure Want To Delete All Students-Results? (Y/N):-")
                            yes_no = yes_no.lower()

                            if yes_no == 'y':
                                d = "delete from `students_exams`"
                                conn.execute(d)
                                conn.commit()
                                print("All Students-Results Deleted.")

                            else:
                                print("You Entered (N) For No.")

                    elif press == 4:
                        print("You Have Follwings Courses Students.")
                        data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Course Not Found.")
                        else:
                            data_len = len(data_t)
                            data_len = str(data_len)
                            print("Found " + data_len + " Records")
                            print("Course-ID,Course-Name")
                            for n in data_t:
                                print(n)

                            course_id = int(input("Enter Course ID For Update-Results (BY COURSE ONLY):-"))
                            course_id = str(course_id)

                            data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "'"
                            cur = conn.cursor()
                            cur.execute(data)
                            data_fetch = cur.fetchall()
                            data_t = tuple(data_fetch)
                            if len(data_t) == 0:
                                print("Student Not Found.")
                            else:
                                data_len = len(data_t)
                                data_len = str(data_len)
                                print("Found " + data_len + " Records")
                                print("You Have Follwings Students In this Course.")
                                print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                for n in data_t:
                                    print(n)

                                student_id = int(input("Enter STUDENT-ID only For (UPDATE SINGLE STUDENT-Results):-"))
                                student_id = str(student_id)

                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "' and `s`.`id` = '" + student_id + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    data_len = len(data_t)
                                    data_len = str(data_len)
                                    print("Found " + data_len + " Records")
                                    print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    data = "select `se`.`id` from `students_exams` as `se`,`students` as `s` where `s`.`id` = `se`.`student_id` and `s`.`course` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Result Not Found.")
                                    else:
                                        day = int(input("Enter Date only To Update Results (BY Date) like (01 OR 29):-"))
                                        month = int(input("Enter Month only To Update Results (BY Date) like(01 OR 11):-"))
                                        year = int(input("Enter Year only To Update Results (BY Date) like(2010 OR 2022):-"))
                                        if day < 10:
                                            day = str(day)
                                            day = "0" + day
                                        else:
                                            day = str(day)

                                        if day < 10:
                                            month = str(month)
                                            month = "0" + month
                                        else:
                                            month = str(month)

                                        year = str(year)
                                        date = day + "/" + month + "/" + year

                                        data = "select `se`.`id`,`s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`se`.`exam`,STRFTIME('%d/%m/%Y',`se`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_exams` as `se` where `c`.`id` = `s`.`course` and `s`.`id` = `se`.`student_id` and `s`.`id` = '" + student_id + "' and STRFTIME('%d/%m/%Y',`se`.`date`) = '" + date + "'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Result Not Found.")
                                        else:
                                            print("Exam-Id,Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Exam,Exam-Date")
                                            for n in data_t:
                                                print(n)

                                            exam_id = int(input("Enter STUDENT-EXAMS-ID First For Update:-"))
                                            exam_id = str(exam_id)
                                            data = "select `se`.`id`,`s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`se`.`exam`,STRFTIME('%d/%m/%Y',`se`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_exams` as `se` where `c`.`id` = `s`.`course` and `s`.`id` = `se`.`student_id` and `s`.`id` = '" + student_id + "' and STRFTIME('%d/%m/%Y',`se`.`date`) = '" + date + "' and `se`.`id` = '" + exam_id + "'"
                                            cur = conn.cursor()
                                            cur.execute(data)
                                            data_fetch = cur.fetchall()
                                            data_t = tuple(data_fetch)
                                            if len(data_t) == 0:
                                                print("Result Not Found.")
                                            else:
                                                print("Exam-Id,Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Exam,Exam-Date")
                                                for n in data_t:
                                                    print(n)

                                                student_exam = input("Enter STUDENT-EXAM MARKS/Pass/Fail/Present/Absent (MAXIMUM 10 CHARACTERS):-")
                                                student_exam = student_exam.lower()

                                                yes_no = input("Are You Sure Want To Update Student-EXAM-RESULTS? (Y/N):-")
                                                yes_no = yes_no.lower()
                                                if yes_no == 'y':
                                                    data = "update `students_exams` set `exam`='" + student_exam + "' where `student_id` ='" + student_id + "' and STRFTIME('%d/%m/%Y',`date`) = '" + date + "' and `id` = '" + exam_id + "'"
                                                    conn.execute(data)
                                                    conn.commit()
                                                    print("1 Result UPDATED")

                                                else:
                                                    print("You Entered (N) For No.")

                    elif press == 0:
                        break
                    # ---> Students-Exams end here


            # ---> Students-Payments start Here
            elif press == 5:
                while True:
                    print('''
                        Press 1 For Check Payments-List.
                        Press 2 For Take-Payments.
                        Press 3 For Delete-All-Payments-List.
                        Press 4 For Update-Payments.
                        Press 0 For Back.
                    ''')

                    press = int(input("Press Any Number:-"))
                    if press == 1:
                        while True:
                            print('''
                                Press 1 For Check ALL Payments-List.
                                Press 2 For Check Payments-List (by Course ONLY).
                                Press 3 For Check Payments-List (by Course ONLY with Date).
                                Press 4 For Check Remaining-Half-Payments-List (Payments-half).
                                Press 0 For Back.
                            ''')
                            press = int(input("Press Any Number:-"))
                            if press == 1:
                                data = conn.execute('''
                                select `s`.`id`,`s`.`first_name`,`s`.`last_name`,
                                `s`.`phone_number`, `c`.`course`,`sp`.`payments`,
                                STRFTIME('%d/%m/%Y,%H:%M',`sp`.`date`) as `date`
                                from `students` as `s`, `courses` as `c`,`students_payments` as `sp`
                                where `c`.`id` = `s`.`course` and `s`.`id` = `sp`.`student_id`;
                                ''')
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Payment Not Found.")
                                else:
                                    print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Payments,Payments-Date")
                                    for n in data_t:
                                        print(n)

                            elif press == 2:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not  Found.")
                                else:
                                    print("Course-ID,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course-ID only To check Payments (BY COURSE only):-"))
                                    course_id = str(course_id)

                                    data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`sp`.`payments`,STRFTIME('%d/%m/%Y,%H:%M',`sp`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_payments` as `sp` where `c`.`id` = `s`.`course` and `s`.`id` = `sp`.`student_id` and `c`.`id` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Payments Not Found.")
                                    else:
                                        print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Payments,Payments-Date")
                                        for n in data_t:
                                            print(n)

                            elif press == 3:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not Found.")
                                else:
                                    print("Course-ID,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course-ID only To check Payments (BY COURSE):-"))
                                    course_id = str(course_id)

                                    data = conn.execute("select `id`,`course` from `courses` where id = '" + course_id + "'")
                                    data_t = tuple(data)
                                    if len(data_t) == 0:
                                        print("Course Not Found.")
                                    else:
                                        print("Course-ID,Course-Name")
                                        for n in data_t:
                                            print(n)

                                        data = "select `sp`.`id` from `students_payments` as `sp`,`students` as `s` where `s`.`id` = `sp`.`student_id` and `s`.`course` = '" + course_id + "'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Payments Not Found.")
                                        else:
                                            day = int(input("Enter Date only To check Payments (BY Date) like (01 OR 29):-"))
                                            month = int(input("Enter Month only To check Payments (BY Date) like(01 OR 11):-"))
                                            year = int(input("Enter Year only To check Payments (BY Date) like(2010 OR 2022):-"))
                                            if day < 10:
                                                day = str(day)
                                                day = "0" + day
                                            else:
                                                day = str(day)

                                            if month < 10:
                                                month = str(month)
                                                month = "0" + month
                                            else:
                                                month = str(month)

                                            year = str(year)
                                            date = day + "/" + month + "/" + year

                                            data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`sp`.`payments`,STRFTIME('%d/%m/%Y',`sp`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_payments` as `sp` where `c`.`id` = `s`.`course` and `s`.`id` = `sp`.`student_id` and `c`.`id` = '" + course_id + "' and STRFTIME('%d/%m/%Y',`sp`.`date`) = '" + date + "'"
                                            cur = conn.cursor()
                                            cur.execute(data)
                                            data_fetch = cur.fetchall()
                                            data_t = tuple(data_fetch)
                                            if len(data_t) == 0:
                                                print("Payment Not Found.")
                                            else:
                                                print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Payments,Payments-Date")
                                                for n in data_t:
                                                    print(n)

                            elif press == 4:
                                data = conn.execute("select * from `students_payments`")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Payment Not Found.")
                                else:
                                    data_t = len(data_t)
                                    data_t = str(data_t)
                                    print("Found " + data_t + " Records")

                                    data = "select `sp`.`id`,`s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`father_name`,`s`.`phone_number`,`c`.`course`,`sp`.`payments`,(`c`.`fee` - `sp`.`payments`) as remaining_fee,`c`.`fee` as `total_course_fee` FROM`students_Payments` as `sp`,`students` as `s`,`courses` as `c`WHERE `s`.`id` = `sp`.`student_id` AND `s`.`course` = `c`.`id`;"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Payment Not Found.")
                                    else:
                                        print("Payment-ID,Student-ID,First-Name,Last-Name,Father-Name,Phone-Number,Course-Name,Payments,Remaining-Payment,Total-Payment")
                                        for n in data_t:
                                            print(n)

                            elif press == 0:
                                break

                    elif press == 2:
                        while True:
                            print('''
                                Press 1 For Take Students-Payments.
                                Press 0 For Back.
                            ''')
                            press = int(input("Press Any Number:-"))
                            if press == 1:
                                print("You Have Follwings Courses Students.")
                                data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                                data_t = tuple(data)
                                if len(data_t) == 0:
                                    print("Course Not Found.")
                                else:
                                    data_len = len(data_t)
                                    data_len = str(data_len)
                                    print("Found " + data_len + " Records")
                                    print("Course-ID,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    course_id = int(input("Enter Course ID For Take Payments (BY COURSE ONLY):-"))
                                    course_id = str(course_id)

                                    data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Student Not Found.")
                                    else:
                                        data_len = len(data_t)
                                        data_len = str(data_len)
                                        print("Found " + data_len + " Records")
                                        print("You Have Follwings Students In this Course.")
                                        print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                        for n in data_t:
                                            print(n)

                                        student_id = int(input("Enter STUDENT-ID only For (TAKE SINGLE STUDENT-PAYMENTS):-"))
                                        student_id = str(student_id)
                                        data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "' and `s`.`id` = '"+student_id+"'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Student Not Found.")
                                        else:
                                            data_len = len(data_t)
                                            data_len = str(data_len)
                                            print("Found " + data_len + " Records")
                                            print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                            for n in data_t:
                                                print(n)

                                            date = datetime.datetime.now()
                                            print(date)
                                            print("This is Your Total Course FEE.")
                                            data = conn.execute("select `course`,`fee` from `courses` where `id` = '"+course_id+"' order by `id` asc")
                                            print("Course-Name,Course-Fee")
                                            for n in data:
                                                print(n)

                                            student_payment = int(input("Enter STUDENT-PAYMENT 1000/2000 (IN NUMBERS):-"))
                                            print(student_payment)
                                            student_payment = str(student_payment)
                                            total_payments = conn.execute("select `fee` from `courses` where `id` = '" + course_id + "'")
                                            print("Course Fee.")
                                            for n in total_payments:
                                                print(n)

                                            date = datetime.datetime.now()
                                            insert_list = [student_id, student_payment,date]

                                            yes_no = input("Are You Sure Want To Add New Student-Payments? (Y/N):-")
                                            yes_no = yes_no.lower()
                                            if yes_no == 'y':
                                                conn.execute('''insert into `students_payments`
                                                (`student_id`,`payments`,`date`)
                                                values(?,?,?)''', insert_list)

                                                conn.commit()
                                                print("1 PAYMENT ADDED")
                                                data = conn.execute("select * from `students_payments` where `id` = (select MAX(id) from `students_payments`)")
                                                print("Payment-ID,Student-ID,Payments,Payments-Date")
                                                for n in data:
                                                    print(n)

                                            else:
                                                print("You Entered (N) For No.")

                            elif press == 0:
                                break

                    elif press == 3:
                        data = conn.execute("select * from `students_payments`")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Payment Not Found.")
                        else:
                            data_t = len(data_t)
                            data_t = str(data_t)
                            print("Found " + data_t + " Records")

                            yes_no = input("Are You Sure Want To Delete All Students-Payments? (Y/N):-")
                            yes_no = yes_no.lower()

                            if yes_no == 'y':
                                d = "delete from `students_payments`"
                                conn.execute(d)
                                conn.commit()
                                print("All Students-Payments Deleted.")

                            else:
                                print("You Entered (N) For No.")

                    elif press == 4:
                        print("You Have Follwings Courses Students.")
                        data = conn.execute("select `id`,`course` from `courses` order by `id` asc")
                        data_t = tuple(data)
                        if len(data_t) == 0:
                            print("Course Not Found.")
                        else:
                            data_len = len(data_t)
                            data_len = str(data_len)
                            print("Found " + data_len + " Records")
                            print("Course-ID,Course-Name")
                            for n in data_t:
                                print(n)

                            course_id = int(input("Enter Course ID For Update-Payments (BY COURSE ONLY):-"))
                            course_id = str(course_id)

                            data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "'"
                            cur = conn.cursor()
                            cur.execute(data)
                            data_fetch = cur.fetchall()
                            data_t = tuple(data_fetch)
                            if len(data_t) == 0:
                                print("Student Not Found.")
                            else:
                                data_len = len(data_t)
                                data_len = str(data_len)
                                print("Found " + data_len + " Records")
                                print("You Have Follwings Students In this Course.")
                                print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                for n in data_t:
                                    print(n)

                                student_id = int(input("Enter STUDENT-ID only For (UPDATE SINGLE STUDENT-Payments):-"))
                                student_id = str(student_id)

                                data = "select `s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course` from `students` as `s`, `courses` as `c` where `c`.`id` = `s`.`course` and `c`.`id` = '" + course_id + "' and `s`.`id` = '" + student_id + "'"
                                cur = conn.cursor()
                                cur.execute(data)
                                data_fetch = cur.fetchall()
                                data_t = tuple(data_fetch)
                                if len(data_t) == 0:
                                    print("Student Not Found.")
                                else:
                                    data_len = len(data_t)
                                    data_len = str(data_len)
                                    print("Found " + data_len + " Records")
                                    print("Student-ID,First-Name,Last-Name,Phone-Number,Course-Name")
                                    for n in data_t:
                                        print(n)

                                    data = "select `sp`.`id` from `students_payments` as `sp`,`students` as `s` where `s`.`id` = `sp`.`student_id` and `s`.`course` = '" + course_id + "'"
                                    cur = conn.cursor()
                                    cur.execute(data)
                                    data_fetch = cur.fetchall()
                                    data_t = tuple(data_fetch)
                                    if len(data_t) == 0:
                                        print("Payment Not Found.")
                                    else:
                                        day = int(input("Enter Date only To Update Results (BY Date) like (01 OR 29):-"))
                                        month = int(input("Enter Month only To Update Results (BY Date) like(01 OR 11):-"))
                                        year = int(input("Enter Year only To Update Results (BY Date) like(2010 OR 2022):-"))
                                        if day < 10:
                                            day = str(day)
                                            day = "0" + day
                                        else:
                                            day = str(day)

                                        if month < 10:
                                            month = str(month)
                                            month = "0" + month
                                        else:
                                            month = str(month)

                                        year = str(year)
                                        date = day + "/" + month + "/" + year

                                        data = "select `sp`.`id`,`s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`sp`.`payments`,STRFTIME('%d/%m/%Y',`sp`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_payments` as `sp` where `c`.`id` = `s`.`course` and `s`.`id` = `sp`.`student_id` and `s`.`id` = '" + student_id + "' and STRFTIME('%d/%m/%Y',`sp`.`date`) = '" + date + "'"
                                        cur = conn.cursor()
                                        cur.execute(data)
                                        data_fetch = cur.fetchall()
                                        data_t = tuple(data_fetch)
                                        if len(data_t) == 0:
                                            print("Payment Not Found.")
                                        else:
                                            print("Payment-ID,Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Payments,Payments-Date")
                                            for n in data_t:
                                                print(n)

                                            payment_id = int(input("Enter STUDENT-PAYMENTS-ID First For Update:-"))
                                            payment_id = str(payment_id)
                                            data = "select `sp`.`id`,`s`.`id`,`s`.`first_name`,`s`.`last_name`,`s`.`phone_number`, `c`.`course`,`sp`.`payments`,STRFTIME('%d/%m/%Y',`sp`.`date`) as `date` from `students` as `s`, `courses` as `c`,`students_payments` as `sp` where `c`.`id` = `s`.`course` and `s`.`id` = `sp`.`student_id` and `s`.`id` = '" + student_id + "' and STRFTIME('%d/%m/%Y',`sp`.`date`) = '" + date + "' and `sp`.`id` = '" + payment_id + "'"
                                            cur = conn.cursor()
                                            cur.execute(data)
                                            data_fetch = cur.fetchall()
                                            data_t = tuple(data_fetch)
                                            if len(data_t) == 0:
                                                print("Payment Not Found.")
                                            else:
                                                print("Payment-ID,Student-ID,First-Name,Last-Name,Phone-Number,Course-Name,Payments,Payments-Date")
                                                for n in data_t:
                                                    print(n)

                                                student_payment = int(input("Enter STUDENT-PAYMENTS like 1000/2000 (MAXIMUM 10 CHARACTERS):-"))
                                                student_payment = str(student_payment)
                                                yes_no = input("Are You Sure Want To Update Student-Payments? (Y/N):-")
                                                yes_no = yes_no.lower()
                                                if yes_no == 'y':
                                                    data = "update `students_payments` set `payments`='" + student_payment + "' where `student_id` ='" + student_id + "' and STRFTIME('%d/%m/%Y',`date`) = '" + date + "' and `id` = '" + payment_id + "'"
                                                    conn.execute(data)
                                                    conn.commit()
                                                    print("1 PAYMENT UPDATED")

                                                else:
                                                    print("You Entered (N) For No.")

                    elif press == 0:
                        break
            # ---> Students-Payments end Here

            # ---> Password start Here
            elif press == 6:
                while True:
                    print('''
                        Press 1 For Password Change.
                        Press 0 For Back.
                    ''')
                    press = int(input("Press Any Number:-"))

                    if press == 1:
                        old_username = input("Enter Your Old USER-NAME:-")
                        old_password = input("Enter Your Old USER-PASSWORD:-")
                        if old_username == user_name_input and old_password == user_password_input:
                            new1_password = input("Enter Your NEW USER-PASSWORD (Maximum 10 Characters):-")
                            new2_password = input("Confirm NEW USER-PASSWORD:-")
                            if new1_password == new2_password:
                                yes_no = input("Are You Sure Want To Change PASSWORD? (Y/N):-")
                                yes_no = yes_no.lower()
                                if yes_no == 'y':
                                    password_update = "update `admins` set `user_password`='" + new2_password + "' where `id` = 1"
                                    conn.execute(password_update)
                                    conn.commit()
                                    print("Password CHANGED.")

                                else:
                                    print("You Entered (N) For No.")

                            else:
                                print("Both NEW USER-PASSWORDS are not SAME!")

                        else:
                            print("Invalid OLD USER-NAME/USER-PASSWORD")

                    elif press == 0:
                        break
            # ---> Password end Here

            # ---> Exit start Here
            elif press == 0:
                break
            # ---> Exit end Here

        except Exception as e:
            print("You Enter Wrong Number", e)
    conn.close()
else:
    print("Invalid USER-NAME OR USER-PASSWORD")


