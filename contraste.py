importar  numpy  como  np

def  contraste ( imagen ):
  ( f , c ) =  imagen . forma
  persona_contraste  =  np . ceros (( f , c ))
  máximo  =  imagen . máximo ()
  mínimo  =  imagen . min ()
  para  i  en el  rango ( 0 , f ):
    para  j  en el  rango ( 0 , c ):
      pixel_actual  =  imagen [ i ][ j ]
      persona_contraste [ i ][ j ] =  round ((( pixel_actual  -  minimo ) / ( maximo  -  minimo )) *  255 )
      persona_contraste [ i ][ j ] =  persona_contraste [ i ][ j ] +  30
      si  persona_contraste [ i ][ j ] >  255 :
        persona_contraste [ i ][ j ] =  255
      elif  persona_contraste [ i ][ j ] <  0 :
        persona_contraste [ yo ][ j ] =  0
  devuelve  persona_contraste . astype ( np . uint8 )
