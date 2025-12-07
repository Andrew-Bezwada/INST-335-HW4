## Data Analysis Report

This analysis was performed on the fastfood.csv dataset, which was obtained from Kaggle and contains nutritional information such as calories, fat, 
sodium, and protein for 515 menu items across 8 major US fast food chains.

The pandas operations executed include reading the CSV file into a DataFrame and then inspecting its structure using the `head()`, `info()`, and 
`describe()` methods. I demonstrated data access using both `loc` (label-based) and `iloc` (position-based) indexing for single rows, row slices, 
and individual cells. I then showed data filtering by using a single Boolean condition (`calories > 800`) and a complex, combined condition 
(`restaurant == 'Mcdonalds' & trans_fat > 1.0`). For column manipulation, I created a new column, which I named `sodium_per_calorie`, by dividing 
the `sodium` content by the `calories`, and subsequently dropped the `vit_a` column. Finally, I used the `groupby()` method to calculate the mean 
`calories` for each fast-food `restaurant`.

The analysis revealed a significant variation in the nutritional content across different menu items and restaurants. For example, the mean calorie 
content displayed a noticeable difference between the chains, suggesting some restaurants generally offer higher-calorie items than others. The 
filtering operation highlighted specific items, often burgers, that far exceeded the 800-calorie limit. A key limitation noticed in the dataset was
the high number of missing values (NaN, "Not A Number") in the vitamin and calcium columns (`vit_a`, `vit_c`, `calcium`), which limits the reliability 
of any analysis based on these micronutrients, which is why I made the decision to drop the `vit_a` column.
