#> python3 my_solution.py arg1 arg2
#arg1 arg2

import sys
count=0
for i in sys.argv:
	if count>=1:
		print(i, end=' ')
	count+=1