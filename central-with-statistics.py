#central-with-statistics.py 
#Use the statistic module to calculate measures of central tendency

#import statistics module
import statistics

#define values
values = [47, 95, 88, 73, 88, 84]

#1. Count
print('1. The Count of values =', len(values))

#2. Sum
print('2. The Sum of values =', sum(values))

#3. Mean
mean = statistics.mean(values)
print(f'3. The Mean of values = {mean:0.2f}')

#4. Median
median = statistics.median(values)
print(f'3. The Mean of values = {median:0.2f}')

#5. Mode
mode = statistics.mode(values)
print(f'3. The Mean of values = {mode}')