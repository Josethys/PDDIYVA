importar  numpy  como  np

def  cortar_imagen ( imagen_gris , inicio_x , inicio_y , alto , ancho ):
  ( f , c ) =  imagen_gris . forma  
  d  =  len ( imagen_gris . forma )
  si  d  ==  2 :
    imagen_cortada  =  imagen_gris [ inicio_y : inicio_y + alto , inicio_x : inicio_x + ancho ]
    volver  imagen_cortada . astype ( np . uint8 )
