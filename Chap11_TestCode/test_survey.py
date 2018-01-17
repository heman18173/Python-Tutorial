import unittest
from survey import ASurvey

class ASurveyTest(unittest.TestCase):
    """Test asurvey calss"""
    def test_store_single_response(self):
        """Test that single response is stored """
        question = "What language you learn first?"
        my_survey = ASurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_3_response(self):
        """Test 3 responses """
        question = "What language you learn first?"
        my_survey = ASurvey(question)
        responses = ['Gujarati', 'Hindi', 'English']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)    

unittest.main()


