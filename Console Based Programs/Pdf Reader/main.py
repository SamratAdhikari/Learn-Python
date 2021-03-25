# PDF Reader
import PyPDF2
from gtts import gTTS


pdfFile = open("test.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)

mytext = ""

for pageNum in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)

	mytext += pageObj.extractText()

# print(mytext)
pdfFile.close()

tts = gTTS(text=mytext, lang="en")
tts.save("aladin.mp3")


	