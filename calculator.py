
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calc_op = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calulator():
    num1 = float(input("Enter the first number: "))
    for i in calc_op:
        print(i)
    should_continue = True
    while should_continue:
        operation = input("Pick the operation which you want to do: ")
        num2 = float(input("Enter the next number: "))
        cal_func = calc_op[operation]
        answer = cal_func(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        if input("Press 'y' to continue or type 'n' to exit. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calulator()

calulator()


