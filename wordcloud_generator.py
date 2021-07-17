#%% ARGS
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--url",required=True ,type=str, help="The amazon URL")
# args = parser.parse_args()
#%% NLTK
def wordcloud_gen(url):
    from nltk import word_tokenize
    from nltk.corpus import stopwords
    import numpy as np
    from nltk.stem import WordNetLemmatizer, PorterStemmer
    import string

    #%% Cleaning Text
    # Using from https://towardsdatascience.com/nlp-preprocessing-with-nltk-3c04ee00edc0
    try:
        stop_words = stopwords.words('english')
    except LookupError:
        import nltk
        nltk.download('stopwords')
        nltk.download('punkt')
        nltk.download('wordnet')
        stop_words = stopwords.words('english')
    #Stemming. This is done so that words like car,cars, car's etc all get mapped to car
    porter = PorterStemmer()
    wnl = WordNetLemmatizer() #Needed so profile doesn't get mapped to profil. This happens since profiling is also a word
    def text_cleaner(review):
        review = review.lower() #Lower Case
        text_p="".join([char for char in review if char not in string.punctuation]) #Remove Punctuation
        words = word_tokenize(text_p) #Use this to split words.    
        filtered_words = " ".join([word for word in words if word not in stop_words])
        wnl.lemmatize(filtered_words) if wnl.lemmatize(filtered_words).endswith('e') else porter.stem(filtered_words)
        return filtered_words
    #%% URL Parser and WebScrapper
    # url=input("Enter the URL \n")
    # url=args.url
    amazon_site=url[12:21]
    asin=url.split("/")[5]
    #%%
    #https://github.com/SinghalHarsh/amazon-product-review-scraper
    from amazon_product_review_scraper import amazon_product_review_scraper
    print("Starting webscrapping...")
    review_scraper = amazon_product_review_scraper(amazon_site=amazon_site, product_asin=asin, sleep_time=2.5,end_page=20)
    reviews_df = review_scraper.scrape()
    content=[text_cleaner(reviews) for reviews in reviews_df["content"].to_list()]
    print("Got Reviews and Cleaned Text")
    #%% Get Word Frequencies
    import collections
    freq = collections.Counter()
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
    plt.savefig("static/wordcloud.png",
                bbox_inches ="tight",
                pad_inches = 1,
                transparent = True)
    # %%
    # import itertools
    # y=[".",")"]
    # x=list(range(10))
    # for item in itertools.product(x,y):
    #     print(f"\"{item[0]}{item[1]}\"",end=',')