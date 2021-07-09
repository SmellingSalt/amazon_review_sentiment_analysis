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