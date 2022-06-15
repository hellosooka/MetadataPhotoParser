from os import path
from PIL import Image, ExifTags
import tkinter as tk
from tkinter.filedialog import askopenfilename
import datetime


#Сбор метадаты
def get_MetaData(image):
    img = Image.open(image)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    return exif

#ПОХУЙ
def main():
    #Получение файла
    image = str(get_file())
    #Проверка расширения файла
    full_name = path.basename(image)
    name = path.splitext(full_name)[1]
    if name == ".jpg":
        #Получение даты
        data = get_MetaData(image = image)
        write_file(data)
    else:
        print("Только JPG")
        exit
    
#Сборка файла
def get_file():
    filename = askopenfilename()
    return filename

#Запись файла
def write_file(data):
    print("Записать Данные в отдельный файл? 1/0")
    otv = int(input())
    if otv == 1:
        date = str(datetime.datetime.now())
        file_data = open(date + ".txt", "w")
        for i in data:
            file_data.write(i + ": "+ str(data[i]))
            file_data.write("\n")


main()