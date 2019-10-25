This is the instructions for installing and running the vmfarms.py app

#CONTENTS

There are 5 files included.

db_create.py  db_query.py  requirements.txt  vmfarms.db  vmfarms.py


requirements.txt
	
	- used to install dependencies for the app

db_create.py

	- this script is run once, to setup the apps database

db_query.py

	- this script is used to verify that the names are being stored in the database

vmfarms.db

	- the apps database

vmfarms.py

	- this script hosts the flask webserver, and handles the write to the db and the url endpoint/argument


#INSTALL

install the dependencies using pip

	pip install --requirement requirements.txt

create the apps database
	
	./db_create.py

#USEAGE

to start up the app, run the vmfarms.py script

	./vmfarms.py

youll see output like this:

	* Serving Flask app "vmfarms" (lazy loading)
 	* Environment: production
   	WARNING: This is a development server. Do not use it in a production deployment.
   	Use a production WSGI server instead.
 	* Debug mode: off
 	* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

now, using your web browser, head to http://127.0.0.1:5000/hello which should greet you with:

	Hello Stranger!

to add a name to the greeting, use the name argument. For example http://127.0.0.1:5000/hello?name=joe will return:

	Hello joe!

This will also save the provided name to the vmfarms.db database. You can verify this using the query script provided.

	db_query.py

youll see output like this:

	NAME =  joe

