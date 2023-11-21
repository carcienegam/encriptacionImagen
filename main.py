import imghdr

# Verifica si la imagen es valida o no
def imagenValida(ruta):
  tipo = imghdr.what(ruta)
  return tipo is not None

# Solicita la ruta
ruta = input('Ruta de la imagen: ')

# Verifica si la imagen es valida o no
if not imagenValida(ruta):
  print('La ruta ingresada no es una imagen válida')
  exit()

# Solicita la clave de enciptacion
clave = int(input('Clave de encriptacion: '))

# Abre y lee la imagen
with open(ruta, 'rb') as img:
  image = img.read()

# Encripta la imagen
image = bytearray(image)
for index, valor in enumerate(image):
  image[index] = valor ^ clave

# Abre y guarda la version encriptada
with open(ruta, 'wb') as img:
  img.write(image)

print('¡Listo!')
