# # Question

# class Question:
#     def __init__(self,text,choices,answer):
#         self.text = text
#         self.choices = choices
#         self.answer = answer

#     def checkAnswer(self,answer):
#         return self.answer == answer

# # Quiz

# class Quiz:
#     def __init__(self,questions):
#         self.questions = questions
#         self.score = 0
#         self.questionIndex = 0

#     def getQuestion(self):
#         return self.questions[self.questionIndex]
    
#     # GONDERILEN SORUYU ALIP EKRANDA GÖSTERMEK VE KULLANICIDAN CEVAP ALMAK
#     def displayQuestion(self): 
#         question = self.getQuestion()
#         print(f'Soru {self.questionIndex + 1}: {question.text}')

#         for q in question.choices:
#             print('-'+ q)

#         answer = input('Cevap: ')
#         self.guess(answer)   #Burada kullanıcının verdiği cevap tahmin'e guess gönderilir.
#         self.displayProgress()
#         self.loadQuestion()  #loadQuestion çalıştırılır.

#     def guess(self, answer):
#         question = self.getQuestion()

#         if question.checkAnswer(answer):
#             self.score += 1
#         self.questionIndex += 1

#     def loadQuestion(self):
#         if len(self.questions) == self.questionIndex:
#             self.showScore()
#         else:
#             self.displayQuestion()

#     def showScore(self):
#         print('Score: ', self.score)

#     def displayProgress(self):
#         totalQuesiton = len(self.questions)
#         questionNumber = self.questionIndex + 1

#         if questionNumber > totalQuesiton:
#             print('Quiz bitti.')
#         else:
#             print(f'Question {questionNumber} of {totalQuesiton}'.center(100,'*'))

    
# q1 = Question('En iyi programlama dili hangisidir?', ['C#','python','javascript','java'], 'python')
# q2 = Question('En populer programlama dili hangisidir?', ['python','javascript','C#','java'], 'python')
# q3 = Question('En cok kazandıran programlama dili hangisidir?', ['C#','javascript','java','python'], 'python')
# q4 = Question('En cok kazandıran programlama dili hangisidir?', ['C#','javascript','java','python'], 'python')
# q5 = Question('En cok kazandıran programlama dili hangisidir?', ['C#','javascript','java','python'], 'python')

# questions = [q1,q2,q3,q4,q5]

# quiz = Quiz(questions)
# quiz.loadQuestion()
# # question = quiz.getQuestion()
# # print(question.text)






ogrenciler = {}
kisiSayisi = int(input('Kaç öğrenci kaydetmek istiyorsunuz: '))
i = 0

while (i < kisiSayisi):
    i += 1
    number = input("Öğrenci No: ")
    name = input("Öğrenci Adı: ")
    surname = input("Öğrenci Soyad: ")
    phone = input("Öğrenci Telefon: ")

    ogrenciler.update({
        number: {
            'ad': name,
            'soyad': surname,
            'telefon': phone
        }
    })

print(ogrenciler)