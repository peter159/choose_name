# -*- coding: utf-8 -*-

from functions import switch_chinese, Pingge, Stroke
from choose_name.algorithms import Wuge

if __name__ == "__main__":
    # stroke = Stroke()
    # pg = Pingge(surname=switch_chinese("林"), name=switch_chinese("谊"), stroke_model=stroke)
    # # pg = Pingge(surname=switch_chinese("林"), name=switch_chinese("胤"), stroke_model=stroke)
    # # pg = Pingge(surname=switch_chinese("林"), name=switch_chinese("子馨"), stroke_model=stroke)
    # # pg = Pingge(surname=switch_chinese("蒋"), name=switch_chinese("旭岚"), stroke_model=stroke)
    # # pg = Pingge(surname=switch_chinese("俞"), name=switch_chinese("敏"), stroke_model=stroke)
    # # pg = Pingge(surname=switch_chinese("陆"), name=switch_chinese("天然"), stroke_model=stroke)
    # # pg = Pingge(surname=switch_chinese("谢"), name=switch_chinese("冬皓"), stroke_model=stroke)
    # print("tiange - 祖先: ", pg.tiange())
    # print("renge - 一生: ", pg.renge())
    # print("dige - 前半生: ", pg.dige())
    # print("zongge - 中老年: ", pg.zongge())
    # print("waige - 灵运: ", pg.waige())
    wg = Wuge("林", "谊", ctype="simplified")
    print(wg.explain())
