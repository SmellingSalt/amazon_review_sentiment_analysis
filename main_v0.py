#%%
from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch
# import requests
# from bs4 import BeautifulSoup #Used to scrape data from HTML docs
# import re #Something like grep in linux. It searches for patterns, substrings in walls of text. It is also needed for webscrapping

#%% Sentiment Analyser
# Using Model from https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment?
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment') #Get the tokenizer object used to train the nn
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment') #Get the neural network
def sentiment_score(review):
    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1
def text_cleaner(review):
    tokens = tokenizer.encode(review)
    ids=tokenizer.convert_ids_to_tokens(tokens)
    words=tokenizer.convert_tokens_to_string(ids)[6:-6]
    return words
#%% URL Parser and WebScrapper
url=input("Enter the URL \n")
# url="https://www.amazon.in/Lays-Potato-Chips-American-Flavour/dp/B08MXP4YDG?pd_rd_w=SDZmN&pf_rd_p=1d9db8b1-280f-4e5c-9d16-085f9071cd55&pf_rd_r=70N63XE3K21ZZRFBWJSE&pd_rd_r=5b5cfcf3-2f59-444d-979e-f04f7833bbe5&pd_rd_wg=y5DVz&pd_rd_i=B08MXP4YDG&psc=1&ref_=pd_bap_d_rp_1_i"
amazon_site=url[12:21]
asin=url.split("/")[5]
#https://github.com/SinghalHarsh/amazon-product-review-scraper
from amazon_product_review_scraper import amazon_product_review_scraper
review_scraper = amazon_product_review_scraper(amazon_site=amazon_site, product_asin=asin, sleep_time=2.5,end_page=20)
reviews_df = review_scraper.scrape()
print("Got Reviews")
# %% 
# reviews_df['sentiment'] = reviews_df['content'].apply(lambda x: sentiment_score(x[:512]))
print("Predicted Sentiment")
#%% Get Word Frequencies
import collections
freq = collections.Counter()
content=[text_cleaner(reviews) for reviews in reviews_df["content"].to_list()]
for review in content:
    freq.update(review.split())
print("Got Words and Frequencies")
# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
stop_words=["0.","0)","1.","1)","2.","2)","3.","3)","4.","4)","5.","5)","6.","6)","7.","7)","8.","8)","9.","9)","0","1","2","3","4","5","6","7","8","9","i", "me", "my", "myself", "we", "our", "ours", "it's","pros", "cons","ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
stop_words=list(string.punctuation)+stop_words
for stopword in stop_words:
    try:
        freq.pop(stopword)
    except KeyError:
        pass
wordcloud = WordCloud(background_color="white",width = 1000, height = 500).generate_from_frequencies(freq)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis('off')
print(freq)
plt.savefig("wordcloud.png",
            bbox_inches ="tight",
            pad_inches = 1,
            transparent = True)
# %%
# import itertools
# y=[".",")"]
# x=list(range(10))
# for item in itertools.product(x,y):
#     print(f"\"{item[0]}{item[1]}\"",end=',')