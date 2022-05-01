importar  numpy  como  np
def  ConvertRGB2Gray ( imagen_rgb ):
  d  =  len ( imagen_rgb . forma )
  si  d  ==  3 :
    R  =  imagen_rgb [:,:, 0 ]
    G  =  imagen_rgb [:,:, 1 ]
    B  =  imagen_rgb [:,:, 2 ]
    imagen_rgb_gris  =  0.3013 * R  +  0.5897 * G  +  0.109 * B
    devuelve  imagen_rgb_gris . astype ( np . uint8 )
