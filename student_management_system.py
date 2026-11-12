import sqlite3
import os
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    print("===============STUDENT MANAGEMENT SYSTEM===============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    while True:

        try:
            answer = int(input("Choose an option: "))
            break
        except ValueError:
            print("Please enter an option avaible in the menu!")
            continue
    return answer


def create_table():

    connection = sqlite3.connect("student_database.db")
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade TEXT, email TEXT)""")

    connection.commit()
    connection.close()


def add_student():

    student_name = input("Enter a student name: ").strip().capitalize()

    while True:

        student_grade = input("Enter grade: ").strip().upper()

        if student_grade not in ("A", "B", "C", "D", "F"):
            print("Please enter a valid grade")
            continue
        else:
            break

    while True:

        student_email = input("Enter email: ").strip().lower()

        if "@" not in student_email:
            print("Please enter a valdid email")
        else:
            break

    connection = sqlite3.connect("student_database.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO students (name, grade, email) VALUES (?, ?, ?)",
                   (student_name, student_grade, student_email))

    print("Student added succefully!")

    if cursor.rowcount == 0:
        print("Student not added")

    connection.commit()
    connection.close()


def view_students():

    connection = sqlite3.connect("student_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        print(
            f"ID: {student[0]} | Name: {student[1]} | Grade: {student[2]} | Email: {student[3]}""\n")


def update_student():

    connection = sqlite3.connect("student_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    while True:
        student_name = input("Search by name: ").capitalize()
        students_found = 0

        for student in students:
            if student[1] == student_name:
                print(
                    f"ID: {student[0]} | Name: {student[1]} | Grade: {student[2]} | Email: {student[3]}")
                students_found += 1
        if students_found == 0:
            print("Student not found. Please enter a valid name")
            continue

        print(f"{students_found} students found:""\n")

        while True:
            try:
                id_student = int(
                    input("\nEnter the ID of the student to update: "))
            except ValueError:
                print("Please enter a valid number")
                continue

            for student in students:
                if student[0] == id_student:
                    print(f"Student selected: {student[1]}")
                    break
            else:
                print("Please enter a valid ID")
                continue
            break

        while True:

            new_grade = input("\nNew Grade: ").strip().upper()

            if new_grade not in ("A", "B", "C", "D"):
                print("Please enter a valid grade")
                continue
            break
        break

    cursor.execute("UPDATE students SET grade = ? WHERE id = ?",
                   (new_grade, id_student))

    print("Student updated succefully")
    time.sleep(2)

    connection.commit()
    connection.close()


def delete_student():

    connection = sqlite3.connect("student_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    while True:

        student_name = input("Search by name: ").capitalize()
        students_found = 0

        for student in students:
            if student[1] == student_name:
                print(
                    f"ID: {student[0]} | Name: {student[1]} | Grade: {student[2]} | Email: {student[3]}")
                students_found += 1
                break
        if students_found == 0:
            print("Student not found. Please enter a valid name")
            continue

        print(f"{students_found} students found:""\n")

        while True:
            id_student = int(
                input("\nEnter the ID of the student to delete: "))

            for student in students:
                if student[0] == id_student:
                    print(f"Student selected: {student[1]}")
                    break
            else:
                print("Please enter a valid ID")
                continue
            break

        while True:
            decision = input(
                "Are you sure you want to delete {student[1]}? [Y/N]").lower().strip()

            if decision == "y":
                cursor.execute("DELETE FROM students WHERE id = ?",
                               (id_student,))
                print("Student deleted sucessfully")
                break
            elif decision == "n":
                print("Deletion canceled")
                print("Going back to main menu")
                time.sleep(3)
                return
            else:
                print("Please choose a valid option")
                continue
        break

    connection.commit()
    connection.close()


def exit_system():
    print("Exiting Student Management System...")
    time.sleep(3)
    print("See you later!")


def main():
    print("Opening Student Management Sytem...")
    time.sleep(5)
    clear_screen()
    create_table()

    while True:
        choice = show_menu()
        clear_screen()

        if choice == 1:
            add_student()
            continue
        elif choice == 2:
            view_students()
            continue
        elif choice == 3:
            update_student()
            continue
        elif choice == 4:
            delete_student()
            continue
        elif choice == 5:
            exit_system()
            break


main()
