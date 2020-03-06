import sys

if(len(sys.argv) != 3):
    print("wrong")

def weirdSum(a, b):
    return str(a-b)+str(a+b)

a = int(sys.argv[1])
b = int(sys.argv[2])

c = weirdSum(a, b)
print(a, "+", b, "=", c)
