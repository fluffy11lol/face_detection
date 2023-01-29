# импорт библиотек
import cv2
import os
import time
import xlsxwriter
import dlib

# создание массива для записи результатов для всех папок
ex_array = []
# получение списка файлов в папке
path = "Person01_br"
# инициализация детектора
detector = dlib.get_frontal_face_detector()
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
		# преобразование изображения в серый цвет
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# получение координат лица
		face_locations = detector(image, 1)
		# проверка наличия лица
		if len(face_locations) == 0:
			negative += 1
		else:
			positive += 1
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
workbook = xlsxwriter.Workbook('hog.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for col, data in enumerate(ex_array):
	worksheet.write_column(row, col, data)
workbook.close()
# запись в файл .txt
with open('hog.txt', 'w') as f:
	for item in ex_array:
		f.write("%s \n" % item)
