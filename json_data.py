import json

message = '{"phone":"0723456789" , "ujumbe" : "Hello json" , "expire":5}'
json_message = json.loads(message)


print(json_message ["phone"])
print(json_message ["ujumbe"])

person = {"name" : "Jackson", "age" : 22 ,"email":"wangloo@gmail.com"}
result = json.dumps(person)
print(result)


file = open("example_2.json", "r")
data =file.read()
json_data = json.loads(data)
print(data)

q1 = json_data["quiz"]["sport"]["q1"]["question"]["answer"]
ans = json_data["quiz"]["sport"]["q1"]["answer"]
print(q1)