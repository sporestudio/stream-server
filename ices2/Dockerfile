FROM debian:bookworm-slim

RUN apt-get update -y && \
    apt-get install -y \
        ices2 \
        vorbis-tools \
        python3 \
        python3-pip && \
    apt-get clean -y

RUN python3 -m pip install watchdog --break-system-packages

COPY ./rootfs/ices2.xml /etc/ices2/ices2.xml
COPY ./utils/update_playlist.py /usr/local/bin/update_playlist.py
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN mkdir -p /var/lib/ices2 /shared && \
    touch /var/lib/ices2/playlist && \
    chmod -R 755 /shared && \
    chmod +x /usr/local/bin/entrypoint.sh /usr/local/bin/update_playlist.py

VOLUME /shared

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]