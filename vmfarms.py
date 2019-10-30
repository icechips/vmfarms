#!/usr/bin/env python3.6

from flask import Flask, request
import sqlite3


#creates a flask app object
app = Flask(__name__)

#create hello endpoint
@app.route('/hello')

#function to grab name argument, return, and save to db
def sayHello():

   if 'name' in request.args:
       person = request.args['name']

       #add person to db
       conn = sqlite3.connect('vmfarms.db')
       cur = conn.cursor()

       cur.execute("INSERT INTO names (name) VALUES (?)", [person])

       conn.commit()
       conn.close()

       return(f"Hello {person}!")

   else:
       return("Hello Stranger!")


if __name__ == "__main__":
        app.run(host='0.0.0.0')
