from classExcelCourse import ExcelTable
from classSections import courseSections
from classTimeTable import TimeTable




while True:
    usr_input = input("create TimeTable(1)|| addInExcel(2) || addSectionInDB(3) || exit(4):: ")
    if(usr_input=="1"):
        print("Happy journey create your TimeTable:)")
        TimeTable.main()
    if(usr_input=="2"):
        print("Enter New Course in your ExcelFile with examDate clash check :)")
        ExcelTable.main()
    if(usr_input=="3"):
        print("Add course sections days in your DB :)")
        courseSections.main()
    if(usr_input=="4"):
        print("Bye!")
        break
    else:
        print("----")
        print("1=>TimeTable 2=> Excel 3=>Database 4=>Exit")
        print("----")