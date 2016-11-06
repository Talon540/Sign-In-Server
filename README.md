# Sign-In-Server

To reduce paper-usage as well as improve speed, we have devised a simple electronic check-in, check-out system for team members to use with their ID Cards when attending Robotics meetings.

## Required Hardware

1. Raspberry Pi 2 w/ Raspbian Jessie Installed

2. USB Barcode Scanner

3. Portable Power Supply (Optional, if using it in a remote environment)

## Dependencies Used

1. mysql-server

2. python-mysql

3. csv

## How to Setup

1. Download the files directly from this repository as a ZIP file

2. Unzip it into whatever directory you wish on the Pi

3. Using terminal, install the required dependencies using "sudo apt-get install mysql-server python-mysql"

  3a. csv should be built into Raspbian by default
  
  3b. When prompted to set up a username/password by MySQL, set the username as "root" and the password as "raspberry"
  
4. Using linux terminal, enter the directory where you unzipped the files; ensure that you can see the file "member_attendance.sql"
  
  4a. Import the Database with "mysql -u root -p member_attendance < member_attendance.sql"
  
5. Test to see if the database has been imported by logging into MySQL in the terminal with "mysql -u root -p"
  
  5a. Enter the command "USE member_attendance;"
  
  5b. Once you have entered the database, run the command "SELECT * FROM attendance;" This is the table that the data from the python script will be parsed into. It should be blank by default.
  
## How to Use

1. Run "badge_scan.py" with the barcode scanner. You can also use a keyboard to enter the ID Number if needed.
  
  1a. For new entries, you will need to register into the database first. Input "3" into the console.
  
  1b. For signing in, input "1" into the console.
  
  1c. For signing out, input "2" into the console.
  
  1d. For using administrator tools (i.e: Exporting the Table to CSV Format for Excel, Clearing the table for the day), input "4" into the console.
    - You will need to input a special pin, by default it is "540". You can change it to whatever you wish.
    
    - By inputting "1", the table will be exported to the Desktop
    
    - By inputting "2", the table will be truncated of sign-in, sign-out, and total minutes. This resets it for the next meeting.
      
      - Be sure that you have downloaded the data before truncating the table!
      
    - If the inputted Admin PIN is incorrect, the system will automatically exit.
## Notes

1. Feel free to edit and modify the code in whatever way you wish, just ensure that you cite this source code
  
