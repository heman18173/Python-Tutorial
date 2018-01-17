class ASurvey():
    """Collect anonymns answer for a survey """
    def __init__(self, question):
        """ Store a question and prepare to store response """
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question """
        print(self.question)

    def store_response(self, new_response):
        """Store single response of survey """
        self.responses.append(new_response)

    def show_results(self):
        """Show all response """
        print("Survey results:")
        for response in self.responses:
            print("- " + response)
