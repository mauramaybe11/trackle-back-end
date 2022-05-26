**Author: Maura Webber**
This is the back-end of Trackle.

# Trackle
Trackle is an app that a lets you log in and track your wordle word, the date that you guessed it and the number of guesses that it took you to guess it. 
It will then show you your average number of guesses. Users have the ability to update the word, number of guesses, and date guessed and or delete the wordle log. Users can also see other users wordle logs. 

## App Images 
### APP Landing Page
![App Landing Page](https://i.imgur.com/LvmPgMJ.png)
### Signed in Landing Page
![Signed In Landing Page](https://i.imgur.com/lh3W0bt.png)
### Create Wordle Log Page
![Create Wordle Log Page](https://i.imgur.com/BhptplM.png)

## Important Links

  - [Client repo](https://github.com/mauramaybe11/trackle-client)
  - [API repo](https://github.com/mauramaybe11/trackle-back-end)
  - [Deployed Client](TBH)
  - [Deployed API](TBH)

***
## ERD
![Trackle API ERD](https://i.imgur.com/Q110qH5.png)


## Routes

| HTTP Method   | URL Path     | Action           | CRUD     |
|:--------------|:-------------|:-----------------|----------|
| GET           | /logs       | index or list    | `R`ead   |
| GET           | /logs/`:id` | show or retrieve | `R`ead   |
| POST          | /logs       | create           | `C`reate |
| PATCH         | /logs/`:id` | update           | `U`pdate |
| DELETE        | /logs/`:id` | destroy          | `D`elete |



### Technologies Used

Front End: 
- Javascript
- CSS
- HTML
- SASS
- Visual Studio Code
- AXIOS
- React
- React-Bootstrap
- React-Router-DOM
- Modal

Back End: 
- Django
- Psql

## Installation 

1. Download this Template
2. Move this file into a folder that has a Django Environment set up 
3. Move into the new project with git init
4. create and checkout to a new branch 
5. create a .env file 
6. Run:   pipenv shell to start up your virtual environment
7. Run:   pipenv install django-rest-auth django-cors-headers python-dotenv dj-database-url
8. Create a psql database for your project, Run:  createdb "project_db_name"
9. Add your database name to the .env file 

## Future Versions
-Create other games on the back and front end so that you can log other games like Quordle, Nerdle, Hexle
