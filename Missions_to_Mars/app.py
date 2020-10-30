from flask import Flask, render_template, redirect
import pymongo
import time
from pprint import pprint
# From the separate python file in this directory, we'll import the code that is used to scrape craigslist
import mission_to_mars

app = Flask(__name__, template_folder="templates")

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_db
collection = db.mars_data

@app.route('/')
def index():
   #results = mongo.db.collection.find_one()
   return "Some data scraped"

# This route will trigger the webscraping, but it will then send us back to the index route to render the results
@app.route("/scrape")
def scrape():

    data_dict = mission_to_mars.scrape()
    collection.insert_one(data_dict)
    
    results = collection.find(data_dict)
    for a in results:
        pprint(a)

    return render_template("index.html", mars_data = data_dict)


if __name__ == "__main__":
    app.run(debug=True)