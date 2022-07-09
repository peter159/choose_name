# -*- coding: utf-8 -*-

# 三才五格
# ref: http://www.360doc.com/content/14/0208/22/8064468_350840429.shtml

from stroke_count import Stroke


class Pingge:
    def __init__(self, surname, name, stroke_model: Stroke) -> None:
        self.surname = surname
        self.name = name
        if not isinstance(stroke_model, Stroke):
            raise TypeError("{} is not a Stroke class".format(stroke_model))
        else:
            self.stroke_model = stroke_model

    def tiange(self):
        if len(self.surname) == 1:
            return self.stroke_model.get_stroke_count(self.surname) + 1
        else:
            surnames = [c for c in self.surname]
            return sum([self.stroke_model.get_stroke_count(x) for x in surnames])

    def dige(self):
        if len(self.name) == 1:
            return self.stroke_model.get_stroke_count(self.name) + 1
        else:
            names = [c for c in self.name]
            return sum([self.stroke_model.get_stroke_count(x) for x in names])

    def renge(self):
        return self.stroke_model.get_stroke_count(
            self.surname[-1]
        ) + self.stroke_model.get_stroke_count(self.name[0])

    def zongge(self):
        return sum(
            [self.stroke_model.get_stroke_count(sn) for sn in self.surname]
        ) + sum([self.stroke_model.get_stroke_count(n) for n in self.name])

    def waige(self):
        if len(self.surname) == 1:
            return self.zongge() - self.renge() + 1
        else:
            return self.zongge() - self.renge()


if __name__ == "__main__":
    stroke = Stroke()
    # pg = Pingge(surname="司徒", name="世民", stroke_model=stroke)
    # pg = Pingge(surname="李", name="世民", stroke_model=stroke)
    # pg = Pingge(surname="林", name="谊", stroke_model=stroke)
    # pg = Pingge(surname="林", name="胤", stroke_model=stroke)
    pg = Pingge(surname="林", name="道华", stroke_model=stroke)
    # pg = Pingge(surname="谢", name="瑞兰", stroke_model=stroke)
    # pg = Pingge(surname="林", name="子馨", stroke_model=stroke)
    print("tiange - 祖先: ", pg.tiange())
    print("renge - 一生: ", pg.renge())
    print("dige - 前半生: ", pg.dige())
    print("zongge - 中老年: ", pg.zongge())
    print("waige - 灵运: ", pg.waige())
