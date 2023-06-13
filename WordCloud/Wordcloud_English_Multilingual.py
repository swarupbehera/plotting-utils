#!/usr/bin/env python
# coding: utf-8

# In[3]:


# !pip install wordcloud


# In[52]:


# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
# df = pd.read_csv(r"clotho_aqa_train.csv", encoding ="latin-1")
df = pd.read_csv(r"clotho_aqa_train_what_inbetween.csv", encoding ="latin-1")
comment_words = ''
listt=list(STOPWORDS)
for i in range(len(listt)):
  listt[i]=listt[i]+"tejesh"
# print(listt)	
#stopwords_newlist = ["https", "co"] + list(STOPWORDS)
#stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.answer:
	
	# typecaste each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "
#for english, stopwords =stopwords in below code
wordcloud = WordCloud(width = 600, height = 400,
				background_color ='white',
				collocations = False,
				stopwords=listt,
				min_font_size = 10).generate(comment_words)	
# plot the WordCloud image					
plt.figure(figsize = (6, 4), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.savefig('2b.pdf', format='pdf', dpi=1600)
plt.show()


# In[59]:


# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
# df = pd.read_csv(r"clotho_aqa_train.csv", encoding ="latin-1")
df = pd.read_csv(r"clotho_aqa_train_how_inbetween.csv", encoding ="latin-1")
comment_words = ''
listt=list(STOPWORDS)
for i in range(len(listt)):
  listt[i]=listt[i]+"tejesh"
# print(listt)	
#stopwords_newlist = ["https", "co"] + list(STOPWORDS)
#stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.answer:
	
	# typecaste each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "
#for english, stopwords =stopwords in below code
wordcloud = WordCloud(width = 600, height = 400,
				background_color ='white',
				collocations = False,
				stopwords=listt,
				min_font_size = 10).generate(comment_words)	
# plot the WordCloud image					
plt.figure(figsize = (6, 4), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.savefig('2c.pdf', format='pdf', dpi=1600)
plt.show()


# In[60]:


# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
# df = pd.read_csv(r"clotho_aqa_train.csv", encoding ="latin-1")
df = pd.read_csv(r"clotho_aqa_train_isare.csv", encoding ="latin-1")
comment_words = ''
listt=list(STOPWORDS)
for i in range(len(listt)):
  listt[i]=listt[i]+"tejesh"
# print(listt)	
#stopwords_newlist = ["https", "co"] + list(STOPWORDS)
#stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.answer:
	
	# typecaste each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "
#for english, stopwords =stopwords in below code
wordcloud = WordCloud(width = 600, height = 400,
				background_color ='white',
				collocations = False,
				stopwords=listt,
				min_font_size = 10).generate(comment_words)	
# plot the WordCloud image					
plt.figure(figsize = (6, 4), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.savefig('2d.pdf', format='pdf', dpi=1600)
plt.show()


# In[20]:


# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
# df = pd.read_csv(r"clotho_aqa_train.csv", encoding ="latin-1")
df = pd.read_csv(r"clotho_aqa_train_what_multi.csv", encoding ="latin-1")
comment_words = ''
listt=list(STOPWORDS)
for i in range(len(listt)):
  listt[i]=listt[i]+"tejesh"
# print(listt)	
#stopwords_newlist = ["https", "co"] + list(STOPWORDS)
#stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.answer:
	
	# typecaste each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "
#for english, stopwords =stopwords in below code
wordcloud = WordCloud(width = 600, height = 400,
				background_color ='white',
				collocations = False,
				stopwords=listt,
				min_font_size = 10).generate(comment_words)	
# plot the WordCloud image					
plt.figure(figsize = (6, 4), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()


# In[61]:


# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
# df = pd.read_csv(r"clotho_aqa_train.csv", encoding ="latin-1")
df = pd.read_csv(r"clotho_aqa_train.csv", encoding ="latin-1")
comment_words = ''
listt=list(STOPWORDS)
for i in range(len(listt)):
  listt[i]=listt[i]+"tejesh"
# print(listt)	
#stopwords_newlist = ["https", "co"] + list(STOPWORDS)
#stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.answer:
	
	# typecaste each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "
#for english, stopwords =stopwords in below code
wordcloud = WordCloud(width = 600, height = 400,
				background_color ='white',
				collocations = False,
				stopwords=listt,
				min_font_size = 10).generate(comment_words)	
# plot the WordCloud image					
plt.figure(figsize = (6, 4), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.savefig('2a.pdf', format='pdf', dpi=1600)
plt.show()

