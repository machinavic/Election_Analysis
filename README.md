# **Module 4_ PyCitySchools with Pandas**

On this challenge, sll concepts learnt on this chapter were applied to a school data analysis.
Dataset here was manipulated, prepared, and summarized using different functions such as: "groupby", "sort_values", "isnull", among other not less important.

## **Overview of School Data Analysis**

Taking into account the revision of the outcomes retrieved, the following findings can be appointed:
- The dataframe has 8 column heads, going from student_id to school_budget, 
- All rows were reviewed checking if null (NaN) values existed, and eliminating them; same was done for deleting duplicated rows.
-The data types were checked as well using the "dtypes" property.
-Data were summarized statistically using the describe function as appears in here below:
![Dataframe_statistics]
-The mean was obtained for math and reading score.
-Others functions as "loc' and "iloc" were used to display certain columns and rows under certain conditions:
![Using_loc_with_conditions]
-And a series of comparisons were made:
![Comparisons]

## **Insights and improvements**

When we talk about data, a lot of info can be retrieved from them.
In this particular case, we could have gotten the following findings:
-how budget was used by grades and type of school;
-average expense per student, per school type.
-all this data could be summarized in a graph.
-using Paretto chart, determining the most important school in this dataframe, among other._Analysis
