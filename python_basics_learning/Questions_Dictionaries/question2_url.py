"""
Below is an example URL sent from a Web Browser after the user fills in a search form with three search criteria: 
https://example.com/?product=shirt&color=red&size=m
https://example.com/?city=Hokkaido&food=Seafood
https://example.com/?city=Osaka&food=Takoyaki

The part of the URL following the '?' is the query string containing the form values being submited to the server.
Write a program to parse the query string into a dictionary with the search criteria as the keys and the user's choices as the values.
Example Output:

	Search Options {'product': 'shirt', 'color': 'red', 'size': 'm'}
https://www.youtube.com/watch?v=xp1vX15inBg&list=PLyb_C2HpOQSDxe5Y9viJ0JDqGUCetboxB
https://www.programiz.com/python-programming/regex
https://www.datacamp.com/cheat-sheet/regular-expresso
"""
import re
import json 

def url_parse_query(url):
    regex_pattern = r'\?(?P<user_query>.+)'
    # re.search(pattern, string, flags=0). Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding Match. 
    match = re.search(regex_pattern, url)
    # group() returns the substring that was matched by the RE.
    user_query_string = match.group('user_query')
    user_query_params = user_query_string.split("&")
    # print(type(user_query_params))
    user_search_dict = {}
    
    for param in user_query_params:
        # unpack - split returns a list of two elements
        key, value = param.split("=")
        user_search_dict[key] = value
        
    return user_search_dict

def user_url_input():
    url = input("Enter a valid url browser: ")
    return url 

def main():
    url = user_url_input()
    user_search = url_parse_query(url)
    print(json.dumps(user_search, indent=3, sort_keys=False))
    
if __name__ == "__main__":
    main()