import random
from collections import Counter
#Def to capture First and Last Name and return as Full Name.
def build_name():
    while True:
        fname = raw_input("First Name: ")
        if not fname:
            print("First Name must contain a value")
        else:
            break

    while True:
        lname = raw_input("Last Name: ")
        if not lname:
            print("Last Name must contain a value")
        else:
            break
    return fname + " " + lname

#Def to capture each number and return as a list
def build_numbers():
    tmppwrnums = list(check_number())
    tmppwrnums.append(check_powerball())
    return tmppwrnums

def check_number():
    place_list = ['2nd', '3rd', '4th', '5th']
    tmpnums = list()
    for c in range (5):
        while True:
            try:
                if c == 0:
                    n = int(raw_input("Enter your 1st number (1 thru 69): "))
                else:
                    n = int(raw_input("Enter your " + str(place_list[c-1]) + " number (1 thru 69 excluding " + str(tmpnums).strip('[]') + " ): "))
            except ValueError:
                print("Must be a number")
            else:
                if n in tmpnums:
                    print("The number " + str(n) + " was already entered.")
                elif n <= 0 or n > 69:
                    print("Number must be 1 thru 69")
                else:
                    if n == 42:
                        print("Don't Panic.")
                    break
        tmpnums.append(n)
        c = c + 1
    return tmpnums

def check_powerball():
    while True:
        try:
            n = int(raw_input("Select Powerball number (1 thru 26): "))
        except ValueError:
            print("Must be a number")
        else:
            if n <=0 or n > 26:
                print("Number must be 1 thru 26")
            else:
                break
    return n
#Def to display each entry any determine winner.
def generate_winner(ticketlist):
    lstnum1 = list()
    lstnum2 = list()
    lstnum3 = list()
    lstnum4 = list()
    lstnum5 = list()
    lstnum6 = list()

    for t in ticketlist:
        print(str(t.name) + " " + str(t.num1) + " " + str(t.num2) + " " + str(t.num3) + " " + str(t.num4) + " " + str(t.num5) + " Powerball: " + str(t.num6))
        lstnum1.append(t.num1)
        lstnum2.append(t.num2)
        lstnum3.append(t.num3)
        lstnum4.append(t.num4)
        lstnum5.append(t.num5)
        lstnum6.append(t.num6)

    winnum1 = find_winner(lstnum1)
    winnum2 = find_winner(lstnum2)
    winnum3 = find_winner(lstnum3)
    winnum4 = find_winner(lstnum4)
    winnum5 = find_winner(lstnum5)
    winnum6 = find_winner(lstnum6, True)

    print("\nPowerball Winning Number:\n" + str(winnum1) + " " + str(winnum2) + " " + str(winnum3) + " " + str(winnum4) + " " + str(winnum5) + " Powerball: " + str(winnum6))

#Def to determine each winning number.  If PB is TRUE means it is the Powerball.
def find_winner(numlst, pb=False):
    num_count = Counter(numlst)
    top_two = num_count.most_common(2)
    if len(top_two)>1 and top_two[0][1] == top_two[1][1]:
        # There is no number that is the most common, or there is a tie so generate a random number.
        if pb == False:
            return random.randint(1,69)
        else:
            return random.randint(1,26)
    return top_two[0][0]
