# Foodstar - Recipe App

Foodstar is an online recipe app made for people with a crawing to cook and eat. Here we can share our passion for food both by adding our favourite recipes but also by commenting on each post/recipe.

![Looking good on different devices](https://res.cloudinary.com/cmanzanada84/image/upload/v1657108242/Readme/HeaderFoodstar_xewzmc.jpg)

## Features 

### Existing Features

- __Header__

    - The Header displays the apps name: Foodstar and also Home, Register, login and if user is logged in it displays Add recipe and logout.

    - The Logo has added neon effects so it looks like it's glowing and flickers a little.

![Header](https://res.cloudinary.com/cmanzanada84/image/upload/v1657108242/Readme/HeaderFoodstar_xewzmc.jpg)
![Header](https://res.cloudinary.com/cmanzanada84/image/upload/v1657110026/Readme/header_login_s83iqd.jpg)

- __The Foodstar options__

    - A visitor can easily browse through recipes and should they wish comment or even add recipes, there is a Register button that when hovered over shifts color.

    - When a user has created an account, they can create/edit/delete recipes of their own making. They can Like/Unlike recipes and they can comment on recipes.


![Foodstar options](https://res.cloudinary.com/cmanzanada84/image/upload/v1657112669/Readme/Site_pagination_gntycx.jpg)
![Foodstar options](https://res.cloudinary.com/cmanzanada84/image/upload/v1657109819/Readme/Like_and_comment_frg5v7.jpg)

- __Foodstar features__

    - User can register an account

![Register an Account](https://res.cloudinary.com/cmanzanada84/image/upload/v1657113324/Readme/register_account_cqvs1v.jpg)

- If a user exists with same name or email, user is notified, same goes for if the password is too common or too short

![Account registration](https://res.cloudinary.com/cmanzanada84/image/upload/v1657113460/Readme/registration_messages_fbergk.jpg)

- A pop-up message tells the user sign up was successful

![Successfull signup](https://res.cloudinary.com/cmanzanada84/image/upload/v1657114258/Readme/popup_signin_djon7b.jpg)

![Registered user can create recipes](https://res.cloudinary.com/cmanzanada84/image/upload/v1657114868/Readme/New_recipe_form_px5pfu.jpg)

![User can edit/delete their own recipes](https://res.cloudinary.com/cmanzanada84/image/upload/v1657115182/Readme/editdelete_bf28by.jpg)

- __The Footer__ 

    - Contains Social media icons.

![Footer](https://res.cloudinary.com/cmanzanada84/image/upload/v1657140667/Readme/social_media_icons_samtw4.jpg)



### Features Left to Implement

- A future idea to implement could be so that a user can see and manage all their recipes in one place.

- An idea for the future would be to implement a search function so users/visitors can search for specific meals.

- Another future idea could be to create a profile page for each user so that they can share more information about themselves.

### Manual Testing 

## Navigation Bar

- Should be visible on every page of the site and when using smaller screen devices the navigation bar should toggle for a better user experience.

- Checked so that the navigation bar was visible on ever page on the site and viewed the site on a smaller screen device to check so that the nav bar toggles correctly. It does and it works as intended.

## Logo

- When clicking on the logo it should take the user back to the home page.

- I clicked on the logo from all of the different pages and it brings user back to home page.

## Home Link

- When clicked upon the user should be redirected to home page.
- Clicked on it as a logged in user and as a logged out user, it brings you back to home page no matter what.

## Add Recipe Link

- Only visible to logged in users and when clicked upon should take you to the Create Recipe Form

- Checked as a visitor and link not visible until I created an account. When account is created its shows and directs you to the Create Recipe Form

## Register Link

- If a user is not logged in or does not have an account, the Register button will be visisble. When clicked upon it should bring the user to the Sign Up form.

- Visited the site both as a logged in user and not logged in user, Register button only visible when user is not logged in. When pressed upon it takes you to the Sign up form as intended.

## Login Link

- If a user is not logged in the Login link should be visible. When clicked on it shoiuld take the user to the Sign In form.

- I entered the site as a not logged in user and clicked on it, redirects you to the Sign In form and when signed in it now displays Logout instead.

## Logout

- If a user is logged in to the site, Logout should be visible and when clicked on it should redirect to log-out page. User is then asked to confirm that they wish to log out.

- Logged in to the site and clicked on log out, it redirects you to the log-out page and asks you to confirm that you wish to sign out.

## Recipe List

- When visiting the site a list of recipes should be visible and a brief introduction to each recipe should be visible as well.

- Visited the site and all published recipes displays along with title of each recipe and a brief intro to each.

## Site Pagination

- The site has a maximum number of 6 recipes per page to make it more user friendly and when a seventh recipe is added the button Next should appear and take user to next page.

- Added 7 recipes and checked so that the Next button appears, it did and it brings the user to the next page when clicked on.

## View Recipe

- A user should after clicking on a recipe to view be redirected to that specific recipes details. Here the user should be able to see all the information regarding that specific recipe. Here a logged in user should also be able to Like/Unlike or comment on the recipe.

- Visited the site first as a not logged-in user and all the information added by the "Chef" is visible, I couldn't Like or comment on the recipe since I was not logged in. I logged in and was then able to both Like/Unlike and also to comment on the recipe.

## Approve and Delete comments

- When a logged in user comments on a recipe this comment should have to be approved by Admin before its published.

- I logged in to the site as a regular user, left a comment on a recipe, a message displayed that my comment is awaiting approval. I logged in as Admin and approved the comment, it the displayed under the recipe. I also later deleted it without issues.

## Manage Recipes

- As a logged in user I should be able to edit or delete recipes I have added.

- I logged in as a regular user and created a recipe, I then without issues edited it and posted it again, after a while I deleted it and this also worked just fine.


## Automated Testing

### Code Validation

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML and CSS code used. The [PEP8 Python Validator](http://pep8online.com/) was used to validate the Python code. 

## Results:

## HTML Validation - all pages clear

The images uploaded to Cloudinary had no alt text and it took some time before I found how to add it. Each image has an alt but for some reason W3.org insists they dont. I have attached an image below to show that they do have alt attributes. This is the only issue raised.

![Image Alt](https://res.cloudinary.com/cmanzanada84/image/upload/v1657147452/Image_Alt_vuztkr.jpg)

## CCS Validation - page clear 

## Python Validation - all pages clear

Files tested: 
*foodstar*
- asgi.py
- settings.py
- urls.py
- wsgi.py

*recipes*
- admin.py
- apps.py
- forms.py
- models.py
- urls.py
- views.py

 I found errors when validating the the settings.py file where certain urls was to long, the character limit on a single line was over the limit. This error  I can ignore as there is no way to reduce the url length to conform to the character limit per line and its built-in code.


###  Bugs
- I hate coding. When I was testing my python code via Pep8, copy pasting between my site and theirs, I git commited and just like that everything stopped working, I read up on how to Git reset cause I thought it was something I had done. After a long time I remembered I had received an email from Heroku... They had perfomed maintenance on my Database so I learned that I had to update my DATABASE_URL

- I have been trying hard to add Summernote to Content section of the Create Recipe form without succes I'm sad to say, due to lack of time I had to give it up.

As far as I know, there are no unfixed bugs. 

## Deployment
 
- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - Go to Github and choose the correct repository, in this case, it was ROCK-PAPER-SCISSORS
  - Then go to the SETTINGS tab
  - Then scroll down to where it says PAGES click on it
  - Here you go to SOURCE then select the MAIN or MASTER branch and press SAVE

The live link can be found here - https://deagustinchristian.github.io/Rock-Paper-Scissors/ 


## Credits 


### Content 

- All text on the website was made up by me. I did use Grammarly on this ReadMe file just so the grammar and spelling was as correct as it could be.

- I have used different sources to learn and understand the coding and the concepts of Django/Python, I studied the following websites and how they did it.

    - I reused alot of code from the Code Institute material

    - This website was really good to get a sense of how to create a website like this one and how Django forms in general work
        - (https://engineertodeveloper.com/getting-started-with-django-forms-create-a-recipe-app/)
    
    - I watched this video on how to restrict who can make posts
        - (https://www.youtube.com/watch?v=TAH01Iy5AuE)

    - I read this material on how to Build and handle Post requests in Django
        - (https://realpython.com/django-social-post-3/)

    - Learned more about Python Import via this site again
        - (https://realpython.com/python-import/)

    - This site was great on getting an idea on how to build a site that allows user generated posts
        - (http://www.learningaboutelectronics.com/Articles/How-to-create-a-website-that-allows-for-user-generated-posts-with-Python-in-Django.php)


### Media

- The images used for the recipes are all taken by except for the placeholder image, that one I got from Adobe Stock where I am a paying member and allowed to use 10 images per month.
