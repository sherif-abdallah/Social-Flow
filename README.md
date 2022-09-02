# Flask Blog
A blog app with many features such as - View Blogs written by community, Write your own blogs by creating an account, Update your profile, Upload Profile Picture, Password reset feature


## Table of Content
- [Flask Blog](#flask-blog)
  * [Tools](#tools)
  * [How to run](#how-to-run)
  * [URL](#URL)
  * [Author](#author)

## Tools
1. Python
2. Flask
3. SQLAlchemy
4. CSS
5. JavaScript
6. Bootstrap

## How to run
* Enter the directory where the script is located then type the following to the console
```sh
$ git clone https://github.com/sherif-abdallah/flask-blog flask-blog
```
* Install Python 3.8 venv, pip and compiler

```sh
$ sudo apt-get install python3.8 python3.8-venv python3-venv
```

* Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m venv venv
$ source venv/bin/activate
```

* Then install the dependencies:

```sh
(venv)$ cd flask-blog
(venv)$ python -m pip install --upgrade pip
(venv)$ python -m pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

* Finally run The Blog Server
```sh
(venv)$ python run.py
```
* And navigate to `http://127.0.0.1:8000`.


## URL
* You can also navigate to the main website without needing to install python, you can navigate it from [here](http://flaskblog.pythonanywhere.com/)
## Author
[Sherif Abdullah](https://github.com/sherif-abdallah)
