# Importing a .csv document

# with open('personalinfo.csv', encoding='utf-8') as csvfile:
#     for data in csvfile:
#         data = data.strip()
#         print(data)

# Line 4
# Imports the file then encodes it. Save .xls a .csv utf-8 (.txt files should not require this)

# Line 6
# .strip() will strip whitespace from document


# read, write, create

# "r" - Read - will read the contents of a file.
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will append to the end of a file
# "w" - Write - will overwrite a file (erase and write over)

# open('DataFile.txt', "r")  reads a file
# open('DataFile.txt', "x")  creates a file
# open('DataFile.txt', "a")  appends the file
# open('DataFile.txt', "w")  writes over the file

# Here is a fun example:

# import.os

# file_name = input("WHAT WOULD YOU LIKE TO CALL YOUR FILE?\nFILENAME >>> ")
# open(f"{file_name}.txt", "x")
# print(f"File Created! Your file '{file_name}' is stored at", os.getcwd())

# Line 31
# Creating a variable for file name, storing it for later

# Line 32
# Uses the data stored within the variable as the file name and using "x" we create file.

# line 33
# prints out response, 'os.getcwd()' is retrieve directory of new file


# ACTIVITY:

# Research ways to and create a DMS (Doc Management System) using this technique.

# - must be able to list files in the Python dir
# - select files and write/delete in python dir
# - etc

# could this be replaced with 'match' statement??

import os
import time


def menu():
    time.sleep(1)
    print("\n______ WELCOME TO THE FMS (FILE MANAGEMENT SYSTEM) ______\n")
    time.sleep(1)
    while True:
        match input("WHAT WOULD YOU LIKE TO DO?\n\n[1] CREATE A FILE\n[2] EDIT A FILE\n[3] DELETE A FILE\n[4] CHANGELOG\n\n>>> "):
            case "1":
                time.sleep(1)
                os.system('cls')
                file_create()
            case "2":
                time.sleep(1)
                os.system('cls')
                file_edit_selection()
            case "4":
                time.sleep(1)
                os.system('cls')
                changelog()
            case _:
                print("\nInvalid option\n")


def changelog():
    with open('data/changelog.txt', 'r') as file: # file defines the file as a variable so you can refer to it later
        for lines in file: # declaring a variable for the content then referring to the file.
            print(lines.strip()) # stripping white space within file (compressing lines)
    match input("\n----- PRESS ENTER TO RETURN TO MENU -----"):
        case _:
            time.sleep(0.5)
            os.system('cls')
            menu()


def file_create():
    global export_path
    while True:
        match input("\nPLEASE SPECIFY THE FILETYPE\n\n[1] TXT\n[2] DOCX\n[3] CSV\n\nFILETYPE >>> "):
            case "1":
                file_type = "txt"
                break
            case "2":
                file_type = "docx"
                break
            case "3":
                file_type = "csv"
                break
            case _:
                print("\nINVALID OPTION\n")

    print(f"\nYOU HAVE SELECTED {file_type.upper()}")
    file_name = input("\nWHAT WOULD YOU LIKE TO CALL IT?\nFILENAME >>> ")
    try:
        open(f"export/{file_name}.{file_type}", "x")
        print(f"\nFILE CREATED! YOUR FILE '{file_name.upper()}' IS STORED AT", export_path.upper()) #   this is a way to print directory of file (joining both main dir and folder
    except FileExistsError:
        print("\nUNABLE TO CREATE FILE. A FILE WITH THAT NAME ALREADY EXISTS!")
    time.sleep(1)

    while True:
        match input("\nWOULD YOU LIKE TO CREATE ANOTHER OR RETURN TO MAIN MENU?\n\n[1] CREATE\n[2] MAIN MENU\n\n>>> "):
            case "1":
                time.sleep(1)
                file_create()
            case "2":
                time.sleep(1)
                os.system('cls')
                menu()
            case _:
                print("\nInvalid option\n")


def file_edit_selection():
    while True:
        file_list = os.listdir(path='./export')  # '.' means current dir and rest folder path
        match input("\nWHAT WOULD YOU LIKE TO DO?\n\n[1] VIEW A FILE\n[2] EDIT A FILE\n[3] MENU\n\n>>> "):
            case "1":
                print("\nTHE FOLLOWING FILES ARE AVAILABLE FOR VIEWING:\n")
                print(file_list)
                view_file = input("\nPLEASE SPECIFY THE FILE\n>>> ")
                try:
                    with open(f"export/{view_file}", "r") as file:
                        for lines in file:
                            lines.strip()
                            os.system('cls')
                            print(lines)
                            time.sleep(3)
                except FileNotFoundError:
                    print(f"\nTHE FILE '{view_file.upper()}' DOESN'T EXIST")
                except PermissionError:
                    print(f"\nUNABLE TO DETERMINE INPUT: INCORRECT ENTRY FORMAT.\nTRY: FILENAME.FILETYPE")
            case "2":
                print("\nTHE FOLLOWING FILES ARE AVAILABLE FOR EDITING:\n")
                print(file_list)
                edit_file = input("\nPLEASE SPECIFY THE FILE\n>>> ")
                try:
                    with (open(f"export/{edit_file}", "a") as file):
                        print("TYPE YOUR TEXT:\n")
                        file.write(input("> "))
                except FileNotFoundError:       # when a file doesn't exist
                    print(f"\nTHE FILE '{edit_file.upper()}' DOESN'T EXIST")
                except PermissionError:     # when a file isn't defined "pressing enter instead of entering file name"
                    print(f"\nUNABLE TO DETERMINE INPUT: INCORRECT ENTRY FORMAT.\nTRY: FILENAME.FILETYPE")
            case "3":
                time.sleep(0.5)
                menu()
            case _:
                print("\nINVALID OPTION")


export_path = os.path.join(os.getcwd(), "export")
menu()
