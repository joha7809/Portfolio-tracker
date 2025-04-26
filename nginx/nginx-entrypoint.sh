#!/bin/sh

# Fix permissions
chmod -R 755 /app/staticfiles
chown -R www-data:www-data /app/staticfiles

# Start nginx
nginx -g "daemon off;"
