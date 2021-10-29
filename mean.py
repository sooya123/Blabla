import csv
with open("HeightWeight.csv") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
height=[]

for i in range(len(filedata)):
    number = filedata[i][1]
    height.append(float(number))

n = len(height)
total = 0
for x in height:
    total = total+x

mean = total/n
print("mean/average is ",mean)

