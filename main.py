# Developer: Jeremy Moser
# Created Date: Wednesday, February 1st, 2023
# Last Modified Date: Tuesday, January 31st, 2023

import time
from wonderwords import RandomWord
import webbrowser
import keyboard

# Initiate i and count variables and values
i = 1
count = 4

# While loop to iterate from i value to count value
while i <= count:
    # Generate a random word utilizing RandomWord
    rw = RandomWord()
    unique_word = rw.word()
    # Build URL and perform search using default browser
    request_url = "https://www.bing.com/search?q=" + unique_word
    webbrowser.open(request_url)
    print("#" + str(i) + ": " + unique_word)
    # Increment i
    i += 1
    # Wait 3 seconds before continuing
    time.sleep(3.5)
    # Close current browser tab and loop
    keyboard.press_and_release("cmd+w")
