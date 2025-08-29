# Dockerfile

FROM python:3.11.3-slim

# Instalamos dependencias del sistema (incluye gettext para i18n)
RUN apt-get update && \
    apt-get install -y gettext gcc build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Seteamos el directorio de trabajo
WORKDIR /app

# Copiamos e instalamos dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

# Comando por defecto (puede ajustarse)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
