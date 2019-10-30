This is the instructions for installing and running the vmfarms.py app

#CONTENTS

There are 6 files included.

db_query.py  requirements.txt  vmfarms.db  vmfarms.py Dockerfile docker-compose.yaml


requirements.txt
	
	- used to install dependencies for the app

db_query.py

	- this script is used to verify that the names are being stored in the database

vmfarms.db

	- the apps database (created after the first run)

vmfarms.py

	- this script hosts the flask webserver, and handles the create/write to the db and the url endpoint/argument

Dockerfile

	- the dockerfile used for image creation

docker-compose.yaml

	- used to configure the building of the docker container

#INSTALL

Once the directory is pulled from github, we just need to issue a docker compose inside of the directory

	docker-compose up

Note: The version in the docker-compose.yaml is set to '3'. If you get a version error, you can change the version in the file to one that satisifes your system.

#USEAGE

Once the docker compose is complete, the app is ready to be used.

youll see output like this:

	Starting vmfarms_vmfarms_1 ... done
	Attaching to vmfarms_vmfarms_1
	vmfarms_1  |  * Serving Flask app "vmfarms" (lazy loading)
	vmfarms_1  |  * Environment: production
	vmfarms_1  |    WARNING: This is a development server. Do not use it in a production deployment.
	vmfarms_1  |    Use a production WSGI server instead.
	vmfarms_1  |  * Debug mode: off
	vmfarms_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

now, using your web browser, head to http://0.0.0.0:5000/hello which should greet you with:

	Hello Stranger!

to add a name to the greeting, use the name argument. For example http://0.0.0.0:5000/hello?name=joe will return:

	Hello joe!

This will also save the provided name to the vmfarms.db database. You can verify this using the query script provided.

	db_query.py

youll see output like this:

	NAME =  joe

