# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# Q2
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

# Q4
list1 = list(filter(lambda x: x>0, [1,-2,3,-5,8,-3]))
print(list1)

# Q5
number = int(0xea)
print(number)

# Q6
list2 = list(map(lambda x:x*3,[1,2,3,4]))
print(list2)

# Q7
list3 = [-8, 2, 7, 5, -3, 5, 0, 1]
max_value = max([-8, 2, 7, 5, -3, 5, 0, 1])
min_value = min([-8, 2, 7, 5, -3, 5, 0, 1])
print(max_value,min_value)

# Q8
a = round(17 / 3, 4)
print(a)

print("print(\"Hello\\nWorld\")")