"""Make a program that takes a user inputed website and turn it into console text.
Like if they were to take a blog post what would show up is the text on the post


Differents Links examples:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
https://www.stereogum.com/2025831/frou-frou-reuniting-for-2019-tour/tour-dates/
https://medium.freecodecamp.org/dynamic-class-definition-in-python-3e6f7d20a381


"""
from scrapy import simple_get
from bs4 import BeautifulSoup

# Summary of the script:
# Basically, takes the url from the user
# checks if the url is valid (OK 200 response)
# then with the help of beautifulsoup library transform the url to a pretify html ready to extract specific content
# Because depending on the class, id and naming the content of the post may vary 
# I provide a couple of examples and a simple method that checks commoms naming for the post content
# After finding the correct the specific tag the library will extract only the text wiht the '.text' call

if __name__ == '__main__':

    def check_content_div(html):

        if html.find(class_= "post_body"):
            return html.find(class_= "post_body").text

        if html.find(class_= "section-content"):
            return html.find(class_= "section-content").text

        if html.find(class_= "article-content clearfix"):
            return html.find(class_= "article-content clearfix").text


    url = input("Hello user enter your BlogPost: ")
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')

    content = check_content_div(html)



    print("\n" + content + "\n")




