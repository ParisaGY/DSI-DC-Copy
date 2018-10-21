## Dataset

This dataset comprises of 6 months of credit history for 30000 individuals from a particular bank that is your client.

Ideally we want to take this data and try to build a model to predict whether or not a individual will be likely to default on their credit given 6 months of credit history.


### Data Dictionary

* ID - Unique user Identification Number
* LIMIT_BAL -  Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit.
* SEX - Gender (1 = male; 2 = female).
* EDUCATION - Education (1 = graduate school; 2 = university; 3 = high school; 4 = others).
* MARRIAGE - Marital status (1 = married; 2 = single; 3 = others).
* AGE - Age (yearS).

* PAY_STAT_XXX - the repayment status in XXX month of 2005.  The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above.

* BILL_AMT_XXX - amount of the bill statement for XXX month of 2005;

* BILL_PAY_XXX - amount of bill paid for XXX month of 2005
* default payment next month - utilizes a binary variable, default on payment (Yes = 1, No = 0) as the response variable
