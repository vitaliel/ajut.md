lint:
	 black --exclude venv/ --line-length 120 --target-version py37 .

check:
	python3 ro_help/manage.py check

migrate:
	python3 ro_help/manage.py migrate

start:
	cd ro_help && python3 manage.py runserver

gen-locale:
	cd ro_help && django-admin makemessages -a

i18n:
	cd ro_help && django-admin compilemessages

gen-migration:
	cd ro_help && python3 manage.py makemigrations
