#   bind - The socket to bind.
#
#       A string of the form: 'HOST', 'HOST:PORT', 'unix:PATH'.
#       An IP is a valid HOST.
bind = "0.0.0.0:443"

# Comodo SSL has been integrated into nginx. Use gunicorn for manual SSL integration in the future.
# Gunicorn has been disabled in docker + docker-compose.
# Absolute path doesn't work, must be relative path and within the project folder.
keyfile = "jackwu.key"
certfile = "www_jackwu_ca.crt"
ca_certs = "bundle.crt"