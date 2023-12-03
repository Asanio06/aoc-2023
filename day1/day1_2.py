import re

d = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}


with open('input.txt') as file:
    numbers = []
    lines = file.readlines()
    for line in lines:
        numbersByIndex = {}
        
        for txt in d:
            for m in re.finditer(txt, line):  
                if m.start() != -1:
                    numbersByIndex[m.start()] = d[txt]
        
        for number in d.values():
            for m in re.finditer(str(number), line):   
                if m.start() != -1:
                    numbersByIndex[m.start()] = number
        
        items = list(map(lambda x: x[1] ,sorted(numbersByIndex.items())))
        numbers.append(int(str(items[0])+str(items[-1])))
        
    print(sum(numbers))
        
