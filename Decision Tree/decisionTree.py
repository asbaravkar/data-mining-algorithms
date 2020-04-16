
def classes(lst):
	freq = {}
	for i in lst:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1
	
	#print(freq)

	return freq

def pi(dct, sample, c, n):
	px = []
	for i in sample:
		summ = 0
		j = 0
		for ele in dct[i]:
			if((ele == sample[i]) and (dct["Play_Tennis"][j] == c)):
				summ += 1
			j += 1
		#print(summ)
		px.append(summ / n)
	
	#print(px)
	return px

f = open("table_data.txt", "r")

lst = []
for ele in f.readlines():
    lst.append(ele.split())

lst.pop()
#print(lst)

dct = {"Day": [], "Outlook": [], "Temperature": [], "Humidity": [], "Wind": [], "Play_Tennis": []}
for ele in lst:
	dct["Day"].append(int(ele[0]))
	dct["Outlook"].append(ele[1])
	dct["Temperature"].append(ele[2])
	dct["Humidity"].append(ele[3])
	dct["Wind"].append(ele[4])
	dct["Play_Tennis"].append(ele[5])

#print(dct)

print("Enter Unknown Sample :- ")
sample = {}

x = input("Outlook (Sunny/Overcast/Rainy) : ")
sample["Outlook"] = x

x = input("Temperature (Hot/Mild/Cool) : ")
sample["Temperature"] = x

x = input("Humidity (High/Normal/Weak/Strong) : ")
sample["Humidity"] = x

x = input("Wind (Weak/Strong) : ")
sample["Wind"] = x

#print(sample)

#Step 1
c = classes(dct["Play_Tennis"])
#print(c)

#Step 2
c1 = c["No"]
c2 = c["Yes"]
n = c1 + c2
c1 = c1 / n
c2 = c2 / n
#print(c1)
#print(c2)

#Step 3
pc1 = pi(dct, sample, "No", c["No"])
pc2 = pi(dct, sample, "Yes", c["Yes"])

pc1x = 1
for i in pc1:
	pc1x *= i
pc1x *= c["No"] / n

pc2x = 1
for i in pc2:
	pc2x *= i
pc2x *= c["Yes"] / n

print("Probability of No class : ",pc1x)
print("Probability of Yes class : ",pc2x)

if(pc1x > pc2x):
	print("Your given sample falls under Play_Tennis = No catagory")
else:
	print("Your given sample falls under Play_Tennis = Yes catagory")


















