#IMPORT DEPENDENCIES
import pymongo
from flask import Flask, render_template
from scrape import scrape

# PyMongo Setup
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.MarsDB

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def displaydata():
    data = list(db.posts.find())[-1]
    return render_template("index.html", data=data)

    
@app.route("/scrape")
def flaskscrape():
    scrapings = scrape()
    #posts = db.posts
    post_id = db.posts.insert_one(scrapings).inserted_id
    return '<meta http-equiv="Refresh" content="3; url=http://127.0.0.1:5000/" /><h1>Scraping complete.</h1>'

if __name__ == '__main__':
    app.run(debug=True)