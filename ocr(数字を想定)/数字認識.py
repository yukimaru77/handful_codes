from PIL import Image
import pyocr

#OCRエンジンを取得する
pyocr.tesseract.TESSERACT_CMD = r'C:/Users/yukit/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
tools = pyocr.get_available_tools()
if len(tools) == 0:
  print("OCRエンジンが指定されていません")
  sys.exit(1)
else:
  tool = tools[0]
#取得完了

  
builder = pyocr.builders.TextBuilder(tesseract_layout=6)

img = Image.open('screen.png') 
img.show()


#画像から文字を読んで、文字列として取り出す。engは数字にも強い。
txt_pyocr = tool.image_to_string(img , lang='eng', builder=builder)

#半角スペースを消す ※読みやすくするため
txt_pyocr = txt_pyocr.replace(',', '').replace(' ', '')

print(txt_pyocr)
