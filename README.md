## Learn-Git

Learning Git and Github is hard!  This repo contains a web application that helps students learn how to use these important development tools.

## Developers

To develop locally:

* Create a virtual environment and install required libraries

  ```
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
  
* Use the `./uplocal` script to launch gunicorn on port 8000


## Deploy in Production

The following steps should be completed as root (run `sudo -i` first):

* Clone the repo in `/`
* Create a virtual environment named `.venv` in the `/learn-git` folder

  ```
  python3 -m venv .venv
  .venv/bin/pip install -r requirements.txt
  ```

* Copy the service file and enable/start the server

  ```
  cp learn-git.service /etc/systemd/system
  systemctl enable learn-git
  systemctl start learn-git
  ```
  
## Redeploy Changes

The script `./redeploy` contains the steps to redeploy changes from Github:

* Stop the server
* Pull from Github
* Start the server

Goto the `/learn-git` folder and run `sudo ./redeploy`.

  