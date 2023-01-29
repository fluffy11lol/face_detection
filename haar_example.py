 # импортирование библиотеки
import cv2

# импортирование изображения
image = cv2.imread("img_3.png")
# преобразование изображения в серый цвет
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# получение координат лица
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
	gray,
	# параметры метода Виолы-Джонса
	scaleFactor=1.02,
	minNeighbors=1,
	minSize=(30, 30)
)
# обводка лица
print(faces)
for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
	break
# вывод изображения
cv2.imshow("Faces found", image)
cv2.waitKey(0)
