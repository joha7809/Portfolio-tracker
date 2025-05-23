#!/bin/sh

# Fix permissions
chmod -R 755 /app/staticfiles
chown -R nginx:nginx /app/staticfiles

# Start nginx
nginx -g "daemon off;"
