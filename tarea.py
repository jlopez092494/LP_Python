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
new_A, new_L = int(orig_A * rFac), int(orig_L * rFac) 

#tuple de valores del size para enviar a funcion Image.new
newSize = (new_A, new_L) 

#nuevaImagen = Image.new("RGB", newSize, None)

allpix = [] 

for x in range(orig_A - 1):
    for y in range(orig_L - 1):
        tempixel = arr[x, y]
        allpix.append(tempixel)

arreglo = np.array(allpix)

print(arreglo)

#print("ARREGLO DE PIXELS:",allpix)

