# Project Description
The goal of the project is to create an interactive conversational agent that assumes the role of a Psychiatrist.The Chatbot will essentially output *canned* responses to a users input. More specifically the bot will be trained to deal with users that are dealing with a variety of emotions such as depression, stress, loneliness. The user in this case will be a patients seeking help. 

## Chosen SDLC
The Software Development Lifecycle that we chose is the agile method. This model allows us to test and debug more due to the short iterations. It also allows us to identify problems and risks earlier and prevent them from happening in the future. Moreover, it provides us with flexibility to change things as we develop the chat bot, certain features or requirements.

## Limitations

•	The code is limited by the NLP algorithm which aims to understand what the user is writing and provide an answer from a json file with possible answers. Therefore, the bot is limited by the size and complexity of the provided responses. 

•	Since the bot is following a predetermined structure the same answer can be provided to the user repetitively. 


## Installation and Setup 

In order to run the chat bot the user must install the following libraries nltk, numpy, tflearn,random, json, pickle, tkinter, nltk. 

## Machine Learning
Machine Learning was used to train a model which can recognize certain patterns and words used in user input. This provides much more flexibility within the system when attempting to interpret these inputs. The bot is able to take the user input and estimate if what the user has said falls into one if its predefined categories that it knows how to respond to. For example, when given the input "I am Lonely" the bot will compare this statement with all its training data, searching for keywords and example statements in each response category with similar sentence structure. Once it has done this it will produce a percentage for each response category. This percentage represents the input statements similarity to the sentences in that category. Finally, it picks the category with the highest percentage similarity and depending on the category, it grabs a pre-written response to print to the user.

The model is traind with TensorFlow's Natural Language Toolkit. Source: https://www.youtube.com/playlist?list=PLzMcBGfZo4-ndH9FoC4YWHGXG5RZekt-Q

![Screenshot](mlExample.PNG)



![Screenshot](synonymExample.png)

## Graphical User Interface
The GUI is created from the python GUI toolkit called Tkinter. The interface is divided into 3 simple areas. First it the text widget, this is where the conversation is displayed. It is vertically scrollable allowing the user to see the conversation history. The second part is the message entry box. This is where the user enters their messages. Finally we have an enter button for the user to click to submit their message. The user can also simply press the enter key instead. The color pallete was designed to have a calming effext. The GUI makes calls to the main.py program to generated responses. It improves the overall system by providing ease of use and a relaxing aesthetic. 

Source: https://docs.python.org/3/library/tkinter.html


## Features in this Assignment
* Google translate API (10 points)
* Wikipedia API (10 points) 


## Google Tranlsate API 
Using this API I added functionality to the thera-bot.This API was added to address any needs for international users. With the google translate API we access googles trained translation model. Therefore, the user can enter a word or phrase they wish to translate and it will be converted into the languages set in the program. In this case I set the default to spanish, but this can be easily changed in the GuiControl.py file. I implemented this into the chatbot, so that a user can enter 1 followed by the phrase they wish to translate, and the google translate api will return the input converted into english so that the user can be sure they are saying what they meant. 



## Wikipedia API

Using Wikipedias API I added a functionality that allows the user to get a brief summary of any topic of their interest. For example if the user wants to learn about Emotional Depression, they can type 2 followed by the topic of interest, and the Wikipedia API will return 3 sentences that summarize this topic. This way a user can understerstand and explore a plethora of topics in order to improve their experience with the thera-bot. 