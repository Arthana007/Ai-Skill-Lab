def main():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")
        return

    is_prime = number >= 2
    divisor = 2

    while is_prime and divisor <= number // divisor:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")


if __name__ == "__main__":
    main()
