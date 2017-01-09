def CheckIfRobotCanLaunchAPPS(SkeletonNeeds):
	for SkeletonPart in SkeletonNeeds:
		if not SkeletonPart:
			return 0
			break
	return 1