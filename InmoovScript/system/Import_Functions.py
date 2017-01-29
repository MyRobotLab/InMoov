def CheckIfRobotCanLaunchAPPS(Needs):
	for modules in Needs:
		if not modules:
			return 0
			break
	return 1
	
#this function usefull to calculate a maximum average
def maxAverage(list,howMany):
	sortedmaxAverage=sorted(list)
	maxAvg=[]
	for value in range(-1, -howMany, -1):
		maxAvg.append(sortedmaxAverage[value])
	return sum(maxAvg) / len(maxAvg)