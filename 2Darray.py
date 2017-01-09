
def main()
import sys

#input
arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

# taking 3 rows at a time
offset = 2
for i in xrange((len(arr)/offset)+1):
	temp_arr = list()
	for j in range(i,i+offset+1):
		temp_arr.append(arr[j])
	calculate(temp_arr)

#computing set of 3 rows
def calculate(temp_arr):
	print("computing for")
	print temp_arr
	for k in xrange(len(temp_arr)+1):
		print k
		tmp_arr = []
		tmp_arr.append(temp_arr[0][k:k+3])
		tmp_arr.append(temp_arr[1][k:k+3])
		tmp_arr.append(temp_arr[2][k:k+3])
		calc(tmp_arr)

greatest =0
sum1 = []
def calc(tmp_arr):
	sum1.append(np.sum(tmp_arr))

				

	
		
	


