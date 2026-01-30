class Solution:
	def countOddEven(self, arr):
		evencount = 0
		oddcount = 0
		for num in arr:
		    if(num%2!=0):
		        oddcount += 1
		    else:
		        evencount += 1
		return oddcount,evencount
		        