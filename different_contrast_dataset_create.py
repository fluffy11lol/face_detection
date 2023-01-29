import cv2
import os

folder = 'Person01'
images = os.listdir(folder)
a = 0
while a <= 5:
	for i in images:
		if ".txt" not in i:
			image = cv2.imread(f"{folder}/" + i)
			image = cv2.convertScaleAbs(image, alpha=a)
			if not os.path.exists(f"Person01_ctr/a=={str(round(a, 1))}"):
				os.makedirs(f"Person01_ctr/a=={str(round(a, 1))}")
			cv2.imwrite(f"Person01_ctr/a=={str(round(a, 1))}/{i[0:(len(i) - 4)]}_{str(round(a, 1))}.jpg", image)

	a += 0.1
