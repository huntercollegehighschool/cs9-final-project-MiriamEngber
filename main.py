"""
Name(s): Miriam Engber
Name of Project: Mad Libs
"""



#Write the main part of your program here. Use of the other pages is optional.
import random

Story1 = "Me and my noun1 decided to have a sleepover. At the sleepover, both of us wanted to verb1. It was a lot of adjective1, but in the end noun1 thought it was too adjective2. So instead, we decided to have a adjective3 pillow fight. It started when personname1 grabbed a pillow and swung it at celebrityname1, hitting them on the back of their bodypart1. Then, celebrityname1 retaliated by verb-ing1 and going away. I threw a pillow at personname1, but missed and hit a noun2, splitting my pillow open!. pluralnoun1 flew everywhere, covering the room in adjective4 feathers. What a mess!"
words1 = ["noun1", "verb1", "adjective1", "adjective2", "adjective3", "personname1", "celebrityname1", "bodypart1", "verb-ing1", "noun2", "pluralnoun1", "adjective4"]
questions1 = ["Enter a noun: ", "Enter a verb: ", "Enter an adjective: ", "Enter an adjective: ","Enter an adjective: ", "Enter a person's name: ", "Enter a celebrity's name: ", "Enter a noun: ", "Enter a plural noun: ", "Enter an adjective: "] 

Story2 = "My friend just bought a pet animal1. It is height1 feet tall and smells like scent1. It is too adjective1 to sleep in her room, so it sleeps in the place1. She feeds it pluralnoun1, but it once ate her noun1! Eventually, it ate her noun2. Her familymember1 told her she needed to give it back to the place2, but she didn't want to. So she pastverb1 away, bringing the animal1. Together they made it to place3, where they were finally adjective2. I haven't talked to her in number1 weeks since she ran away, so I really hope she and her pet are adjective3 and adjective4."
words2 = ["animal1", "height1", "scent1", "adjective1", "place1", "pluralnoun1", "noun1", "noun2", "familymember1", "place2", "pastverb1", "place3", "adjective2", "number1", "adjective3", "adjective4"]
questions2 = ["Enter an animal: ", "Enter a number: ", "Enter a smell: ", "Enter an adjective: ", "Enter a place: ", "Enter a plural noun: ", "Enter a noun: ", "Enter a noun: ", "Enter a type of family member: ", "Enter a place: ", "Enter past tense verb: ", "Enter a place: ", "Enter an adjective: ", "Enter a number: ", "Enter an adjective: ", "Enter an adjective: "] 

Story3 = "My familymember1 took me to the verbing1 mall to buy a adjective1 pair of sneakers. My old ones were too adjective2 and had a adjective3 hole in the toe. Any time I stepped in a puddle, my bodypart1 would get totally adjective4. At the mall, we went to the noun1 shack, where they sell the best sneakers in place1. I picked out a adjective5 pair and was so excited I started to verb1 right there in the store. My familymember1 said they make my feet look like noun2. I love my new sneakers and they are great for verbing2 in pluralnoun1!"
words3 = ["familymember1", "verbing1", "adjective1", "adjective2", "adjective3", "bodypart1", "adjective4", "noun1", "place1", "adjective5", "verb1", "noun2", "verbing2", "pluralnoun1"]
questions3 = ["Enter a type of family member: ", "Enter a verb ending in ing: ", "Enter an adjective: ", "Enter an adjective: ", "Enter an adjective: ", "Enter a body part: ", "Enter an adjective: ", "Enter a noun: ", "Enter a place: ", "Enter an adjective: ", "Enter a verb: ", "Enter a noun: ", "Enter a verb ending in ing: ", "Enter a plural noun: "]

Story4 = "Today I went to the zoo. I saw a adjective1 noun1 jumping up and down in its noun2. He pastverb1 adverb1 through the large tunnel that led to its adjective2  noun3. I got some food1 and passed them through the cage to a gigantic adjective3 noun4 towering above my head. Feeding that animal made me adjective4. I went to get a adjective5 scoop of ice cream. It filled my stomach. Afterwards I had to verb1 adverb2 to catch our bus. When I got home I pastverb2 my mom for a adjective6 day at the zoo."
words4 = ["adjective1", "noun1", "noun2", "pastverb1", "adverb1",  "adjective2", "noun3", "food1", "adjective3", "noun4", "adjective4", "adjective5", "verb1", "adverb2", "pastverb2", "adjective6"]
questions4 = ["Enter an adjective: ", "Enter a noun: ", "Enter a noun: ", "Enter a past verb: ", "Enter an adverb: ", "Enter an adjective: ", "Enter a noun: ", "Enter an item of food: ", "Enter an adjective: ", "Enter a noun: ", "Enter an adjective: ", "Enter an adjective: ", "Enter a verb: ", "Enter an adverb: ", "Enter a past verb: ", "Enter an adjective: "]



mystorychoice = random.randint(0,3)
#mystorychoice = 3
print(mystorychoice)

stories = [Story1, Story2, Story3, Story4]
wordschoice = [words1, words2, words3, words4]
questionschoice = [questions1, questions2, questions3, questions4]

Story = stories[mystorychoice]
words = wordschoice[mystorychoice]
questions = questionschoice[mystorychoice]

numofwords = len(words)
answers = [] # empty list
for item in questions:
  response = input("" + item + "")
  answers.append(response)

for i in range(0, numofwords):
  Story = Story.replace(words[i], answers[i])
  #print(Story)
  #print("**********")
print(Story)


#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
