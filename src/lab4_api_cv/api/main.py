import shutil
from pathlib import Path
from fastapi import FastAPI, UploadFile, HTTPException
from lab4_api_cv.services.image_service import analizar_imagen

app = FastAPI()

# Carpeta base segura
DATA_DIR = Path("data").resolve()

@app.post("/analyze-image")
def analyze_image(file: UploadFile):

    # Crear carpeta si no existe
    DATA_DIR.mkdir(exist_ok=True)

    # Sanitizar el nombre del archivo (evita ../ etc.)
    safe_filename = Path(file.filename).name

    # Construir ruta segura
    path = (DATA_DIR / safe_filename).resolve()

    # Validar que no salga del directorio permitido
    if DATA_DIR not in path.parents:
        raise HTTPException(status_code=400, detail="Invalid filename")

    # Guardar archivo
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Procesar imagen
    resultado = analizar_imagen(str(path))

    return {
        "mensaje": "Procesamiento exitoso",
        "resultado": resultado
    }


@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}
