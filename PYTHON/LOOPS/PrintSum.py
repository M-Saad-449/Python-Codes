sum = 0
sum_2 = 0

for i in range (0,51,2):
    if i%2==0:
        sum+=i
    else:
        continue
for j in range (1,51,2):
    if j%2!=0:
        sum_2+=j
    else:
        continue
print(sum)
print(sum_2)
