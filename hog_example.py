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
print(faces_location)
x = faces_location[0].left()
y = faces_location[0].top()
w = faces_location[0].bottom()
h = faces_location[0].right()
# обводка лица
cv2.rectangle(image, (x, y), (h, w), (0, 255, 0), 2)
# вывод изображения
cv2.imshow("Faces found", image)
cv2.waitKey(0)
