import plotly.figure_factory as ff
import statistics 
import random 
import csv
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("P110.csv")
data=df["id"].tolist()
population_mean=statistics.mean(data)


data_set=[]
for i in range(0,1000):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    data_set.append(value)
    mean=statistics.mean(data_set)
    print(mean)


mean_list=[]
for i in range(0,100):
    set_of_means=random_set_of_mean(30)
    mean_list.append(set_of_means)
show_fig(mean_list)

df=mean_list
fig=ff.create_distplot([df],["temp"], show_hist=False)
fig.show()
print(data_set)

