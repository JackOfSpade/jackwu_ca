#   bind - The socket to bind.
#
#       A string of the form: 'HOST', 'HOST:PORT', 'unix:PATH'.
#       An IP is a valid HOST.
bind = "0.0.0.0:443"

# Comodo SSL has been integrated into nginx. Use gunicorn for manual SSL integration in the future.
# Gunicorn has been disabled in docker + docker-compose.
keyfile = "jackwu.key"
certfile = "www_jackwu_ca.crt"
ca_certs = "bundle.crt"