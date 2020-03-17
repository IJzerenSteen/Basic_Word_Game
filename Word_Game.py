#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time 

def word():
    
    """"This a basic word game that the last letter of your word 
    should be same with the first letter of your new word. 
    The first word couple isn't counted in the score."""

    
    player_word=input("Pls, write a word. ---->    ")
    player_word2=input("Pls, write a word. ---->    ")
    
    count=0
    
    while True:
        
        if player_word[-1] == player_word2[0]:
            player_word=input((len(player_word2)*" ") + "Pls, write a word. ---->      ")
            
        else:
            time.sleep(2)
            print(f"Game Over! Your score is {count}.")
            word()
        
        
        if player_word2[-1] == player_word[0]:
            player_word2=input("Pls, write a word. ---->    ")
            count=count+1
            
        else:
            time.sleep(2)
            print(f"Game Over! Your score is {count}.")
            word()
            
word()

