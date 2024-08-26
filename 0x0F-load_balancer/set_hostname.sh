#!/usr/bin/env bash
# This script sets the hostname and updates the /etc/hosts file.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <web-02>"
    exit 1
fi

NEW_HOSTNAME=$1

# Set the hostname
echo "web-01" > /etc/hostname
hostname "web-01"

# Update /etc/hosts
sed -i "/127.0.1.1/c\127.0.1.1\tweb-01" /etc/hosts

echo "Hostname set to web-01"
