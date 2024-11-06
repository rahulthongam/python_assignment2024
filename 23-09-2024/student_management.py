students=[]

def add_student(stu_id,name,grade):
    
    student_details = {
        'ID': stu_id,
        'Name': name,
        'Grade': grade}
    students.append(student_details)
    print(f"ID:{stu_id} Name: {name} Grade:{grade} added successfully.")
    
n=int(input("Enter the number of students: "))
for i in range(n):
    while True:
        stu_id=int(input("Enter Student ID: "))
        #check duplicate
        duplicate= False
        for student in students:
            if student['ID']==stu_id:
                print(f"This student having ID {stu_id} already exists!")
                duplicate=True
        if not duplicate:
            name=input("Enter Student Name: ")
            grade=input("Enter Student Grade: ")
            add_student(stu_id, name, grade)
            break
        
print("ID           Name          Grade")
for i in students:
    print(f"{i['ID']}           {i['Name']}           {i['Grade']}")
