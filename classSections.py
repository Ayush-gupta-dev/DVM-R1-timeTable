import sqlite3

class courseSections:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        # Creating the 'courses' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                CourseName TEXT NOT NULL,
                Sec TEXT NOT NULL,
                Days TEXT NOT NULL,
                TimeSlot1 TEXT NOT NULL,
                TimeSlot2 TEXT
            )
        ''')

        connection.commit()
        connection.close()

    def admin_authenticate(self):
        actual_password = "1234"
        entered_password = input("Enter the admin password: ")
        return entered_password == actual_password

    def admin_add_course(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        course_name = input("Enter the CourseName: ")
        sec = input("Enter the Section: ")
        days = input("Enter the Days: ")
        time_slot1 = input("Enter the TimeSlot1: ")
        time_slot2 = input("Enter the TimeSlot2: ")

        cursor.execute('''
            INSERT INTO courses (CourseName, Sec, Days, TimeSlot1, TimeSlot2)
            VALUES (?, ?, ?, ?, ?)
        ''', (course_name, sec, days, time_slot1, time_slot2))

        connection.commit()
        connection.close()

    def admin_print_courses(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM courses')
        admin_courses = cursor.fetchall()

        for course in admin_courses:
            print(course)

        connection.close()

    def main():
        courseInstance = courseSections("courses.db")
        courseInstance.create_table()
        if courseInstance.admin_authenticate():
            while True:
                print("\nAdmin Menu:")
                print("1. Add Course")
                print("2. Print Courses")
                print("3. Exit")

                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    courseInstance.admin_add_course()
                elif admin_choice == "2":
                    courseInstance.admin_print_courses()
                elif admin_choice == "3":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("Authentication failed.")


