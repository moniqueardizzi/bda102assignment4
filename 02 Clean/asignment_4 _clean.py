
# coding: utf-8

# In[1]:


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests
import string
import pandas as pd

#nltk.download('stopwords')
#nltk.download('punkt')


# In[2]:


#Load data 
url = "https://raw.githubusercontent.com/moniqueardizzi/bda102assignment4/master/Mining/tweets_2_with_sentiment.csv"
df_tweets = pd.read_csv(url)


# In[53]:


#define townization and cleaning functions
def tokenize_and_clean(s) :
    #parse the string into tokens
    tokens = word_tokenize(s)
    
    clean_tokens = []
    for t in tokens :
        ct = clean_token(t)
        if ct != None :
            clean_tokens.append(ct)

    return ' '.join(clean_tokens)

def clean_token(t) :
    
    #build tranformation table for puncuation
    punc_tbl = str.maketrans('', '', string.punctuation)
    
    #get list of stop workds
    stop_words = set(stopwords.words('english'))
    
    #convert to lower 
    t = t.lower()
    
    #only keep alpha words
    if not t.isalpha() :
        t = ''    

    #remove any remaining puncuation
    t = t.translate(punc_tbl)
    
    #null out stop words
    if t in stop_words :
            t = ''   
            
    #remove any remaining two and one letter words 
    if len(t) < 3 :
        t = ''

    if t != '' :
        return t
    else :
        return None


# In[54]:


#Apply tokenization and cleaning to all rows and store results in new column  
df_tweets["tokenized_cleaned"] = [tokenize_and_clean(r['Tweet']) for i, r in df_tweets.iterrows()]


# In[56]:


#save to csv
df_tweets.to_csv('./tweets_2_with_sentiment_and_clean.csv')

