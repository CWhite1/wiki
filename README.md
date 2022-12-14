# CS50 W - Wiki
#### Video Demo:  <https://youtu.be/ZJLr87jQUtg>
#### Project Description:

This is Wiki, Project 1 of CS50's Web Programming in Python and Javascript course. 
> The requirements for this project were to decison a web platform with Django that mirrors the usage and look of the Wikepedia website.

#### Specifications

1. Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry and renders a page that displays the contents of that encyclopedia entry.
* This view renders the contents of the encyclopedia entry by calling the get_entry function in util.py.
* If an entry requested does not exist, the user is presented with an error page stating"Sorry, This Page Does not Exist, Please Create One".
* If the entry requested does exist, the user is presented with a page that displays the content of the entry. The title of the page includes the name of the entry.

2. Index Page: When the user visits index.html the application lists the names of all pages, the user can click on any entry name to be taken directly to that entry page.  

3. Search Input: The user can type any query into the search box in the sidebar to search for an encyclopedia entry.
* If the query matches the name of an encyclopedia entry, the user is directed to that entry’s page.
* If the query does not match the name of an encyclopedia entry, the user is taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.
* If the query or substring is not found in the list of entries, the user is sent to an error_page stating the page does not exist, please create a new page.

4. New Page: Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry.
* Users enter a title for the page and, in a textarea, enter the Markdown content for the page.
* Users click a button at the bottom of the create page to save their new page.
* When the page is saved, if an encyclopedia entry already exists with the same title, the user is presented with an error message.
* If the encyclopedia entry does not exist the new page is saved in entires and the user is taken to the new entry’s page.

5. Edit Page: On each entry page, the user is able to click the edit page link and taken to a page where the user can edit that entry’s Markdown content in a textarea.
* The textarea is pre-populated with the existing Markdown content of the page.
* Once the edits have been made. the user can click a button to save the changes made to the entry.
* Once the entry is saved, the user is redirected back to that entry’s updated page.

6. Random Page: Clicking “Random Page” in the sidebar takes user to a random encyclopedia entry.

7. Markdown to HTML Conversion: On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user. This is done 
through a convert_markdown function is encylopedia_extras.py in the template tags folder.  I learned how to execute this function from a you tube video.

>Issues that Had to be Resolved:  

* I had a few issues with routing in the beginning; especially combining the href links to the list of entires on the entry function; but, was able to solve using 
the <str:name> method in urls.py.  That said, when I needed to use <str:name> again it with the edit function I ran into some issues where the edit page rendered 
instead of the entry page.  This was struggle and surprised me as they were each url was set up to a different function; however, I was able to resolve by placing 
'edit/<str:name/> in the edit url and changing the name=edit and for entry I changed to 'entry/<str:name/> and name=entry.  That said, the backslash at the end was 
also important as I was get a TemplateNotFound error without it. 

 * I also had a few issues with the search bar function not continuing to search for sunbstrings after it found a match.  If the matches were in a row it would 
 continue; however, as soon as it did not find a match it would stop and render the template.  After using the debugging tool and the print function I was able to 
 determine that the issue I was having was due to the indentation of the return statement.  Upon completion, I also have to run a for loop which seems unneccessary, 
 but was the only was I could get the matched_entry_list to display on the html page.  I also had to place another loop in the html page to display the list.  This 
 part of the function looks ugly, but works none the less. 

 * The final issue I had was with the csrf_token on the edit and create page.  I built this program with the desktop version of VS Code and creating a page and 
 editing the forms through page worked fine with the {% csrf_token %} within the form; however, with the online version I received: 
 
 **Forbidden  (403) CSRF verification failed. Request aborted.**

> Reason given for failure:

    Origin checking failed - https://cwhite1-code50-4882659-7v9vg5w7fp4j-8000.preview.app.github.dev does not match any trusted origins.

>I was only able to resolve this issue by adding this to settings.py.  Both create and edit worked well after this.

'''
    CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1',
                        'http://127.0.0.1:8000/',
                        'https://cwhite1-code50-4882659-7v9vg5w7fp4j-8000',
                        'https://cwhite1-code50-4882659-7v9vg5w7fp4j-8000.preview.app.github.dev'
                        ]
'''

* The final issue I had was when a user forgets to put a title in the create page title input, this causes the file to be saved in entries as .md. This causes the 
entire program to crash as when the homepage is rendered, the empty title gives the user a failed Template load error.  This took me a while to determine as I saved 
it like this by accident.  I have remedied this error by putting the **required** attribute in the html page, not allowing the user to submit without either the 
content or the title.  Ideally this should be hardcoded in views.py; which I may choose to do in the future.
