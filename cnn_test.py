# импорт библиотек
import cv2
import os
import time
import xlsxwriter

# создание массива для записи результатов для всех папок
ex_array = []
# подключение модели
net = cv2.dnn.readNetFromCaffe("Deep-Learning-Face-Detection-main/deploy.prototxt.txt",
                               "Deep-Learning-Face-Detection-main/res10_300x300_ssd_iter_140000.caffemodel")
# получение списка файлов в папке
path = "Person01_br"
br_folders = os.listdir(path)
# перебор папок
for folder in br_folders:
	# создание массива для записи результатов для каждой папки
	text = []
	# переменные для подсчета времени и количества лиц
	endtime = 0
	negative = 0
	positive = 0
	total = 0
	images = os.listdir(f"{path}/{folder}")
	# запуск таймера
	start_time = time.time()
	# перебор изображений в папке
	for i in images:
		# загрузка изображения
		image = cv2.imread(f"{path}/{folder}/" + i)
		# преобразование изображения в blob
		blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
		                             (300, 300), (104.0, 177.0, 123.0))
		net.setInput(blob)
		detections = net.forward()
		for t in range(0, detections.shape[2]):
			# извлечение вероятности (вероятность, что объект является лицом)
			confidence = detections[0, 0, t, 2]
			if confidence > 0.95:
				positive += 1
				break
			else:
				negative += 1
				break
	# остановка таймера
	endtime = round((time.time() - start_time), 3)
	# подсчет общего количества лиц
	total = positive + negative
	# запись результатов в массив
	text.append(folder[3:])
	text.append(positive)
	text.append(negative)
	text.append(total)
	text.append(round(positive / total * 100, 3))
	text.append(endtime)
	text.append(round(total / endtime, 3))
	ex_array.append(text)
	print(folder + " done")
# сортировка массива по первому элементу
ex_array.sort(key=lambda x: float(x[0]))
# запись в файл .xlsx
print(ex_array)
workbook = xlsxwriter.Workbook('CNN.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for col, data in enumerate(ex_array):
	worksheet.write_column(row, col, data)
workbook.close()
# запись в файл .txt
with open('CNN.txt', 'w') as f:
	for item in ex_array:
		f.write("%s \n" % item)
