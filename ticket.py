class Ticket:
    tikcount = 0

    def __init__(self, name, numlist):
        self.name = name
        self.num1 = numlist[0]
        self.num2 = numlist[1]
        self.num3 = numlist[2]
        self.num4 = numlist[3]
        self.num5 = numlist[4]
        self.num6 = numlist[5]
        Ticket.tikcount += 1
