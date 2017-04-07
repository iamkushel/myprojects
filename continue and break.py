print ("below is continue")

for i in range(1,10):
    if i == 5:
       continue  #continue statement doesn't exit from loop it just skips that step
    elif i < 10:
       print(i)

print ("below is for break")

for i in range(1,10):
    if i == 5:
       break   #the break statement exists out of loop it doesn't check for any below statement
    elif i < 10:
       print(i)
