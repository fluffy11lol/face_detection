import cv2
import os

folder = 'Person01'
images = os.listdir(folder)
b = -127
while b <= 190:
	for i in images:
		if ".txt" not in i:
			image = cv2.imread(f"{folder}/" + i)
			image = cv2.convertScaleAbs(image, beta=b)
			if not os.path.exists(f"Person01_br/b=={str(round(b, 1))}"):
				os.makedirs(f"Person01_br/b=={str(round(b, 1))}")
			cv2.imwrite(f"Person01_br/b=={str(round(b, 1))}/{i[0:(len(i) - 4)]}_{str(round(b, 1))}.jpg", image)

	b += 1
