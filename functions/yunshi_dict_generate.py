# -*- coding: utf-8 -*-

import pandas as pd
from collections import defaultdict

class YunshiDict:
    def __init__(self) -> None:
        self.__yunshi_dict()

    def get_yunshi(self, key):
        return self.dict_out[key]

    def __yunshi_dict(self):
        """generate yunshi dict from file"""
        df = pd.read_excel("database/wuge-yunshi/yunshi_dict.xlsx")
        dict_out = defaultdict(list)
        for _, row in df.iterrows():
            dict_out[row["key"]].extend([row["value1"], row["value2"]])
        self.dict_out = dict_out

if __name__ == "__main__":
    yunshi_dict = YunshiDict()
    print(yunshi_dict.get_yunshi(23))
    print(YunshiDict().get_yunshi(23))
