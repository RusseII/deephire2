import json
from watson_developer_cloud import AlchemyLanguageV1


class SentAnalysis:

    def __init__(self):
        self.key = '41cf0a29262eb4e33fa32de1ab61106be23a91d4'
        self.alchemy_language = AlchemyLanguageV1(api_key=self.key)

    def get_sentiment(self, text):
        print(json.dumps(self.alchemy_language.combined(text='I would tell him to back off, and that I need to be alone. ', extract='doc-emotion', sentiment=1, max_items=1), indent=2))


sent = SentAnalysis()
sent.get_sentiment("Fuck off man, this is my customer! ")
