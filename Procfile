web: sh -c "python manage.py collectstatic --noinput --settings=portfolio_pkg.settings_production && gunicorn portfolio_pkg.wsgi --bind 0.0.0.0:$PORT --log-file -"
release: sh -c "python manage.py migrate --settings=portfolio_pkg.settings_production && python manage.py collectstatic --noinput --settings=portfolio_pkg.settings_production"
