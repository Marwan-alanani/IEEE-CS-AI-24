count = input("Enter numbers seperated by spaces: ").split()

for i in range(len(count)):
    if not count[i].isdigit():
        print("all values entered must be digits.")
        count[i] = input(f"replace {count[i]} with a digit: ")

count = [int(i) for i in count]


class Solution(object):
    def sampleStats(self, count):
        mode = count.index(max(count))
        maximum = 0
        for i in range(len(count) - 1, -1, -1):
            if count[i] != 0:
                maximum = i
                break
        minimum = 0
        for i in range(len(count)):
            if count[i] != 0:
                minimum = i
                break
        total = 0
        for i in range(len(count)):
            total += i * count[i]
        mean = float(total) / sum(count)
        mid = float(sum(count)) / 2
        total = 0
        median = 0
        for i in range(len(count)):
            total += count[i]
            if total >= mid:
                if sum(count) % 2:
                    median = i
                else:
                    if total == mid:
                        num = 0
                        # get next number
                        for j in range(i + 1, len(count)):
                            if count[j]:
                                num = j
                                break
                        median = (float(i + num)) / 2

                    else:
                        median = i
                # break after total is greater than or eqal the midpoint of the data
                break
        return [minimum, maximum, mean, median, mode]


print(Solution().sampleStats(count))
