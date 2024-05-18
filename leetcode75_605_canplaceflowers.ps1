#https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
#605. Can Place Flowers
#if its the start, or end, of the array, two consecutive zeros are needed to plant, otherwise, 3 are needed
#if there is a one, the previous and following number will be a 0


$flowerbed = @(1,0,1,0,1,0,0,1,0,0,1)
$n = 2
$flowerBedLength = $flowerbed.Length


$countOfConsecutiveOpenPlots = 0
$countOfFlowersWeCanAdd = 0
for ($i = 0; $i -le $flowerBedLength-1; $i++) {
    
    Write-Verbose "Plot has a $($flowerbed[$i]) in it. Key: 0 = empty space, 1 = flower" -Verbose

    #if the plot is empty...
    if ($flowerbed[$i] -eq 0){
        
        #add the the count of consecutive open plots
        $countOfConsecutiveOpenPlots += 1
        
        
        
        if ($countOfConsecutiveOpenPlots -eq 3)  {
            
            $countOfFlowersWeCanAdd += 1

            #since we put a flower in the middle of 3 consecutive open plots, the count of consecutive open plots now -eq 1
            $countOfConsecutiveOpenPlots = 1
            
        }

        if (($countOfConsecutiveOpenPlots -eq 2) -and (($i -eq 1))){
            Write-Verbose "There are two consecutive plots at the beginning. Adding a flower in the first plot" -Verbose
            $countOfFlowersWeCanAdd += 1
            
            #since we put a flower in plot 1, and plot to is open, count of open plots -eq 1
            $countOfConsecutiveOpenPlots = 1
        }
        
        elseif (($countOfConsecutiveOpenPlots -eq 2) -and ($i -eq $flowerBedLength-1)){
            Write-Verbose "There are two consecutive plots at at the end. Adding a flower in the last plot" -Verbose
            $countOfFlowersWeCanAdd += 1
            
            #set the count of consecutive open plots to 0. This isn't functionally necessary, but its nice to be tidy
            $countOfConsecutiveOpenPlots = 0
        }
    }
    else {
        #if the plot has a flower, can't fill it, and count of consecuitve open plots resets 
        $countOfConsecutiveOpenPlots = 0 
        
    }
}


Write-Output "Count of flowers that can be added is $countOfFlowersWeCanAdd, and, n, the count of flowers we want to add,is $n..."
if ($n -gt $countOfFlowersWeCanAdd){
    Write-Output "We cannot add as many flowers as we want"
}
else {
    Write-Output "We can add all the flowers that we want to add"
}


    




