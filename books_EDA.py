import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv('books.csv', error_bad_lines = False, warn_bad_lines = False)  # import data

df.rename(columns = {'  num_pages': 'num_pages'}, inplace = True)
df.drop(['bookID', 'isbn', 'isbn13'], axis = 1, inplace = True)

# first let's plot the number of books in all the different languages

langdf = pd.DataFrame(np.unique(df.language_code, return_counts = True))
langdf.index = ["language code", "count"
langdf = langdf.sort_values(by = ["count"], axis = 1, ascending = False)

plt.figure(figsize = (12, 8))
plt.title("Language Codes")

ax = sns.barplot(x = langdf.values[0].tolist(), y = langdf.values[1].tolist())
ax.set(xlabel = "Language Codes", ylabel = "Count")
for item in ax.get_xticklabels(): item.set_rotation(45)
plt.show()

# because the majority of books are in english, let's adjust our data frame to only have english books

df = df[(df.language_code == 'eng')|(df.language_code == 'eng-US')|(df.language_code == 'eng-GB')]

#next, plot the most rated books

most_rated = df.sort_values('ratings_count', ascending = False).head(10).set_index('title')
plt.figure(figsize = (12, 8))
plt.title("Top 10 most rated")
ax = sns.barplot(x = most_rated.ratings_count, y = most_rated.index)
ax.set(xlabel = "ratings count", ylabel = "books")
plt.show()