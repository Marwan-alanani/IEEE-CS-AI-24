def main():
    # list index matches month last day
    lastDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = int(input("Day: "))
    month =  int(input("Month: "))
    year = int(input("Year: "))

    # if leap year and in february
    if year%4 == 0 and month == 2 :
        if day == lastDays[1]:
            day+=1
        elif day == lastDays[1]+1:
            month += 1
            day = 1

    # if last day in year
    elif day == lastDays[11] and month == 12:
        year+=1
        month = 1 
        day = 1
    
    # if last day in month
    elif day == lastDays[month-1]:
        month += 1
        day = 1

    else:
        day += 1
    print(f"Day:{day}  Month:{month}  Year:{year}")

main()
    