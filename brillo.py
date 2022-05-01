importar  numpy  como  np

def  brillo ( imagen , factor_corrección ):
  ( f , c ) =  imagen . forma
  persona_brillo  =  np . ceros (( f , c ))
  para  i  en el  rango ( 0 , f ):
    para  j  en el  rango ( 0 , c ):
      persona_brillo [ i ][ j ] =  imagen [ i ][ j ] +  factor_corrección
      si  persona_brillo [ i ][ j ] >  255 :
        persona_brillo [ i ][ j ] =  255
      elif  persona_brillo [ i ][ j ] <  0 :
        persona_brillo [ i ][ j ] =  0
  volver  persona_brillo . astype ( np . uint8 )
