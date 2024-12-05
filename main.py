import sqlite3
import sqlalchemy

db = sqlite3.connect('university.db')

cursor = db.cursor()

# 1 add student; 2 show the list of students, 3 add course; 4 show the list of course; 5 update student info; 6 update course info
choice = input('Оберіть дію')

#cursor.execute("""CREATE TABLE students (
    #id integer,
    #name text,
    #age integer,
    #courses text
#)""")


#cursor.execute("""CREATE TABLE courses (
    #course_id integer,
    #course_name text,
    #instructor text
#)""")



#ще не придумав як нормально зробити id :|
if choice == '1':
    id = input("id ¯\_(ツ)_/¯")
    name_student = input("Ім'я студента")
    age_student = input("Вік студента")
    major_student = input("Major студента")
    cursor.execute(
        "INSERT INTO students (id, name, age, courses) "
        "VALUES (?, ?, ?, ?)",
        (id, name_student, age_student, major_student)
    )
elif choice == '2':
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())
elif choice == '3':
    id_cours = input("id ¯\_(ツ)_/¯")
    name_cours = input("Ім'я курса")
    instructor_cours = input("Ім'я інструктора курса")
    cursor.execute(
        "INSERT INTO courses (course_id, course_name, instructor) "
        "VALUES (?, ?, ?)",
        (id_cours, name_cours, instructor_cours)
    )
elif choice == '4':
    cursor.execute("SELECT * FROM courses")
    print(cursor.fetchall())
elif choice == '5':
    id_2 = input('Введіть id студента, інформацію якого треба змінити')
    id = input("Новий id ¯\_(ツ)_/¯")
    name_student = input("Нове ім'я студента")
    age_student = input("Новий вік студента")
    major_student = input("Новий major студента")
    cursor.execute("UPDATE students "
                   "SET (id, name, age, courses) "
                   "WHERE id = id_2")
elif choice == '6':
    id_2 = input('Введіть id курса, інформацію якого треба змінити')
    id_cours = input("Новий id ¯\_(ツ)_/¯")
    name_cours = input("Нове ім'я курса")
    instructor_cours = input("Нове ім'я інструктора курса")
    cursor.execute("UPDATE students "
                   "SET (course_id, course_name, instructor) "
                   "WHERE id_cours = id_2")

db.commit()

db.close()


