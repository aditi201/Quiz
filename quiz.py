class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     """Q1. In Python, Dictionaries are immutable \n(a)False\n(b)True\n""",
     """Q2. What is the output of the following dictionary operation
     dict1 = {"name": "Mike", "salary": 8000}
     temp = dict1.pop("age")
     print(temp)
     
(a)KeyError: ‘age’
(b)None\n""",
     """Q3. Please select all correct ways to empty the following dictionary
     student = { 
       "name": "Emma", 
       "class": 9, 
       "marks": 75 
     }
     
(a)del student
(b)del student[0:2]
(c)student.clear()\n""",
     """Q4.Items are accessed by their position in a dictionary and All the keys in a dictionary must be of the same type.
(a)True
(b)False\n""",
     """Q5.Dictionary keys must be immutable
(a)True
(b)False\n"""
    
     
     
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "b"),
     Question(question_prompts[4], "a"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))
     p=score/len(questions)*100;
     if(p<45):
          print("u need to work hard, u got only",p,"%")
     else:
          print("gud")

run_quiz(questions)
