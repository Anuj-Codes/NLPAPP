# Import
import paralleldots

class API:
    def __init__(self):
        # Setting your API key
        paralleldots.set_api_key('2azu85T1DwAADvRowrfrwEUIBorMElK6kIDK03AVJp8')

    def sentiment_analysis(self,text):
        response =paralleldots.sentiment(text)
        return response

    def Emotion_recognition(self,text):
        response=paralleldots.emotion(text);
        return response

    def NER_recognition(self,text):
        response=paralleldots.ner(text);
        return response