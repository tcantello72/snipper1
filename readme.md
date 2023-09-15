# Toby's API

This is my first attempt at a true API. This use Python back-end with Flask-Marshmallow, Flask-SQLAlchemy and swagger.

## Installation

From the command prompt run.
```bash
python -V
```
An example of what you will see if you have Python installed already. Need at least Python 3.0 installed.
```bash
Python 3.11.3
```
If you need to install Python you can go to [www.python.org](http://www.python.org) and install the latest version. Make sure to click the Add to PATH when asked.

Clone the repo.

Open the repo in your IDE. The IDE that I used was Visual Studio Code.

Open a terminal to the command prompt and make sure you are in the root folder for the project.

Now we need to set-up the virtual environment using the following three commands. 
```bash
C:\(path to the root folder of the project)>pip install virtualenv

C:\(path to the root folder of the project)>py -m venv env

C:\(path to the root folder of the project)>.\env\Scripts\activate
```

If the virtual environment was set-up correctly who should see the following:
```bash
(env) C:\(path to the root folder of the project)>
``` 
Now if we need to install the required packages. I have included all the required packages in the requirements.txt file. We will use this file to install the packages at one time.
```bash
(env) C:\(path to the root folder of the project)>pip install -r requirements.txt
``` 
After all the packages install you can run start the app on the local server with the following command
```bash
(env) C:\(path to the root folder of the project)>py app.py
``` 
After the server starts you will see the following:
```bash
(env) C:\(path to the root folder of the project)>py app.py
 * Serving Flask app 'config'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.28.137.26:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 103-794-599
```
Now open your browser and type in address to the local server [http://127.0.0.1:5000](http://127.0.0.1:5000). your server address maybe different. The standard for Flask is Http://127.0.0.1:5000

This is what you should see:
