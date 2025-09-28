#!/usr/bin/env bash
set -euo pipefail

echo "[entrypoint] Boot…"

# (Optionnel) Si plus tard tu ajoutes une DB, tu peux faire une attente socket ici
# cf. plus haut dans notre échange.

# Prépare les dossiers static/media (liés à des volumes dans le compose)
mkdir -p /app/static /app/media || true

# Migrations/collectstatic pilotés par ENV
if [[ "${RUN_MIGRATIONS:-0}" == "1" ]]; then
  echo "[entrypoint] manage.py migrate…"
  python manage.py migrate --noinput
fi

if [[ "${RUN_COLLECTSTATIC:-0}" == "1" ]]; then
  echo "[entrypoint] manage.py collectstatic…"
  python manage.py collectstatic --noinput
fi

# Django derrière Traefik (TLS terminé au proxy) → conseille SECURE_PROXY_SSL_HEADER
# à mettre dans settings.py :
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# USE_X_FORWARDED_HOST = True

# Si une commande est passée par docker-compose, on l'exécute
if [[ "$#" -gt 0 ]]; then
  echo "[entrypoint] exec: $*"
  exec "$@"
fi

# Fallback (au cas où le compose n'a pas de command)
echo "[entrypoint] default -> gunicorn djangoProject.wsgi:application"
exec gunicorn djangoProject.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 2 --timeout 60 --log-level info