#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install tensorflow')
get_ipython().system('pip install nltk')


# In[11]:


import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


# In[12]:


##Función para quitar link, hashtags, emojis y caracteres especiales.
def clean_text(text):
    clean=text
    reg = re.compile('\&amp')
    clean = clean.apply(lambda r: re.sub(reg, string=r, repl='&'))
    reg = re.compile('\\n')
    clean = clean.apply(lambda r: re.sub(reg, string=r, repl=' '))
    reg = re.compile('@[a-zA-Z0-9\_]+')
    clean = clean.apply(lambda r: re.sub(reg, string=r, repl='@'))
    reg = re.compile('#[a-zA-Z0-9\_]+')
    clean = clean.apply(lambda r: re.sub(reg, string=r, repl='#'))
    reg = re.compile('https?\S+(?=\s|$)')
    clean = clean.apply(lambda r: re.sub(reg, string=r, repl='www'))
    clean = clean.replace(r'[^\x00-\x7F]+', '', regex=True)
    return clean.apply(lambda x: ' '.join(re.sub("(#[A-Za-z0-9]+)|(/[A-Za-z0-9]+)|(@[A-Za-z0-9]+)|(www.[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(/+:\/\/\S+)"," ",x).split()))

#Función para remover las stopwords
def byestop(text):
    nostop = text
    stop = stopwords.words('english')
    ##algo raro pasa que se tenía que pasar dos veces por el filtro para que se removieran las palabras, luego lo checo.
    nostop = text.apply(lambda words: ' '.join(word.lower() for word in words.split() if word not in stop))
    return nostop.apply(lambda words: ' '.join(word.lower() for word in words.split() if word not in stop))


# In[ ]:




