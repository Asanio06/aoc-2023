with open('input.txt') as file:
    numbers = []
    lines = file.readlines()
    s = 0
    for line in lines:
        _numbers = [i for i in list(line) if i.isdigit()]
        numbers.append(int(_numbers[0]+_numbers[-1]))
    print(sum(numbers))
        
