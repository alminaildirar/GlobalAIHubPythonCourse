#!/usr/bin/env python3
#COURSE GRADE APPLICATION

def CalculatePassingGrade(midterm_grade,project_grade,final_grade):
    passing_grade = midterm_grade*(0.3) + project_grade*(0.3) + final_grade*(0.4)
    return passing_grade

    
StudentDict =[{"Name":"","Surname":"",
                    "Student Number":"","Midterm Grade":"",
                    "Project Grade":"","Final Grade":"","Passing Grade":""},
              {"Name":"","Surname":"",
                    "Student Number":"","Midterm Grade":"",
                    "Project Grade":"","Final Grade":"","Passing Grade":""},
              {"Name":"","Surname":"",
                    "Student Number":"","Midterm Grade":"",
                    "Project Grade":"","Final Grade":"","Passing Grade":""},
              {"Name":"","Surname":"",
                    "Student Number":"","Midterm Grade":"",
                    "Project Grade":"","Final Grade":"","Passing Grade":""},
              {"Name":"","Surname":"",
                    "Student Number":"","Midterm Grade":"",
                    "Project Grade":"","Final Grade":"","Passing Grade":""}]


for i in range(len(StudentDict)):
    print("-----------------------------------------------")
    print("Please enter the information of the " + str(i+1) + ". student. ")
    StudentDict[i]["Name"]=str(input("Name: "))
    StudentDict[i]["Surname"]=str(input("Surname: "))
    StudentDict[i]["Student Number"]=str(input("Student Number: ")) 
    
    
    case = True
    while case:
        try:
            
            StudentDict[i]["Midterm Grade"]=int(input("Midterm Grade: ")) 
            if 0 <= StudentDict[i]["Midterm Grade"] <=100:
                case=False
            else:
                print("Please enter a number between 0 and 100.")
                
        except ValueError:
            print("Please enter a number!")
            
            
   
    case = True           
    while case:
        try:
            StudentDict[i]["Project Grade"]=int(input("Project Grade: ")) 
            if 0 <= StudentDict[i]["Project Grade"] <=100:
                case=False
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a number!")
            
            
    
    case = True
    while case:
        try:
            StudentDict[i]["Final Grade"]=int(input("Final Grade: ")) 
            if 0 <= StudentDict[i]["Final Grade"] <=100:
                case=False
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a number!")
            
                
    StudentDict[i]["Passing Grade"] = CalculatePassingGrade(StudentDict[i]["Midterm Grade"],StudentDict[i]["Project Grade"],StudentDict[i]["Final Grade"])
       

PassingGrades= []
for i in range(len(StudentDict)):
   PassingGrades.append(StudentDict[i]["Passing Grade"])
   
PassingGrades.sort()
PassingGrades.reverse()

print("-----------------------------------------------")
print("Highest passing grade: " + str(PassingGrades[0]))
print("Lowest passing grade: " + str(PassingGrades[(len(PassingGrades)-1)]))
    
    

     