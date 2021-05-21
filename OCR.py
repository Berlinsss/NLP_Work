from aip import AipOcr

""" My APPID AK SK  """
APP_ID1 = '24147388'
API_KEY1 = 'QU5nINLo2vXhnnljIiBk2BwB'
SECRET_KEY1 = 'sZBkkSKlw876QzTbHXHNmGKvOZLcU9Sy'

APP_ID2 = '24205701'
API_KEY2 = 'YsobyEQFsVQnk9iZkyEqhbU7'
SECRET_KEY2 = 'nAdD3L2Whmxgx0GYGnFHGlFg0jZZ3Mga'

client = AipOcr(APP_ID2, API_KEY2, SECRET_KEY2)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_handwriting(fpath,str):
    image = get_file_content(fpath)

    """ 调用百度OCR手写文字识别, 图片参数为本地图片 """
    #handwriting调用的是手写具体的在ocr.py中，
    results = client.handwriting(image)["words_result"]

    for result in results:
        text = result["words"]
        str = str + '\n' + text

    return str


