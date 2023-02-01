# Developer: Jeremy Moser
# Created Date: Monday, January 30th, 2023
# Last Modified Date: Tuesday, January 31st, 2023

import time
from wonderwords import RandomWord
import webbrowser
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=3, minute=30)
def scheduled_job():

    # Initiate i and count variables and values
    i = 1
    count = 30

    # While loop to iterate from i value to count value
    while i <= count:
        # Generate a random word utilizing RandomWord
        rw = RandomWord()
        unique_word = rw.word()

        # Build URL and perform search using default browser
        request_url = "https://www.bing.com/search?q=" + unique_word
        edge_path = "/Macintosh HD/Applications/Microsoft Edge.app"
        webbrowser.register("Edge", None, webbrowser.BackgroundBrowser(edge_path))
        webbrowser.get("Edge").open(request_url)
        print("#" + str(i) + ": " + unique_word)
        # Increment i
        i += 1
        # Wait 3 seconds before continuing
        time.sleep(3.5)


sched.start()
