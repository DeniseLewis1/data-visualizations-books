import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

with open("books.csv","r") as datafile:
  data = pd.read_csv(datafile,delimiter=",")

# Bubble chart comparing the number of pages in each book to the book’s rating on Goodreads
#fig = sns.scatterplot(x="average_rating", y="# num_pages", size="# num_pages", data=data)
#plt.xlabel("Average Rating")
#plt.ylabel("Number of Pages")
#plt.title("Rating vs Pages")
#plt.savefig("ratings_vs_pages_bubble_plot.png")

# Scatterplot to compare number of book reviews and ratings
# plt.scatter(data["average_rating"], data["ratings_count"])
# plt.xlabel("Average Rating")
# plt.ylabel("Number of Reviews")
# plt.title("Ratings vs Reviews")
# plt.savefig( "ratings_vs_reviews_scatter_plot.png")

#print(data["language_code"])

# Pie chart that shows the most common book languages
languages_list = data["language_code"].tolist()

languages = []
for language in languages_list:
  if language not in languages:
    languages.append(language)

language_count = []
for language in languages:
  language_count.append(languages_list.count(language))

subset_language_count = []
subset_languages = []

# Identify languages with at least 100 books
for index in range(len(languages)):
  if language_count[index] >= 100:
    subset_languages.append(languages[index])
    subset_language_count.append(language_count[index])

plt.pie(subset_language_count, labels=subset_languages)
plt.title("Book Languages")
plt.savefig("book_languages_pie_chart.png")
  