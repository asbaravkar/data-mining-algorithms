import math


def distance(a, b):
	d = math.sqrt(((a[0]-b[0]) ** 2) + ((a[1]-b[1]) ** 2))
	return d


f = open("input_data2.txt", "r")

def cal_cost(m, k, d):
	cost = 0
	for i in range(n):
		if i not in m:
			d_index = 0
			min_value = 100000000000000
			for j in range(k):
				if(d[m[j]][i] < min_value):
					d_index = m[j]
					min_value = d[m[j]][i]
			cost += min_value

	return cost

lst = []
for ele in f.readlines():
    lst.append(ele.split())
#print(lst)

n = len(lst)

k = int(input("Enter the value of k : "))
#print(k)

for i in range(n):
	for j in range(2):
		lst[i][j] = float(lst[i][j])	

d = []
for i in range(n):
	d.append([])
	for j in range(n):
		d[i].append(0)
#print(d)

for i in range(n):
	for j in range(i, n):
		d[i][j] = distance(lst[i], lst[j])
		d[j][i] = d[i][j]
#print(d)

#Initial Medoids
m = []
c = []
for i in range(k):
	m.append(i)
	c.append([i])
#print(m)
#print(c)

c_cost = 0
for i in range(k, n):
	d_index = 0
	min_value = 100000000000000
	for j in range(k):
		if(d[j][i] < min_value):
			d_index = j
			min_value = d[j][i]
	c[d_index].append(i)
	c_cost += d[d_index][i]

#print(c)
#print(c_cost)

while(True):
	flag = 0
	for i in range(k):
		c_copy = c[:]
		#print(c_copy)	
		
		for j in range(k, n):
			m_copy = m[:]
			print(m_copy)
			m_copy[i] = j
			print(m_copy)
			cost = cal_cost(m_copy[:], k, d[:])
			
			if(cost < c_cost):
				flag = 1
				m[i] = j
				c.clear()
				print(c)
				for x in range(k):
					c.append([m[x]])

				for x in range(n):
					if x not in m:
						d_index = 0
						min_value = 100000000000000
						for l in range(k):
							if(d[m[l]][x] < min_value):
								d_index = l
								min_value = d[m[l]][x]
						
						c[d_index].append(x)
				print(c)
				c_cost = cost
			
	if(flag == 0):
		break


print("Final Clusters : ")
for i in range(k):
	for j in c[i]:
		print(j, end=' ')
	print()
				




























