importar  numpy  como  np

def  agregar_marcos ( imagen_gris , alto , ancho ):
  ( f , c ) =  imagen_gris . forma  
  d  =  len ( imagen_gris . forma )
  si  d  ==  2 :
    nueva_imagen  =  np . ceros (( f + alto * 2 , c + ancho * 2 ))
    nueva_imagen [ alto : - alto , ancho : - ancho ] =  imagen_gris

    volver  nueva_imagen . astype ( np . uint8 )
