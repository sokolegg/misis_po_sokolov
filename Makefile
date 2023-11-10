build:
	sudo docker build -t misis .

run_local:
	python main.py

run:
	sudo  docker run --env-file=.env -p 7000:80 -d misis