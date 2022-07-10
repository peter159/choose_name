# -*- coding: utf-8 -*-

# ref: https://github.com/secsilm/zi-dataset

import pandas as pd
from collections import defaultdict


class Stroke:
    def __init__(self, db_path="database/zi-dataset/zi-dataset.tsv") -> None:
        self.db_path = db_path
        self.__get_character_db()

    def __get_character_db(self):
        df = pd.read_csv(self.db_path, sep="\t")
        df = df.loc[
            df["stroke_count"] != "画",
        ]
        df["stroke_count"] = df["stroke_count"].apply(lambda x: int(x.replace("画", "")))
        self.stroke_db = df

    def get_stroke_count(self, character="林"):
        stroke_cnt = defaultdict(int)
        for _, row in self.stroke_db.iterrows():
            stroke_cnt[row["zi"]] = row["stroke_count"]
        return stroke_cnt[character]

    def get_characters(self, stroke_count=3):
        cnt_stroke = defaultdict(list)
        for _, row in self.stroke_db.iterrows():
            cnt_stroke[row["stroke_count"]].append(row["zi"])
        return cnt_stroke[stroke_count]


if __name__ == "__main__":
    stroke = Stroke()
    print(stroke.get_stroke_count("林"))
    print(stroke.get_characters(stroke_count=10))
