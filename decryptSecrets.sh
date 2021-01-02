#!/bin/sh

# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$ENCRYPTION_KEY" \
    --output ./serviceAccountKey.json ./serviceAccountKey.json.gpg