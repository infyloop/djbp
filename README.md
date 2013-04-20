A simple django note taking app. Written for a demo talk, with couple of best practices kept in mind. 


[![Build Status](https://travis-ci.org/fRuiApps/djbp.png?branch=master)](https://travis-ci.org/fRuiApps/djbp)

You can get started with cloning the repo. 

To install with a test environment - `pip install -r requirements/test.txt`

To install for a local setup - `pip install -r requirements/local.txt`


run the tests - `pyhton manage.py test noteapp --settings=djnotes.settings.test`

run the shell - `python manage.py test noteapp --settings=djnotes.settings.local`

running schemamigration - `pmp schemamigration noteapp --auto --settings=djnotes.settings.local`

run the dev server - `python manage.py test noteapp --settings=djnotes.settings.local`


TODO : 

0. Add docs

1. Add forms, and test for forms.
