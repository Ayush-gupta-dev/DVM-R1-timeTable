import csv
import sqlite3

class TimeTable:
    def __init__(self, database_name):
        self.database_name = database_name
    def print_all_courses(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM courses')
        admin_courses = cursor.fetchall()

        for course in admin_courses:
            print(course)

        connection.close()
   
    def checkClash(self,course_name, chosen_section, days, time,user_timetable):
        result_day=False
        result_time=False
        print(user_timetable,days,time)
        for tup in user_timetable:
            if(course_name==tup[0] and chosen_section==tup[1] ):
                print("already enrolled")
                return True
        for tup in user_timetable:
            for val in tup[2]:
                if any(char in val[0] for char in days[0]):
                    result_day = True
                    break
        for tup in user_timetable:
            for val in tup[3]:
                if(val==time[0]):
                    result_time=True
                    break
        if(result_day and result_time):
            print("time clash!!")
        return (result_day and result_time)

    def user_enroll(self):
        user_name = input("Enter your name: ")
        user_timetable = []

        while True:
            self.print_all_courses()
            course_name = input("Enter the CourseName you want to enroll in (or type 'exit' to stop): ")
            if course_name.lower() == 'exit':
                break

            connection = sqlite3.connect(self.database_name)
            cursor = connection.cursor()

            cursor.execute('''
                SELECT * FROM courses
                WHERE CourseName = ?
            ''', (course_name,))
            admin_sections = cursor.fetchall()

            if not admin_sections:
                print(f"No sections found for {course_name}. Please choose another course.")
                connection.close()
                continue

            print("\nAvailable sections:")
            for section in admin_sections:
                print(f"Section: {section[2]}, Days: {section[3]}, TimeSlot1: {section[4]}, TimeSlot2: {section[5]}")

            chosen_section = input("Choose a section to enroll in: ")

            if chosen_section not in [section[2] for section in admin_sections]:
                print("Invalid section. Please choose a valid section.")
                connection.close()
                continue
            
            cursor.execute('''
                SELECT Days FROM courses
                WHERE CourseName=? AND Sec=?
            ''',(course_name,chosen_section,))
            days= cursor.fetchone()
            Slot1 = cursor.execute('''
                SELECT TimeSlot1 FROM courses
                WHERE CourseName=? AND Sec=? 
            ''',(course_name,chosen_section,)).fetchone()

            Slot2 = cursor.execute('''
                SELECT TimeSlot2 FROM courses
                WHERE CourseName=? AND Sec=? 
            ''',(course_name,chosen_section,)).fetchone()
            timeslot = input(f"Enter the timeslot {Slot1} , {Slot2} you want to enroll for (1 or 2): ")
            time = Slot1 if timeslot == "1" else Slot2

            clashValue = self.checkClash(course_name, chosen_section, days, time,user_timetable)
            if not clashValue:
                user_timetable.append((course_name, chosen_section, days, time))
                print(f"Enrollment successful for {user_name} in {course_name}, Section {chosen_section} on {days}, {timeslot}.")

            connection.close()

        self.export_user_timetable(user_name, user_timetable)

    def export_user_timetable(self, user_name, user_timetable):
        csv_file_name = f"{user_name}_timetable.csv"
        with open(csv_file_name, 'w', newline='') as csvfile:
            fieldnames = ['CourseName', 'Section', 'Day', 'TimeSlot']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for course in user_timetable:
                writer.writerow({
                    'CourseName': course[0],
                    'Section': course[1],
                    'Day': course[2][0],
                    'TimeSlot': course[3][0]
                })

        print(f"User timetable exported to {csv_file_name}.")
    def main():
        user_timeTable = TimeTable("courses.db")
        user_timeTable.user_enroll()

