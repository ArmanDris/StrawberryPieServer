# gunicorn_config.py
accesslog = "-"
access_log_format = "%(h)s %(r)s %(s)s %(t)s %(b)s"
bind = "localhost:8000"