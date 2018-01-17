from survey import ASurvey

#Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = ASurvey(question)
#Show the question
my_survey.show_question()
print("Enter q to quit:")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show survey results
print("\n Thank you to participate in survey...")
my_survey.show_results()