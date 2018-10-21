'''
CLASS: Web Scraping with Beautiful Soup
What is web scraping?
- Extracting information from websites (simulates a human copying and pasting)
- Based on finding patterns in website code (usually HTML)
What are best practices for web scraping?
- Scraping too many pages too fast can get your IP address blocked
- Pay attention to the robots exclusion standard (robots.txt)
- Let's look at http://www.facebook.com/robots.txt
What is HTML?
- Code interpreted by a web browser to produce ("render") a web page
- Let's look at example.html
- Tags are opened and closed
- Tags have optional attributes
How to view HTML code:
- To view the entire page: "View Source" or "View Page Source" or "Show Page Source"
- To view a specific part: "Inspect Element"
- Safari users: Safari menu, Preferences, Advanced, Show Develop menu in menu bar
- Let's inspect example.html
'''

# read the HTML code for a web page and save as a string
# with open('example.html', 'rU') as f:
#    html = f.read()

# read the HTML code using requests
import requests
<<<<<<< HEAD
<<<<<<< HEAD
url = "https://raw.githubusercontent.com/ga-students/DC-DSI-3/master/curriculum/05-week/5.08-getting-data/code/example.html?token=AWPwgCbwBpoZMVW1QNHWjqDa4_e6juVBks5YWrYnwA%3D%3D"
html = requests.get(url)

# convert HTML into a structured Soup object
from bs4 import BeautifulSoup
b = BeautifulSoup(html.text)

# print out the object
print (b)
print (b.prettify())
=======
html = requests.get()
=======
url = "https://raw.githubusercontent.com/ga-students/DC-DSI-3/master/curriculum/05-week/5.08-getting-data/code/example.html?token=AWPwgCbwBpoZMVW1QNHWjqDa4_e6juVBks5YWrYnwA%3D%3D"
html = requests.get(url)
>>>>>>> d46954cd5e7783041a111cdd734fec00ff86db88

# convert HTML into a structured Soup object
from bs4 import BeautifulSoup
b = BeautifulSoup(html.text)

# print out the object
<<<<<<< HEAD
print b
print b.prettify()
>>>>>>> 036367a6aad4a887a3d52b3cad2d170153f71140
=======
print (b)
print (b.prettify())
>>>>>>> d46954cd5e7783041a111cdd734fec00ff86db88

# 'find' method returns the first matching Tag (and everything inside of it)
b.find(name='body')
b.find(name='h1')

# Tags allow you to access the 'inside text'
b.find(name='h1').text

# Tags also allow you to access their attributes
b.find(name='h1')['id']

# 'find_all' method is useful for finding all matching Tags
b.find(name='p')        # returns a Tag
b.find_all(name='p')    # returns a ResultSet (like a list of Tags)

# ResultSets can be sliced like lists
len(b.find_all(name='p'))
b.find_all(name='p')[0]
b.find_all(name='p')[0].text
b.find_all(name='p')[0]['id']

# iterate over a ResultSet
results = b.find_all(name='p')
for tag in results:
<<<<<<< HEAD
<<<<<<< HEAD
    print (tag.text)
=======
    print tag.text
>>>>>>> 036367a6aad4a887a3d52b3cad2d170153f71140
=======
    print (tag.text)
>>>>>>> d46954cd5e7783041a111cdd734fec00ff86db88

# limit search by Tag attribute
b.find(name='p', attrs={'id':'scraping'})
b.find_all(name='p', attrs={'class':'topic'})
b.find_all(attrs={'class':'topic'})

# limit search to specific sections
b.find_all(name='li')
b.find(name='ul', attrs={'id':'scraping'}).find_all(name='li')

'''
EXERCISE ONE
'''

# find the 'h2' tag and then print its text
<<<<<<< HEAD
<<<<<<< HEAD
results2 = b.find_all(name='h2')
for tag in results2:
    print (tag.text)

# find the 'p' tag with an 'id' value of 'lab' and then print its text
results3=b.find(name='p', attrs={'id':'lab'})
print(results3)

# find the first 'p' tag and then print the value of the 'id' attribute
b.find_all(name='p')[0]['id']


# print the text of all four resources
results3=b.find_all(name='li')
for tag in results3:
    print (tag.text)
# print the text of only the API resources

results2 = b.find_all(name='ul',attrs={'id':'api'})
for tag in results2:
    print (tag.text)
=======
=======
results2 = b.find_all(name='h2')
for tag in results2:
    print (tag.text)
>>>>>>> d46954cd5e7783041a111cdd734fec00ff86db88

# find the 'p' tag with an 'id' value of 'lab' and then print its text
results3=b.find(name='p', attrs={'id':'lab'})
print(results3)

# find the first 'p' tag and then print the value of the 'id' attribute
b.find_all(name='p')[0]['id']


# print the text of all four resources
results3=b.find_all(name='li')
for tag in results3:
    print (tag.text)
# print the text of only the API resources

<<<<<<< HEAD
>>>>>>> 036367a6aad4a887a3d52b3cad2d170153f71140
=======
results2 = b.find_all(name='ul',attrs={'id':'api'})
for tag in results2:
    print (tag.text)
>>>>>>> d46954cd5e7783041a111cdd734fec00ff86db88
