# Summary of the script:
# Basically, takes the url from the user
# checks if the url is valid (OK 200 response)
# then with the help of beautifulsoup library transform the url to a pretify html ready to extract specific content
# Because depending on the class, id and naming the content of the post may vary 
# I provide a couple of examples and a simple method that checks commoms naming for the post content
# After finding the correct the specific tag the library will extract only the text wiht the '.text' call
