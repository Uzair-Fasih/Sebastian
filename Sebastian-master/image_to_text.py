import pytesseract
from PIL import Image
import sys
import json
img=Image.open('test.png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
s= pytesseract.image_to_string(img)
#res=result.encode('utf-8')
res=s.encode('utf-8')
#print(type(res))
#res.encode('ascii','ignore')
#r=json.dumps(s,ensure_ascii=False)
#print(r)
sys.stdout.write(res.decode("utf-8"))




