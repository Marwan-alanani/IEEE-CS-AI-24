def main():    
    year = input("Enter year: ")
    while(not (year.isdigit() and year > 0)):
        year = input("Enter a valid year")
    print(is_leap(int(year)))


def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


main()
