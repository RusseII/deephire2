import urllib2
import json


class ATS:

    def __init__(self):
        self.key = '81UZVRVH3uldQNobChyi65jPLQbFux3f'

    # get all answers to the questionnaire
    def get_response(self, url):
        content = json.loads(urllib2.urlopen(url + self.key).read())
        if not content:
            print("list is empty")
            return None
        return content

    # get names of a particular applicant
    def get_names(self, applicant_id):
        url = 'https://api.resumatorapi.com/v1/applicants/' + applicant_id + '?' + 'apikey='
        response = self.get_response(url)
        return response['first_name'], response['last_name']

    # get answers for a particular questionnaire, of a particular application
    def get_answers(self, applicant_id):
        url = 'https://api.resumatorapi.com/v1/questionnaire_answers/questionnaire_id/questionnaire_20170325222929_1MD9CIFKLEZ58ZAX/applicant_id/' + applicant_id + '?apikey='
        response = self.get_response(url)
        return response

    # main function that should be used to get all data (all information for all applicants)
    def get_all(self):
        url = 'https://api.resumatorapi.com/v1/jobs/job_20170322142227_DYY2JLPRNHJ2TKRE?apikey='
        response = self.get_response(url)
        people = []
        for applicant_id in response['job_applicants']:
            person_info = {}
            first, last = self.get_names(applicant_id['prospect_id'])
            person_info['answers'] = self.get_answers(applicant_id['prospect_id'])
            person_info['first_name'] = first
            person_info['last_name'] = last
            people.append(person_info)
        # print(people)
        return people
#USEAGE
#ats = ATS()
#ats.get_all()

