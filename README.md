COOK IT!
Project is for sworn foodies that likes to cook and share their best recipe. Page must be easy to scroll and works
essentially like social network (f.ex Pinterest). Also can suggest 'clean' design and is not overloaded with details.

UX
Web site is for regular people who loves food making. In order them to share they must easily post, edit or like someonelese's recipe.
Chosen helps user to easily find all functions. For example:
Feature 1: allows user to register and log in;
Feature 2: allows register user to post new recipe;
Feature 3: allows register user to edit recipe;
Feature 4: allows user to like by pressing on heart icon;
Feature 5: app could be used on any size device. It's fully responsive;
Feature 6: every recipe got author name by the dish title;
Feature 7: icons next to allergens and extra info are fully customized;
Feature 8: user is allowed to post URL of their dish;
Feature 9: add/edit menu got accordion, so user fills information in short sections;
Feature 10: after log-in nav menu shows user name;
Feature 11: user is allowed to search by type, cuisine, or name;

Features to implement:
- Truncation of cooking instructions;
- Log-in/Register could be placed into modals;
- Using WTForms on Add/Edit forms;
- user could upload photos instead of sending a link;
- Using partials and include the favorite section should show actual dish instead of button;

Technologies used:
- jQuery: used for show-more button in add section;
- Bootstrap and flexbox used to make ir responsive;
- Flask micro-framework used for back-end functions;
- MongoDB - to store information in non relational database;

Deployment:
- PyCharm IDE was used for coding the app and uploading to GitHub;
- Further details are found inside requirements.txt file;
- According to specification of the project - it was uploaded to Heroku;

TESTING:
- Add/Edit functions adds/edits new recipe on the website. Changes can be seen on MongoDB as well. 
Redirects back to home page after submission;
- Delete function is fully working, instance disappears from a screen and MongoDB;
- Upon creation of new user - a new instance appears on MongoDB, and user name top of the page. 
Redirects back to home page after submission;
- Upon log-in user name appears at the top of the screen, next to the recipe that has been posted by user in session. 
Redirects back to home page after submission;
- Like function works. On pressing heart icon the number increases, the change can be seen on MongoDB;
- Search function filters successfully on entering type, dish name or cuisine. Deleted recipies will not be shown;
- User's can only edit/delete only recipies they posted;

Credits:
Would like to thank Miguels Blog https://blog.miguelgrinberg.com/ for helping me out with registration/login function;
Also my mentor Spencer Barriball for helping me out with SEARCH function, TESTING and guiding me through the project with valuable advice;
Images were taken from BBC Foods;
'Favorites' code were amended from stackoverflow