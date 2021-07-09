# amazon_review_sentiment_analysis

## Setup with VSCode

More information [can be found here.](https://code.visualstudio.com/docs/remote/create-dev-container#_set-up-a-folder-to-run-in-a-container) 

The Dockerfile installs a tensorflow image with some useful packages and creates a user `nonrootuser` that will be the default user to work inside the container.

### devcontainer.json

The folder `.devcontainer` has the required settings to allow for this workspace to be mounted onto the container. 

This file allows for VSCode to be mounted onto the container for developments and puts 