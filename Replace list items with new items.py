
# Replace list items with new items


l = []
x = 0  
print("Enter 8 numbers ")
try:
    while x < 8:
      
        i = int(input("Please enter numbers: "))
        l.append(i)
        x += 1
    s = l[1]
    s = s * s
    f = l[3]
    f= f * f
    for i in range (len(l)):
        if i==2:
            l[i] = s
        elif i == 4:
            l[i] = f
        else :
            pass
    for x in range(len(l)):
        print("Updated list :", l[x])
except ValueError:
    print ('Invalid input.')


# In[ ]:




