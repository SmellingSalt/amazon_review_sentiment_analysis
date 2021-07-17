import os
import flask_key_gen
from flask import Flask, render_template, url_for, redirect
from forms import url_input
app = Flask(__name__, template_folder='WebSite')
try:
    app.config['SECRET_KEY']=os.environ['FLASK_KEY']
except KeyError:
    raise KeyError("The Environment Variable FLASK_KEY has not been set. Please set it before proceeding.")

@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST']) #Both these routes are handled by this function
def home():
    form=url_input()
    # asin="B08697MJFD"
    # value=str(asin)+".png"
    # return render_template("result.html",value=value)
    return render_template("index.html",form=form)

@app.route("/url_check", methods=["GET","POST"]) #Both these routes are handled by this function
def result():
    form=url_input()
    items=os.listdir('static')
    for item in items:
        if item.endswith('.png'):
            os.remove(os.path.join("static", item))
    if form.validate_on_submit():
        from wordcloud_generator import wordcloud_gen
        asin=wordcloud_gen(form.url.data)
        return render_template("result.html",value=asin)

#This way it runs in debug mode if the .py script is directly run 
if __name__=='__main__': 
    app.run(debug=False, port=4000,host='0.0.0.0')