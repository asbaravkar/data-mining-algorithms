
f = open("input.txt", "r")

lst = []
for ele in f.readlines():
    lst.append(ele.split())

#print(lst)

n = len(lst)
#print(n)
sumx, sumy = 0, 0
sumx2, sumxy = 0, 0
for ele in lst:
	sumx += int(ele[0])
	sumy += int(ele[1])
	sumx2 += int(ele[0]) ** 2
	sumxy += int(ele[0]) * int(ele[1])
#print(sumx, sumy)
#print(sumx2, sumxy)

A = [[n, sumx], [sumx, sumx2]]
B = [sumy, sumxy]

#print(A)
#print(B)

det_A = (n * sumx2) - (sumx * sumx)
#print(det_A)

adj_A = [[sumx2, -sumx], [-sumx, n]]
#print(adj_A)

inv_A = [[sumx2/det_A, -sumx/det_A], [-sumx/det_A, n/det_A]]
#print(inv_A)

X = [(inv_A[0][0] * B[0]) + (inv_A[0][1] * B[1]), (inv_A[1][0] * B[0]) + (inv_A[1][1] * B[1])]
print(X)


x = input("Enter Year Of Experiance : ")

y = X[0] + (X[1] * float(x))

print("Predicted Salary : ",y)

















































