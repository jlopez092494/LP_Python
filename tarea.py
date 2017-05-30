from PIL import Image
import os
import numpy as np

imagen = Image.open("wonder.jpg")
imagen.show()
arr = imagen.load()

#sacando size original de la imagen
orig_A, orig_L = imagen.size 

#factor de resizing
rFac = orig_A / (orig_A / 2)

#nuevos valor de width y height
new_A, new_L = 250, 400 

#tuple de valores del size para enviar a funcion Image.new
newSize = (new_A, new_L) 

allpix = [] 

for x in range(orig_A):
    for y in range(orig_L):
        tempixel = arr[x, y]
        bw_arr = int(round(sum(tempixel)) / float(len(tempixel)))
        allpix.append(bw_arr)

#arreglo = np.array(allpix)
#print(arreglo)

buff = ''.join(map(str, allpix))
nuevaImagen = Image.frombytes("RGB",newSize,buff,'raw')
#nuevaImagen = Image.frombytes("RGB",newSize,buffe,"raw")
nuevaImagen.save("nueva.bmp")
nuevaImagen.show()

#print("ARREGLO DE PIXELS:",allpix)

