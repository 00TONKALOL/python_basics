file = open('text.txt','a')
file.write("Hello World\n")

file.close()

try:
    file = open('text.txt','r')
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("File not found")

# read and create csv files in python
data = [9,10]
x=data[0]
y=data[1]
x , y = data
print(x)
print(y)

#classes,inheritance
def population():
    return "Nairobi , 4000000"
name, pp = population()

print(name)
print(pp)












