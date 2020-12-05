with open('Day 01 Report Repair.in.txt') as f:
    numbers = list(map(lambda l: int(l.strip()), f.readlines()))

    for i in range(len(numbers) - 2):
        for j in range(i + 1, len(numbers) - 1):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(numbers[i], '*', numbers[j], '*', numbers[k], '=', numbers[i] * numbers[j] * numbers[k])
