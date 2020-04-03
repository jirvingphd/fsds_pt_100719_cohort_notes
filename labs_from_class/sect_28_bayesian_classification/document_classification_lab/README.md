
# Document Classification with Naive Bayes - Lab

## Introduction

In this lesson, you'll practice implementing the Naive Bayes algorithm on your own.

## Objectives

In this lab you will:  

* Implement document classification using Naive Bayes

## Import the dataset

To start, import the dataset stored in the text file `'SMSSpamCollection'`.


```python
# Your code here
```

## Account for class imbalance

To help your algorithm perform more accurately, subset the dataset so that the two classes are of equal size. To do this, keep all of the instances of the minority class (spam) and subset examples of the majority class (ham) to an equal number of examples.


```python
# Your code here
```

## Train-test split

Now implement a train-test split on the dataset: 


```python
# Your code here
from sklearn.model_selection import train_test_split
X = None
y = None
X_train, X_test, y_train, y_test = None
train_df = None
test_df = None
```

## Create the word frequency dictionary for each class

Create a word frequency dictionary for each class: 


```python
# Your code here
```

## Count the total corpus words
Calculate V, the total number of words in the corpus: 


```python
# Your code here
```

## Create a bag of words function

Before implementing the entire Naive Bayes algorithm, create a helper function `bag_it()` to create a bag of words representation from a document's text.


```python
# Your code here
```

## Implementing Naive Bayes

Now, implement a master function to build a naive Bayes classifier. Be sure to use the logarithmic probabilities to avoid underflow.


```python
# Your code here
def classify_doc(doc, class_word_freq, p_classes, V, return_posteriors=False):
    pass
```

## Test your classifier

Finally, test your classifier and measure its accuracy. Don't be perturbed if your results are sub-par; industry use cases would require substantial additional preprocessing before implementing the algorithm in practice.


```python
# Your code here

```

## Level up (Optional)

Rework your code into an appropriate class structure so that you could easily implement the algorithm on any given dataset.

## Summary

Well done! In this lab, you practiced implementing Naive Bayes for document classification!
