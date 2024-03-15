import psycopg2


#create a connection to the database
#port number and other arguments are default and don't need to be specified
connection = psycopg2.connect(dbname="A3", #database name
                        host = "localhost", #host (in this case the computer running the code)
                        user="postgres", #username
                        password="password"#password
                              ) 
#auto-commit changes to the database
#without this, changes are reset when this code exits
connection.autocommit = True

#create the psycopg cursor which runs the queries
cursor = connection.cursor()


#this function displays all the students
def getAllStudents():
     #select everything in the students table
     cursor.execute("SELECT * FROM students")
     toPrint = cursor.fetchall() #get the result of the above query
     for s in toPrint: #print results line by line
          print(s)

#This function adds a new student to the database
def addStudent(first_name, last_name, email, enrollment_date):
     #insert a new student into the students table with the given properties
     cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date)" + 
                    "VALUES('"+first_name+"', '"+last_name+"', '"+email+"', '"+enrollment_date+"')")

#This function updates a certain student's email based on a given ID
def updateStudentEmail(student_id, new_email):
     #update the email by setting the value in the email column to the new email, but only if the student ID matches
     cursor.execute("UPDATE students SET email = '" + new_email + "' WHERE student_id = " + str(student_id) + "; ")

#This function deletes a certain student from the database based on a given ID
def deleteStudent(student_id):
     #delete student with matching student ID
     cursor.execute("DELETE FROM students WHERE student_id = " + str(student_id) + ";")

############################################
## EVERYTHING PAST HERE IS JUST INTERFACE ##
############################################

#print out the chocies the user can make
print("""
     Pick an option:\n
     1: Get all students\n
     2: Add Student\n
     3: Update student email\n
     4: Delete student
""")

#repeat forever
while True:
     #get user choice as an integer
     choice = int(input("\n--> "))

     #collect input / execute one of the 4 fucntions
     
     if choice == 1:
          getAllStudents()

     if choice == 2:
          fname = input("Enter first name--> ")
          lname = input("Enter last name--> ")
          email = input("Enter email--> ")
          edate = input("Enter enrollment date--> ")
          addStudent(fname, lname, email, edate)

     if choice == 3:
          sid = input("Enter student ID--> ")
          newmail = input("Enter new email address--> ")
          updateStudentEmail(sid, newmail)

     if choice == 4:
          sid = input("Enter student ID--> ")
          deleteStudent(sid)

     print() #\n


          
