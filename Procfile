web: daphne Chatter.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python Chatter/manage.py runworker channels -v2