build:
	sudo docker build -t misis .

run_local:
	python main.py

run:
	sudo docker run --env-file=.env -p 7000:80 -d misis --name sokolov

stop:
	sudo docker stop sokolov

update:
	git pull

deploy: update stop build run