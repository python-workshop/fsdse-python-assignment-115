
def build(numbers):
    newlist = []
    if not numbers:
        return False
    for number in numbers:
       if number not in newlist:
           newlist.append(number)
    print(newlist)
