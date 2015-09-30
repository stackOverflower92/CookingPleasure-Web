Istruction to set up COOKING PLEASURE (with sample user):

INSTALLATION:
1- Unzip the archive in the destination folder
2- go into mysql and create the database CookingPleasure :
	create database CookingPleasure;
3- create a user within the database to connect django :
	create user 'developeraccess'@'%' IDENTIFIED BY 'developeraccess';
4- give all privileges on the database to the user :
	grant all privileges on CookingPleasure.* to developeraccess with grant option;
5- import the dump file into the database :
	mysql -u developeraccess -p CookingPleasure < dumpCookingPleasure.sql

START :
positioning within the folder with the terminal :
1- issue the command :
	python manage.py runserver
2- Now you can access the site by opening a browser and enter the address : [ http://127.0.0.1:8000/ ]
3- from home you can reach the application by pressing the button : [ ' go to the app ! ' ]
4- You will be redirected to the login screen where we can create our user
or log on the sample user : [user : user , password : password ] ;
