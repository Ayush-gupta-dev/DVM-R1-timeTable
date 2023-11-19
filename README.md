# DVM-R1-timeTable

# How to Run?
* run main.py from terminal
* Do install sqlite viewer and office viewer extension to see changes in Vs code only.

## Requirements fulfilled::
1. TimeTable in excel with admin privilige password
2. CSV exported from instance of Sections and checks for TimeClash for users
3. Sections created in Database by admin (SQLite)
4. Class, Methods used
5. getFn => to get course info like credit examdate course code
6. Another getFn => to get All section of a given course , input M1 , from database all L1,L2,T1,T2 of M1 fetched.
7. populate_course=>in excel populate_section=>in Sql


![Screenshot from 2023-11-19 21-25-07](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/16c3977a-5edd-4309-a047-b83b7c49e376)
![Screenshot from 2023-11-19 21-26-15](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/7bb73335-a561-4832-b40f-72f7c77e158b)
![Screenshot from 2023-11-19 21-26-27](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/37858592-4aa2-4e4b-8723-f9aeb1fbbbcc)

![Screenshot from 2023-11-19 21-22-56](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/510baf61-95d9-492e-b4f5-694db401cd1e)
![Screenshot from 2023-11-19 21-23-27](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/fadafe5d-af44-4bec-ac4d-082db248f12c)
![Screenshot from 2023-11-19 21-24-12](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/eefdc4ce-25e8-413f-b6c3-0e8c4756bff4)
![Screenshot from 2023-11-19 21-24-24](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/d8ad703c-33f8-4a61-beeb-51dd97134fc1)
![Screenshot from 2023-11-19 21-24-58](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/e54f6087-2979-4213-bfff-dad0aba4680a)

![Screenshot from 2023-11-19 21-26-32](https://github.com/Ayush-gupta-dev/DVM-R1-timeTable/assets/137040550/ac887d10-d57d-40d1-a115-70d8d93bfe21)

## Edge Cases (in future)
1. Password authentication is not strong
2. Time clash work on exact time if (M,T,W 1-2) (T,F 1-2) => clash BUT (M,T,W 1-2) (T,F 12-2) => No clash
