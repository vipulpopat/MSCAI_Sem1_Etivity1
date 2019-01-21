# Etivity 1 : CE5062 CE6002

## Task 1
Load **bank-et1.csv** into a Pandas dataframe. Examine the first few data rows and the last few data rows. Identify an attribute that can be the target/dependable variable for 2-class classification. Follow the examples in the provided notebook *“Lab 1 - Exploratory Data Analysis. ipynb”* (see section Material, Resources and Online Meetings below).

## Task 2
Follow the examples in the provided notebook “Lab 1 - Exploratory Data Analysis. ipynb ” (see section Material, Resources and Online Meetings below) to perform EDA of the bank data set.

* Calculate statistics for the numerical and categorical attributes.
* Use at least two different plotting techniques to plot the distribution of two numerical and two categorical attributes. Draw short conclusions (in a markdown cell).
* Generate two plots with the combined distribution of attributes and draw conclusions from them (in a markdown cell).
* Generate additional plots to identify two numerical attributes that can potentially be used for predicting the value of the dependent variable you chose in Task 1.
You won't find two numerical attributes that will perfectly classify a dependent variable. Pick the best you can find.

## Task 3
Consider the two numerical attributes picked in Task 2 and describe (in a markdown cell) how a perceptron can be used to perform 2-class classification. Use the following terms in your description:

* Input space
* Output space
* Unknown target function
* Data set
* Hypothesis set
* Final Hypothesis
* In-sample error
* Out-of-sample error

## Task 4
Run the provided perceptron learning algorithm (PLA) on the dataset provided in the notebook. Take note of the number of iterations that were required to come to the final hypothesis and the final error. Once you are satisfied you understand these results, run the PLA algorithm on the dataset you have explored in the previous tasks (using the selected dependent variable and the two most promising numerical attributes/features). If results are unsatisfactory (if you don't get results at all, why would this be?), investigate how the PLA algorithm can be changed to improve the performance. Change the provided algorithm accordingly and plot estimates for P[Ein-Eout|>e]. Exercise 1.10 (see Python code below in the Resources section) gives an example of how you can create such plots. In the same plot add the Hoeffding Bound  and conclude whether or not the found results obey the Hoeffding Equation (in a markdown cell). Draw conclusions on whether or not you have found proof that learning is possible (in a markdown cell).

HINT: The videos discuss the 'Pocket' algorithm as an improvement on the PLA.

## Post
Git push your notebook to the repository for E-tivity 1 and submit a post to the forum for E-tivity 1 with the following content:

The names of the target variable you have chosen in Task 1 and the two numerical attributes you have chosen in Task 2. Your classification description required in Task 3.
Summary (max 200 words) of the most interesting discoveries in the data set as result of performing EDA in Task 2.
A link to your code in GitLab.

 **E-tivity 1: Exploratory Data Analysis & The Learning Problem**

## Respond
Respond to the post of one of your peers on the following aspects:

**CS5062**

* The quality of plots in their EDA
* The quality of conclusions drawn from their EDA
* Their classification description

**CE6002**

* Their implementation of the Pocket algorithm
* Their visualisation of the probability estimates
* Their choice of parameters used in the visualisation of the probability estimates
