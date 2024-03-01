#!/usr/bin/env bash

# Create a sample apache-access.log file
cat <<EOF > apache-access.log
192.168.1.1 - - [01/Jan/2024:00:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [01/Jan/2024:00:00:01 +0000] "POST /login HTTP/1.1" 401 5678
192.168.1.3 - - [01/Jan/2024:00:00:02 +0000] "GET /about.html HTTP/1.1" 404 9012
192.168.1.4 - - [01/Jan/2024:00:00:03 +0000] "GET /contact.html HTTP/1.1" 200 3456
192.168.1.5 - - [01/Jan/2024:00:00:04 +0000] "GET /products HTTP/1.1" 301 7890
EOF
