# README #

### Basic setup ###
#### Python dependencies and database setup
 
 In the terminal (with your python virtualenv activated):
 
```
#!python
pip install -r requirements/dev.txt 
python manage.py migrate
python manage.py createsuperuser
fab initial_data


```

Next copy the file *collective_beat/settings/local.example.py* and place it in the same directory under name *"local.py"*.

#### Html/css/js dependencies

```
#!bash

npm -g install bower (Node should be installed)
bower install (withing this directory)
```
