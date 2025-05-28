def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnoz(x, y):
    return x * y

def podziel(x, y):
    if y == 0:
        return "Błąd! Dzielenie przez zero."
    return x / y

if __name__ == "__main__":
    print("Prosty Kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    while True:
        wybor = input("Wybierz (1/2/3/4): ")

        if wybor in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Podaj pierwszą liczbę: "))
                num2 = float(input("Podaj drugą liczbę: "))
            except ValueError:
                print("Nieprawidłowe dane. Proszę podać liczby.")
                continue

            if wybor == '1':
                print(f"{num1} + {num2} = {dodaj(num1, num2)}")
            elif wybor == '2':
                print(f"{num1} - {num2} = {odejmij(num1, num2)}")
            elif wybor == '3':
                print(f"{num1} * {num2} = {pomnoz(num1, num2)}")
            elif wybor == '4':
                print(f"{num1} / {num2} = {podziel(num1, num2)}")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
