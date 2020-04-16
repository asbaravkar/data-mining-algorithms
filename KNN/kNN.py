import math

def distance(gender, height, maximum, minimum, gd, ht):
	#print(lst1)
	#print(lst2)
	#print(maximum)
	#print(minimum)
	delta = 1
	if(gd == gender):
		d1 = 0
	else:
		d1 = 1

	d2 = abs(ht - height) / (maximum - minimum)

	return ((delta * d1) + (delta * d2)) / 2
	

f = open("input_data1.txt", "r")

lst = []
for ele in f.readlines():
    lst.append(ele.split())

#lst.pop()
#print(lst)

dct = {"Gender": [], "Height": [], "Class": []}
for ele in lst:
	dct["Gender"].append(ele[1])
	dct["Height"].append(float(ele[2]))
	dct["Class"].append(ele[3])
#print(dct)

n = len(lst)
#print(n)
k = int(math.sqrt(n))
if(k % 3 == 0):
	k += 1
#print(k)

print("Enter Unkown Sample : ")
gd = input("Gender : ")
ht = float(input("Height : "))

#print(gd, ht)

maximum = max(dct["Height"])
minimum = min(dct["Height"])

#print(maximum, minimum)

dis = []

for i in range(n):
	dis.append(distance(dct["Gender"][i], dct["Height"][i], maximum, minimum, gd, ht))

#print(dis)


lst1 = []
for i in range(k):
	lst1.append([dct["Gender"][i], dct["Height"][i], dct["Class"][i], dis[i]])
#print(lst1)

for i in range(k, n):
	for j in range(0, k):
		if(dis[i] < lst1[j][3]):
			lst1[j] = [dct["Gender"][i], dct["Height"][i], dct["Class"][i], dis[i]]
			#print(lst1)
			break

#print(lst1)

print("Nearest Samples : ")
for ele in lst1:
	print(ele[0], ele[1], ele[2], ele[3])

count = [0, 0, 0]
for ele in lst1:
	if(ele[2] == "Short"):
		count[0] += 1
	elif(ele[2] == "Medium"):
		count[1] += 1
	else:
		count[2] += 1

index = count.index(max(count))
if(index == 0):
	clas = "Short"
elif(index == 1):
	clas = "Medium"
else:
	clas = "Tall"
#print(index)

print("Unkown Sample is placed in class : ",clas)





































