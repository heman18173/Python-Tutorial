import unittest
from survey import ASurvey

class ASurveyTest(unittest.TestCase):
    
    def setUp(self):
        """
        Create class to test with setUp Method
        """
        question = "What language you learn first?"
        self.my_survey = ASurvey(question)
        self.responses =  ['Gujarati', 'Hindi', 'English']
        
    """Test asurvey calss"""
    def test_store_single_response(self):
        """Test that single response is stored """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
       
    def test_store_3_response(self):
        """Test 3 responses """
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)    

unittest.main()


