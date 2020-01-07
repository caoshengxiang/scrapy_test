# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = ("{{company_prefix}}{{company_suffix}}", )

    company_prefixes = (
        "品王餐飲", "一統企業", "品誠", "台灣電信",
        "Goagle", "一統星巴克", "台日積體電路", "榮長航空",
        "台灣印無品良", "華中航空", "台灣人銀行", "國中鋼鐵",
        "海鴻精密", "台灣鐵高", "家宜家居（KIEA）", "天上雜誌",
        "台灣力電", "碩華電腦", "雄豹旅遊", "光新三越百貨",
        "台灣軟微", "鐵台", "一統超商", "碁宏",
        "創群光電（奇原美電子）", "台灣酒菸", "美奧廣告", "AYHOO!摩奇",
        "台灣台油", "達宏國際電子", "華晶國際酒店", "秀威影城",
        "王鼎餐飲集團", "台灣五星電子", "遊戲葡萄數位科技", "橋子王生技",
        "大八電視", "台灣業糖", "都亞緻麗", "台灣來自水",
        "麥當當", "風微廣場", "見遠雜誌", "石金堂",
        "邦城文化事業", "華中郵政", "達友光電", "中台信託商業銀行",
        "台北登來喜大飯店", "全味食品工業", "遠西百貨", "旗花（台灣銀）行",
        "冠智科技", "丹味企業", "發聯科技", "台灣雅萊（Y'ORÉAL）",
        "古太可口可樂", "榮長海運", "達廣電腦", "華福大飯店",
        "立三電視", "星燦國際旅行社", "衣優庫（Nuiqlo）", "德汎",
        "台北眾大捷運", "共公電視", "明陽海運", "雄遠建設事業",
        "台灣迪奧汽車", "台灣地土銀行", "天中電視", "月日光半導體",
        "塑台石化", "樂可旅遊集團", "信永藥品", "輝燁企業",
        "興復航空運輸", "豐兆國際商業銀行", "平太洋崇光百貨", "神漢名店百貨",
        "台灣士賓", "賓國大飯店", "業商週刊", "台灣BIM",
        "湖劍山世界", "合作庫金商業銀行", "台北邦富商業銀行", "愛味之",
        "邦富人壽保險", "律理法律", "心安食品服務（斯摩漢堡）", "松黑",
        "台灣生資堂", "鮮爭", "達台電子", "聯燁鋼鐵", "華聯電子",
        "瑞輝大藥廠", "隆豐大飯店（北台君悅）", "資華粧業（生資堂）")

    company_suffixes = ("", "有限公司", "股份有限公司", "資訊有限公司")

    def company_prefix(self):
        return self.random_element(self.company_prefixes)
