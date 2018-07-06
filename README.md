#Group assignment

Topic: Legalization of Pot
Source: Twitter - 
#CannabisAct
#BillC45
#C45
#Legalization
#CannabisinCanada
#C46
#marijuananews
#marijuana
#cannabis
#marijuanaDecriminalization
#blessthiscountry
#LegaliseCannabis
												                ]#
Jason Baker  (jabaker@mcmaster.ca)
Monique Ardizzi (monique.a.ardizzi@gmail.com)
Meera Ragunathan (m.ragunathan@icloud.com)
Jeff Ciraolo (jeff.ciraolo@gmail.com
Jonathan Bungcayao (jbbungcayao@gmail.com)



Roles:

Mining: Jason, Jonathan
Cleaning: Jeff
Analyse: Meera
Building a Model: Monique
Train+Test: Monique
Output: All ]#

Instructions/Walkthrough:  

The python scripts with output will be best viewed in a web browser at our git repo: https://github.com/moniqueardizzi/bda102assignment4  

1. 01 Mining folder 
- Please see miningNotes.txt which outlines the hashtags and methods used to pull our data  
- mining.py contains the script used to pull the data  
- tweets_2.csv was the final tweet set pulled for the project which was reformatted in Excel and began to have sentiment labelling done, and the dataset was stored as tweets_2_with_sentiment.csv  

2. 02 Clean folder  
- Python scripts used to clean the data are contained in this folder along with notes  
- tweets_2_with_sentiment_and_clean.csv is the file after the cleaning process  

3. 03 Model Building folder    
- Assigned a random number to each row in tweets_2_with_sentiment_and_clean.csv and shuffled and split the file - all done in Excel    
- tweets_2_with_sentiment_and_clean_train_test.csv contains 600 of the tweets  
- Completed labelling of train/test (tweets_2_with_sentiment_and_clean_train_test.csv) in Excel    
- tweets_2_study_cleaned.csv contains the remainder of the tweets from our data, left unlabelled  
- Model Build.ipynb contains the code to split the train and test data into 500 train tweets and 100 test tweets, reformat the input, build a feature extraction function, build and validate a Naive Bayes classifier, and then use the classifier to predict the sentiment on our unlabelled dataset, tweets_2_study_cleaned.csv  
- tweets_2_study_with_predicted_sentiment.csv contains the tweets that were not part of the train/test data with their predicted sentiment  

4. 04 Analyze folder
- Python script imports the tweets_2_study_with_predicted_sentiment.csv data, splits the data into positive, negative, and neutral sentiment, and does a Bag of Words analysis on each sentiment segment  

5. 05 Analyze Results folder   
- Contains the BOW frequency count data files for each of the sentiment classes 

6. Output 
- BDA102 Assignment 4 - Sentiment Analysis Implementation of Legalization of Weed.pptx contains a summary of our work and findings  



