def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True


try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input.")
else:
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")
