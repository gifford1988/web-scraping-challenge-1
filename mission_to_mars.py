#IMPORT DEPENDENCIES
from pymongo import MongoClient
from flask import Flask, render_template
from scrape import scrape

# PyMongo Setup
client = MongoClient()
db = client['MarsDB']
collection = db['ScrapedData']

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def displaydata():
    featured_image = 'https://jpl.nasa.gov/spaceimages/images/mediumsize/PIA19871_ip.jpg'
    return render_template("index.html", featured_image=featured_image)
    
@app.route("/scrape")
def flaskscrape():
    scrapings = scrape()
    posts = db.posts
    post_id = posts.insert_one(scrapings).inserted_id

if __name__ == '__main__':
    app.run(debug=True)