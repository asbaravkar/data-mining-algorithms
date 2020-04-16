
f = open("input2.txt", "r")

lst = []
for ele in f.readlines():
    lst.append(ele.split())

print(lst)

n = len(lst)

sumx1, sumx2, sumy, sumx1y, sumx2y, sumx1_2, sumx2_2, sumx1x2 = 0, 0, 0, 0, 0, 0, 0, 0

for ele in lst:
	sumx1 += int(ele[1])
	sumx2 += int(ele[2])
	sumy += int(ele[0])
	sumx1y += int(ele[1]) * int(ele[0])
	sumx2y += int(ele[2]) * int(ele[0])
	sumx1_2 += int(ele[1]) ** 2
	sumx2_2 += int(ele[2]) ** 2
	sumx1x2 += int(ele[1]) * int(ele[2])

print(sumx1, sumx2, sumy, sumx1y, sumx2y, sumx1_2, sumx2_2, sumx1x2)

A = [[n, sumx1, sumx2], [sumx1, sumx1_2, sumx1x2], [sumx2, sumx1x2, sumx2_2]]
print("A: ",A)
'''
n 		sumx1 		sumx2
sumx1   sumx1_2 	sumx1x2
sumx2 	sumx1x2 	sumx2_2
'''
B = [sumy, sumx1y, sumx2y]
print(B)

det_A = n*((sumx1_2*sumx2_2)-(sumx1x2*sumx1x2)) - sumx1*((sumx1*sumx2_2)-(sumx1x2*sumx2)) + sumx2*((sumx1*sumx1x2)-(sumx1_2*sumx2))
print(det_A)

adj_A = [[((sumx1_2*sumx2_2)-(sumx1x2*sumx1x2)), -((sumx1*sumx2_2)-(sumx1x2*sumx2)), ((sumx1*sumx1x2)-(sumx1_2*sumx2))],
		 [-((sumx1*sumx2_2)-(sumx2*sumx1x2)), ((n*sumx2_2)-(sumx2*sumx2)), -((n*sumx1x2)-(sumx1*sumx2))],
		 [((sumx1*sumx1x2)-(sumx2*sumx1_2)), -((n*sumx1x2)-(sumx2*sumx1)), ((n*sumx1_2)-(sumx1*sumx1))]]
print(adj_A)

inv_A = [[adj_A[0][0]/det_A, adj_A[0][1]/det_A, adj_A[0][2]/det_A],
		 [adj_A[1][0]/det_A, adj_A[1][1]/det_A, adj_A[1][2]/det_A],
		 [adj_A[2][0]/det_A, adj_A[2][1]/det_A, adj_A[2][2]/det_A]]
print(inv_A)
			
X = [(inv_A[0][0]*B[0])+(inv_A[0][1]*B[1])+(inv_A[0][2]*B[2]),
	 (inv_A[1][0]*B[0])+(inv_A[1][1]*B[1])+(inv_A[1][2]*B[2]),
	 (inv_A[2][0]*B[0])+(inv_A[2][1]*B[1])+(inv_A[2][2]*B[2])]
print(X)

x1 = float(input("Enter No. of salesmen : "))
x2 = float(input("Enter Annual Add cost : "))

y = X[0] + (X[1] * x1) + (X[2] * x2)

print("Predicted annual sales : ",y)













