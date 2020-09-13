### We will use gtts module to convert the written text into audio. 

#Import the module
!pip install gtts

#call the module
from gtts import gTTS

#import os module to store the audio file
import os


#here is the text you want to convert
text= ' Myself vikas. I am a second year Electronics student'

#choose the language of the audio file 
language= 'en'

#finally convert the text 
speech= gTTS(text=text,lang=language, slow= False)

#save the audio file as text.mp3
speech.save('text.mp3')
