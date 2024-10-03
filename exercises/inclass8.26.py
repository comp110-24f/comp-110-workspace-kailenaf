def sum(num1: int, num2: int) -> int:
    """The sum of two numbers"""
    return num1 + num2


print(sum(num1=1, num2=4))


x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(x)
