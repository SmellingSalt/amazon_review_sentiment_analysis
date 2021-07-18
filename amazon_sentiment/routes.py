#Contains all the routing info.
import os
from flask import  render_template, url_for, redirect
from amazon_sentiment.forms import url_input
from amazon_sentiment.wordcloud_generator import wordcloud_gen

from amazon_sentiment import app
@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST']) #Both these routes are handled by this function
def home():
    form=url_input()
    return render_template("index.html",form=form)

@app.route("/url_check", methods=["GET","POST"]) #Both these routes are handled by this function
def result():
    form=url_input()
    if form.validate_on_submit():
        static_path="amazon_sentiment"+app.static_url_path#url_for('static',filename='')
        items=os.listdir(static_path)
        for item in items:
            if item.endswith('.png'):
                path=static_path+"/"+item
                os.remove(path)        
        asin=wordcloud_gen(form.url.data)
        return render_template("result.html",value=asin)