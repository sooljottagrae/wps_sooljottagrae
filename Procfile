web: gunicorn --pythonpath sooljottagrae/ --bind :5494 --workers=3 sooljottagrae.wsgi
worker: celery --workdir=sooljottagrae/ --app=fastube.celery:app --concurrency=3 worker
flower: celery --workdir=sooljottagrae/ --app=fastube.celery:app flower
