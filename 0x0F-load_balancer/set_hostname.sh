#!/usr/bin/env bash
# This script sets the hostname and updates the /etc/hosts file.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <ochuks1>"
    exit 1
fi

NEW_HOSTNAME=$1

# Set the hostname
echo "ochuks" > /etc/hostname
hostname "ochuks"

# Update /etc/hosts
sed -i "/127.0.1.1/c\127.0.1.1\tochuks" /etc/hosts

echo "Hostname set to ochuks"
