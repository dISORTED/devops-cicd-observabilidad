FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements primero (mejora la caché)
COPY app/requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY app/ /app/app/

# Variables de entorno por defecto
ENV PORT=8080
ENV SERVICE_NAME=nublibar-demo

# Ejecutar inicialización de OTEL y levantar la app
CMD python -c "import app.otel" && uvicorn app.server:app --host 0.0.0.0 --port ${PORT}
