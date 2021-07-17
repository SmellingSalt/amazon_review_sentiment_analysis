#This way it runs in debug mode if the .py script is directly run 
from amazon_sentiment import app
if __name__=='__main__':
    app.run(debug=False, port=4000, host="0.0.0.0")