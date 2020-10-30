from flask import Flask, render_template, redirect
import pymongo
from datetime import datetime, time
# From the separate python file in this directory, we'll import the code that is used to scrape craigslist
import mission_to_mars

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_db

@app.route('/')
def home():
   #results = mongo.db.collection.find_one()
   return render_template('index.html') #data_dict = data_dict)

# This route will trigger the webscraping, but it will then send us back to the index route to render the results
@app.route("/scrape")
def scrape():

    data_dict = mission_to_mars.scrape()
    
    return render_template('index.html', data_dict = data_dict)


if __name__ == "__main__":
    app.run(debug=True)