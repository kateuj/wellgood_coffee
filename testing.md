# WellGood Coffee Testing

![Screen mock-ups of WellGood Coffee website](media/readme-images/screen-mock-up.png)

[View the live project here.](https://wellgood-coffee-f56fcdb787d6.herokuapp.com/)

As with any project, I have been rigorously testing throughout the development process of this web application. I have documented my testing strategy that I planned before I started developing, as well as main bugs that arose whilst developing and how I approached fixing them. I have also tested my web app on different devices and asked family and friends to use and give feedback as to how to improve user experience and inform me of any bugs spotted during use.

With the scale of this project in the grand scheme of things being quite small, automated testing with softwares like Jest or Pytest, for Javascript and Python respectively in this instance it has not been necessary, but I undestand with larger projects with more extensive functions, that this would be useful and essential. I am keen to use Jest and Pytest in future larger projects.

I have applied what I have learned about Test Driven Development into my project and documented some examples of where I have used it in this file.

I have used a mixture of manual and automated testing while developing, both of which play a key role in forming a web application that works correctly and consistently. Automated testing can be great for doing quick overview results, for example checking code compliant with style guides etc., especially with more extensive projects and applications. Manual testing has allowed me to look at things at a deeper level, checking things like user experience design and in turn finding areas for improvement to strengthen my application as a whole. Using both has allowed me to build reliable functions and code and a higher quality end product.

# Table of Contents

1. [Automated Testing](#automated-testing)
2. [Test Driven Development](#test-driven-development)
3. [Manual Testing](#manual-testing)

# AUTOMATED TESTING

## HTML Validator - [W3C](https://validator.w3.org/)

I put every template page in my site into the HTML validator. This was useful to highlight some code errors that I had missed looking through manually.

### Home Page

#### Before
![Home page validator results before](media/testing-images/html-validator/home-page-html-validator-before.png)
#### After updates
![Home page validator results after](media/testing-images/html-validator/home-page-html-validator-after.png)

### Coffee Quiz

#### Before
![Quiz page validator results before](media/testing-images/html-validator/quiz-html-validator-before.png)
#### After updates
![Quiz page validator results after](media/testing-images/html-validator/quiz-html-validator-after.png)

### Product List Page

![Product list page validator results after](media/testing-images/html-validator/products-html-validator.png)

### Product Detail Page

![Product detail page validator results before](media/testing-images/html-validator/product-details-html-validator.png)

### About Page

#### Before
![About page validator results before](media/testing-images/html-validator/about-html-validator-before.png)
#### After updates
![About page validator results after](media/testing-images/html-validator/about-html-validator-after.png)

### Contact Page

#### Before
![Contact page validator results before](media/testing-images/html-validator/contact-page-html-validator-before.png)
#### After updates
![Contact page validator results after](media/testing-images/html-validator/contact-page-html-validator-after.png)

### Profile Page

The validator would not work for the deployed link of this page, saying it was not retreiveable. This will be due to the fact that the profile only loads when a session cookie is in place from a user login, so it would not be able to render in the validator. To work around this I added the raw code into the validator, and checked through for any justified errors. The validator, due to the fact the raw code has templating code in it that refers to the base.html for the header etc., as well as having python language in it, it was throwing alot of irrelevant errors, as you can see below. I checked each of them one by one, and none were justified errors that required changes.

![Profile page validator results after](media/testing-images/html-validator/profile-html-validator.png)

### Product Management Page / Add Product Page

The validator highlighted:
* __Warning:__ 

![Add Product page validator results before](media/testing-images/html-validator/product-management-html-validator-before.png)

![Add Product page validator results after](media/testing-images/html-validator/product-management-html-validator-after.png)

### Edit Product Page

![Edit Product page validator results](media/testing-images/html-validator/edit-product-html-validator.png)

### Sign In Page

![Sign in page validator results](media/testing-images/html-validator/login-page-html-validator.png)

### Sign Out Page

![Sign out page validator results](media/testing-images/html-validator/sign-out-page-html-validator.png)

### Register Page

![Register page validator results](media/testing-images/html-validator/register-page-html-validator.png)

### Checkout Page

![Checkout page validator results](media/testing-images/html-validator/checkout-page-html-validator.png)

### Bag Page

![Bag page validator results](media/testing-images/html-validator/bag-page-html-validator.png)


## CSS Validator - [W3C](https://jigsaw.w3.org/css-validator/)

No errors were found in my CSS code when put through the validator.
![CSS validator results](media/testing-images/css-validator.png)

## JSHint Validator - [JSHint](https://jshint.com/)

### Product.js
* __Warning:__ 

![product.js validator results](media/testing-images/product-js-validator.png)

### Countryfield.js
* __Warning:__ 

![countryfield.js validator results](media/testing-images/country-field-js-validator.png)

### Quiz.js
* __Warning:__ 

![quiz.js validator results](media/testing-images/quiz-js-validator.png)

## Python Validator - [Code Institute Python Linter](https://pep8ci.herokuapp.com/)

### run.py file

The validator highlighted:
* __Error:__"no new line at end of file" - added new line at the bottom of the code which cleared the error.

![run.py validator results](recipes/static/assets/readme-images/runpy-validator.png)

### routes.py file

The validator highlighted:
* __Error:__"no new line at end of file" - added new line at the bottom of the code.
* __Error:__"expected 2 blank lines, found 1" - added extra line.
* __Error:__"line too long" - split the line up.
* __Error:__"over-indented" - reduced indentation.
* __Error:__"blank line contains whitespace" - removed white space.
* __Error:__"missing whitespace around operator" - added whitespace.

Cleared all the errors below.

![routes.py validator results](recipes/static/assets/readme-images/routespy-validator.png)

### models.py file

The validator highlighted:
* __Error:__"no new line at end of file" - added new line at the bottom of the code.
* __Error:__"expected 2 blank lines, found 1" - added extra line.
* __Error:__"line too long" - split the line up.

Cleared all the errors below.

![models.py validator results](recipes/static/assets/readme-images/modelspy-validator.png)

### __init__.py file

The validator highlighted:
* __Error:__"indentation not a multiple of 4" - fixed indent.
* __Error:__"over-indented" - reduced indent.
* __Error:__"module level import not at top of file" - this line has to be at the end of the file to be called after the rest.

![init.py validator results](recipes/static/assets/readme-images/initpy-validator.png)

## Lighthouse

To test performance and accessibility, I used Lighthouse within the Chrome Developer Tools. Accessibility was down by 1% on the search page, based on the contrast between the pink background and white recipe name text on top.

| Page | Results |
| --- | --- |
| Home Page | <img src="recipes/static/assets/readme-images/home-page-lighthouse.png" alt="Light house results for home page"> |
| Login Page | <img src="recipes/static/assets/readme-images/login-page-lighthouse.png" alt="Light house results for log in page"> |
| Register Page | <img src="recipes/static/assets/readme-images/register-page-lighthouse.png" alt="Light house results for register page"> |
| profile Page | <img src="recipes/static/assets/readme-images/profile-page-lighthouse.png" alt="Light house results for profile page"> |
| Search Page | <img src="recipes/static/assets/readme-images/search-page-lighthouse.png" alt="Light house results for search page"> |
| Contact Page | <img src="recipes/static/assets/readme-images/contact-page-lighthouse.png" alt="Light house results for contact page"> |
| Add Recipe Page | <img src="recipes/static/assets/readme-images/add-recipe-page-lighthouse.png" alt="Light house results for add recipe page"> |
| Edit Recipe Page | <img src="recipes/static/assets/readme-images/edit-recipe-page-lighthouse.png" alt="Light house results for edit recipe page"> |
| Add Product Page | <img src="recipes/static/assets/readme-images/add-Product-page-lighthouse.png" alt="Light house results for add Product page"> |
| Edit Product Page | <img src="recipes/static/assets/readme-images/edit-Product-page-lighthouse.png" alt="Light house results for edit Product page"> |
| Recipes Page | <img src="recipes/static/assets/readme-images/recipes-page-lighthouse.png" alt="Light house results for recipes page"> |

# TEST DRIVEN DEVELOPMENT



# MANUAL TESTING

## Testing User Stories

### First time user

| Goals | How are they achieved? | Image |
| --- | --- | --- |
| As a first time user, I need to be able to understand the purpose of the site instantly and lead intuitively to thr first call-to-action. | This is achieved through a simple and clear synopsis on screen as the first thing the user sees. Right below to call-to-action to 'Register' is easily visible. | ![Home Page](/recipes/static/assets/readme-images/home-page.png) |
| I want to be able to start creating digital Products quickly and add recipes to them. | Once the new user has registered they are automatically redirected to their profile where they can create Products and the create recipes within them. | ![profile Page](/recipes/static/assets/readme-images/profile-page.png) |
| I need to have simple instructions and layout so I am not overwhelmed by too much content or instructions. | This is achieved with clear calls to action buttons, like the buttons on each Product card on the user's profile clearly demonstrate what is possible as next steps. | ![profile Page](/recipes/static/assets/readme-images/profile-page.png) |
| I want to be able to get inspiration and a feel for what other recipes users have uploaded. | Whether logged in or not I can filter through and view all the recipes on the site, with 3 simple dropdown filters. A link to this page is in the nav bar on all pages. | ![Search page](/recipes/static/assets/readme-images/search-page.png)|
| Should I have any questions or issues, I need to be able to contact the developer easily | The user can find a link to the contact form on all pages in both the nav bar and footer, so wherever the user is looking on the page, a link will always be clearly visible | ![Contact Page](/recipes/static/assets/readme-images/contact-page.png) |


### Returning/Frequent user
| Goals | How are they achieved? | Image |
| --- | --- | --- |
| As a returning user, I want to easily log in to my existing account to access my content. | The home page displays a prominent login call to action button and once a user is logged in, they are redirected to their profile to see their current Products.| ![Home Page](/recipes/static/assets/readme-images/home-page.png) ![profile Page](/recipes/static/assets/readme-images/profile-page.png)|
| I want to be able to modify or delete existing Products and recipes | From their profile, the user can edit their Product names by clicking the edit button on their chosen Product card. They can also delete Products and all recipes within that Product, just by clicking the delete button on the Product card. They will be met with a modal pop-up asking them to confirm their action, to avoid Products and recipes within them being deleted accidentally. From the recipes page view, they can edit and delete recipes using the buttons at the bottom of the recipe info. | ![profile Page](/recipes/static/assets/readme-images/profile-page.png) ![Recipes page](/recipes/static/assets/readme-images/edit-delete-recipe-buttons.png) |

## Devices Used For Testing

I have asked friends and family to test the site on their devices. This app has been tested on the following:

Poco X3 NFC - Chrome
Iphone 10 - Firefox
Ipad Pro - Safari
Huawei Matebook Pro - Microsoft Edge and Chrome
Google Pixel - Chrome

## Full Manual Testing

### Home
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login button | User is redirected to the Login page when clicked | Clicked Login button | Redirected to the login page | Pass |
| Register button | User is redirected to the Register page when clicked | Clicked the Register button | Redirected to the register page | Pass  |

### Login
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login with correct credentials | User is redirected to the their profile with a flash message at the top of the page that says 'Welcome "Username"' | Used correct credentials in input fields | Redirected to the profile and flash message appeared | Pass |
| Login with incorrect credentials | User is kept on the Login page and a flash message appears at the top of the page saying 'Incorrect Username and/or Password' | Used incorrect credentials in input fields | Flash message appeared | Pass  |
| Register link | User is redirected to the Register page when clicked | Clicked the Register button | Redirected to the register page | Pass  |

### Register
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Register with incorrect username format | It stays on the register page and a validation message appears asking them to match the required format. | Entered a username below 5 characters, over 15 characters and with special characters. | Validation message appeared | Pass |
| Register with incorrect password format | It stays on the register page and a validation message appears asking them to match the required format. | Tried to register with a password below 5 characters, over 15 characters, only numbers, only lowercase letters, only uppercase characters, only lowercase characters and numbers, only uppercase characters and numbers, only special characters. | Validation message appeared | Pass |
| Input correct username and password. | User is redirected to their profile and flash message 'Registration successful'. | Registered with correct details. | Redirected to the profile with flash message "Registration successful".| Pass |
| Login link | Redirect to the login page. | Clicked login button | Redirected to the the login page | Pass |

### Search
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Select a meal type filter dropdown option | Should filter recipes to show only recipes that match the meal type and selection remain visible in the dropdown | Selected each of the dropdown options to view recipes filtered for each | Recipes filtered successfully and selection remained visible in dropdown | Pass |
| Select a dish origin filter dropdown option | Should filter recipes to show only recipes that match the dish origin and selection remain visible in the dropdown | Selected each of the dropdown options to view recipes filtered for each | Recipes filtered successfully and selection remained visible in dropdown | Pass |
| Select a star rating filter dropdown option | Should filter recipes to show only recipes that match the star rating and selection remain visible in the dropdown | Selected each of the dropdown options to view recipes filtered for each | Recipes filtered successfully and selection remained visible in dropdown | Pass |
| Select a filter dropdown option from two of the dropdowns | Should filter recipes to show only recipes that match the dish origin and selection remain visible in the dropdown | Selected a dropdown option from two dropdowns (tried all combinations) at the same time | Recipes filtered successfully  and selection remained visible in dropdown| Pass |
| Select a filter dropdown option from all three of the dropdowns | Should filter recipes to show only recipes that match the dish origin | Selected a dropdown option for all three dropdowns at the same time | Recipes filtered successfully and selection remained visible in dropdown| Pass |
| Clear selection button | Should reset all filters to blank by refreshing the page | Click the 'clear selection' button | Page refreshed successfully | Pass |
| Collapsed recipe | Should open to display recipe info when clicked | Click recipe title | Recipe info appeared correctly | Pass |

### Contact
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Input first name with over 30 characters | Should not be possible, after 30 characters, characters typed will not appear | Tried to input more than 30 characters | No characters typed over 30 characters appear | Pass |
| Leave inputs blank | Stays on page and validation message with appear prompting the user to input info into field | Left username, email and message inputs empty individually before pressing submit button | Validation message appeared to prompt user to add input | Pass |
| Email input without @ symbol | Validation message appears to prompt user to add @ sign | Input text into email input without @ symbol | Validation message is visible | Pass |
| Type a message with not enough characters | Validation message is visible | Added an input less than 10 characters long | Validation message is visible | Pass |
| Type a message with too many characters | Should not be possible, after 750 characters, characters typed will not appear | Tried to type a message with more than 750 characters | No characters typed over 750 characters appear | Pass |
| Submit will all correct format inputs | Redirect to the thank you page | Input correctly into fields and click submit button | Redirected to thank you page | Pass |

### Thank you
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Redirect countdown | Redirect to the home page after 5 second countdown | Load the thank you page | Redirected to home page successfully after 5 seconds | Pass |

### profile
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Add Product button | Redirect to add Product page | Click add Product button | Redirected to add Product page successfully | Pass |
| Edit Product button | Redirect to edit Product page for specific Product | Click edit Product button | Redirected to edit Product page successfully | Pass |
| View Recipes button | Redirect to recipes page with view of recipes linked to specific Product | Click view recipes button | Redirected to view recipes page successfully with view of recipes linked to specific Product | Pass |
| Add Recipe button | Redirect to add recipe page | Click add recipe button | Redirected to add recipe page successfully | Pass |
| Delete Product button | Modal pop-up to confirm the user wants to delete with 'delete' and 'cancel' buttons | Click delete Product button | Modal pop-up appears with 'delete' or 'cancel' options. Cancel button closes the modal. Delete button successfully deletes the chosen Product | Pass |

### Recipes
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Add Recipe button | Redirect to add recipe page | Click add recipe button | Redirected to add recipe page successfully | Pass |
| Back to Products button | Redirect to profile page | Click back to Products button | Redirected to profile page successfully | Pass |
| Collapsed recipe | Should open to display recipe info when clicked | Click recipe title | Recipe info appeared correctly | Pass |

### Edit Product
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Pre-populated input field | Previously saved Product name to pre-populate the input field | Direct to the edit Product page from profile | Previously saved Product name was pre-populated into the input field, ready for editing | Pass |
| Save changes button | Redirect to profile, flash message 'Product updated', with the chosen Product name updated on its respective card | Save changes button | Redirected to profile page successfully with flash message 'Product updated', Product name updated on card | Pass |

### Add Recipe
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Input fields left empty when form submitted | Validation message to appear "Please fill in this field" | Submit the form with each input left empty on their own | Each input had the validation message appear as expected | Pass |
| Input fields left too short when form submitted | Validation message to appear "Please lengthen this text to 5 characters or more" | Submit the form with each input short strings individually | Each input had the validation message appear as expected | Pass |
| Input fields with too many characters | Should not be possible, after max length, characters typed will not appear | Tried to type a message with more than max length in each input field | No characters typed over 750 characters appear | Pass |
| Create recipe button | Redirect to profile, with recipe in their chosen Product card | Click create recipe button | Redirect to profile successfully, with recipe in their chosen Product card | Pass |
| Dropdown options left empty | If a dropdown is left empty when form submitted, validation message should appear | Leave each dropdown empty individually to check | The form does not submit, but no validation message appears to tell the user why | Fail |
After adding an if statement to check if dropdowns are left blank, I re-tested.
| Dropdown options left empty | If a dropdown is left empty when form submitted, validation message should appear | Leave each dropdown empty individually to check | The form does not submit and flash message appears telling the user to make a selection | Pass |

### Edit Recipe
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Pre-populated input field | Previously saved recipe inputs to pre-populate the input field | Direct to the edit recipe page from profile | Previously saved recipe info was pre-populated into the input field, ready for editing | Pass |
| Save changes button | Redirect to profile, flash message 'Recipe updated', with the chosen Product name updated on its respective card | Save changes button | Redirected to profile page successfully with flash message 'Product updated', Product name updated on card | Pass |

### Add Product
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Create Product button |  | Click create Product button | Redirected to profile page successfully with flash message 'Product created' | Pass |

### 404 Page
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| User tries to access an incorrect URL or page cannot cannot be found | User is redirected to the 404 page with a message displayed "Sorry this page doesn't exist", with a button linked to the Home page. | Typed an incorrect URL into address bar | Not redirected to custom 404 page. | Fail |
I revisited the 404 app route and found a code error - not '@app.errorhandler', so fixed this and tested again.
![404 App route fix](/recipes/static/assets/readme-images/404-page-route-update.png)
| User tries to access an incorrect URL or page cannot cannot be found | User is redirected to the 404 page with a message displayed "Sorry this page doesn't exist", with a button linked to the Home page. | Typed an incorrect URL into address bar | Redirected to custom 404 page | Pass |

### Log out nav bar
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| User logs out using log out link in nav bar | User is redirected to login page with a message displayed "You have been logged out", and the link disappears from the nav bar, replaced by Login and Register | Click on log out link | Redirected successfully to login page with a message displayed "You have been logged out", and the link disappears from the nav bar. Register and Login reappear as links in nav bar. | Pass |


### Footer
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Links change when logged in | User logs in and links change from 'Login, Register and Contact' to 'profile, Logout, Contact' | Login to registered user accunt | Links changed from 'Login, Register and Contact' to 'profile, Logout, Contact' | Pass |

## Bugs

### Solved Bugs

| No. | Bug | How I solved the issue |
| --- | --- | --- |
| 1. | Pre-populated dropdown options not working in the Edit Recipe form. | Removed ‘selected’ from options.  |
| 2. | Contact form submit button triggering a new window to open Thank you page rather than just redirect. | Changed from 'window.open' to 'window.location.replace' in function.  |
| 3. | Mobile side nav not working. | Code was missing a closing bracket, so added to fix.  |
| 4. | Product dropdown on add recipe and edit recipe pages showing all Products on database, not just specific user's Products. | I updated the app routes to include user queries and update the render template to call just the user's Products. |
| 5. | Recipe Ingredients and Instructions displaying as one full line without breaks on recipes page and search page. | Searched solutions and found this to add to breaks to the code [Line Breaks Solutions](https://stackoverflow.com/questions/3206344/passing-html-to-template-using-flask-jinja2) |
| 6. | If dropdowns on Add and edit recipe pages not selected, no validation message appearing | Inspecting the dropdowns in google dev tools I spotted that materialize adds a "display:none" to dropdowns, which removes the usual validation messages. I searched for a solution and found this 'select' code snippet [Dropdown solution](https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown ) to remove the materialize CSS on it so that the validation now shows again. Given this issue, I intend on using Materialize alternatives in future to avoid this issue. |
| 7. | Custom 404 page not appearing when incorrect URLs are created | Needed to change the app route to '@app.errorhandler(404)' [Custom 404 app route solution](https://stackoverflow.com/questions/73140435/why-custom-404-page-not-working-with-flask) |
| 8. | White space appearing below nav bar on index page | I found this happened after I changed the search icon from a materialize icon to a font awesome icon. I tested different sizes but the white space remained, so I reverted back to the materialize icons for the menu and nav bar icons used to avoid this issue. |

### Unsolved Bugs

None known at this time.