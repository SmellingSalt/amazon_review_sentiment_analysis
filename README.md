# amazon_review_sentiment_analysis
If you want to run the server, do it with the following command after cloning or downloading this repository.
```bash
docker-compose up
```
The host port `4001` is mapped to the container's `4000` so if you want to access the website from another device in the same network, use the following address 
```
<YOUR_HOST_IP_ADDRESS>:40001
```
## Setup with VSCode

More information [can be found here.](https://code.visualstudio.com/docs/remote/create-dev-container#_set-up-a-folder-to-run-in-a-container) 

### Dockerfile/DockerCompose

The docker container built is from the default ubuntu image. It creates a user named `nonroot` that runs the server within the container itself, with the commands in the `docker-compose.yaml` file.



# FLASK
Running 
```bash
export FLASK_APP = flask_site.py
```
will export the name of the main flask site rendering python file o the environment variable `FLASK_APP` which will enable you to run a server with

```bash
flask run
```
## Rendering Webpages.
* You have to import from the flask module `render_template`.
* The initialisation of the app should have the location of where the `html` templates are in,. (Flask defaults to looking for a folder named `templates` in your root directory if this is not mentioned)
  ```python
    app = Flask(__name__, template_folder='WebSite')
  ```
* Standard `jinja` codes can be written to aid the HTML creation process.
* Content Delivery Networks (CDNs) can be used to create the css/javascript styles for the HTML as well. There is a bootstrap library for flask that helps with this. It is not used here.
* To Include your own `css`, import `url_for` from flask. Then add the following line to your HTML base document.
  ```html
   <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='index.css')}}">  
  ```
  * Note that this seems to work only if the `.css` files are present in the folder `static/*css`. This does not seem to work for nested directories. Needs to be investigated.

## FORMS
Instead of making the form directly in the HTML document, Flask can aid with the creation of it with the help of the `flask_wtf` package.
Create a `forms.py` file and add the information of the form that you want to create in it. Each form is a class, having various attributes.
Look at the `forms.py` here for more information about it.

### Form authentication.
In the main `flask_site.py`, add a secret key for the app with 
``` python
app = Flask(__name__, template_folder='WebSite')
app.config['SECRET_KEY']='<SecretKeyHere>'

```
#### Generation of a secret key
It can be done with the following python script
```python
import secrets
print(secrets.token_hex(16)) #16 byte length
```
### Form rendering
Import the created class into `flask_site.py`, as done in the file in the repository.
The next step is to add this class to the HTML form. Pass an instance of the created form class to whichever HTML doc has to render the form, in its app route.
```python

```
In the HTML tag, you can access the form fields by.
```jinja
{{form.url(class_="form_style")}}
```