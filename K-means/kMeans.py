import math


def distance(a, b):
	d = math.sqrt(((a[0]-b[0]) ** 2) + ((a[1]-b[1]) ** 2))
	return d

def partitioned(d):
	n = len(d)
	d_10 = []
	for i in range(n):
		d_10.append([0, 0])
	for i in range(n):
		if(d[i][0] <= d[i][1]):
			d_10[i][0] = 1
			d_10[i][1] = 0
		else:
			d_10[i][0] = 0
			d_10[i][1] = 1
	return d_10


def calculate_centroid(c, lst):
	n = len(c)
	summ = [0, 0]
	for i in c:
		summ[0] += lst[i][0]
		summ[1] += lst[i][1]
	avg = [summ[0] / n, summ[1] / n]
	return avg

f = open("input_data2.txt", "r")

lst = []
for ele in f.readlines():
    lst.append(ele.split())

#print(lst)

n = len(lst)

k = int(input("Enter the value of k : "))
#print(k)

for i in range(n):
	for j in range(k):
		lst[i][j] = float(lst[i][j])	

c = []
c_obj = []
c_prev = []
for i in range(k):
	c.append(lst[i])
	c_obj.append([])
	c_prev.append(lst[i])

#print(c)
print("Initial Clusters : ")
for i in range(k):
	print(c[i][0], c[i][1])

d = []
for i in range(n):
	d.append([0, 0])
#print(d)


while(1):
	for i in range(n):
		for j in range(k):
			d[i][j] = distance(lst[i], c[j])

	print("Distance Matrix : ",d)

	d_10 = partitioned(d)
	#print(d_10)

	for i in range(n):
		for j in range(k):
			if(d_10[i][j] == 1):
				c_obj[j].append(i)
	#print(c_obj)
	
	for i in range(k):
		c[i] = calculate_centroid(c_obj[i], lst[:])
	print("Clusters : ",c)
	
	print(lst)
	flag = True
	for i in range(k):
		if((c_prev[i][0] != c[i][0]) or (c_prev[i][1] != c[i][1])):
			flag = False
			break
	if(flag):
		break
	else:
		for i in range(k):
			c_prev[i][0] = c[i][0]
			c_prev[i][1] = c[i][1]

print(c)














