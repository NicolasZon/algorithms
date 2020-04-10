import math

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minValue = [math.inf]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.minValue[-1] >= x:
            self.minValue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.stack.pop()
        if self.minValue[-1] == x:
            self.minValue.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minValue[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()

print(minStack.push(-2))

print(minStack.push(0))

print(minStack.push(-3))

#   --> Returns -3.
print(minStack.getMin())

print(minStack.pop())

#      --> Returns 0.
print(minStack.top())

#   --> Returns -2.
print(minStack.getMin())