import pandas as pd
import googletrans
from googletrans import Translator
words = list(map(str,input("enter all words seperated by space: ").split()))

dict = {'Word': words}  

df = pd.DataFrame(dict)

df.to_csv('data.csv') 

translator = Translator()
translations = {}
word = {}
count = 0
print(googletrans.LANGUAGES)
for column in df.columns:
  unique_elements = df[column].unique()
  for element in unique_elements:
    count+= 1
    translations[element] = translator.translate(element, 
    dest=input("Enter code as per above directory for word " + str(count) + " : ") #Code to define destination language
    ).text

print(translations)
