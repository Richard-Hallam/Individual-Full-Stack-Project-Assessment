# User Experience 
## Target User
The target use is anyone who wants to have a single place to keep track of their purchases and incomes.
## Goal
Make an easy to use trasaction tracking app.
## User Stories
### User Story: Create Account
As a user I want to be able to make an account so only  I can access my stored information
### User Story: Log In

**As an existing user,** I want to log in with my credentials, So that I can access my data.

### User Story Add Transaction

**As a user,** I want to add new transactions to the app, So that I can keep track of my spending.

### User Story: View transactions

**As a user,** I want to view a list of my transactions, So that I can review my spending history.

### User Story: Delete transactions

**As a user,** I want to delete a transaction from the app, So that I can correct any mistakes in my records.

### User Story: Update Transaction

**As a user,** I want to update existing transactions, So that I can modify incorrect information or change details.


# Features
## Database Structure
![erd](https://github.com/user-attachments/assets/547ecb80-9220-4f12-a95d-3967fa00cc9a)
# Design
## Wireframes
### Login page
![Login page](https://github.com/user-attachments/assets/44ab6aa0-1945-4176-8a98-b4ed1b9771bc)
### Home page
![Home page](https://github.com/user-attachments/assets/355546b4-a9cc-4097-833a-fafcb2774f09)
### Accounts page
![Accounts page](https://github.com/user-attachments/assets/936ec059-271a-4da5-9da1-877a11e0a81e)
### Add transaction page
![modal](https://github.com/user-attachments/assets/7b8ff477-192f-4a30-98be-299a4554fbc1)
## Colour Scheme
![colourScheme](https://github.com/user-attachments/assets/4e331c55-fa85-4867-8831-345ef8f6c6d9)
I have chosen the above colour scheme which will allow for good text contrast and a consistent look throughout the application.

## Fonts
I have chosen the lato font because of its readability and simplicity.
https://fonts.google.com/specimen/Lato

# Technologies
Django

HTML

CSS

Bootstrap 5

Crispy forms 2.0

asgiref


dj-database-url


django-allauth


psycopg2






# Testing and validation

## Manual testing
At the end of the development process I went through every available url while both logged in and logged out to ensure they behaved as expected.
I also added, edited and deleted multiple transactions to ensure they behave as expected.

### Manual Tests
#### register account
    Registration of account functions correctly 
#### login to account
    Login functions correctly
#### Logout of account
    user is able to logout
    The user does not have their data displayed when they are logged out.
#### Navigate to transactions page
    Navigation functions correctly
#### Page shows a list of transactions
    Transaction list is shown
    Transaction list is correct for the data in the database
#### Create a new transaction
    New transaction creation functions correctly
#### Account balance displays correct ammount when transaction is added 
    correct balance displays for income 
    correct balance displays for expense
#### Edit a transaction
    Correct balance displays for income
    correct balance displays for expense
#### Account balance displays correct ammount when transaction is edited
    correct balance displays for income 
    correct balance displays for expense
#### Transactions can be deleted
    Transaction deletion functions correctly
#### Account balance displays correct ammount when transaction is deleted
    correct balance displays for income 
    correct balance displays for expense

## HTML
Html was validated using the w3 markup validation service https://validator.w3.org/nu/.
This did throw up errors from the parts of the html that were for django specifically but as the validator does not cover django they could be ignored.
![homehtmlvalidator](https://github.com/user-attachments/assets/d83e797f-cf86-4f4b-ae89-d49afc6a2aac)

## CSS
CSS was validated using jigsaw https://jigsaw.w3.org/css-validator/

## Python
Python was validated using the CI Python Linter https://pep8ci.herokuapp.com/#
discovered errors were corrected
![transactionsModels](https://github.com/user-attachments/assets/1334b087-b8f0-4978-ab2d-83de355fc357)
![home_views](https://github.com/user-attachments/assets/39b63d73-50f6-46e5-ac01-5f1d89425bfe)

## User stories 

As a user I want to be able to make an account so only  I can access my stored information **PASS**


As an existing user, I want to log in with my credentials, So that I can access my data.**PASS**



As a user, I want to add new transactions to the app, So that I can keep track of my spending.**PASS**



As a user, I want to view a list of my transactions, So that I can review my spending history.**PASS**



As a user, I want to delete a transaction from the app, So that I can correct any mistakes in my records.**PASS**



As a user, I want to update existing transactions, So that I can modify incorrect information or change details.**PASS**


# Agile
During the development aglie methodology was used throughout. The project used project board to track tasks that were planned, in progress and completed. These tasks were designed to meet the requirements of the user stories to ensure the project functions as intended.


# Deployment
The app was deployed on heroku using a postgres database provided by the code institute.
