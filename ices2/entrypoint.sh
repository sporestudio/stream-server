#!/usr/bin/env bash

# Update the playlist file
python3 /usr/local/bin/ices2_playlist.py

# Start the ices2 server
exec ices2 /etc/ices2/ices2.xml
 
 