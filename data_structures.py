#data structures
#collection
#list, dictionary , set
scores= [67,76,78,59,98,34,56,46,74,87,59,86,96,54,35,78,65,90,88,89]
#access a score
print(scores[0])
print(scores[1])

# add a score
scores.append(12)
print(scores)

#remove
scores.remove(56)
print(scores)

print(len(scores))
scores.sort(reverse=True)
print(scores)

#slice a list
top_5 = scores[-5:]
print(top_5)

#dictionary

person={"name": "Zubeidah","age":19 , "weight":58 , "county":"Nairobi"}
print(person["name"])
print(person["age"])

#set
days={"mon","tue","wed","thu","fri","sat","sun" ,"mon"}
print(days)

for s in scores:
    if s<50:
        pass
    print(s) #for each scores in scores

    for d in days: # for each day in days
        print(d)