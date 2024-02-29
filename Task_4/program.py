import functions
numbers = functions.get_numbers()
minimum = functions.find_min(numbers)
maximum = functions.find_max(numbers)
mean = functions.find_mean(numbers)
modes = functions.find_mode(numbers)
median = functions.find_median(numbers)
range_ = functions.find_range(numbers)
variance = functions.find_variance(numbers)
STD = functions.find_STD(numbers)
Q1,Q2,Q3 = functions.find_Quartiles(numbers)
IQR = functions.find_IQR(numbers)

print(f"Min: {minimum}")

print(f"Max: {maximum}")

print(f"Mean: {mean}")
if modes:
    print("Mode(s): ",end="")
    for i in range(len(modes)-1):
        print(modes[i],end=",")
    print(modes[-1])
else:
    print("There is no mode")

print(f"Median: {median}")

print(f"Range: {range_}")

print(f"Variance: {variance}")

print(f"Standard Deviation: {STD}")

print(f"({Q1}, {Q2}, {Q3})")

print(f"Interquartile Range (IQR): {IQR}")
