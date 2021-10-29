import csv
from collections import Counter 
with open("HeightWeight.csv") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
height=[]

for i in range(len(filedata)):
    number = filedata[i][1]
    height.append(float(number))

n = len(height)
data = Counter(height)
modedata_for_range={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for i, occurence in data.items():
    if 50 < float(i)<60:
        modedata_for_range["50-60"] += occurence
    elif 60 < float(i)<70:
        modedata_for_range["60-70"] += occurence

    elif 70 < float(i)<80:
        modedata_for_range["70-80"] += occurence
    
