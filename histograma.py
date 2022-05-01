importar  matplotlib . pyplot  como  plt
importar  numpy  como  np

def  imagen_histograma ( imagen_gris ):
  ( f , c ) =  imagen_gris . forma
  histograma  =  np . ceros (( 1 , 256 ))
  para  i  en el  rango ( 0 , f ):
    para  j  en el  rango ( 0 , c ):
      valor  =  imagen_gris [ i ][ j ]
      histograma [ 0 ][ valor ] =  histograma [ 0 ][ valor ] +  1

  por favor parcela ( histograma [ 0 ])
