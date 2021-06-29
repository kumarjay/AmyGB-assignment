To run this application:
```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app
```
Execute this command. 
Where workers is the no of workers you want and bind is local host address.

You can also run gunicorn config file
```bash
gunicorn -c gunicorn.py wsgi:app
```