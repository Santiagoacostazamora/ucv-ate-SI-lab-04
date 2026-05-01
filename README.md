# UCV-ATE-SI-Lab04: API de Visión Computacional

## Descripción

Este proyecto es una API REST desarrollada con FastAPI para el análisis de imágenes utilizando técnicas de visión computacional. Forma parte del laboratorio 4 del curso de Arquitectura de Tecnologías Empresariales - Sistemas de Información en la Universidad Católica del Venezuela.

La API permite subir imágenes y analizarlas para detectar bordes utilizando el algoritmo de Canny de OpenCV, además de obtener las dimensiones de la imagen.

## Características

- **Análisis de Imágenes**: Detección de bordes mediante el algoritmo de Canny.
- **Información de Dimensiones**: Obtención del alto y ancho de la imagen.
- **API RESTful**: Endpoints simples y eficientes con FastAPI.
- **Gestión de Dependencias**: Utiliza Poetry para la gestión de paquetes.
- **Pruebas**: Configurado con pytest para testing.
- **Calidad de Código**: Integración con SonarCloud para análisis estático.

## Tecnologías Utilizadas

- **FastAPI**: Framework web para construir APIs REST.
- **OpenCV**: Biblioteca de visión computacional para procesamiento de imágenes.
- **NumPy**: Para operaciones numéricas.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.
- **Poetry**: Herramienta de gestión de dependencias y empaquetado.
- **Pytest**: Framework para pruebas unitarias.

## Instalación

### Prerrequisitos

- Python 3.13 o superior.
- Poetry instalado en el sistema.

### Pasos de Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd ucv-ate-si-lab04
   ```

2. Instala las dependencias usando Poetry:
   ```bash
   poetry install
   ```

3. Activa el entorno virtual:
   ```bash
   poetry shell
   ```

## Uso

### Ejecutar la API

Para iniciar el servidor de desarrollo:

```bash
uvicorn src.lab4_api_cv.api.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

### Documentación Interactiva

FastAPI proporciona documentación automática en:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints de la API

### POST /analyze-image

Analiza una imagen subida y devuelve información sobre sus dimensiones y detección de bordes.

**Parámetros:**
- `file`: Archivo de imagen (multipart/form-data).

**Respuesta de Éxito (200):**
```json
{
  "mensaje": "Procesamiento exitoso",
  "resultado": {
    "alto": 480,
    "ancho": 640,
    "bordes_detectados": 1
  }
}
```

**Campos del Resultado:**
- `alto`: Altura de la imagen en píxeles.
- `ancho`: Ancho de la imagen en píxeles.
- `bordes_detectados`: 1 si se detectaron bordes, 0 en caso contrario.

### GET /

Endpoint de salud para verificar que la API está funcionando.

**Respuesta:**
```json
{
  "mensaje": "API de Visión Computacional funcionando"
}
```

## Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

Actualmente, hay una prueba básica en `tests/test_api.py`.

## Estructura del Proyecto

```
ucv-ate-si-lab04/
├── pyproject.toml          # Configuración de Poetry y dependencias
├── README.md               # Este archivo
├── sonar-project.properties # Configuración de SonarCloud
├── src/
│   └── lab4_api_cv/
│       ├── api/
│       │   └── main.py     # Punto de entrada de la API
│       └── services/
│           └── image_service.py # Lógica de análisis de imágenes
└── tests/
    └── test_api.py         # Pruebas unitarias
```

## Contribución

1. Fork el proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto es parte de un laboratorio académico y no tiene una licencia específica asignada.

## Autor

- **Santiago Acosta Zamora** - [oacostaz@ucvvirtual.edu.pe](mailto:oacostaz@ucvvirtual.edu.pe)

## Análisis del Proyecto

### Funcionalidad Principal

La funcionalidad principal se centra en el procesamiento de imágenes mediante la detección de bordes. El servicio `image_service.py` utiliza OpenCV para:

1. Leer la imagen en escala de grises.
2. Aplicar el filtro de Canny para detectar bordes.
3. Calcular si hay bordes presentes (basado en la suma de píxeles del resultado de Canny).
4. Devolver las dimensiones de la imagen.

### Arquitectura

- **Capa API**: `main.py` maneja las rutas HTTP y la subida de archivos.
- **Capa de Servicios**: `image_service.py` contiene la lógica de negocio para el análisis de imágenes.
- **Separación de Preocupaciones**: El código está modularizado para facilitar el mantenimiento y las pruebas.

### Mejoras Potenciales

- Agregar validación de tipos de archivos de imagen.
- Implementar manejo de errores más robusto.
- Expandir las funcionalidades de análisis (detección de objetos, OCR, etc.).
- Agregar logging para monitoreo.
- Mejorar las pruebas con casos más específicos.