FROM python:3.11-slim

# Install ffmpeg for video processing
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .
COPY templates/ templates/
COPY static/ static/

# Create directories
RUN mkdir -p /tmp/video-chopper/uploads /tmp/video-chopper/output /tmp/video-chopper/previews

# Use PORT env variable
CMD sh -c "gunicorn main:app --bind 0.0.0.0:\${PORT:-8080} --timeout 0 --workers 2"
