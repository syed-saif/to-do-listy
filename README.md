# To-Do Listy!
A simple to-do list application made with Python-Django and Bootstrap4 (and a wee-bit of JS and jQuery).

## Installation
To use this app in your machine, do the following:

* Clone this repository:
```bash
git clone https://github.com/syed-saif/to-do-listy.git
```
* Highly recommend: use a [virtual environment](https://pypi.org/project/virtualenv/ "Virtualenv"), to keep this repo's installations separate. [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/ "Virtualenvwrapper") is a good wrapper for this. Install a venv for python 3.7 or above:
```bash
mkvirtualenv -p /path/to/python<=3.7 todo
```
* After setting up the virtualenv, `cd` to the directory where you cloned this repo. Then do:
```bash
pip install -r requirements.txt
```
* Then run the Django dev server, from the root directory of this repo:
```bash
python3 manage.py runserver
```
* Now the app should be accessible through the [localhost](http://localhost:8000)


## P.S
This was my first Django app (:P). This project was done in 2 days or so, as I quickly wanted to go through all that Django has to offer. And I have to admit, using Django saved a **ton** of time, as it already had the common bells and whistles built in. The idea of an ORM is the best part as, we don't have to write those SQL queries. Overall this was a fun project, as I learned Django and got to use Bootstrap properly this time.
Do star the repo :P 
