# App4Notes
#### Live-Link


### Description:
A Django Notes application which essentially saves notes and retrieves them for a user at a go.

### Authors
* Martin Mandina

### Installation Technologies Required:
* Django
* Python
* Virtual environment

### SETUP & INSTALLATION INSTRUCTIONS:
 * Ensure that Python3.6 is installed.
 * Open Terminal.
 * Change working directory to preferred location where you want to clone directory.
 * Create a virtual environment on your working directory.
 * Switch to the virtual environment by command ```source <your virtual name>/bin/activate``` on the terminal. 
 * Install django and depedencies listed in the ```requirements.txt```
  * Create a .env file and add own credentials where appropriate

```
SECRET_KEY = '<Secret_key>'
DB_NAME = 'ProjectApp'
DB_USER = '<Username>'
DB_PASSWORD = '<password>'
DEBUG=False
DB_HOST='127.0.0.1'
MODE='dev' 
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='<email to send confirmation message>'
EMAIL_HOST_PASSWORD='<email password>'
```
* Lastly open the application on your browser by running python3 manage.py runserver

#### TECHNOLOGIES:
* Python3
* postgresql
* Django
* Bootstrap3
* CSS
* Heroku

#### DEPENDECIES
* gunicorn

### CONTACT INFORMATION
#### Martin Mandina
* martinsmandina@gmail.com

#### License  & Copyright information
Copyright (c) 2020 **Martin Mandina,

[MIT License](./LICENSE)





  

