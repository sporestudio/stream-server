FROM debian:bookworm-slim

RUN apt-get update -y && \
    apt-get install ices2 vorbis-tools python3 -y && \
    apt-get clean -y

COPY ./rootfs/ices2.xml /etc/ices2/ices2.xml
COPY music/Adele-SomeoneLikeYou.ogg /var/lib/ices2/Adele-SomeoneLikeYou.ogg
COPY update_playlist.py /usr/local/bin/update_playlist.py
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/update_playlist.py
COPY playlist /var/lib/ices2/playlist


ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]