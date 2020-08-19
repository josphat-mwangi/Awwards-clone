##  Awards

## Description 
The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

## User Stories
1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page


## Setup/Installation Requirements
1. Internet access
2. $ git clone : https://github.com/josphat-mwangi/Awwards-clone.git
3. $ cd Awards
4. $ python3.6 -m venv virtual (install virtual environment)
5. $ source virtual/bin/activate
6. $ python3.6 -m pip install -r requirements.txt (install all dependencies)
7. Run "python3 manage.py runserver" from the terminal


## Technologies used
. Python3.6
. django framework
. Bootstrap
. PostgreSQL


### BDD Specifications Table
|        User Requirements                 |           Input                           |           Output                         |
|------------------------------------------|-------------------------------------------|------------------------------------------|
| Sign Up/Login                            | To create a new account, click on the sign| If login is successful, the user is      |
|                                          | up link and fill in the form details. To  | redirected to the home page              |
|                                          | login, fill in the details                |                                          |
| Add a new project                        | Click on the submit new project tab on the| You will be navigated to a page which    |
|                                          | navbar and submit the project details     | has a form to submit the project         |
| Review a project                         | Click on the Review button                | You will be navigated to a page where you|
|                                          |                                           | can post your review                     |
| Create a profile                         | Click on the profile tab then Edit Profile| A new profile for the user will be       |
|                                          | button                                    | created                                  |
| Search for a project                     | Enter the project's name into the search  | You will be redirected to a page with all||                                          | bar in the navbar                         | results matching your search. You can    |
|                                          |                                           | then click on the project you want       |
| Log out                                  | Click on the Account button and select    | You will be logged out                   ||                                          | log out                                   |                                          |
