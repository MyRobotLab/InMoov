# ##############################################################################
# 								ImageDisplay SERVICE FILE
# ##############################################################################

ImageDisplay=Runtime.createAndStart("ImageDisplay", "ImageDisplay")
if LoadingPicture:
	r=ImageDisplay.displayFullScreen(RuningFolder+'/system/pictures/loading_1024-600.jpg',1)
