# DjangoEcommerceApi

#### created
* initialize repository



#### update 1
* make a basic API project for showing list of products by rest framework 



#### update 2
* primary comments was added.
* auto slug feature was added (signals.py).
* change database columns. models.py, serializers.py files was edited.
* signals.py file was created.



#### update 3
* fix some bugs in models.py and serializers.py files.
* switch database from sqlite to postgresql.
* hidden important and personal information in settings.py file, .env-sample file was added.
* url router and viewset class. urls.py and views.py files was edited.



#### update 4
* add some tests to tests.py file.
* models.py, urls.py (config), settings.py files was edited.
* add create and retrieve Api view in views.py file.



#### update 5
* settings.py --> Add 'django_cleanup.apps.CleanupConfig' to INSTALLED_APPS.
* admin.py --> Register 'Brand' and 'Category' models.
* models.py --> Add 'Brand' and 'Category' models. Change modeling system (better modeling).
* serializers.py --> Add 'create' method to make new object for 'Brand' and 'Category' models.
* signals.py --> Update slug generator (better slug generator).
* views.py --> Add feature to download images from received urls and set that for current object (ImageField get image just not url).