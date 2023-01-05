
# JSON unicode to string
Set ensure_ascii=False in json.dumps() to encode Unicode as-is into JSON

    import json

    unicodeData= {
        "string1": "體",
        "string2": u"\u4f53"
    }
    print("unicode Data is ", unicodeData)

    encodedUnicode = json.dumps(unicodeData, ensure_ascii=False) # use dump() method to write it in file
    print("JSON character encoding by setting ensure_ascii=False", encodedUnicode)

    print("Decoding JSON", json.loads(encodedUnicode))

    unicode Data is  {'string1': '體', 'string2': '体'}
    JSON character encoding by setting ensure_ascii=False {"string1": "體", "string2": "体"}
    Decoding JSON {'string1': '體', 'string2': '体'}
    
    
  最近在看image caption資料集，2017 AI challenge的描述檔是存成json格式，且描述句子是以unicode格式，但是輸出列印不需要手動轉換。
