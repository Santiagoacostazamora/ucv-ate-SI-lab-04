import cv2

def analizar_imagen(path: str):
    imagen = cv2.imread(path, 0)
    bordes = cv2.Canny(imagen, 50, 150)

    return {
        "alto": imagen.shape[0],
        "ancho": imagen.shape[1],
        "bordes_detectados": int(bordes.sum() > 0)
    }
