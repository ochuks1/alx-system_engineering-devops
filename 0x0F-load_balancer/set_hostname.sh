#!/usr/bin/env bash
# This script sets the hostname and updates the /etc/hosts file.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <hostname>"
    exit 1
fi

NEW_HOSTNAME=$1

# Set the hostname
echo "$NEW_HOSTNAME" > /etc/hostname
hostname "$NEW_HOSTNAME"

# Update /etc/hosts
sed -i "/127.0.1.1/c\127.0.1.1\t$NEW_HOSTNAME" /etc/hosts

echo "Hostname set to $NEW_HOSTNAME"
