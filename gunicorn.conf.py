#   bind - The socket to bind.
#
#       A string of the form: 'HOST', 'HOST:PORT', 'unix:PATH'.
#       An IP is a valid HOST.

bind = "0.0.0.0:8000"

#   workers - The number of worker processes that this server
#       should keep alive for handling requests.
workers = 4

#   keepalive - The number of seconds to wait for the next request
#       on a Keep-Alive HTTP connection.
#       A positive integer. Generally set in the 1-5 seconds range.
keepalive = 5

keyfile = "private.key"
certfile = "certificate.crt"
ca_certs = "ca_bundle.crt"