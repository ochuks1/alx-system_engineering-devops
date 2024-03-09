#!/usr/bin/env bash

# Displays all active IPv4 IPs on the machine

# Get the local hostname
hostname=$(hostname)

# Resolve the IP address of the hostname
ip=$(getent hosts "$hostname" | awk '{print $1}')

# Output the IP address
echo "$ip"
