import json
from watson_developer_cloud import AlchemyLanguageV1


class SentAnalysis:

    def __init__(self):
        self.key = '41cf0a29262eb4e33fa32de1ab61106be23a91d4'
        self.alchemy_language = AlchemyLanguageV1(api_key=self.key)

    def get_sentiment3(self, text1, text2, text3):
        q1 = json.dumps(self.alchemy_language.combined(text=text1, extract='doc-emotion', sentiment=1, max_items=1), indent=2)
        q2 = json.dumps(self.alchemy_language.combined(text=text2, extract='doc-emotion', sentiment=1, max_items=1), indent=2)
        q3 = json.dumps(self.alchemy_language.combined(text=text3, extract='doc-emotion', sentiment=1, max_items=1), indent=2)
        return q1, q2, q3

    def get_sentiment(self, text):
        return json.dumps(self.alchemy_language.combined(text='I would tell him to back off, and that I need to be alone. ', extract='doc-emotion', sentiment=1, max_items=1), indent=2)
