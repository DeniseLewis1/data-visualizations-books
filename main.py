import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

with open("books.csv","r") as datafile:
  data = pd.read_csv(datafile,delimiter=",")

# Bubble chart comparing the number of pages in each book to the book’s rating on Goodreads
fig = sns.scatterplot(x="average_rating", y="# num_pages", size="# num_pages", data=data)
plt.xlabel("Average Rating")
plt.ylabel("Number of Pages")
plt.title("Rating vs Pages")
plt.savefig("ratings_vs_pages_bubble_plot.png")