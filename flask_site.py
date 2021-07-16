from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder='WebSite')

@app.route("/")
@app.route("/home") #Both these routes are handled by this function
def home():
    return render_template("index.html")


#This way it runs in debug mode if the .py script is directly run 
if __name__=='__main__': 
    app.run(debug=True)