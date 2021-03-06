---
title: Advanced Model Evaluation
type: lesson
duration: "1:25"
creator:
    name: Jonathan Balaban / Kiefer / Arun
    city: ATL / SF / NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Advanced Model Evaluation
Week 4 | Lesson 4.07

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Learn about and use sklearn functions to help perform different kinds of model evaluation
- Demonstrate how to use sklearn GridSearch to autotune models
- Visualize gridsearch function
- Emphasize inverse relation between 'C' and penalty

---
<a name="introduction"></a>
## Introduction to gridsearch

A correlation matrix is used to investigate the dependence between multiple variables at the same time. The result is a table containing the correlation coefficients between each variable and the others. This is ideal for feature selection when deciding which features to use in a predictive model.		 

**Check:** Explain cross-validation.

NumPy has an easy to use method perform to perform matrix correlations called ‘corrcoef’. [Review the code](./code/starter-code/4.07-breast-cancer-coefficients.ipynb) for performing a Pearson correlation coefficient matrix on the Breast Cancer Dataset.

What is "gridsearch?"

Gridsearch is the process of searching for the optimal set of tuning parameters for a model. It searches across values of parameters and uses cross-validation to evaluate the effect. It's called gridsearch because the idea is that there is a "grid" of parameters that are iteratively searched.

What kind of "tuning parameters" would we use this to search for?

**Check:** Recall and explain regularization.

<a name="demo"></a>
## Demo: Grid Search

For regularization like Ridge or Lasso, the optimal tuning parameters cannot be formulated automatically. We iteratively search for the best parameter for our problem.

sklearn's LogisticRegression class can accept an "l2" or "l1" **penalty** keyword argument, for Ridge and the Lasso, respectively. The **C** parameter indicates the inverse of the regularization strength. The larger the 'C', the smaller the penalty. The smaller the 'C', the larger the penalty.

```python
from sklearn.linear_model import LogisticRegression

# Logistic regression with a strong Lasso penalty:
sparse_logreg = LogisticRegression(penalty='l1', C=0.0001) # C indicates strong, l1 penalty indicates LASSO

# Logistic regression with a weak Ridge penalty:
shrunk_logreg = LogisticRegression(penalty='l2', C=1000.0) # C indicates weak, l2 penalty indicates Ridge
```

[This link](http://datascience.stackexchange.com/questions/10805/does-scikit-learn-use-regularization-by-default/10806) contains a brief discussion of scikit-learning regularizing by default and a way to almost completely circumvent that.

Here is a comparison of what regularization (or, equivalently, differing values of 'C') looks like in linear and logistic regression.
![](assets/images/linear-logistic-regularization-visualization.jpeg)

Review [GridSearch Example](./code/starter-code/4.07-search-grid.ipynb) and [Classification Report](./code/starter-code/4.07-classification-report.ipynb) techniques for use in independent practice and project work.

<a name="guided-practice"></a>
## Discussion & Guided Practice: Gridsearch with multinomial logistic modeling on crime data

So far, we have been using logistic regression for binary problems where there are only two class labels. As we discussed yesterday, logistic regression can be extended to dependent variables with multiple classes.

**Check:** What things should we keep in mind?

Multinomial vs. OvR
- (both) 'k' classes
- (M) 'k-1' models with 1 reference category
- (OvR) 'k*(k-1)/2' models

We are using the gridsearch in conjunction with multinomial logistic to optimize a model that predicts the category (type) of crime based on various features captured by San Francisco police departments.

[Multinomial logistic regression starter](../4.08-gridsearch-lab/4.08-gridsearch-starter-code.ipynb)

<a name="conclusion"></a>
## Conclusion
- Recap topic(s) covered
- Review logit coefficients

***

### ADDITIONAL RESOURCES
- Python [Lesson Correlation Matrix Example](./code/starter-code/4.07-breast-cancer-coefficients.ipynb)
- Python [Lesson GridSearch Example](./code/starter-code/4.07-search-grid.ipynb)
- Python [Lesson Classification Report Example](./code/starter-code/4.07-classification-report.ipynb)
