**1. When would I use a Python dictionary to store data, instead of another data structure?**
_Python Dictionary can be used to store data when the data consist of key-value pairs . It also helps in data lookups. Good for most types of relational information_

**2. When writing Python code, why would you write a function?**   
_Functions are defined for the purposes of computations and code re-usability.  Typically, I will use a function when I want several actions, whether they are related or unrelated to be performed continuously as part of a loop._

**3. I have a Python list named mylist. What is the difference between `sorted(mylist)` and `mylist.sort()`?**   
_With sorted(mylist) : Will return a new list containing all items from the iterable in ascending order. mylist.sort() : Returns None because it sorts the variable 'mylist' inplace, but does not have a output._

**4. I have a Pandas DataFrame named users. One of the Series is named age. I run this code: `users[users.age > 25]`. What does this code return, and how does it "work"?**
_Assuming that the age column is a has a numeric dtype this code will look at the age column of users and return all observations in the users dataframe who have a value in the 'age' column that is greater than 25.
In SQL speak this would be equivalent to "SELECT * FROM users WHERE age > 25"_

**5. What is the difference between a bar plot and a histogram?**
_Histogram shows the distributions of some variables whiles bar plot is used to compare variables with respect to a certain descriptive statistics._

 **6. What is the difference between regression and classification problems, and how can you convert a regression problem into a classification problem?**
_Regression problems are used to predict some continuous variable, whiles classification problems are used to predict a binary or multi-class variable. You can convert a regression problem into a classification problem by adding a binary or multi-class response variable to the independent variables._

**7. When Netflix predicts the number of stars that you will use to rate a movie, are they solving a regression or classification problem?**
_This one is a bit tricky.
_Naturally the target variables would be seen as a classification being that there are 5 distinct options, but these options are actually continuous meaning that there is a linear relation between all of the target classes. A '4' is closer related to a '5' than it is a '2' Additionally, you will notice that many shows on Netflix have average ratings of a star and some decimal further confirming a continuous variable.  Essentially, the problem can go either way depending on how the 'Star' classes are considered or constructed._

**8. What's wrong with training and testing a machine learning model on the same data?**
_It is important not to test the prediction of an estimator on the data used to fit the estimator as this would not be evaluating the performance of the estimator on new data.  This will result in a model that is fit too well to the training data, i.e. 'Over-fit'.   This is why we use various cross validation techniques like train-test split_

**9. What is the purpose of model evaluation procedures that "hold out" data, like train/test split and cross-validation?**
_When talking about 'Hold Out' data we could be referencing two different things.
- 1. We 'Hold Out' data we could use to build our model in a train-test split and instead use it to test our data.   
- 2. We could 'Hold out' know data from our entire process in that we don't use it for training or testing.  This allows us to plan for additional variance after we tune via the train-test cycle._

**10. What are a few metrics (single numbers) I might use to evaluate how well a regression model is doing?  Include scoring criteria and what is considered when calculating the each metric**
_- R-Square: Scores between 0 and 1. Metric is the assessment of Explained variance divided by total(actual) variance.  (R-square can actually range to negative infinity if the line the is fit to the information is worse at summarizing that variance than plotting the y intercept).
- Mean Absolute Error (MAE): Scores from 0 to infinity.  MAE is a measurement of absolute error (observed variance)
- Mean Squared Error (MSE):Scores from 0 to infinity. Similar to MAE, but the results are squared which allows observations with greater error to have greater influence on the overall score.
- Median Absolute Error(MAD):_Scores range from 0 to infinity. The median of the absolute deviations from the data's median._

**11. Why is a confusion matrix useful for evaluating the performance of a classifier?**
_A confusion matrix will show over all how a classifier is performing for every class in the problem.  With it we can assess how often a classifier is correctly classifying as well as how often it is incorrectly classifying.  Most importantly when seeing how often our classifier is wrong or right we can see what how often we predict one class as a different class.  These are often referenced as false negatives and false positives.  As we know models can never be 100% accurate.  Various situations will cause us to have to make sacrifices when we tune our model, sometimes this is by overfitting our model one way causing it to be more sensitive to certain combinations of features and more likely to have false negatives as opposed to false positives, or vice-versa._

 **12. I built a machine learning model to solve a binary classification problem. The accuracy of my classifier is 99%, and the AUC is 0.51. Is my model doing well? Why or why not?**
 _The model is not doing well because the AUC is about 0.51, which means that the classifier is not able to differentiate between the labels, hence a random classifier. The higher the AUC, the better the model and vice versa. The 99% accuracy score is likely the result of using unbalanced classes._

**13. With regard to machine learning models, why should I care the about bias-variance trade-off?**
_We should care because bias introduces under-fitting into the model whiles variance introduces over-fitting into the model, so we need to worry about this issue so that our model can generalize well to unseen data._

**14. How does regularization reduce overfitting?**
_Regularization reduces over-fitting by penalizing the parameters in the model as a result of using L1 or L2 penalty regularization terms. When we add a regularization term to the loss function, we shrink the weights a little, increasing the bias while reducing variance._

**15. What are a few advantages and disadvantages of decision trees, as compared to other machine learning models?**
_Advantages of Decision Trees:
  - Simple to understand and interpret.
  - Requires little data preparation.
  - Able to handle both numerical and categorical data.
  - Uses a white box model.
  - Possible to validate a model using statistical tests. That makes it possible to account for the reliability of the model.
  - Robust. Performs well even if its assumptions are somewhat violated by the true model from which the data were generated.
  - Performs well with large datasets.
  - Once trained can be implemented on hardware and has extremely fast execution.
Disadvantages of Decision Trees:
  - Locally-optimal(small changes in variable measures can cause misclassification).
  - Practical decision-tree learning algorithms are based on heuristics such as the greedy algorithm where locally-optimal decisions are made at each node.
  - Such algorithms cannot guarantee to return the globally-optimal decision tree.
  - Overfitting.
  - Decision-tree learners can create over-complex trees that do not generalize well from the training data.
  - There are concepts that are hard to learn because decision trees do not express them easily, such as XOR, parity or multiplexer problems. In such cases, the decision tree becomes prohibitively large.
  - Decision tree learners create biased trees if some classes dominate. It is therefore recommended to balance the dataset prior to fitting with the decision tree._
