import sys 
sys.set_int_max_str_digits(2147483647)
fac = int(input())

facnum = list()
facv = 1
for i in range(1, fac+1):
    facnum.append(fac)
    fac-=1

for i in range(1, len(facnum)+1):
    facv *= facnum[i-1]
    i-=1

print(facv) 
 
