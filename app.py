#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


import os
import bz2
import re
from tqdm import tqdm
import tensorflow as tf
from sklearn.utils import shuffle
from matplotlib import pyplot as plt
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding,LSTM,Dropout,Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from keras.models import load_model
from keras import backend as K


# In[2]: Load Model


model = load_model('LSTMmodel.h5')
print("model loaded")


# In[3]: Train Model


train_file = bz2.BZ2File('test.ft.txt.bz2')


# In[4]:


train_file_lines = train_file.readlines()
train_file_lines = [x.decode('utf-8') for x in train_file_lines]
train_labels = [0 if x.split(' ')[0] == '__label__1' else 1 for x in train_file_lines]
train_sentences = [x.split(' ', 1)[1][:-1].lower() for x in train_file_lines]
for i in range(len(train_sentences)):
    train_sentences[i] = re.sub('\d','0',train_sentences[i])
    
                                                       
for i in range(len(train_sentences)):
    if 'www.' in train_sentences[i] or 'http:' in train_sentences[i] or 'https:' in train_sentences[i] or '.com' in train_sentences[i]:
        train_sentences[i] = re.sub(r"([^ ]+(?<=\.[a-z]{3}))", "<url>", train_sentences[i])
X_train,X_test,y_train,y_test=train_test_split(train_sentences,train_labels,train_size=0.80,test_size=0.20,random_state=42)
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(X_train)


#In[5]: Find the rating


def rate(p):
   return (p*5)


# In[6]:


#!C:\Users\xitis\AppData\Local\Programs\Python\Python37-32\python.exe
import sys
from flask import Flask, render_template, url_for,json, request, jsonify, redirect
import MySQLdb


# In[7]:



app = Flask(__name__)

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="pukar11",
                  db="rating")
c = conn.cursor()


# In[8]:


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/jacket", methods=['GET'])
def jacket():
    conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="pukar11",
                  db="rating")
    c = conn.cursor()

    #Fetch the reviews and their corresponding ratings for a product
    c.execute("SELECT * FROM jacket ORDER BY timeadded DESC")

    data = c.fetchall()

    #Fetch the overall rating of a product
    c.execute("SELECT * FROM product")

    stars = c.fetchone()

    return render_template('jacket.html', data=data, stars = stars)


# In[9]:


@app.route("/postreview", methods=['POST'])
def postreview():
    #Get the data posted from the form
    message = request.get_json(force=True)
    review = message['review']
    uname = message['uname']

    #assign the review text to a variable
    a=[review]

    #predict the outcome
    pred=model.predict(pad_sequences(tokenizer.texts_to_sequences(a),maxlen=100))
    value=rate(pred.item(0,0))

    #Save the review, username and predicted value to the database
    conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="pukar11",
                  db="rating")
    c = conn.cursor()

    c.execute(
      """INSERT INTO jacket (uname, review, rate)
      VALUES (%s, %s, %s)""",(uname, review , value ))
    
    conn.commit()

    #Calculate average of the ratings including the recent value
    c.execute("""SELECT AVG(rate) FROM jacket""")

    avg = c.fetchone()

    #Update the overall rating of a product in database
    c.execute("""UPDATE product SET rating = %s WHERE id = %s""",(avg,1))

    conn.commit()

    return



if __name__ == "__main__":
    app.run()




