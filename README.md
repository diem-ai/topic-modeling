##  Topic Modeling with Latent Dirichlet Allocation (LDA) and Latent Sentiment Analysis (LSA)
- Collecting top 500 news at https://www.reuters.com/breakingviews
- The goal is to break text documents down into topics by word and to experience how topics are modelled with different appraches. We want to find “topics” that are collections of words that appear in similar documents
- There are 2 popular libraries for LDA/LSAsuch as scikit-learn and gensim. I choose gensim for this project.

## Project Notes
### Dataset
- Retrieving top 500 latest breaking news from https://www.reuters.com/breakingviews 
- Cleaning the data with beautifulsoup & save them into csv file (data/breakingnews.csv) in order to do analysis and to build model
### Code
- model_preparation.ipynb:
   * Read breakingnews.csv and clean special letters
   * Visualize the most popular words by WordCloud
   * Create dictionary from processed data and save it as dictionary.plk (/data/dictionary.pkl)
   * Create a corpus from processed data and save it in <code>/data/corpus.pkl</code>
   * Create bag of words (BOW) and save it in /data/bow.pkl
   * Create a TF-IDF and save it in /data/tfidf.pkl
- Topic Modeling-LDA.ipynb:
   * Build LDA model with bag-of-word from corpus.pkl,bow.pkl and dictionary.pkl
   * Build LDA model with bag-of-word from ifidf.pkl,bow.pkl and dictionary.pkl
   * Print top 5 topics of each model and interpret the results
   * Visual the topics and their words with pyLDAvis
   * Calulate Perplexity and Topic Cohenrence between two models
- Topic Modeling-LSA.ipynb:
   * Build LSA model with bag-of-word from corpus.pkl,bow.pkl and dictionary.pkl
   * Build LSA model with bag-of-word from ifidf.pkl,bow.pkl and dictionary.pkl
   * Print top 5 topics of each model and interpret the results

### View notebooks without installation
- Check out htlm directory

## Project tasks:
- Cleaning the dataset & Lemmatization
- Creat a dictionay from processed data
- Create Corpus and LDA/LSA Model with bag of words
- Create Coprpus and LDA/LSA with TF-IDF
- Caculate the Perplexity and Topic Cohenrence between two models
- Visualize topics with the help of pyLDAvis

## Requirements
- Python >= 3.7
- Jupyter Notebook

## Dependencies
- pandas
- matplotlib
- seaborn
- pyLDAvis
- scikit-learn
- numpy
- gensim
- Scipy
- nltk
- string
- beautifulsoup
- WordCloud

## Run on local:
- Checkout the project : git clone https://github.com/diem-ai/topic-modeling.git
- Install the latest version of libraries in requirements and dependencies
- Run get_historical_news.py to collect 500 latest news : python get_historical_news.py
- Run model_preparation.ipynb to produce the data
- Run Topic Modeling-LDA.ipynb for LDA topic modeling
- Run Topic Modeling-LSA.ipynb for LSA topic modeling
