#central-native.py 
#Use native Python programming to calculate measures of central tendency

#assign values
values = [47, 95, 88, 73, 88, 84]

#1. Count
print('1. The Count of values =', len(values))

#2. Sum
print('2. The Sum of values =', sum(values))

#3. Mean
mean = sum(values)/len(values)
print (f'3. The Mean of values = {mean:0.2f}'  )

#4. Median
length = len(values)
sv = sorted(values)

if length % 2 == 1:
    median = sv[length // 2]
else:
    num1 = sv[length // 2]
    num2 = sv[(length // 2) - 1]
    median = (num1 + num2)/2

print(f'4. The Median of values = {median}')
      
#5. Mode

L1=[]

i = 0
while i < len(sv) :
    L1.append(sv.count(sv[i]))
    i += 1
    
d1 = dict(zip(sv, L1))

d2={k for (k,v) in d1.items() if v == max(L1) }
  
print('5. The Mode of values = ' + str(d2))