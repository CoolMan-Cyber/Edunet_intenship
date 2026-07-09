import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

#1.display first five rows
print(df.head())
print("\n")

#2.display last five rows
print(df.tail())
print("\n")

#3.giving information about dataset
print(df.info())
print("\n")

#4.let count total number of students who scored more than 95
print(df.value_counts("math score"))
print("\n")

#5.To Filter Students having maths score more than 95
print(df[df["math score"]>95]) 
print("\n")

#6.let calculate average mean score
a=df["math score"].mean()
print("average mean value:", a)
print("\n")

#7.getting maximum score in maths
print("Maximum Math Score:",df["math score"].max())
print("\n")

#8.gender wise average mean in maths score
print("Gender wise Average mean score in maths:", df.groupby("gender")["math score"].mean())
print("\n")

#9.let sort by maths score
print("Sort by Maths Value:\n",df.sort_values(by="math score"))
print("\n")

#10.let display column name
print("Column Names:\n",df.columns)
