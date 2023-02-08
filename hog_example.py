# импортирование библиотеки
import cv2
import dlib

# импортирование изображения
image = cv2.imread("img_3.png")
# преобразование изображения в серый цвет
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# получение координат лица
detector = dlib.get_frontal_face_detector()
faces_location = detector(image, 1)
for (i, rect) in enumerate(faces_location):
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
# обводка лица
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# вывод изображения
cv2.imshow("Faces found", image)
cv2.waitKey(0)
