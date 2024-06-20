#!/bin/bash

# Define variables
KEY_NAME="school"
KEY_SIZE=4096
PASSPHRASE="betty"
OUTPUT_DIR="$HOME/.ssh"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Generate the RSA key pair
ssh-keygen -t rsa -b $KEY_SIZE -N "$PASSPHRASE" -C "Generated key for ALX project" -f "$OUTPUT_DIR/$KEY_NAME"

# Output success message
echo "Generating public/private rsa key pair."
echo "Your identification has been saved in $OUTPUT_DIR/$KEY_NAME."
echo "Your public key has been saved in $OUTPUT_DIR/$KEY_NAME.pub."
echo "The key fingerprint is:"
ssh-keygen -l -f "$OUTPUT_DIR/$KEY_NAME"
echo "The key's randomart image is:"
ssh-keygen -lv -f "$OUTPUT_DIR/$KEY_NAME"

# List the generated files
ls -l "$OUTPUT_DIR/$KEY_NAME" "$OUTPUT_DIR/$KEY_NAME.pub"
