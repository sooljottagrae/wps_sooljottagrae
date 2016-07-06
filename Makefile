migrate:
	- python sooljottagrae/manage.py makemigrations users posts tags
	- python sooljottagrae/manage.py migrate

test:
	- pep8 . -v
	- python sooljottagrae/manage.py test users posts tags -v2 
