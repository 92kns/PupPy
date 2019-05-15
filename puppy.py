#puppy

import os
import numpy as np
import math
import webbrowser as wb


class puppy:

    def __init__(self):
        print('what does a good boy do?')

    def bork(self):
        print('bork')
        self._bork_vid()
        #TODO add web api to launch browser to borking videos

    def _bork_vid(self):
        wb.open_new("https://www.youtube.com/results?search_query=bork")

    



if __name__ == "__main__":
    # testing script
    new_pup = puppy()
    new_pup.bork()
    


    

