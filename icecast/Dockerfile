FROM debian:bookworm-slim

# Instalar Icecast y dependencias
RUN apt-get update && \
    apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# Copiar configuración personalizada
COPY icecast.xml /etc/icecast2/icecast.xml

# Volumen compartido para archivos de audio
VOLUME /shared_media

# Puerto expuesto
EXPOSE 8000

# Comando de inicio
CMD ["icecast2", "-c", "/etc/icecast2/icecast.xml"]