"""EMPLOYEE DATABASE MANAGEMENT"""

# importing pickle module to read and store the data after completion of execution
import pickle
# creating a class
class Employee:
    # initializing the attributes of the employee
    def __init__(self, name, ID_number, department, job_title):
        self.name = name
        self.ID_number = ID_number
        self.department = department
        self.job_title = job_title
# displaying the menu for the which the user want to perform operation
def display_menu():

    print("_"*30)
    print('1. Look up an employee in the dictionary.')
    print('2. Add a new employee to the dictionary.')
    print('3. Change an existing employee name, ID number, department and job title in the dictionary.')
    print('4. Delete an employee from the dictionary.')
    print('5. Quit from the program.')
    print("_" * 30)

try:
    #opening a file in binary mode
    with open("employee_DB", "rb") as f:
        #if file is there the data in file is stored in employee_data variable
        employee_data = pickle.load(f)
except:
    #if file is not found it creates an empty dictionary for employee_data and shows warning message
    employee_data = {}
    print("Warning: File Not Found")


#looking up for employee details using id
# here employee_dict refers to employee_data
def lookup_employee(employee_dict):
    employee_id = input("Enter the employee ID number: ")
    #checks if id is present or not
    if employee_id in employee_dict:
        #retrieves the associate value with id and store in employee variable
        employee = employee_dict[employee_id]
        print("***Here are the Employee details*** ")
        print(f"Name of the Employee : {employee.name}")
        print(f"ID number of the Employee : {employee.ID_number}")
        print(f"Department in which Employee works : {employee.department}")
        print(f"Job Title of the Employee : {employee.job_title}")

# if ID is not present
    else:
        print("---Given Employee ID is not there----")
        print("_" * 30)
        #prints the employee ID which are present in DB
        print("Here are the employee_ID present in the database.")

# adding new employee into the Db
def add_new_employee(employee_dict):
    employee_id = input("Enter the employee ID number: ")
    # check ID is present or not
    if employee_id in employee_dict:
        #if ID is already present it gives the details of that employee
        print(f"Employee_id : {employee_id} already exists. here are the details")
        employee = employee_dict[employee_id]
        print(f"Name of the Employee : {employee.name}")
        print(f"ID number of the Employee : {employee.ID_number}")
        print(f"Department in which Employee works : {employee.department}")
        print(f"Job Title of the Employee : {employee.job_title}")

    # if ID is not present
    else:
        print("_" * 30)
        # user asks for input of name,jobtitle and department
        name = input("Enter Name : ")
        department = input("Enter the department : ")
        job_title = input("Enter the Job Title : ")
        #object new_employee hold the data of the new entry and stored in dictionary using ID as a key
        new_employee = Employee(name,employee_id, department, job_title)
        employee_dict[employee_id] = new_employee
        print(f"Employee Id : {employee_id} successfully saved in database")
        print("_" * 30)
#changing the details of the existing employee
def change_existing_employee_details(employee_dict):
    employee_id = input("Enter the Employee ID : ")
    #checks ID is present or not
    if employee_id in employee_dict:
        employee = employee_dict[employee_id]
        #asking user for the input
        name = input("Enter New name : ")
        department = input("Enter the new department : ")
        job_title = input("Enter the new job title : ")
        #updating the values stored in employee to the new details
        employee.name = name
        employee.department = department
        employee.job_title = job_title
        print("New Employee details updated.")
        print("_" * 30)
    #if iD not present
    else:
        print("Employee details not found")
# delecting the details of the employee from DB
def deleting_employee_details(employee_dict):
    employee_id = input("Enter the Employee ID : ")
    # checks ID present or not
    if employee_id in employee_dict:
        print("_" * 30)
        #deleting the details of the employee with that ID
        del employee_dict[employee_id]
        print("Employee details deleted successfully")
        print("_" * 30)
    # if ID not present
    else:
        print("Employee ID not found")
# condition always true until the user wants to exit from the program
while True:
    display_menu()
    choice = input("Enter the choice of (1 to 5) : ")

    if choice == '1':
        lookup_employee(employee_data)
    elif choice == '2':
        add_new_employee(employee_data)
    elif choice == '3':
        change_existing_employee_details(employee_data)
    elif choice == '4':
        deleting_employee_details(employee_data)
    elif choice == '5':  # breaks the loop
        print("Quitting the program")
        break
    else:
        print("Entered wrong choice.")
# the entered and modified data will dumped into the database by using pickle
try:
    with open("employee_DB", "wb") as f:
        pickle.dump(employee_data, f)
        print("File saved")
except:
    print("Warning : not an Executable file")




