# gunicorn_config.py
accesslog = "-"
access_log_format = "%(h)s %(r)s %(s)s %(t)s %(b)s"
bind = "127.0.0.1:8000"