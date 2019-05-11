# Latent Dirichlet Allocation (LDA) and Topic Modeling
- Data is collected on https://www.reuters.com/breakingviews by a scrapping script
- The goal is to break text documents down into topics by word. 
- What is laten feature ? Mathematically, we want to find “topics” that are collections of words that appear in similar documents. More generally, it is a collection of features in a dataset.
- There are several libraries for LDA such as scikit-learn and gensim. I choose gensim for this project.

# Project tasks:
- Cleaning the dataset & Lemmatization
- Creat a dictionay from processed data
- Create Corpus and LDA Model with bag of words
- Create Coprpus and LDA with TF-IDF
- Caculate the Perplexity and Topic Cohenrence between two models
- Visualize topics with the help of pyLDAvis
# Dataset:
- Request real time data from https://www.reuters.com/breakingviews

# Requirements
- Python >= 3.7
- Jupyter Notebook

# Dependencies
- pandas
- matplotlib
- seaborn
- pyLDAvis
- scikit-learn
- numpy
- gensim

# Run on local:
- checkout the project : git clone https://github.com/diem-ai/topic-modeling.git
- install libraries in requirements and dependencies
- Read the notebook without installation: view Breakingnews-Topic Modeling-LDA.htlm file.

# Improvements (Next commits):
- Pulling more data + Appyling dimensionality reductions (Trunked Singular Decomposition - SVD)
- try out the same datasets with Latent Sentiment Analysis (LSA) and Non Negative Matrix (NNM) to see which one outperform which one
