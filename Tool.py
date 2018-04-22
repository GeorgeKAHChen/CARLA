def CombineFigures(img1, img2, model):
	#This function will combine two figures in different RGB channel
	#Where img1 is initial image, img2 is boundary image
	#Also, if model = 1, means background is 255 and 0 means 0
	imgout = [img1, img1, img1]
	Judge = 0
	if model == 1:
		Judge = 255
	for i in range(0, len(img2)):
		for j in range(0, len(img2[i])):
			if img2[i][j] != Judge:
				img[0][i][j] = 255

	return imgout

