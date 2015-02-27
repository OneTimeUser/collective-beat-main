# README #

### Basic setup ###
* in the terminal: 
```
#!python
pip install -r requirements/dev.txt 
python manage.py migrate
python manage.py createsuperuser


```

* copy the file *collective_beat/settings/local.example.py* and place it in the same directory under name *"local.py"*