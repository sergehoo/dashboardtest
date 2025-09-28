FROM python:3.11-slim

WORKDIR /app

# Env python “propre”
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# OS deps minimalistes (build + pillow)
RUN set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      build-essential gcc \
      libjpeg62-turbo libpng16-16 zlib1g \
      curl ca-certificates \
    ; \
    rm -rf /var/lib/apt/lists/*

# Dépendances Python
# (assure-toi d’avoir un requirements.txt à la racine)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Code
COPY . /app/

# Dossiers static/media
RUN mkdir -p /app/static /app/media

# Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000