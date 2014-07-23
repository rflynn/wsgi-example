nginx + wsgi

http://uwsgi-docs.readthedocs.org/en/latest/WSGIquickstart.html#putting-behind-a-full-webserver
```
location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:3031;
}
```
