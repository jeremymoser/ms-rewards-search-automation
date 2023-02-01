# Developer: Jeremy Moser
# Created Date: Wednesday, February 1st, 2023
# Last Modified Date: Tuesday, January 31st, 2023

import time
from wonderwords import RandomWord
import webbrowser
import keyboard

def perform_search():
    # Initiate variables
    counter = 1
    searches = 2

    print("Today's searches include:")
    print("=========================")

    # While loop to iterate from counter to searches value
    while counter <= searches:
        # Generate a random word utilizing RandomWord
        rw = RandomWord()
        unique_word = rw.word()
        # Build URL and perform search using default browser
        request_url = "https://www.bing.com/search?q=" + unique_word
        webbrowser.open(request_url)
        print("#" + str(counter) + ": " + unique_word)
        # Increment i
        counter += 1
        # Wait 3.5 seconds before continuing
        time.sleep(3.5)
    # Close current browser
    keyboard.press_and_release("ctrl+shift+w")
    print("=========================")

perform_search()