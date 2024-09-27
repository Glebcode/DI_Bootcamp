# Exercise 1
# def myFunc():
#     '''buils in showing function.'''
#     print(abs(-10), int('10'))
#     user_input = input('Your thoughts ?  ')
#     print(user_input)
# myFunc()
# print(myFunc.__doc__)

# Exercise 2
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
def __str__(self):
    return f"{self.amount} {self.currency}"
    print(f"{self.amount} {self.currency}")

def __int__(self):
    return self.amount

def __repr__(self):
    return self.__str__()




c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str([c1.amount, c1.currency]))
print(int(c1.amount))
print(repr([c1.amount, c1.currency]))
print(c1.amount + 5)
c1.amount + c2.amount
c1.amount += 5
print(repr([c1.amount, c1.currency]))
print(c1.amount)
c1.amount += c2.amount
print(repr([c1.amount, c1.currency]))
c1.amount + c3.amount

