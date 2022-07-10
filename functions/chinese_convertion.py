# -*- coding: utf-8 -*-

import opencc

def switch_chinese(character, type="s2t"):
    """switch traditional chinese and simplified chinese
    s2t.json 简体到繁体
    t2s.json 繁体到简体
    s2tw.json 简体到台湾正体
    tw2s.json 台湾正体到简体
    s2hk.json 简体到香港繁体（香港小学学习字词表标准）
    hk2s.json 香港繁体（香港小学学习字词表标准）到简体
    s2twp.json 简体到繁体（台湾正体标准）并转换为台湾常用词汇
    tw2sp.json 繁体（台湾正体标准）到简体并转换为中国大陆常用词汇
    t2tw.json 繁体（OpenCC 标准）到台湾正体
    t2hk.json 繁体（OpenCC 标准）到香港繁体（香港小学学习字词表标准）
    t2jp.json 繁体（OpenCC 标准，旧字体）到日文新字体
    jp2t.json 日文新字体到繁体（OpenCC 标准，旧字体）
    hk2t.json 香港繁体（香港小学学习字词表标准）到繁体（OpenCC 标准）
    tw2t.json 台湾正体到繁体（OpenCC 标准）
    """
    if type == "s2t":
        js = "s2t.json"
    else:
        js = "t2s.json"

    converter = opencc.OpenCC(js)
    return converter.convert(character)
