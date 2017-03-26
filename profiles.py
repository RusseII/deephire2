import json
import ats
import sent_analysis


class Profiles:

    def __init__(self):
        ats_obj = ats.ATS()
        self.all_stuff = ats_obj.get_all()

    def get_profiles(self):
        my_sent_analysis = sent_analysis.SentAnalysis()
        for person in self.all_stuff:
            q1, q2, q3 = my_sent_analysis.get_sentiment3(person['answers'][0]['answer_value_01'], person['answers'][0]['answer_value_02'], person['answers'][0]['answer_value_03'])
            d = json.loads(q1)
            e = json.loads(q2)
            f = json.loads(q3)
            person["q1"] = d
            person["q2"] = e
            person["q3"] = f

        print(self.all_stuff)
        return self.all_stuff


profile = Profiles()
profile.get_profiles()
