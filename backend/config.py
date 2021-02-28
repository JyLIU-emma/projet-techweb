import os
from gevent import monkey

monkey.patch_all()
import multiprocessing
debug = False
bind = "0.0.0.0:2021"
pidfile = "gunicorn.pid"
accesslog = "/mnt/d/1-M2-S2/3-tech-web/logs/gunicorn.log"
workers = multiprocessing.cpu_count()*2+1
workers_class = "gevent"
deamon = True