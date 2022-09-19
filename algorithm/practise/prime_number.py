def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    number = 13
    print(f"{number}: {prime_number(number)}")