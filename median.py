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
height.sort()

if n % 2 == 0:
    median1 = float(height[n//2])
    median2 = float(height[n//2-1])
    median = (median1+median2)/2

else : 
    median = height[n//2]

print("median is",median)


