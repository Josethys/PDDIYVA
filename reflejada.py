importar  numpy  como  np

def  refleja_imagen ( imagen_gris ):
  ( f , c ) =  imagen_gris . forma
  d  =  len ( imagen_gris . forma )
  imagen_reflejada  =  np . ceros (( f , c ))
  si  d  ==  2 :
    para  i  en el  rango ( 0 , f ):
      para  j  en el  rango ( 0 , c ):
        imagen_reflejada [ i ][ j ] =  imagen_gris [ i , c - ( j + 1 )]

  volver  imagen_reflejada . astype ( np . uint8 )
