import os
# import pandas as pd

import json

class portfolio:
    def __init__(self, res_path):
        self.path = res_path + "\\data\\portfolio.json"
        self.dct = self.get_dct()

    def get_dct(self):
        with open(self.path) as fi:
            d = json.load(fi)
        return d