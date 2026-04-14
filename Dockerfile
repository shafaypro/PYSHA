FROM python:3.12-slim AS builder

ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md /app/
COPY src /app/src
RUN pip install --prefix=/install ".[llm-anthropic,llm-openai,llm-ollama,tts-edge,skills-web,skills-wikipedia,skills-news,skills-system,web]"

# --- runtime image ---
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg mpg123 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
COPY src /app/src
COPY pyproject.toml README.md /app/

EXPOSE 8000
ENV PYSHA_WEB_HOST=0.0.0.0 PYSHA_WEB_PORT=8000
CMD ["pysha", "web"]
