import ticket
import utils

#Powerball Generator
bolcont = True
ticketlist = list()

print("\nWelcome to the Powerball drawing.\nYou can enter a Powerball ticket for as many employees as you would like.\nWhen done the winning number will be drawn.\n")

#While loop to enter as many tickets as needed.
while bolcont != False:

        print("Please enter your name")

        #Build the employees name.
        fullname = utils.build_name()
        #Capture the Powerball numbers
        pwrnums = list(utils.build_numbers())
        #Create the ticket
        pwrtick = ticket.Ticket(fullname,pwrnums)
        #Save the ticket to list to generate winner later.
        ticketlist.append(pwrtick)

        while True:
            cont = raw_input("\nWould you like to create another Powerball ticket? (Y/N): ")
            if cont.upper() == "N":
                bolcont = False
                break
            else:
                if cont.upper() != "Y":
                    print("Please enter Y or N")
                else:
                    break
#Spacer for format because I am being picky.
print("\n")
#Display all entries and find the winner.
utils.generate_winner(ticketlist)

raw_input("\nPress ENTER to close.")
