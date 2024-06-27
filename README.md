<h1 align="center" id="title"><img src="#" height="125" alt="#"></h1>

WellGood Coffee Roasters is an up-and-coming roastery that have approached me to create a website to showcase their brand and all they have to offer. It is their platform to sell their retail coffee, equipment as well as offer their customers a place to order coffee subscriptions.
Their mission is to get a more wide-spread client base, offering delivery to all of the UK.
They specialise in roasting limited edition retail bags of coffee, which works perfectly for their subscription customers who can choose their favourite coffee notes and get a new bag to try every subscription cycle.
They want to inspire their customers to start their real coffee adventure, explore and find a new hobby in doing so, just like they have.

I have created this as my fourth milestone project for the Code Institute's Level 5 Diploma in Web Application Development.

[View the live project here.](#)

## Table of Contents

1. [User Experience (UX)](#user-experience-(UX))
2. [Features](#features)
3. [Deployment](#deployment)
4. [Technologies Used](#technologies-used)
5. [Code](#code)
6. [Credits](#credits)

<img src="#" alt="Screen mockup of WellGood Coffee">

## User Experience (UX) 

### User stories

<table>
  <thead>
    <tr>
      <th>As a...</th>
      <th>I want to be able to…</th>
      <th>So that I can…</th>
    </tr>
    <tr>
      <th colspan="3">Viewing and Navigation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Visitor</td>
      <td>Immediately understand the purpose of the site</td>
      <td>Tell quickly whether this site is going to be of interest to me</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>View a list of products</td>
      <td>Select some to purchase</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Take a coffee quiz</td>
      <td>To work out what sort of coffee would suit me best</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>View individual product details</td>
      <td>To view the price, description, product rating, product image to check before potential purchase</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Quickly identify sales, deals and special offers</td>
      <td>Save money on my purhcases and potentially buy more on top of my current order</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Easily view my total spend at any time</td>
      <td>Keep to my budget</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>View product reviews from past customers</td>
      <td>Make an informed decision when choosing which products to purchase</td>
    </tr>
    </tbody>
    <thead>
    <tr>
      <th colspan="3">Registration and User Accounts</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td>New visitor</td>
      <td>Register for an account</td>
      <td>To have all orders and profile information in one place for future purchases and subscriptions</td>
    </tr>
    <tr>
      <td>Registered User</td>
      <td>Login or logout</td>
      <td>Access my personal account information, previous purchases, view and edit subscriptions </td>
    </tr>
    <tr>
      <td>Registered User</td>
      <td>Recover my password in case I forget it</td>
      <td>Recover access to my account</td>
    </tr>
    <tr>
      <td>Registered User</td>
      <td>Receive an email confirmation after registering</td>
      <td>Verify that my account registration was successful</td>
    </tr>
    <tr>
      <td>Registered User</td>
      <td>Have a personalised user profile</td>
      <td>View my personal order history and order confirmation, and save my payment information</td>
    </tr>
    <tr>
      <td>Registered User</td>
      <td>Have my email address verified by the site</td>
      <td>Ensure my email address and personal data are safe and secure</td>
    </tr>
    <tr>
      <td>Registered User</td>
      <td>See my past order history</td>
      <td>Make repeat orders</td>
    </tr>
    <tr>
      <td>Registered User</td>
      <td>See my past reviews</td>
      <td>Jog my memory on products I liked or disliked in the past if I haven't purchased in a long time</td>
    </tr>
    </tbody>
    <thead>
    <tr>
      <th colspan="3">Sorting and Searching</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td>Shopper</td>
      <td>Sort the list of available products</td>
      <td>Easily identify the best rated, best priced and categorically sorted products</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Sort a specific category of product</td>
      <td>Find the best priced or best rated product in a specific category, or sort the products in that category by name</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Sort multiple categories of products simultaneously</td>
      <td>Find the best priced or best rated products across broad categories such as 'sweet treats' or 'condiments'</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Search for a product by name or description</td>
      <td>Find a specific product I would like to purchase</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Easily see what I've searched for and the number of results</td>
      <td>Quickly decide whether the product I want is available</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Easily see if a product is out of stock</td>
      <td>Quickly see that the product I want isn't available for purchase</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Save my billing and shipping details</td>
      <td>Checkout even quicker and more conveniently on future orders</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Leave my views and feedback about products</td>
      <td>Help future shoppers make informed decisions about purchases</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Edit/Update my reviews</td>
      <td>Change my review if I change my mind about a product or the the product quality changes over time</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Delete my reviews</td>
      <td>Remove my review if I feel it is no longer accurate but don't want to leave any further reviews</td>
    </tr>
    </tbody>
    <thead>
    <tr>
      <th colspan="3">Purchasing and Checkout</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td>Shopper</td>
      <td>Easily select the size and quantity of a product when purchasing it</td>
      <td>Ensure I don't accidentally select the wrong product, quantity or size</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>View items in my bag to be purchased</td>
      <td>Identify the total cost of my purchase and all items I will receive</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>View the total cost of my purchase before checking out</td>
      <td>So that I can see what the total cost of my purchase is including any additional costs such as shipping are   before making my final purchase</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Adjust the quantity of individual items in my bag</td>
      <td>Easily make changes to my purchase before checkout</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Easily enter my payment information</td>
      <td>Check out quickly with no hassles</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Feel my personal and payment  information is safe and secure</td>
      <td>Confidently product the needed information to make a purchase</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>View an order confirmation at checkout</td>
      <td>Verify that I haven't made any mistakes</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Receive an email confirmation after checking out</td>
      <td>Keep the confirmation of what I've purchase for my records</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Contact the store easily with any questions or concerns</td>
      <td>Get further information about a product or purchase</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>See what discounts have been applied to my order</td>
      <td>Identify the total cost of my purchase after discounts are applied</td>
    </tr>
        <tr>
      <td>Shopper</td>
      <td>See at a glance if there are any items in my shopping basket</td>
      <td>See quickly at a glance if there are any items already in my basket</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Be informed if the store doesn't have enough stock to fulfill the amount I need</td>
      <td>Only order the amounts currently available so as not to cause any delays with my order or have to deal with   refunds later on in the sale cycle</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>See how much I need to spend to qualify for free shipping</td>
      <td>Ensure I am getting the best value on potentially larger purchases</td>
    </tr>
    <tr>
      <td>Shopper</td>
      <td>Be able to checkout without registering for an account</td>
      <td>Checkout quickly and easily even if I don't want to register for an account with the store</td>
    </tr>
    </tbody>
    <thead>
    <tr>
      <th colspan="3">Admin and Store Management</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td>Store Owner/Staff Member</td>
      <td>Add a product</td>
      <td>Add new items to my store</td>
    </tr>
    <tr>
      <td>Store Owner/Staff Member</td>
      <td>Edit/Update a product</td>
      <td>Change product prices, descriptions, images and other product criteria</td>
    </tr>
    <tr>
      <td>Store Owner/Staff Member</td>
      <td>Delete a product</td>
      <td>Remove items that are no longer for sale</td>
    </tr>
    <tr>
      <td>Store Owner/Staff Member</td>
      <td>Manage Stock levels</td>
      <td>Keep track of available inventory</td>
    </tr>
    <tr>
      <td>Store Owner/Staff Member</td>
      <td>Add a discount code</td>
      <td>Add new discount codes to my store</td>
    </tr>
    <tr>
      <td>Store Owner/Staff Member</td>
      <td>Edit/Update a discount code</td>
      <td>Change discount amounts and criteria and whether or not the codes are currently active or note</td>
    </tr>
    <tr>
      <td>Store Owner/Staff Member</td>
      <td>Delete a discount code</td>
      <td>Remove discount codes that are no longer valid or required</td>
    </tr>
  </tbody>
</table>

### User Journey
I created UX flow charts using FigJam to map out the user stories.

![UX Flow key](media/readme-images/ux-flow-key.png)

New visitor

![UX Flow for new visitor](media/readme-images/new-user-ux-flow.png)

Returning and frequent visitor

![UX Flow for returning visitor](media/readme-images/returning-user-ux-flow.png)

### Design

#### Colour Scheme
The colour scheme was primarily crafted with a focus on aesthetics and accessibility. I decided to go with a simplistic and minimalist style choice, mostly using the Bootstrap colour pallette, this minimalist and understated approach I feel provided an excellent contrast against the vibrant colours of the food/product pictures, allowing the products themselves to shine through the design.

<img src="media/readme-images/colour-palette-ms4.png" alt="Screen mockup of WellGood Coffee">


#### Colour Accessibility
			
To ensure the colours chosen met the WCAG 2.1 AA guidelines as minimum and AAA guidelines where possible as with previous projects I used Coolors Contrast Checker which can be found [here](https://coolors.co/contrast-checker/000000-ffffff). However Coolors doesn't support `rgba` so for these colours I used Siege Media which can be found [here](https://www.siegemedia.com/contrast-ratio).

For further information on these guidelines, you can visit the following link. [Web Content Accessibility Guidelines (WCAG) 2.1 (w3.org)](https://www.w3.org/TR/WCAG21/).
        

- ##### Colour Palette and Results
    - Text Colour 1 - [Coolors Contrast Checker](https://coolors.co/contrast-checker/084298-ffffff)<br>
    <img src="readme_and_testing_media/text1-contrast.png" alt="Contrast check of text colour 1 against white background">

    - Text Colour 2 - [Coolors Contrast Checker](https://coolors.co/contrast-checker/212529-ffffff)<br>
    <img src="readme_and_testing_media/text2-contrast.png" alt="Contrast check of text colour 2 against white background">

    - Text Colour 3 - [Siege Media Contrast Checker](https://www.siegemedia.com/contrast-ratio#rgba%2833%2C%2037%2C%2041%2C%200.75%29-on-white)<br>
    <img src="readme_and_testing_media/text3-contrast.png" alt="Contrast check of text colour 3 against white background">  

    - Button Colour 1 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/ffffff-0d6efd)<br>
    <img src="readme_and_testing_media/button-text1-contrast.png" alt="Contrast check of white text against button 1 colour">

    - Button Colour 2 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/ffffff-198754)<br>
    <img src="readme_and_testing_media/button-text2-contrast.png" alt="Contrast check of white text against button 2 colour">

    - Button Colour 3 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/ffffff-dc3545)<br>
    <img src="readme_and_testing_media/button-text3-contrast.png" alt="Contrast check of white text against button 3 colour">

    - Badge Colour 1 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/ffffff-dc3545)<br>
    <img src="readme_and_testing_media/button-text3-contrast.png" alt="Contrast check of white text against badge 1 colour">

    - Badge Colour 2 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/ffffff-0d6efd)<br>
    <img src="readme_and_testing_media/button-text1-contrast.png" alt="Contrast check of white text against badge 2 colour">

    - Badge Colour 3 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/212529-ffc107)<br>
    <img src="readme_and_testing_media/badge-text3-contrast.png" alt="Contrast check of black text against badge 3 colour">

    


#### Typography
The main considerations for the font were aesthetics and accessibility. I chose the Roboto Condensed font as a personal preference as I like the way it looks on the page. It is also a very widely used font developed by Google.this ensures a fairly wide availability across devises.

 - ##### Fallback Font

    For my fallback font I have opted to stick with the Google recommended fonts when downloading the Roboto Condensed font, if no fonts can be found on the user system is will default to the sans-serif family which has many widely used fonts including Arial. Arial is the most widely used font for both online and printed media. Arial is said to be one of the safest web fonts, and is available on all major operating systems.  


#### Imagery

  - ##### Logo
    The Keto Kreations logo was created using Logo.com which can be found [here](https://logo.com/).
    <img src="media/logo.webp" alt="Keto Kreations Logo">

  - ##### Welcome Image
    The welcome/hero image was found at Freepik [here](https://www.freepik.com/free-photo/ketogenic-low-carbs-diet-food-selection-white-wall_12757333.htm#query=keto%20food%20transparent&position=26&from_view=search&track=ais&uuid=6594cbc6-5c09-4e67-925f-dfdfc7f00692)
    <img src="media/hero.webp" alt="Welcome/hero image">
    Attribution - <a href="https://www.freepik.com/free-photo/ketogenic-low-carbs-diet-food-selection-white-wall_12757333.htm#query=keto%20food%20transparent&position=26&from_view=search&track=ais&uuid=6594cbc6-5c09-4e67-925f-dfdfc7f00692">Image by master1305</a> on Freepik

  - ##### 404 Image
    The image used on the 404 page was found at Freepik [here](https://www.freepik.com/free-vector/error-404-concept-landing-page_4660894.htm#query=404%20image&position=9&from_view=search&track=ais&uuid=b78a78a6-bfe8-4b6a-a66f-7ce0423dbe75)
    <img src="media/404.webp" alt="404 Image">
    Attribution - <a href="https://www.freepik.com/free-vector/error-404-concept-landing-page_4660894.htm#query=404%20image&position=9&from_view=search&track=ais&uuid=b78a78a6-bfe8-4b6a-a66f-7ce0423dbe75">Image by pikisuperstar</a> on Freepik

  - #### Product Images
    All product images were also sourced from Freepik, all of the attributions for these images are in the below table.

  <table>
  <thead>
    <tr>
      <th>Product</th>
      <th>SKU</th>
      <th>Image</th>
      <th>Attribution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Keto Bread</td>
      <td>PAN-BRE-BRE</td>
      <td><img src="media/bread.webp" height="125" alt="Keto bread image"></td>
      <td><a href="https://www.freepik.com/free-photo/front-view-black-bread-slices-black-board-mixed-colors-distressed-background_17243793.htm#query=bread%20sliced&position=20&from_view=search&track=ais&uuid=4fd5b5e9-a0c9-4b07-b1a3-efb33ab3b7ac">Image by mdjaff</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Bread rolls</td>
      <td>PAN-BRE-BRR</td>
      <td><img src="media/bread-rolls.webp" height="125" alt="Keto bread rolls image"></td>
      <td><a href="https://www.freepik.com/free-photo/fresh-brown-buns-wooden-board-light-background_13517267.htm#query=bread%20roll%20bap&position=30&from_view=search&track=ais&uuid=2f2492e6-a203-4a21-8bef-d9318998fb2c">Image by azerbaijan_stockers</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Bagels</td>
      <td>PAN-BRE-BAG</td>
      <td><img src="media/bagels.webp" height="125" alt="Keto bagels image"></td>
      <td><a href="https://www.freepik.com/free-photo/concept-tasty-food-bagel-top-view_40451427.htm#page=2&query=bagels&position=13&from_view=search&track=sph&uuid=e3e7e088-9004-48b4-b2d3-55167b0fc625">Image by atlascompany</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Fusilli Pasta</td>
      <td>PAN-PAS-FUS</td>
      <td><img src="media/pasta.webp" height="125" alt="Keto fusilli pasta image"></td>
      <td><a href="https://www.freepik.com/free-photo/wooden-bowl-italian-uncooked-dry-pasta-fusilli-high-quality-photo_13211012.htm#query=dry%20pasta&position=11&from_view=search&track=ais&uuid=78f523ff-5eba-48e4-b3cb-ab9aa74c0976">Image by azerbaijan_stockers</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Spaghetti Pasta</td>
      <td>PAN-PAS-SPA</td>
      <td><img src="media/spaghetti.webp" height="125" alt="Keto spaghetti pasta image"></td>
      <td><a href="https://www.freepik.com/free-photo/raw-dry-spaghetti-glass-jar-marble-table_16937021.htm#query=dry%20spaghetti&position=11&from_view=search&track=ais&uuid=0139bc79-5dd6-4a24-82a1-e19cc7645619">Image by azerbaijan_stockers</a> on Freepik</td>
    </tr>
    <tr>
      <td>Cauliflower Rice</td>
      <td>PAN-PAS-CAU</td>
      <td><img src="media/cauliflower-rice.webp" height="125" alt="Cauliflower rice image"></td>
      <td><a href="https://www.freepik.com/free-photo/yellow-delicious-cuscus-plate_12178556.htm?query=riced%20cauliflower#from_view=detail_alsolike#position=0&query=riced+cauliflower">Image by senivpetro</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Brownies</td>
      <td>SWE-CAK-BRO</td>
      <td><img src="media/brownies.webp" height="125" alt="Keto brownies image"></td>
      <td><a href="https://www.freepik.com/free-photo/overhead-shot-freshly-baked-brownies-wooden-board_11600017.htm#query=brownies&position=23&from_view=search&track=sph&uuid=1b094c71-3b60-46a9-8a8c-700f2d09362e">Image by wirestock</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Cookies</td>
      <td>SWE-CAK-COO</td>
      <td><img src="media/cookies.webp" height="125" alt="Keto cookies image"></td>
      <td><a href="https://www.freepik.com/free-photo/top-view-chocolate-cookies_9469437.htm#page=2&query=cookies&position=3&from_view=search&track=sph&uuid=6220e534-55ca-461c-b248-fd62a9e6ecdb">Image by Freepik</a></td>
    </tr>
    <tr>
      <td>Keto Popcorn</td>
      <td>SWE-POP-POP-120</td>
      <td><img src="media/popcorn.webp" height="125" alt="Keto popcorn image"></td>
      <td><a href="https://www.freepik.com/free-photo/caramel-popcorn-table_1274451.htm#query=popcorn&position=28&from_view=search&track=sph&uuid=0338ee99-5b19-4d53-aeda-ab5d4813ce3d">Image by topntp26</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Caramel Popcorn</td>
      <td>SWE-POP-CAR-120</td>
      <td><img src="media/caramel-popcorn.webp" height="125" alt="Keto caramel popcorn image"></td>
      <td><a href="https://www.freepik.com/free-photo/delicious-popcorn_6543842.htm#query=caramel%20popcorn&position=10&from_view=search&track=ais&uuid=e8a2ab27-db5f-4288-bc3a-27771f1097ec">Image by Racool_studio</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Protein Bars</td>
      <td>SWE-BAR-PRO-120</td>
      <td><img src="media/protein-bars.webp" height="125" alt="Keto protein bars image"></td>
      <td><a href="https://www.freepik.com/free-photo/top-view-blueberry-snack-bars_8810571.htm#query=protein%20bar&position=15&from_view=search&track=ais&uuid=9926ea94-e326-4b8c-a11a-13d1a58b4997">Image by Freepik</a></td>
    </tr>
    <tr>
      <td>Fat bombs</td>
      <td>SWE-CAK-FAT-180</td>
      <td><img src="media/fat-bombs.webp" height="125" alt="Fat bombs image"></td>
      <td><a href="https://www.freepik.com/free-photo/chocolate-balls_4378130.htm#query=chocolate%20protein%20ball&position=3&from_view=search&track=ais&uuid=2f922c19-9bf2-4575-892a-8ac53c90d618">Image by Freepik</a></td>
    </tr>
    <tr>
      <td>Keto Chocolate Bars</td>
      <td>SWE-BAR-CHO-120</td>
      <td><img src="media/chocolate-bars.webp" height="125" alt="Keto chocolate bars image"></td>
      <td><a href="https://www.freepik.com/free-photo/chocolate-cocoa-crumbs_4822037.htm#query=chocolate%20bar%20homemade&position=28&from_view=search&track=ais&uuid=fb9859a4-57a0-412c-bdf3-b8bec93ed875">Image by Freepik</a></td>
    </tr>
    <tr>
      <td>Keto Sweets</td>
      <td>SWE-SWE-SWE-120</td>
      <td><img src="media/sweets.webp" height="125" alt="Keto sweets image"></td>
      <td><a href="https://www.freepik.com/free-photo/colorful-marmelades-out-paper-wrap_10464684.htm#query=homemade%20sour%20sweets&position=32&from_view=search&track=ais&uuid=a4bdac4c-c410-4439-96cd-6ec512275ce7">Image by azerbaijan_stockers</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Ketchup</td>
      <td>CON-SAU-KET-460</td>
      <td><img src="media/ketchup.webp" height="125" alt="Keto ketchup image"></td>
      <td><a href="https://www.freepik.com/free-photo/fresh-tomato-juice-ready-serve_13901110.htm#query=homemade%20ketchup&position=17&from_view=search&track=ais&uuid=c1d3eb5d-4ef6-4dc8-9d1b-6b6c11d7bd2f">Image by jcomp</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Sticky BBQ Sauce</td>
      <td>CON-SAU-STI-460</td>
      <td><img src="media/sticky-bbq.webp" height="125" alt="Keto sticky bbq sauce image"></td>
      <td><a href="https://www.freepik.com/free-photo/filling-red-confiture-into-red-cup-from-spoon_6422433.htm#page=3&query=bbq%20sauce&position=12&from_view=search&track=ais&uuid=41a9c062-1ce3-443a-bc8d-7be88d26a5de">Image by azerbaijan_stockers</a> on Freepik</td>
    </tr>
    <tr>
      <td>Chilli Sauce</td>
      <td>CON-SAU-CHI-460</td>
      <td><img src="media/chilli.webp" height="125" alt="Chilli sauce image"></td>
      <td><a href="https://www.freepik.com/free-photo/chili-sauce-peppers-dark-wooden-surface_13806336.htm#page=4&query=homemade%20bbq%20sauce&position=41&from_view=search&track=ais&uuid=1806e449-4564-4e9b-a546-77843f6a34d8">Image by jcomp</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Curry Sauce</td>
      <td>CON-SAU-CUR-450</td>
      <td><img src="media/curry.webp" height="125" alt="Keto curry sauce image"></td>
      <td><a href="https://www.freepik.com/free-photo/front-view-delicious-tomato-soup-cooked-from-fresh-tomatoes-with-seasonings-dark-space_15005434.htm#query=tika%20sauce&position=48&from_view=search&track=ais&uuid=b33bbe1b-1360-43f6-82ba-c3dabcbaf555">Image by KamranAydinov</a> on Freepik</td>
    </tr>
    <tr>
      <td>Keto Pasta Sauce</td>
      <td>CON-SAU-PAS</td>
      <td><img src="media/pasta-sauce.webp" height="125" alt="Keto pasta sauce image"></td>
      <td><a href="https://www.freepik.com/free-photo/bottle-borscht-tomatoes-garlic_5969440.htm#page=7&query=tomato%20pasta%20sauce%20jar&position=30&from_view=search&track=ais&uuid=fa9b956b-b24d-4cbd-b908-87283a7bb8b7">Image by Freepik</a></td>
    </tr>
    <tr>
      <td>Coconut Oil</td>
      <td>CON-OIL-COC</td>
      <td><img src="media/coconut-oil.webp" height="125" alt="Coconut oil image"></td>
      <td><a href="https://www.freepik.com/free-photo/jug-coconut-oil-whit-coconut-put-dark-background_10992006.htm#query=coconut%20oil%20homemade&position=11&from_view=search&track=ais&uuid=dc5f5871-1436-455d-bd6e-adc8251663f4">Image by jcomp</a> on Freepik</td>
    </tr>
    <tr>
      <td>Extra Virgin Olive Oil</td>
      <td>CON-OIL-OLI</td>
      <td><img src="media/olive-oil.webp" height="125" alt="Extra virgin olive oil image"></td>
      <td><a href="https://www.freepik.com/free-photo/tasty-looking-olives-extra-virgin-olive-oil-olive-leafs-dark-wooden-background_17234457.htm#query=olive%20oil&position=10&from_view=search&track=ais&uuid=d5b32484-2bdf-41a1-b8cd-5a9bd98b1dd5">Image by wirestock</a> on Freepik</td>
    </tr>
  </tbody>
</table>
<br>

All other imagery on the website are basic icons obtained from Font Awesome which can be found [here](https://fontawesome.com/).


### Wireframes
The wireframes were creates using [Figma](https://www.figma.com/). I have deviated somewhat from my original wireframes, but this was mainly design preference and ensuring a good responsive layout on smaller screens.

I did not create separate wireframes for mobile and tablet as the layout is identical.

  - #### Mobile Wireframes

  <img src="media/readme-images/MS4-mobile-wireframes.png" alt="Website mobile wireframes">


  - #### Tablet Wireframes

  <img src="media/readme-images/MS4-tablet-wireframes.png" alt="Website tablet wireframes">

[Link to my Figma page](https://www.figma.com/design/IYOwfhepgdhys2z3s7EsUc/Milestone-4---WellGood-Coffee-Roasters?node-id=0-1&t=pPxFqoFWM4APLAXC-1)
  
### Database Schema
The database schema flow charts were created using [Miro](https://www.miro.com/).

<img src="media/readme-images/database-schema.png" alt="Database schema chart">


[Back to top](#title)  

## Features

- Fully responsive across all screen sizes.

<table>
    <thead>
        <tr>
            <th colspan="2">Desktop</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Welcome page</td>
            <td><img height=300 src="readme_and_testing_media/welcome-desktop.png"
                    alt="Screenshot of welcome screen on laptop"></td>
        </tr>
        <tr>
            <td>Products page</td>
            <td><img height=300 src="readme_and_testing_media/products-desktop.png"
                    alt="Screenshot of products page on laptop"></td>
        </tr>
        <tr>
            <td>Product details page</td>
            <td><img height=300 src="readme_and_testing_media/productdeatil1-dekstop.png"
                    alt="Screenshot of product details page on laptop"></td>
        </tr>
        <tr>
            <td>Product details page</td>
            <td><img height=300 src="readme_and_testing_media/productdetail2-dekstop.png"
                    alt="Screenshot of product details page on laptop"></td>
        </tr>
        <tr>
            <td>Shopping bag page</td>
            <td><img height=300 src="readme_and_testing_media/bag-desktop.png"
                    alt="Screenshot of shopping bag page on laptop"></td>
        </tr>
        <tr>
            <td>Checkout page</td>
            <td><img height=300 src="readme_and_testing_media/checkout-desktop.png"
                    alt="Screenshot of checkout page on laptop"></td>
        </tr>
        <tr>
            <td>Checkout page</td>
            <td><img height=300 src="readme_and_testing_media/checkout2-desktop.png"
                    alt="Screenshot of checkout page on laptop"></td>
        </tr>
        <tr>
            <td>Checkout success page</td>
            <td><img height=300 src="readme_and_testing_media/checkoutsuccess-desktop.png"
                    alt="Screenshot of checkout success page on laptop"></td>
        </tr>
        <tr>
            <td>Profile page</td>
            <td><img height=300 src="readme_and_testing_media/profile1-desktop.png"
                    alt="Screenshot of profile page on laptop"></td>
        </tr>
        <tr>
            <td>Profile page</td>
            <td><img height=300 src="readme_and_testing_media/profile2-desktop.png"
                    alt="Screenshot of profile page on laptop"></td>
        </tr>
        <tr>
            <td>Product management page</td>
            <td><img height=300 src="readme_and_testing_media/productmanagement-desktop.png"
                    alt="Screenshot of product management page on laptop"></td>
        </tr>
        <tr>
            <td>Add product page</td>
            <td><img height=300 src="readme_and_testing_media/addproduct1-desktop.png"
                    alt="Screenshot of add product page on laptop"></td>
        </tr>
        <tr>
            <td>Add product page</td>
            <td><img height=300 src="readme_and_testing_media/addproduct2-desktop.png"
                    alt="Screenshot of add product page on laptop"></td>
        </tr>
        <tr>
            <td>Add variant page</td>
            <td><img height=300 src="readme_and_testing_media/addvariant-dekstop.png"
                    alt="Screenshot of add variant page on laptop"></td>
        </tr>
        <tr>
            <td>Edit product page</td>
            <td><img height=300 src="readme_and_testing_media/editproduct1-desktop.png"
                    alt="Screenshot of edit product page on laptop"></td>
        </tr>
        <tr>
            <td>Edit product page</td>
            <td><img height=300 src="readme_and_testing_media/editproduct2-desktop.png"
                    alt="Screenshot of edit product page on laptop"></td>
        </tr>
        <tr>
            <td>Edit variant page</td>
            <td><img height=300 src="readme_and_testing_media/editvariant-desktop.png"
                    alt="Screenshot of edit variant page on laptop"></td>
        </tr>
        <tr>
            <td>Product management modal</td>
            <td><img height=300 src="readme_and_testing_media/productmanagementmodal1-desktop.png"
                    alt="Screenshot of product management modal on product management page laptop"></td>
        </tr>
        <tr>
            <td>Product management modal</td>
            <td><img height=300 src="readme_and_testing_media/productmanagementmodal2-desktop.png"
                    alt="Screenshot of product management modal on product management page laptop"></td>
        </tr>
        <tr>
            <td>Stock management page</td>
            <td><img height=300 src="readme_and_testing_media/stockmanagement1-desktop.png"
                    alt="Screenshot of stock management page laptop"></td>
        </tr>
        <tr>
            <td>Login page</td>
            <td><img height=300 src="readme_and_testing_media/login-desktop.png" alt="Screenshot of login page laptop">
            </td>
        </tr>
        <tr>
            <td>Logout page</td>
            <td><img height=300 src="readme_and_testing_media/logout-desktop.png"
                    alt="Screenshot of logout page laptop"></td>
        </tr>
        <tr>
            <td>Register page</td>
            <td><img height=300 src="readme_and_testing_media/register-desktop.png"
                    alt="Screenshot of register page laptop"></td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th colspan="2">Tablet</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Welcome page</td>
            <td><img height=300 src="readme_and_testing_media/welcome-tablet.png"
                    alt="Screenshot of welcome screen on tablet"></td>
        </tr>
        <tr>
            <td>Products page</td>
            <td><img height=300 src="readme_and_testing_media/products-tablet.png"
                    alt="Screenshot of products page on tablet"></td>
        </tr>
        <tr>
            <td>Product details page</td>
            <td><img height=300 src="readme_and_testing_media/productdetail1-tablet.png"
                    alt="Screenshot of product details page on tablet"></td>
        </tr>
        <tr>
            <td>Product details page</td>
            <td><img height=300 src="readme_and_testing_media/productdetail2-tablet.png"
                    alt="Screenshot of product details page on tablet"></td>
        </tr>
        <tr>
            <td>Shopping bag page</td>
            <td><img height=300 src="readme_and_testing_media/bag-tablet.png"
                    alt="Screenshot of shopping bag page on tablet"></td>
        </tr>
        <tr>
            <td>Checkout page</td>
            <td><img height=300 src="readme_and_testing_media/checkout1-tablet.png"
                    alt="Screenshot of checkout page on tablet"></td>
        </tr>
        <tr>
            <td>Checkout page</td>
            <td><img height=300 src="readme_and_testing_media/checkout2-tablet.png"
                    alt="Screenshot of checkout page on tablet"></td>
        </tr>
        <tr>
            <td>Checkout success page</td>
            <td><img height=300 src="readme_and_testing_media/checkoutsuccess-tablet.png"
                    alt="Screenshot of checkout success page on tablet"></td>
        </tr>
        <tr>
            <td>Profile page</td>
            <td><img height=300 src="readme_and_testing_media/profile1-tablet.png"
                    alt="Screenshot of profile page on tablet"></td>
        </tr>
        <tr>
            <td>Profile page</td>
            <td><img height=300 src="readme_and_testing_media/profile2-tablet.png"
                    alt="Screenshot of profile page on tablet"></td>
        </tr>
        <tr>
            <td>Profile page</td>
            <td><img height=300 src="readme_and_testing_media/profile3-tablet.png"
                    alt="Screenshot of profile page on tablet"></td>
        </tr>
        <tr>
            <td>Product management page</td>
            <td><img height=300 src="readme_and_testing_media/productmanagement1-tablet.png"
                    alt="Screenshot of product management page on tablet"></td>
        </tr>
        <tr>
            <td>Product management page</td>
            <td><img height=300 src="readme_and_testing_media/productmanagment2-tablet.png"
                    alt="Screenshot of product management page on tablet"></td>
        </tr>
        <tr>
            <td>Add product page</td>
            <td><img height=300 src="readme_and_testing_media/addproduct1-tablet.png"
                    alt="Screenshot of add product page on tablet"></td>
        </tr>
        <tr>
            <td>Add product page</td>
            <td><img height=300 src="readme_and_testing_media/addproduct2-tablet.png"
                    alt="Screenshot of add product page on tablet"></td>
        </tr>
        <tr>
            <td>Add variant page</td>
            <td><img height=300 src="readme_and_testing_media/addvariant1-tablet.png"
                    alt="Screenshot of add variant page on tablet"></td>
        </tr>
        <tr>
            <td>Add variant page</td>
            <td><img height=300 src="readme_and_testing_media/addvariant2-tablet.png"
                    alt="Screenshot of add variant page on tablet"></td>
        </tr>
        <tr>
            <td>Edit product page</td>
            <td><img height=300 src="readme_and_testing_media/editproduct1-tablet.png"
                    alt="Screenshot of edit product page on tablet"></td>
        </tr>
        <tr>
            <td>Edit product page</td>
            <td><img height=300 src="readme_and_testing_media/editproduct2-tablet.png"
                    alt="Screenshot of edit product page on tablet"></td>
        </tr>
        <tr>
            <td>Edit variant page</td>
            <td><img height=300 src="readme_and_testing_media/editvariant1-tablet.png"
                    alt="Screenshot of edit variant page on tablet"></td>
        </tr>
        <tr>
            <td>Edit variant page</td>
            <td><img height=300 src="readme_and_testing_media/editvariant2-tablet.png"
                    alt="Screenshot of edit variant page on tablet"></td>
        </tr>
        <tr>
            <td>Product management modal</td>
            <td><img height=300 src="readme_and_testing_media/productmanagementmodal1-tablet.png"
                    alt="Screenshot of product management modal on product management page tablet"></td>
        </tr>
        <tr>
            <td>Product management modal</td>
            <td><img height=300 src="readme_and_testing_media/productmanagementmodal2-tablet.png"
                    alt="Screenshot of product management modal on product management page tablet"></td>
        </tr>
        <tr>
            <td>Stock management page</td>
            <td><img height=300 src="readme_and_testing_media/stockmanagement1-tablet.png"
                    alt="Screenshot of stock management page tablet"></td>
        </tr>
        <tr>
            <td>Stock management page</td>
            <td><img height=300 src="readme_and_testing_media/stockmanagement2-tablet.png"
                    alt="Screenshot of stock management page tablet"></td>
        </tr>
        <tr>
            <td>Login page</td>
            <td><img height=300 src="readme_and_testing_media/login-tablet.png" alt="Screenshot of login page tablet">
            </td>
        </tr>
        <tr>
            <td>Logout page</td>
            <td><img height=300 src="readme_and_testing_media/logout-tablet.png" alt="Screenshot of logout page tablet">
            </td>
        </tr>
        <tr>
            <td>Register page</td>
            <td><img height=300 src="readme_and_testing_media/register-tablet.png"
                    alt="Screenshot of register page tablet"></td>
        </tr>
        <tr>
            <td>Sidenav</td>
            <td><img height=300 src="readme_and_testing_media/sidenav-tablet.png" alt="Screenshot of sidenav tablet">
            </td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th colspan="2">Mobile</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Welcome page</td>
            <td><img height=300 src="readme_and_testing_media/welcome-mobile.png"
                    alt="Screenshot of welcome screen on mobile"></td>
        </tr>
        <tr>
            <td>Products page</td>
            <td><img height=300 src="readme_and_testing_media/products-mobile.png"
                    alt="Screenshot of products page on mobile"></td>
        </tr>
        <tr>
            <td>Products page</td>
            <td><img height=300 src="readme_and_testing_media/products2-mobile.png"
                    alt="Screenshot of products page on mobile"></td>
        </tr>
        <tr>
            <td>Product details page</td>
            <td><img height=300 src="readme_and_testing_media/productdetail1-mobile.png"
                    alt="Screenshot of product details page on mobile"></td>
        </tr>
        <tr>
            <td>Product details page</td>
            <td><img height=300 src="readme_and_testing_media/productdetail2-mobile.png"
                    alt="Screenshot of product details page on mobile"></td>
        </tr>
        <tr>
            <td>Shopping bag page</td>
            <td><img height=300 src="readme_and_testing_media/bag1-mobile.png"
                    alt="Screenshot of shopping bag page on mobile"></td>
        </tr>
        <tr>
            <td>Shopping bag page</td>
            <td><img height=300 src="readme_and_testing_media/bag2-mobile.png"
                    alt="Screenshot of shopping bag page on mobile"></td>
        </tr>
        <tr>
            <td>Checkout page</td>
            <td><img height=300 src="readme_and_testing_media/checkout1-mobile.png"
                    alt="Screenshot of checkout page on mobile"></td>
        </tr>
        <tr>
            <td>Checkout page</td>
            <td><img height=300 height=300 src="readme_and_testing_media/checkout2-mobile.png"
                    alt="Screenshot of checkout page on mobile"></td>
        </tr>
        <tr>
            <td>Checkout success page</td>
            <td><img height=300 src="readme_and_testing_media/checkoutsuccess1-mobile.png"
                    alt="Screenshot of checkout success page on mobile"></td>
        </tr>
        <tr>
            <td>Checkout success page</td>
            <td><img height=300 src="readme_and_testing_media/checkoutsuccess2-mobile.png"
                    alt="Screenshot of checkout success page on mobile"></td>
        </tr>
        <tr>
            <td>Profile page</td>
            <td><img height=300 src="readme_and_testing_media/profile1-mobile.png"
                    alt="Screenshot of profile page on mobile"></td>
        </tr>
        <tr>
            <td>Profile page</td>
            <td><img height=300 src="readme_and_testing_media/profile2-mobile.png"
                    alt="Screenshot of profile page on mobile"></td>
        </tr>
        <tr>
            <td>Profile page</td>
            <td><img height=300 src="readme_and_testing_media/profile3-mobile.png"
                    alt="Screenshot of profile page on mobile"></td>
        </tr>
        <tr>
            <td>Product management page</td>
            <td><img height=300 src="readme_and_testing_media/productmanagement1-mobile.png"
                    alt="Screenshot of product management page on mobile"></td>
        </tr>
        <tr>
            <td>Product management page</td>
            <td><img height=300 src="readme_and_testing_media/productmanagement2-mobile.png"
                    alt="Screenshot of product management page on mobile"></td>
        </tr>
        <tr>
            <td>Add product page</td>
            <td><img height=300 src="readme_and_testing_media/addproduct1-mobile.png"
                    alt="Screenshot of add product page on mobile"></td>
        </tr>
        <tr>
            <td>Add product page</td>
            <td><img height=300 src="readme_and_testing_media/addproduct2-mobile.png"
                    alt="Screenshot of add product page on mobile"></td>
        </tr>
        <tr>
            <td>Add variant page</td>
            <td><img height=300 src="readme_and_testing_media/addvariant1-mobile.png"
                    alt="Screenshot of add variant page on mobile"></td>
        </tr>
        <tr>
            <td>Add variant page</td>
            <td><img height=300 src="readme_and_testing_media/addvariant2-mobile.png"
                    alt="Screenshot of add variant page on mobile"></td>
        </tr>
        <tr>
            <td>Edit product page</td>
            <td><img height=300 src="readme_and_testing_media/editproduct1-mobile.png"
                    alt="Screenshot of edit product page on mobile"></td>
        </tr>
        <tr>
            <td>Edit product page</td>
            <td><img height=300 src="readme_and_testing_media/editproduct2-mobile.png"
                    alt="Screenshot of edit product page on mobile"></td>
        </tr>
        <tr>
            <td>Edit variant page</td>
            <td><img height=300 src="readme_and_testing_media/editvariant1-mobile.png"
                    alt="Screenshot of edit variant page on mobile"></td>
        </tr>
        <tr>
            <td>Edit variant page</td>
            <td><img height=300 src="readme_and_testing_media/editvariant2-mobile.png"
                    alt="Screenshot of edit variant page on mobile"></td>
        </tr>
        <tr>
            <td>Product management modal</td>
            <td><img height=300 src="readme_and_testing_media/productmanagementmodal1-mobile.png"
                    alt="Screenshot of product management modal on product management page mobile"></td>
        </tr>
        <tr>
            <td>Product management modal</td>
            <td><img height=300 src="readme_and_testing_media/productmanagementmodal2-mobile.png"
                    alt="Screenshot of product management modal on product management page mobile"></td>
        </tr>
        <tr>
            <td>Stock management page</td>
            <td><img height=300 src="readme_and_testing_media/stockamanagement1-mobile.png"
                    alt="Screenshot of stock management page mobile"></td>
        </tr>
        <tr>
            <td>Stock management page</td>
            <td><img height=300 src="readme_and_testing_media/stockmanagement2-mobile.png"
                    alt="Screenshot of stock management page tablet"></td>
        </tr>
        <tr>
            <td>Login page</td>
            <td><img height=300 src="readme_and_testing_media/login-mobile.png" alt="Screenshot of login page mobile">
            </td>
        </tr>
        <tr>
            <td>Logout page</td>
            <td><img height=300 src="readme_and_testing_media/logout-mobile.png" alt="Screenshot of logout page mobile">
            </td>
        </tr>
        <tr>
            <td>Register page</td>
            <td><img height=300 src="readme_and_testing_media/register-mobile.png"
                    alt="Screenshot of register page mobile"></td>
        </tr>
        <tr>
            <td>Sidenav</td>
            <td><img height=300 src="readme_and_testing_media/sidenav-mobile.png" alt="Screenshot of sidenav mobile">
            </td>
        </tr>
    </tbody>
</table>

<hr>

- Intuitive and easy to navigate using the top navbar on larger screens and sidenav on smaller screens which present different options to the user depending on whether or not they are logged in, and if they are a 'super user' as well as if there are products currently in their shopping bag. 

	There is also a search function allowing the customer to search for the exact products they need .There are also various appropriately marked buttons throughout the site making navigation easy.

  <img src="readme_and_testing_media/navbar.png" alt="Navbar">
  <img src="readme_and_testing_media/mobilenav.png" alt="Mobile navbar">
  <img src="readme_and_testing_media/sidenav.png" alt="Sidenav">
  <img src="readme_and_testing_media/buttons.png" alt="Navigation buttons">
<hr>

- Full account management including the ability to...
	- Sign in
	- Sign out
	- Sign up
	- Reset forgotten passwords

	The main functionality for account management is provided by AllAuth built into Django but the pages have been restyled to fit in with the page design and be fully responsive.

  <img src="readme_and_testing_media/login-desktop.png" alt="Login page">
  <img src="readme_and_testing_media/logout-desktop.png" alt="Logout page">
  <img src="readme_and_testing_media/register-desktop.png" alt="Register page">
  <img src="readme_and_testing_media/passwordreset.png" alt="Password reset page">
<hr>

- A homepage designed to convey straight away exactly what the site is about to the user.

  <img src="readme_and_testing_media/welcome-desktop.png" alt="Password reset page">
<hr>

- A contact button which is always visible in the navbar or sidenav, giving users a quick and convenient way to contact the store with any queries.

  <img src="readme_and_testing_media/navbar.png" alt="Navbar">
  <img src="readme_and_testing_media/sidenav.png" alt="Sidenav">
<hr>

- A product page offering basic product information and pictures as well as various filtering and sorting options allowing the user to easily navigate the products available in the store. 

  <img src="readme_and_testing_media/products-desktop.png" alt="Products page">
  <img src="readme_and_testing_media/productsort.png" alt="Products sort dropdown">

<hr>

- Conveniently placed badges and tags on products giving instant feedback to the user as to whether a product is new, on sale or out of stock as well as which category it belongs to.

  <img src="readme_and_testing_media/badges.png" alt="Product badges">
  <img src="readme_and_testing_media/badges2.png" alt="Product badges">
<hr>

- A product details page giving more in depth information about the product such as the description, stock availability, reviews, ingredients, allergens and nutritional information.

	It also shows any reviews that have been left for the product as well as giving registered users the ability to leave their own reviews.

  <img src="readme_and_testing_media/productdeatil1-dekstop.png" alt="Product details page">
  <img src="readme_and_testing_media/productdetail2-dekstop.png" alt="Product details page">
<hr>

- A product selector on each product page where the product has different variants such as different package sizes, which also shows how many of each variant is currently in stock for purchase. When selected the price on the page is dynamically updated.

  <img src="readme_and_testing_media/sizeselector.png" alt="Product size selector">
<hr>

- The ability to store items in the shopping bag for purchase as well as the ability to update the quantity required or remove them all together.

  <img src="readme_and_testing_media/bag-desktop.png" alt="Bag page">
  <img src="readme_and_testing_media/qtyselector.png" alt="Quantity selector">
  
<hr>

- The ability to add available discount codes to your order.

  <img src="readme_and_testing_media/discountbox.png" alt="Discount box">
<hr>

- A secure checkout page powered by Stripe payments which shows a summary of the order and also give the user the ability to save their details for future orders if they are already registered.

  <img src="readme_and_testing_media/checkout-desktop.png" alt="Checkout Page">
  <img src="readme_and_testing_media/checkout2-desktop.png" alt="Checkout Page">
  <img src="readme_and_testing_media/saveinfo.png" alt="Save info selector">
  <img src="readme_and_testing_media/stripe.png" alt="Stripe payment box">
<hr>

- A checkout success page with give confirmation of the current order as well as a summary of the order.

  <img src="readme_and_testing_media/checkoutsuccess-desktop.png" alt="Stripe payment box">
<hr>

- A user profile page which give users the ability to view and update their default delivery information, as well as an order history section, giving the user the ability to view details of all their past orders. 

  There is also a reviews section which give the user the ability to see the past reviews as well as being able to edit or delete those reviews.
  
  <img src="readme_and_testing_media/profile1-desktop.png" alt="Profile page">
  <img src="readme_and_testing_media/profile2-desktop.png" alt="Profile page">
<hr>

- For super users the is a product management section which provides the ability to do the following...
		- Add, edit and delete products and product variants
		- Add, edit and delete discount codes
		- Manage the stock levels of the store

    <img src="readme_and_testing_media/productmanagement-desktop.png" alt="Product management page">
<hr>

- Custom success, warning and error messages giving customers feedback on their actions as they navigate the site, as well as a preview of their shopping carts when changes are made to their current 'bag items'.

    <img src="readme_and_testing_media/successmessage.png" alt="Success message">
    <img src="readme_and_testing_media/errormessage.png" alt="Error message">
    <img src="readme_and_testing_media/shoppingbagpreview.png" alt="Shopping bag preview">
<hr>

- Confirmation emails sent for all orders made as well as when the custom makes contact with the store via the 'Contact' modal on the site.

  <img src="readme_and_testing_media/contactmodal.png" alt="Contact modal">
  <img src="readme_and_testing_media/messagesent.png" alt="Message sent success message">
  <img src="readme_and_testing_media/enquiryemail.png" alt="Customer enquiry email">
  <img src="readme_and_testing_media/confirmationemail.png" alt="Customer enquiry confirmation email">
  <img src="readme_and_testing_media/checkoutsuccess.png" alt="Checkout success">
  <img src="readme_and_testing_media/orderconfirmationemail.png" alt="Order confirmation email">
<hr>

- A custom 404 page that informs the user the page they are looking for hasn't been found with a button directing them back to the homepage.

    <img src="readme_and_testing_media/404.png" alt="404 page">
<hr>

- A back to top button on the products page which only appears when the customer begins scrolling down.

  <img src="readme_and_testing_media/bttbutton.png" alt="Back to top button">
<hr>

- Defensive programming has been used throughout the development of the application, to prompt users when they are either about to permanently delete something that cannot be done such as a product or discount code, as well as to stop users accessing pages they aren't authorised to access, for instance any page that requires a user to be logged in or for a user to be a super user.

  <img src="readme_and_testing_media/deleteproductmodal.png" alt="Delete product modal">
  <img src="readme_and_testing_media/defensiveerror.png" alt="Not super user error message">

<hr>

- An intuitive stock management system which checks stock values before allowing a user to place an order in case someone else has made an order since they added the product to their cart, as well updating the stock counts dynamically as and when orders are placed.

  <img src="readme_and_testing_media/stockerror.png" alt="Not enough stock error message">

<hr>


### Future Features

Given additioanl time and resource some future features that I would like to encorporate into this project are...

- The abilitiy to sign up and sign in using social accounts such as google or facebook.
- To restric reviews so that a personal can only review a product that they have previously purchased
- For the user to be able to store favourite products or a wishlist
- Product recommendations based on previous purchases and also other similar user profiles
- Abdandoned cart recovery
- A loyalty program
- A feature where users can request notification emails when their favourite products come back into stock

### Accessibility
-   The use of semantic HTML.
-   Ensuring the colours and text use meet accessibility standards set by [w3.org](https://www.w3.org/TR/WCAG21/).
-   Ensuring all clickable buttons and links are tabbable using the keyboard.
-   Using descriptive alt tags on all images.
-   Using correct aria labels where necessary.
-   Being mindful in the creation of the design to ensure it is intuitive and as easy to navigate as possible.

### Development Process
As well as using [Figma](https://www.figma.com/) to create wireframes and flow charts for this project, I also used Figma's Kanban template to keep track of tasks as I found the "sticky note" style more user friendly and it suited my style of task management better.

You can view the Kanban board [here](https://www.figma.com/file/rspHu8qzVH35mFzarGLARC/Keto-Kreations-Kanban?type=whiteboard&node-id=0%3A1&t=CzMSWuqP3I3DBtYb-1).

<img src="readme_and_testing_media/kanban.png" alt="Screenshot of Kanban board">

[Back to top](#title)  

## Technologies Used

### Languages Used
-   HTML
-   CSS
-   Vanilla javaScript
-   Python


### Databases Used
-   sqlite3 in development - A relational database
-   PostgreSQL via ElephantSQL in production - A relational database

### Frameworks, Libraries & Programs Used

-   [Amazon AWS](https://aws.amazon.com/) - For static file storage
-   [Bootstrap](https://getbootstrap.com/) - Version 5.3.0 - For the layout and framework of the website, it was also used to create the various modals which were then restyled to match the rest of the website.
-   [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - For AWS implementation
-   [Cloud Convert](https://cloudconvert.com/) - To compress and convert images to webp.
-   [Code Institute PEP8 Python Linter](https://pep8ci.herokuapp.com/) - To check for linting errors in my python code.
-   [Coolors](https://coolors.co/) - To check contrast and accessibility of the colours I chose to use.
-   [ElephantSQL](https://www.elephantsql.com/) - To host my PostgreSQL database
-   [Figma](https://www.figma.com/) - To create the wireframes, user journey flow chart and database schema flow chart as well as the Kanban feature to manage the development process.
-   [dj-database-url](https://pypi.org/project/dj-database-url/) - So that I can use databse URLs in Django
-   [Django](https://www.djangoproject.com/) - An open source python web framework
-   [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - For Django form styling
-   [Font Awesome](https://fontawesome.com/) - Used for the GitHub icon used in the footer button.
-   [Figma](https://www.figma.com/) - For my wireframes, database schema diagram and also as a Kanban board for project management
-   [Git](https://git-scm.com/) - For version control.
-   [GitHub](https://github.com/) - To store website files and repository for the website.
-   [Google Dev Tools](https://developer.chrome.com/docs/devtools) - Built into the chrome browser to test features and design and to troubleshoot as I went along as well as for testing later on using tools such a Lighthouse.
-   [Google Fonts](https://fonts.google.com/) - To import the fonts I chose for the website.
-   [Gmail](https://mail.google.com/) - As my email hosting provider
-   [Gunicorn](https://gunicorn.org/) - As a HTTP server within my Heroku app
-   [Heroku](https://www.heroku.com/) - To host my application
-   [JSHint](https://jshint.com/) - To validate and test javaScript code.
-   [Mini Webtool](https://miniwebtool.com/django-secret-key-generator/) - To generate a secret key for Django
-   [Pillow](https://pillow.readthedocs.io/en/stable/) - For image processing in Django 
-   [Psycopg2](https://pypi.org/project/psycopg2/) - To more easily manage my PostgrSQL databse using Python
-   [Siege Media](https://www.siegemedia.com/contrast-ratio) - To check contrast and accessibility of the `rgba` colours I chose to use.
-   [Stripe](https://stripe.com/gb) - For payment processing
-   Lighthouse - Built into Google Dev Tools for testing.
-   [SQLAlchemy](https://www.sqlalchemy.org/) - Database abstraction library, used to interact with PostgreSQL.
-   [VS Code](https://code.visualstudio.com/) - Was used as my code editor to write code, version control using git and pushing changes for storage to GitHub.
-   [Website Mockup Generator](https://websitemockupgenerator.com/) - To create the website mockup images at the top of the README.
-   [W3C](https://www.w3.org/) - To validate and test HTML and CSS code.


[Back to top](#title)  

## Testing

Please see [TESTING.md](TESTING.md) for all testing performed


## Deployment

The project was deployed to [Heroku](https://www.heroku.com/) using a free relational database from [ElephantSQL](https://www.elephantsql.com/). Before deploying to Heroku I would first set up the database so I will explain the deployment in 2 two parts.

### ElephantSQL

1. Navigate to [ElephantSQL.com](https://www.elephantsql.com/) and click “Get a managed database today”

2. Select “Try now for FREE” in the TINY TURTLE database plan.

3. Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account.

4. In the Create new team form:
    - Add a team name (your own name is fine)
    - Read and agree to the Terms of Service
    - Select Yes for GDPR
    - Provide your email address
    - Click “Create Team”

5. Your account should now be successfully created.

6. Click “Create New Instance”.

7. Set up your plan:
    - Give your plan a Name (this is commonly the name of the project)
    - Select the Tiny Turtle (Free) plan
    - You can leave the Tags field blank

8. Select a data centre closest to you - I used EU-West-1 (Ireland).

9. Click "Review".

10. Check your details are correct and then click “Create instance”.

11. Your database should now be successfully created.

12. Return to the ElephantSQL dashboard and click on the database instance name for this project.

13. In the URL section, clicking the copy icon will copy the database URL to your clipboard. Keep this tab open as we will need this URL later.

### Heroku

1. To successfully deploy on Heroku we first to install some dependencies to that you can use Postgres on your deployed site. 

    ```bash
    pip3 install dj_database_url
    pip3 install psycopg2
    ```

2. We then need to create some files: a requirements.txt file and a Procfile.

3. The requirements.txt file contains all the applications and dependencies that are required to run the app. To create the requirements.txt file run the following command in the terminal:

    ```bash
    pip3 freeze --local > requirements.txt
    ```

4. The Procfile tells Heroku which files run the app and how to run it. To create the Procfile run the following command in the terminal:

    ```bash
     web: gunicorn [your app name].wsgi:application
    ```

5. If the Procfile has been created correctly it will have the Heroku logo next to it. It is also important to check the Procfile contents, as sometimes on creation a blank line will be added at the end of the file. This can sometimes cause problems when deploying to Heroku, so if the file contains a blank line at the end, delete this and save the file. Make sure to save both these files and then add, commit and push them to GitHub.

6. Login (or sign up) to [Heroku.com](https://www.heroku.com).

7. Click the new button and then click create new app.

8. You will then be asked to give your app a name (these must be unique) and select a region. Once these are completed click create app.

9. You will now need to connect the Heroku app to the GitHub repository for the site. Select GitHub in the deployment section, find the correct repository for the project and then click connect.

10. Once the repository is connected, you will need to provide Heroku some config variables it needs to build the app. Click on the settings tab and then click reveal config vars button. You will now need to add the environment key/value variables some of which were used in the env.py file and some of which will be different:

    | KEY | VALUE |
    | -- | -- |
    | AWS_ACCESS_KEY_ID | `your variable here if you have it already` |
    | AWS_SECRET_ACCESS_KEY | `your variable here if you have it already` |
    | DISABLE_COLLECTSTATIC | 1* |
    | DATABASE_URL | `your variable here`** |
    | EMAIL_HOST_PASS | `your variable here` |
    | EMAIL_HOST_USER | `your variable here` |
    | SECRET_KEY | `your variable here` |
    | STRIPE_PUBLIC_KEY | `your variable here` |
    | STRIPE_SECRET_KEY | `your variable here` |
    | STRIPE_WH_SECRET | `your variable here` |
    | USE_AWS | True |
    | DEVELOPMENT | True*** |

    *This is temporary and will be removed later.

    **This is where we paste our URL from step 13 in ElephantSQL section.

    ***This variable is to be deleted once debugging is complete and you are ready to deploy your "production" app.

11. You then need to add the hostname of your Heroku app to settings.py which can be found in the Heroku settings tab under Domains.

    ```bash
    ALLOWED_HOSTS = ['keto-kreations-25ff0a2cbc9e.herokuapp.com', 'localhost']
    ```

12. We now need to migrate our database to our ElephantSQL databse. Go to the top right hand of Heroku and select, more then select Run console. Type bash and click Run then type the following commands.

    ```bash
    python3 manage.py makemigrations --dry-run
    python3 manage.py makemigrations
    python3 manage.py migrate --plan
    python3 manage.py migrate
    ```
    
13. Assuming all your migrations were completed succesfully you can now create your superuser by running the below command and filling in your details.

      ```bash
      python3 manage.py createsuperuser    
      ```

14. Now that the relational database has been set up and the tables created and superuser created, we can now click open app and the application should now open in a new tab. If you haven't set up your AWS yet your CSS and images wont have loaded yet. We will set that up next.

### Amazon AWS

  #### Setting up an S3 Bucket
  1. Create an [Amazon AWS](aws.amazon.com) account

  2. Search for **S3** and create a new bucket
      - Allow public access
      - Acknowledge

  3. Under **Properties > Static** website hosting
      - Enable
      - `index.html` as index document
      - Save

  4. Under **Permissions > CORS** use:
      ```bash
          [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
      ]
      ```

  5. Under **Permissions > Bucket Policy**:
      - Generate Bucket Policy and take note of **Bucket ARN**
      - Chose **S3 Bucket Policy** as Type of Policy
      - For **Principal**, enter `*`
      - Enter **ARN** noted above
      - **Add Statement**
      - **Generate Policy**
      - Copy **Policy JSON Document**
      - Paste policy into **Edit Bucket policy** on the previous tab
      - Save changes

  6. Under **Access Control List (ACL)**:
      - For **Everyone (public access)**, tick **List**
      - Accept that everyone in the world may access the Bucket
      - Save changes

  #### Setting up AWS IAM
  1. From the **IAM dashboard** within AWS, select **User Groups**:
      - Create new group e.g. `manage-keto-kreations`
      - Click through without adding a policy
      - **Create Group**

  2. Select **Policies**:
      - Create policy
      - Under **JSON** tab, click **Import managed policy**
      - Choose **AmazongS3FullAccess**
      - Edit the resource to include the **Bucket ARN** noted earlier when creating the Bucket Policy:

      ```bash
            "Resource": [
                            "arn:aws:s3:::keto-kreations",
                            "arn:aws:s3:::keto-kreations/*"
                  ]
      ```

      - Click **next step** and go to **Review policy**
      - Give the policy a name e.g. `keto-kreations-policy` and description
      - **Create policy**

  3. Go back to **User Groups** and choose the group created earlier
      - Under **Permissions > Add permissions**, choose **Attach Policies** and select the one just created
      - **Add permissions**

  4. Under **Users**:
      - Choose a user name e.g. `keto-kreations-staticfiles-user`
      - Select **Programmatic access** as the **Access type**
      - Click Next
      - Add the user to the Group just created
      - Click Next and **Create User**

  5. **Download the `.csv` containing the access key and secret access key. This will NOT be available to download again**

  #### Hooking Django up to S3

  1. Install boto3 and django-storages
      ```bash
      pip3 install boto3
      pip3 install django-storages
      pip3 freeze > requirements.txt
      ```

  2. Add the values from the `.csv` you downloaded to your Heroku Config Vars under Settings:
      ```bash
      AWS_ACCESS_KEY_ID
      AWS_SECRET_ACCESS_KEY
      ```

  3. Delete the `DISABLE_COLLECTSTATIC` variable from your Config Vars and deploy your Heroku app, if you have enabled automatic deployment in Heroku this will happen automatically the next push you make to GitHub

  4. With your S3 bucket now set up, you can create a new folder called `media` (at the same level as the newly added `static` folder) and upload any required media files to it, making sure they are publicly accessible under **Permissions**


### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Login to GitHub.
2. Locate the repository, you can use a link you have been provided with or use the search function in the top left of the screen.
3. In the top right hand corner of the page locate and click the 'fork' button.
4. Near the bottom of the page click the green button that says 'Create Fork'.
5. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Login to GitHub.
2. Locate the repository, you can use a link you have been provided with or use the search function in the top left of the screen.
3. Near the top of the repository click the green 'Code' button.
4. To clone the repository using HTTPS, under HTTPS copy the link provided.
5. Open the terminal in your code editor. 
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type git clone, and then paste the URL you copied in Step 3.
8. Press Enter. Your local clone should be created.
9. To install all the required dependencies you just need to run the following...
    ```bash
    pip3 install -r requirements.txt
    ```

[Back to top](#title)  

## Credits

### Code

-   Social Media Integration for Facebook, LinkedIn & Google - Code from [Abi Harrison Meta Tags Webinar](https://www.youtube.com/watch?v=t-4qqmikIqk).

All other small code snippets used are referenced in the code as a comment.

All other code was written by the developer.

### Content

-   Ingredients, allergens, product descriptions and nutritional information is made up data using ChatGPT
-   All other static content for this website was written by the developer.
 

### Media

-   Logo - The logo was created using [Logo.com](https://logo.com/)

### Acknowledgements

I 100% couldn't have completed this project on my own so would like to acknowledge the following people for their contributions, whether they know they helped or not...

-   My Fiancé and children for their unwavering support.
-   [Iris Smok](https://github.com/Iris-Smok) my cohort facilitator for her support and for checking in on me when I have had to take some time away from the keyboard.
-   [Martina Terlevic](https://github.com/SephTheOverwitch) for her advice and support.
-   The [Code Institute](https://codeinstitute.net/) student support for checking in on me when it seems I might have gone MIA.
-   The people on my cohort for their support, encouragement and for reviewing my project.

[Back to top](#title)  