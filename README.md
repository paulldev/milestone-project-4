# Sandnes Biljard

### Live website (Heroku): https://ci-milestoneproject-4.herokuapp.com/

### Repository: https://github.com/paulldev/milestone-project-4

## Introduction

Sandnes Biljard is a web app which for pool halls that also sell alcohol.
Due to Covid-19, restrictions must be made to promote social distancing. Since the bar is an area where people can gather, this web app allows customers to order and pay for drinks from the pool table they are playing at. They simply order from their phone and the staff will deliver their drinks to them.

All code produced is my own. Other code taken from or referenced, is from course material and bootstrap documentation. Any other sources I used as a reference are included as a link in my code. All solutions are based on course material, official documentation, and lots of trial and error.

## UX

### Strategy Plane

> What are you aiming to achieve and for whom?

I want my web app allow pool halls to operate their business while complying with social distancing rules.
I also want user to be able to leave anonymous feedback about their experience. This gathered information can be used by the pool hall to improve their services.

### Scope Plane

> Which features (based on information from the strategy plane) do you want to include in your design?

I want customers to be able to:
- order and pay for their drinks online and have them delivered to their pool table.
- view the list of drinks for sale, add them to their shopping cart, and securely pay through the web app.

I want staff to be able to:
- receive orders and fullfill them by viewing orders in the admin section.
- to be able to receive feedback about the condition of the pool tables, and the service they provided to customers. This information can then be used to repair tables or improve other services.

### Structure Plane

> How is the information structured and how is it logically grouped.

The data will be stored in a PostgreSQL database with the following structure:
**1. Category (type of drink):**
- name (hot drinks, non alcoholic, wine, spirits, beer)
- friendly name

**2. Product (drinks for sale):**
- category (see Catories above)
- name of drink
- alcoholic
- description
- price
- image url
- image

**3. Checkout:**
- Order (full order)
- OrderLineItem (each item order)

**3. Feedback:**
- PoolTable (customer rating of table condition)
- Review (customer reviews)


### Skeleton Plane

> How will our information be represented, and how will the user navigate to the information and features?

The information is represented as 3 web pages:
- **Home:**
The home page will have a navigation bar which links to:
- The home page
- The feedback page
- The account login/logout
- The shopping cart page

The body of the home page will have a button to order drinks (sends you to the product page).

### Surface Plane

> What will our finished product look like?

The finished product will be a responsive web app which allows users to:
- view products
- order products
- securely pay for products with credit card
- give anonymous feedback to the pool hall
- view products before progressing to Checkout
- view a confirmation receipt after payment

## Features
- Accounts allow users to login to the web app to gain access to all the features.
- Badge allows customers to see how many products have been added to their shopping cart
- Shopping cart displays the total cost of purchases as the user is adding products to buy

## Future features to implement

Since this web app is a minimal viable product, there were several features which could be added in the future:
- allow users to see their order history, not just a recept after ordering.
- change feedback form items to drop-down lists (for table number)
- change feedback form items to checkboxes (for ratings, etc)
- allow customers to remove/edit items in their shopping cart
- allow customers to pay with other options, not just credit card
- implement toasts for additional feedback for the user

## Technologies used

| Name                   | Type      | Site url                                                       | Why use it?                                                                           |
| :--------------------- | :-------- | :------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| HTML5                  | Language  | https://www.w3.org/TR/html52/                                  | To structure the website                                                              |
| CSS3                   | Language  | https://www.w3.org/Style/CSS/Overview.en.html                  | To style and layout the website                                                       |
| Javascript             | Language  | https://developer.mozilla.org/en-US/docs/Web/JavaScript        | To create responsive, interactive elements for web pages                              |
| jQuery                 | Library   | https://jquery.com/                                            | To make DOM traversal, manipulation, event handling, animation, and Ajax much simpler |
| Croppola               | Tool      | https://croppola.com/                                          | To crop my images                                                                     |
| Reduce Images          | Tool      | https://www.reduceimages.com/                                  | To reduce the size of my images                                                       |
| PostgreSQL | Heroku 3rd party add-on      | https://www.postgresql.org/                               | To allow a PostgreSQL database to be used.                                                    |
| Heroku | web hosting      | https://www.heroku.com/                               | To allow a hosting of web app.                                                    |
| Python | Language      | https://www.python.org/                               | To allow a server side coding.                                                    |
| Django | Framework      | https://www.djangoproject.com/                               | To allow a server side coding with extra features built in.                                                    |

## Testing

**Manual testing was recorded in the following table:**
From inside **DevTools > Sources > Watch**, we add each variable to be tested as we run the app.

| Description              | Tests                          | Results  |
| :----------------------- | :----------------------------- | :------- |
|Click order drinks|Do drinks display|Pass|
|Add drink to cart|Does price total increment|Pass|
|Add drink to cart|Does bage icon increment total increment|Pass|
|Click shopping cart|Do ordered items appear with correct values|Pass|
|Click secure checkout|Are you taken to the checkout|Pass|
|Click secure checkout|Do products and prices appear correctly|Pass|
|Click complate order|Is receipt correct|Pass|
|Click complate order|Is payment correctly processed on stripe website|Pass|
|Click complate order|Does payment work for cards with and without need for authentication|Pass|
|Click rate us|Does feedback table display correct|Pass|
|Click rate us|Does user get redirected to feedback_received page|Pass|
|Navbar links|Do they open the correct page|Pass|


## Deployment

All development was done using Gitpod as the IDE. Regular commits were made, which were then pushed to GitHub.
When working on certain features, a new branch was created, which was then merged with the master branch after it was tested to be working.

The project is hosted on **Heroku** at the following url: https://ci-milestoneproject-4.herokuapp.com/
The project **repository** is located at the following url: https://github.com/paulldev/milestone-project-4

### Deployment to Heroku:
- Create a repository using the template from https://github.com/Code-Institute-Org/gitpod-full-template
- Install Django framework: `pip3 install django`
- Create project in current directory: `django-admin startproject sandnes_biljard .`
- Test installation was successful: `python3 manage.py runserver`

Migrations are performed after changed/additions to our models:
- Make migrations: `python3 manage.py makemigrations`
- Perform migrations: `python3 manage.py migrate`

- Create super user: `python3 manage.py createsuperuser`
- Install allauth: `pip3 install django-allauth`
- Update settings.py and urls.py with information from https://django-allauth.readthedocs.io/en/latest/installation.html
- Create requirements.txt file: pip3 freeze > requirements.txt (this will be done each time a new package is installed)
- Create app: `python3 manage.py startapp home` (this is used when creating our other apps)

For security, environment variables were used for sensitive information throughout the project.

Deploy to heroku:
- Create a new app in heroku and add a Postgres database (free plan).
- From Heroku website (Deploy tab), link our Github with Heroku.

To use postgres:
- `pip3 install dj_database_url`
- `pip3 install psycopg2-binary`
- Install gunicorn: `pip3 install gunicorn`
- Create Procfile in root directory 

Connect Django to AWS:
- `pip3 install boto3`
- `pip3 install django-storages`

## Credits

### Media

All images were taken from the royalty free section of https://pixabay.com/

## Acknowledgements

Special thanks to my mentor, Aaron Sinnott. I appreciated his insight, advice, and his time.