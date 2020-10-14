# SOLVED

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for booking in self.bookings:
            if start < booking[1] and end > booking[0]:
                return False
        self.bookings.append((start, end))
        return True


lst = [[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
want = [True,   True,   False,   False,   True,   False,   True,   True,   False,   False,False,   False,   False,   False,False,   False,   False,   False,False,   True]

obj = MyCalendar()
for i in range(len(lst)):
    l = lst[i]
    w = want[i]
    out = obj.book(l[0], l[1])
    if out != w:
        print(i)
        print(obj.bookings)
        print((l[0], l[1]))
        print("Expected: " + str(w) + ", Actual: " + str(out))
        print()