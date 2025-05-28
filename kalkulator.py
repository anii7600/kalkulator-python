def kalkulator():
    print("Kalkulator")
    a = float(input("Liczba 1: "))
    b = float(input("Liczba 2: "))
    op = input("+ - * /: ")
    if op == '+': print(a + b)
    elif op == '-': print(a - b)
    elif op == '*': print(a * b)
    elif op == '/': print(a / b)
    else: print("Błędna operacja")

kalkulator()
