# SOLVED

class Node:

    def __init__(self, val: int, minVal: int):
        self.value = val
        self.minValue = minVal

    def __str__(self) -> str:
        return f"{self.value}"
    
    def __repr__(self) -> str:
        return f"{self.value}"

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append(Node(val, self.min))

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.stack[-1].minValue if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.min


def execute(actions, values):
    obj = MinStack()

    for i in range(len(actions)):
        action = actions[i]
        value = values[i]

        print(action)
        if action == "MinStack":
            continue
        elif action == "push":
            obj.push(value[0])
        elif action == "getMin":
            print(obj.getMin())
        elif action == "pop":
            obj.pop()
        elif action == "top":
            print(obj.top())
        else:
            print("dead")
            exit(1)
    print()



actions = ["MinStack","push","push","push","getMin","pop","top","getMin"]
values =  [[],[-2],[0],[-3],[],[],[],[]]

execute(actions, values)


actions = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
values = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

execute(actions, values)
