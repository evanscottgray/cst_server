# cst_server
listens for hooks

get this thingy, fill in user and generate a simple api key.

```shell
cd ssl
openssl genrsa -out server.key 4096
openssl req -new -key server.key -out server.csr -subj /CN=localhost/
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

then add it to trusted certs, be sure to always always always trust

get chrome addon and fill in api_key where appropriate

start server, add addon to chrome and have fun.


if you can do `curl "https://localhost:15000/token?key=the_key_from_config"`

and get data back without adding a -k, everything should be working.
