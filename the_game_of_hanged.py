#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import os
import pickle
from data import *


# In[4]:


#Ask the user his name and creat a dictionary in which to put his name and score
name_key = input("What is your name?\n")

#Look if a dictionary score exist

if os.path.exists("score.txt") == False:
    
    #Creat a dictionary
    score = {
        name_key : 0
    }
    
    #Add the dictionary to score.txt
    with open("score.txt", "wb") as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(score)
        
else:
    #Extract the score dictionary
    with open("score.txt", 'rb') as file:
        depickler = pickle.Unpickler(file)
        score = depickler.load()
        
    exists = False
    for key, value in score.items():
        if name_key == key:
            print("Great you are already in the list of scores.\n")
            print("Your score is: {}.\n".format(value))
            exists = True
    if exists == False:
        score[name_key] = 0
        print("It is your first time playing. Welcome!\n")


# In[5]:


answer = "y"
while answer == "y":
    #Initialization
    lives = 8
    letter_guessed = []
    
    #Retrieve a random word from data
    word = random.choice(list_words)
    
    #Creat a string of * as long as the word
    hidden_word = ""
    for i in word:
        hidden_word = hidden_word + "*"
        
    #Informations given to the user    
    print("Here is the hidden word: {}.\n".format(hidden_word))
    print("You have {} lives.\n".format(lives))
    
    #Reapeat till user find the word or loose all his lives
    while hidden_word != word and lives != 0:
        
        #Ask him to guess a letter
        try_letter = input("Try to guess one letter.\n")
        #Is the letter identical to one already guessed
        
        while any([1 for element in letter_guessed if element == try_letter]): 
            print("You already used this letter.\n Here are the letters you already try {}".format(letter_guessed))
            try_letter = input("Try to guess one letter.\n")

        letter_guessed.append(try_letter)

        #Compare the letter with the word
        switch = True
        for i, letter in enumerate(word):
            if letter == try_letter:
                hidden_word = hidden_word[:i] + letter + hidden_word[i+1:]
                switch = False
        if switch:
            print("'{}' isn't a letter in the word.\n".format(try_letter))
            lives -= 1
            print("You have {} lives.\n".format(lives))
        
        #Display the world but with the letter found
        print(hidden_word)
        
    #Verify if we can end the game
    if hidden_word == word:  
        print("Congratulation! The word was '{}'.\n".format(word))
    else:
        print("You lost all of your lives.\n")
        print("The word was '{}'.\n".format(word))
        
    #Add the number of lives to the score of the person
    score[name_key] += lives
    answer = input("Do you still want to play? (y/n)\n")
        
print("Thank you for playing!\n")
print("You have a score of {}.\n".format(score[name_key]))


# In[ ]:




