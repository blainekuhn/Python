
"""This program is a calendar.  You can add to it and update it."""
from time import sleep, strftime

NAME = "Blaine"
calendar = {}
def welcome():
  "Welcome %s" % NAME
  print "Opening..."
  sleep(1)
  print strftime("%A %m/%d/%Y")
  print strftime("%I:%M:%S")
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter A to Add, U to \
    Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":  #View the calendar
      if len(calendar.keys()) < 1:
        print "The calendar is empty."
      else:
        print calendar
    elif user_choice == "U": #Update the calendar
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
    elif user_choice == "A": #Add to the calendar
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or \
       int(date[6:]) < int(strftime("%Y"))):
        print "An invalid date was entered."
        try_again = raw_input("Would you like to try again?  Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "The event was added."
    elif user_choice == "D": #Delete calendar entry
      if len(calendar.keys()) < 1:
        print "The calendar is empty."
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "The entry was deleted."
            print calendar
          else:
            print "Invalid event."
    elif user_choice == "X":
      start = False
    else:
      print "An invalid command was entered."
      break
start_calendar()
