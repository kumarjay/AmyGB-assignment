To run this application:

gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app

Execute this command. 
Where workers is the no of workers you want and bind is local host address.
