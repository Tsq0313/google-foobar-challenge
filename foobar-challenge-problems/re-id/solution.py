import math

def solution(i):
 	res = ""
  	for num in range(2, 20261):
    	if isPrime(num):
      		res += str(num)
      		if len(res) > i + 5:
        		break
  return res[i : i + 5]

def isPrime(num):
    end = int(math.sqrt(num)) + 1
    for i in range(2, end):
        if num % i == 0: 
            return False
    return True