# Deterministic deploy for the demo-projects hub (used by the RubberDuck
# runtime-mcp pentest pipeline, which prefers a Dockerfile over buildpack
# autodetect). Runs the hub control plane bound to 0.0.0.0:8000 so it's
# reachable inside a container.
FROM python:3.12-slim

WORKDIR /app

# Install hub deps first for layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# launcher.py reads these (env-overridable); bind all interfaces on a common port.
ENV HUB_HOST=0.0.0.0 \
    HUB_PORT=8000 \
    PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "demo-projects/launcher.py"]
