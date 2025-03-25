from functools import reduce


def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(5,10))

add_two = lambda a, b : a + b

print(add_two(5,10))
scores = [{"eng":56 ,"mat":67},
    {"eng":68 ,"mat": 78},
    {"eng":45 ,"mat":66},
    {"eng":70 ,"mat": 88}]

sorted_by_maths=sorted(scores,key=lambda x: x['mat'])
print(sorted_by_maths)

def get_eng(score):
    return score["eng"]

sorted_by_eng = sorted(scores, key=get_eng)
print(sorted_by_eng)

ages = [70,80,90,64,77,56,10,44,15,78,56,23,90,48,98,75]
total_age = reduce(lambda x,y: x+y ,ages ,0)
print(total_age)

new_ages = map(lambda x : x+1,ages)
print(new_ages)

above_60 = filter(lambda age : age > 60,ages)
print(list(above_60))




