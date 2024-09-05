def main():
    try:
        studentList = open("students.txt", 'r')
        students = studentList.readlines()
        studentList.close()
        #print(students)
        for s in students:
            #print(s)
            parts = s.split(',')
    
    except FileNotFoundError:
        print("File not found")

main()