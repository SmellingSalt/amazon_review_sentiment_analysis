#Only the imports, and secret key generation. Nothing else.
import os
import amazon_sentiment.flask_key_gen
from flask import Flask
app = Flask(__name__, template_folder='WebSite')
app.config['SECRET_KEY']=os.environ['FLASK_KEY'] #This is generated with the second import

from amazon_sentiment import routes