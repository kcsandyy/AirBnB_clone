AirBnB clone - Web static
HTML
CSS

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

TASKS

0. Inline styling
A HTML page that displays a header and a footer

1. Head styling
A HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

2. CSS files
HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

3. Zoning done!
 HTML page that displays a header and footer by using CSS files (same as 2-index.html)

Layout:

Common:
no margin
no padding
font color: #484848
font size: 14px
font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
icon in the browser tab
Header:
color: white
height: 70px
width: 100%
border bottom 1px #CCCCCC
logo align on left and center vertically (20px space at the left)
Footer:
color white
height: 60px
width: 100%
border top 1px #CCCCCC
text Best School center vertically and horizontally
always at the bottom at the page

4. Search!
HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on 3-index.html)

Container:
between header and footer tags, add a div:
classname: container
max width 1000px
margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
center horizontally
Filter section:
tag section
classname filters
inside the .container
color white
height: 70px
width: 100% of the container
border 1px #DDDDDD with radius 4px
Button search:
tag button
text Search
font size: 18px
inside the section filters
background color #FF5A5F
text color #FFFFFF
height: 48px
width: 20% of the section filters
no borders
border radius: 4px
center vertically and at 30px of the right border
change opacity to 90% when the mouse is on the button

5. More filters
 HTML page that displays a header, footer and a filters box.

Layout: (based on 4-index.html)

Locations and Amenities filters:
tag: div
classname: locations for location tag and amenities for the other
inside the section filters (same level as the button Search)
height: 100% of the section filters
width: 25% of the section filters
border right #DDDDDD 1px only for the first left filter
contains a title:
tag: h3
font weight: 600
text States or Amenities
contains a subtitle:
tag: h4
font weight: 400
font size: 14px
text with fake contents
Requirements:

You must use: header, footer, section, button, h3, h4 tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 4 CSS files:
styles/4-common.css: for the global style (body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/5-filters.css: for the filters style

6. It's (h)over
 HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on 5-index.html)

Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
tag ul
classname popover
text should be fake now
inside each div
not displayed by default
color #FAFAFA
width same as the div filter
border #DDDDDD 1px with border radius 4px
no list display
Location filter has 2 levels of ul/li:
state -> cities
state name must be display in a h2 tag (font size 16px)
Requirements:

You must use: header, footer, section, button, h3, h4, ul, li tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 4 CSS files:
styles/4-common.css: for the global style (body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/6-filters.css: for the filters style

7. Display results
 HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 6-index.html)

Add Places section:
tag: section
classname: places
same level as the filters section, inside .container
contains a title:
tag: h1
text: Places
align in the top left
font size: 30px
contains multiple “Places” as listing (horizontal or vertical) describe by:
tag: article
width: 390px
padding and margin 20px
border #FF5A5F 1px with radius 4px
contains the place name:
tag: h2
font size: 30px
center horizontally
Requirements:

You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 5 CSS files:
styles/4-common.css: for the global style (i.e. body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for footer style

8. More details
HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on 7-index.html)

Add more information to a Place article:

Price by night:
tag: div
classname: price_by_night
same level as the place name
font color: #FF5A5F
border: #FF5A5F 4px rounded
min width: 60px
height: 60px
font size: 30px
align: the top right (with space)
Information section:
tag: div
classname: information
height: 80px
border: top and bottom #DDDDDD 1px
contains (align vertically):
Number of guests:
tag: div
classname: max_guest
width: 100px
fake text
icon
Number of bedrooms:
tag: div
classname: number_rooms
width: 100px
fake text
icon
Number of bathrooms:
tag: div
classname: number_bathrooms
width: 100px
fake text
icon
User section:
tag: div
classname: user
text Owner: <fake text>
Owner text should be in bold
Description section:
tag: div
classname: description

9. Full details
 HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 8-index.html)

Add more information to a Place article:

List of Amenities:
tag div
classname amenities
margin top 40px
contains:
title:
tag h2
text Amenities
font size 16px
border bottom #DDDDDD 1px
list of amenities:
tag ul / li
no list style
icons on the left: Pet friendly, TV, Wifi, etc… feel free to add more
List of Reviews:
tag div
classname reviews
margin top 40px
contains:
title:
tag h2
text Reviews
font size 16px
border bottom #DDDDDD 1px
list of review:
tag ul / li
no list style
a review is described by:
h3 tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
p tag for the text (font size 12px)

10. Flex
Improve the Places section by using Flexible boxes for all Place articles

Flexbox Froggy

11. Responsive design
Improve the page by adding responsive design to display correctly in mobile or small screens.

Examples:

no horizontal scrolling
redesign search bar depending of the width
etc.
12. Accessibility
Improve the page by adding Accessibility support

Examples:

Colors contrast
Header tags
etc.


