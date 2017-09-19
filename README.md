# level1
level1 goals for off season 


sum = 0 
for x in range(1,1000) :
    div = x / 5
    rem5 = x % 5
    rem3 = x % 3
    if rem5 == 0 or rem3 == 0: 
        print ("%d is divisible by 5 or 3!!!" % x) 
        sum = sum + x 
        print(sum)
    

    #print("%d divison result %d, remainder %d" % (x,div, rem))
    
