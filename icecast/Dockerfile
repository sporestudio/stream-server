FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y icecast2 && \
    mkdir -p /var/log/icecast2 && \
    chown -R nobody:nogroup /var/log/icecast2 && \
    rm -rf /var/lib/apt/lists/*

COPY icecast.xml /etc/icecast2/icecast.xml

VOLUME /shared

EXPOSE 8000

CMD ["icecast2", "-c", "/etc/icecast2/icecast.xml"]
