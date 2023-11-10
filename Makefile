build:
	sudo docker build -t misis .

run_local:
	python main.py

run:
	sudo docker run --env-file=.env -p 7000:80 -d --name sokolov misis

stop:
	sudo docker stop sokolov
	sudo docker rm sokolov

update:
	git pull

stats:
	sudo docker stats

launch: update stop build run

deploy:
	sudo ssh -i ~/Downloads/misis.pem ubuntu@ec2-3-249-39-102.eu-west-1.compute.amazonaws.com "cd osokolov/misis_po_sokolov/ && sudo make launch"