import csv
file = open("raw_data.csv","r")
with open ('raw_data.csv', newline = '') as csvfile:
    datas = csv.DictReader(csvfile)
    for data in datas:
        print(data)
# data = file.readline()

#remove tags
tags = []
for i in range(len(data)):
    if data[i:i+2] == "at":
        # print(data[i:i+2])
        begin = i
    if data[i:i+11] == "destination":
        # print(data[i:i+11])
        end = i+11
        # print(data[begin:end+1])
        tags.append(data[begin:end+1])
for tag in tags:
    data = data.replace(tag, ", ")

for i in range(len(data)):
    if data[i:i+6] == "source":
        # print(data[i:i+6])
        begin = i
        data2 = data[i+6:]
        # print(data[begin:end])
        tags.append(data[begin:end])
for tag in tags:
    data = data.replace(tag, "")

data = data[1:]
print(data)

file = open("test.txt","a")
for i in range(len(data)):
    file.write(data[i])