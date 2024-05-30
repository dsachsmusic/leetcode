#https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
#605. Can Place Flowers

flower_bed = [1,0,0,0,1,0,0,0,0,0,1]
n = 2
flower_bed_length = len(flower_bed)

count_of_consecutive_open_plots = 0
count_of_flowers_we_can_add = 0

for i in range(len(flower_bed)):
    if flower_bed[i] == 0: # if the plot is empty
        count_of_consecutive_open_plots += 1
        print(count_of_consecutive_open_plots)
        if count_of_consecutive_open_plots == 3:
            count_of_flowers_we_can_add += 1

            count_of_consecutive_open_plots = 1  # flower in middle of 3 plots, one plot remains open to right

        if count_of_consecutive_open_plots == 2 and i == 1:  # if the first two plots are open
            count_of_flowers_we_can_add += 1 
            count_of_consecutive_open_plots = 1  #flower in plot 1, plot 2 remains open
        elif count_of_consecutive_open_plots == 2 and i == flower_bed_length - 1:  #last two plots are empty
            count_of_flowers_we_can_add += 1
            count_of_consecutive_open_plots = 0  # to be tidy, though not necessary to do, since script is over
    else:
        count_of_consecutive_open_plots = 0  # if the current plot is full, can't place flower, and reset to 0

if n > count_of_flowers_we_can_add:
    print('We cannot as many flowers as we want', n, 'because we only have', count_of_flowers_we_can_add, 'open plots')
else: 
    print('We can add', n, 'flowers because we have', count_of_flowers_we_can_add, ' open plots')
    
