num = [1,2,3,4,1]

consecutive_increases = 0
for i in range(len(num)):
    if i < len(num)-1:
        if num[i] > num[i+1]:
            consecutive_increases = 0
        else:
            consecutive_increases += 1
            if consecutive_increases == 3:
                print("True")
                break
    else:
        print("False")