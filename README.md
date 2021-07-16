# amazon_review_sentiment_analysis

## Setup with VSCode

More information [can be found here.](https://code.visualstudio.com/docs/remote/create-dev-container#_set-up-a-folder-to-run-in-a-container) 

### Dockerfile

The Dockerfile installs a tensorflow image with some useful packages and creates a user `nonrootuser` that will be the default user to work inside the container.

Build the dockerfile with

``` bash
docker build . -t tensorflow
```

Once the container is built, run it with

```bash
docker run -it --name amazon_sentiment_analysis -v $PWD:/home/nonrootuser/codes/ --gpus all tensorflow
```

### VSCode

* Install this extension

  ```text
  Id: ms-azuretools.vscode-docker
  Description: Makes it easy to create, manage, and debug containerized applications.
  Version: 1.14.0
  Publisher: Microsoft
  VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
  ```

* Click the extension on the bar on the left.

* Under the containers tab, right click `tensorflow`-->`Attach Visual Studio Code`

The container terminal can be exited by clicking the button on the bottom left, `Container tensorflow..` -->`Close Remote Connection`



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