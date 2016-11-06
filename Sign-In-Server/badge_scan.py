import MySQLdb
import csv
import sys
#Imports the MySQLdb, csv, and sys libraries

db = MySQLdb.connect("localhost", "root", "raspberry", "member_attendance")
curs = db.cursor()
#Establishes the connection to the database, as well as creates the cursor object to execute MySQL Commands
while True:
    student_id = raw_input("Please Scan Your Student ID Card or enter your ID number ")
    #Student inputs the ID or scans it using a barcode scanner
    choice1 = int(raw_input("Are you 1: Signing In, 2: Signing Out, 3: Registering your ID, or 4: Admin Tools "))
    if choice1 == 1:
        signtime = "update attendance set signin = null where id = %s"
        #Timestamp for signing in
        try:
            curs.execute(signtime, (student_id))
            db.commit()
            print "You have Signed in"
        except:
            db.rollback()
            print "Error in signing in"
    if choice1 == 2:
        signtimeout = "update attendance set signout = null where id = %s"
        #Timestamp for signing out
        try:
            curs.execute(signtimeout, (student_id))
            db.commit()
            print "You have Signed Out"
        except:
            db.rollback()
            print "Error in signing out"
        minutes_calc = "UPDATE attendance SET minutes = TIMESTAMPDIFF(MINUTE, signin, signout) where id = %s"
        #Command for subtracting signout time from signin time, thus determining total time spent at a meeting in minutes
        try:
            curs.execute(minutes_calc, (student_id))
            db.commit()
        except:
            db.rollback()
            print "Error in logging total time spent at today's meeting"
    if choice1 == 3:
        student_name = raw_input("Please enter your name Case Sensitive (Ex: John D) ")
        create_profile = "INSERT INTO attendance (name, id) VALUES (%s, %s)"
        #Command for registering into te database by creating a new row in the table with the student's ID and Name
        try:
            curs.execute(create_profile, (student_name,student_id))
            db.commit()
            print "You have registered into the database, you have also automatically signed in"
        except:
            db.rollback()
            print "Error in registering"
    if choice1 == 4:
        password = 540
        print("")
        password_input = int(raw_input("Hello Admin, please input the PIN for access to the Admin Tools "))
        if password_input == 540:
            print("")
            choice2 = int(raw_input("Hello Admin, would you like to 1: Export today's data, or 2: Clear Sign-In and Sign-Out Times "))
            if choice2 == 1:
                print("")
                print("Exporting Table")
                
                curs.execute("SELECT * FROM attendance")
                rows = curs.fetchall()
                filename = open('/home/pi/Desktop/table.csv', 'w')
                myFile = csv.writer(filename)
                myFile.writerows(rows)
                filename.close()
                #Exports the table to a csv file on the desktop, where it can be transfered to a Windows Machine for viewing in Excel
                print("Table exported to Desktop")
            if choice2 == 2:
                print("")
                print("Clearing Today's Sign-In Times")

                clear_signin = "UPDATE attendance SET signin = ''"
                clear_signout = "UPDATE attendance SET signout = ''"
                clear_minutes = "UPDATE attendance SET minutes = ''"
                #Clears the columns for Sign-In, Sign-Out, and Minutes for the next day
                try:
                    curs.execute(clear_signin)
                    curs.execute(clear_signout)
                    curs.execute(clear_minutes)
                    db.commit()
                except:
                    db.rollback()
                    print "Error in clearing data"
        else:
            print("PIN incorrect, exiting program")
            sys.exit()
