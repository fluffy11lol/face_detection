# импортирование библиотек
import numpy as np
import cv2

# импортирование модели для распознавания
net = cv2.dnn.readNetFromCaffe("Deep-Learning-Face-Detection-main/deploy.prototxt.txt",
                               "Deep-Learning-Face-Detection-main/res10_300x300_ssd_iter_140000.caffemodel")
# загрузка изображения
image = cv2.imread("img_9.png")
# получение размеров изображения
(h, w) = image.shape[:2]
# создание blob из изображения
blob_image = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                                   (300, 300), (104.0, 177.0, 123.0))
# передача blob в модель
net.setInput(blob_image)
# получение результатов обработки моделью
detections = net.forward()
# цикл по всем найденным лицам
for i in range(0, detections.shape[2]):
	# получение точности распознавания
	confidence = detections[0, 0, i, 2]
	# если точность больше 95% - рисуем прямоугольник
	if confidence > 0.60:
		rect = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = rect.astype("int")
		y = startY - 10 if startY - 10 > 10 else startY + 10
		cv2.rectangle(image, (startX, startY), (endX, endY),
		              (0, 0, 255), 2)
# вывод изображения
cv2.imshow("Faces found", image)
cv2.waitKey(0)
