
# coding: utf-8

# In[183]:


from __future__  import division
import nltk
import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
#just get enhancem text 
def smart_text(text):
    text = text.lower()
    text = text.replace(',', ' ')
    text = text.replace('/', ' ')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace('.', ' ')
    return text
# split text in to n-terms
def generate_ngrams(text, n):
    text = text.lower()
    text = text.replace(',', ' ')
    text = text.replace('/', ' ')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace('.', ' ')
    text = text.split()
    ngrams_list = []
    for num in range(0, len(text)):
        ngram = ' '.join(text[num:num + n])
        ngrams_list.append(ngram)
 
    return set(ngrams_list)
# text
text = "Markov (Bigram) assumption Andrei that MarkovThe assumption that the probability of a word depends only onthe previous word, i.e., it looks one word into the past."
#one term  text 
list_of_single_words = generate_ngrams(text ,1)
#2 terms text
list_of_double_words = generate_ngrams(text ,2)
smart_txt = smart_text(text)
#print(list_of_single_words) datafram with unigram


# ha ha ha simple pro
def bi_pro(double_words, single):
    double_word_count = smart_txt.count(double_words) 
    print(double_word_count)
    single_word_count = smart_txt.count(single) 
    pro =double_word_count/single_word_count
    return pro

print(bi_pro('assumption that','that'))  


# In[184]:


# 2 ways to print uni gram count  df , df2
data = [{x:smart_txt .count(x)} for x in list_of_single_words]
df = pd.DataFrame(data=data)
pd.set_option('display.max_columns', 500)
df
df2 = pd.DataFrame(data = [[x,smart_txt .count(x)] for x in list_of_single_words]).T
df2


# In[ ]:





# In[185]:


# enhancem this matrix to be a pandaDataFram table
def count_bigram(list_of_single_words):
    matrix = []
    ls = list(list_of_single_words)
    for i in range(len(ls)):
        for j in range(len(ls)):
                #print(ls[i]+' '+ls[j])
                matrix.append(smart_txt.count(ls[i]+' '+ls[j]))

    #print(matrix)
    return matrix


# In[186]:


count_bigram=count_bigram(list_of_single_words)
data = np.array(count_bigram).reshape(len(list_of_single_words),len(list_of_single_words))
pd.DataFrame(data , columns=list_of_single_words , index=list_of_single_words)


# In[187]:


#bigram pro table
def pro_table(list_of_single_words):
    bigram_pro_table = []
    ls_conv = list(list_of_single_words)
    for i in range(len(ls_conv)):
        for j in range(len(ls_conv)):
#             print(ls_conv[i]+' '+ls_conv[j])
            pro = smart_txt.count(ls_conv[i]+' '+ls_conv[j])/smart_txt.count(ls_conv[i])
            bigram_pro_table.append(pro )

    #print(bigram_pro_table) 
    return bigram_pro_table


# In[188]:


pro_table= pro_table(list_of_single_words)
pd.DataFrame(np.array(pro_table).reshape(len(list_of_single_words),len(list_of_single_words)),columns=list_of_single_words,index=list_of_single_words)

