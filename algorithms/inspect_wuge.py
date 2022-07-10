# -*- coding: utf-8 -*-

from choose_name.functions import YunshiDict
from choose_name.functions import Pingge, Stroke
from choose_name.functions import switch_chinese
from collections import defaultdict


class Wuge:
    def __init__(self, surname, lastname, ctype="simplified") -> None:
        if ctype == "simplified":
            self.surname = switch_chinese(surname, type="s2t")
            self.lastname = switch_chinese(lastname, type="s2t")
        self.surname = surname
        self.lastname = lastname

    def explain(self):
        stroke = Stroke()
        pg = Pingge(self.surname, self.lastname, stroke_model=stroke)
        yunshi_dict = YunshiDict()
        explainer = defaultdict(list)
        explainer["天格 - 祖先"].extend(yunshi_dict.get_yunshi(pg.tiange()))
        explainer["人格 - 一生"].extend(yunshi_dict.get_yunshi(pg.renge()))
        explainer["地格 - 前半生"].extend(yunshi_dict.get_yunshi(pg.dige()))
        explainer["总格 - 中老年"].extend(yunshi_dict.get_yunshi(pg.zongge()))
        explainer["外格 - 灵运"].extend(yunshi_dict.get_yunshi(pg.waige()))
        return {k: v for k, v in explainer.items()}
