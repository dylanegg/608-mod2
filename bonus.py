# bonus.py 
# create a new file named bonus.py that calculates the 
# count, sum, mean, median, and mode for a new
# set of data with at least 100 or more data points

#import statistics module
import statistics

#define values
values =[81,89,13,18,43,98,7,9,8,36,85,11,79,27,51,51,43,35,47,47,3,63,2,85,48,4,97,63,36,58,97,39,15,28,57,98,61,66,10,66,67,1,83,30,22,54,2,16,70,93,60,96,2,71,8,29,86,83,92,44,36,27,21,59,9,49,70,39,73,66,95,43,77,26,70,56,42,49,43,25,94,15,7,39,20,63,11,66,9,73,20,74,79,64,15,29,78,15,69,3,90,46,60]

#1. Count
print('1. The Count of values =', len(values))

#2. Sum
print('2. The Sum of values =', sum(values))

#3. Mean
mean = statistics.mean(values)
print(f'3. The Mean of values = {mean:0.2f}')

#4. Median
median = statistics.median(values)
print(f'4. The Median of values = {median:0.2f}')

#5. Mode
mode = statistics.mode(values)
print(f'5. The Mode of values = {mode}')