# https://stackoverflow.com/questions/67440510/cv2-error-opencv4-5-2-error-215assertion-failed-src-empty-in-functi

from PIL import Image
import os
import glob

# ------------------ ПУТЬ ДО ФАЙЛОВ------------------------
path_to_file = os.getcwd()
output_file = path_to_file + '\\Сжатые изображения'
# ------------------------------------------
print(path_to_file)
# ----------------------- ПРОВЕРКА НА СУЩЕСТВУЮЩУЮ ПАПКУ ------------------------------------
try:
    os.mkdir(output_file)
except:
    pass
# ------------------------------------------------------------

print('Сжать JPG: 1')
print('Сжать PNG: 2')
print('Сжать JPG и PNG: 3')

num = input("Введите цифру => ") 

# --------------------------------- САМ АЛГОРИТМ СЖАТИЯ ДАННЫХ ---------------------------------------------------
def data_compression(name):
    jpgphoto = path_to_file + "/*." + str(name)    
    size = (1920,1080)   

    for infile in glob.glob(jpgphoto, recursive=True):     
        f,ext = os.path.splitext(infile)     

        print(f)
        print(ext)

        k,c = os.path.split(f)        
        img = Image.open(infile)      

        if (name == 'png'):
            img = img.convert("RGB")

        img.thumbnail(size, Image.ANTIALIAS)        
        img.save(output_file+ "\\" + c + ".jpg", "JPEG", quality=90) 

# --------------------------- ВЫБОР РАСШИРЕНИЯ ---------------------------------------
try:
    if (num == '1'):
        data_compression('jpg')

    if (num == '2'):
        data_compression('png')

    if(num == '3'):
        data_compression('jpg')
        data_compression('png')

except Exception as e:
    print(e)

print('Сжатие данных прошло успешно.')
os.system("pause")
