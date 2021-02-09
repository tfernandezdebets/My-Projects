import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load rankings data here:
wood_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#print(wood_rankings.dtypes)
#print(wood_rankings.head())
#print(steel_rankings.dtypes)
#print(steel_rankings.head())

# write function to plot rankings over time for 1 roller coaster here:
def rankings_1_roller_coaster(name, park_name, df):
 ranks = df['Rank'][(df.Name == name) & (df.Park == park_name)].values.tolist()
 years = df['Year of Rank'][(df.Name == name) & (df.Park == park_name)].values.tolist()

 plt.figure(figsize=(10,8))
 ax = plt.subplot()
 plt.plot(years, ranks)
 plt.title('{} ({}) Yearly Rankings'.format(name, park_name))
 plt.xlabel('Years')
 plt.ylabel('Rank')
 ax.invert_yaxis()
 plt.show()

 return ranks, years

#rankings_1_roller_coaster('El Toro', 'Six Flags Great Adventure', wood_rankings)
#plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def rankings_2_roller_coasters(name1, park_name1, name2, park_name2, df):
 ranks1 = df['Rank'][(df.Name == name1) & (df.Park == park_name1)].values.tolist()
 years1 = df['Year of Rank'][(df.Name == name1) & (df.Park == park_name1)].values.tolist()
 ranks2 = df['Rank'][(df.Name == name2) & (df.Park == park_name2)].values.tolist()
 years2 = df['Year of Rank'][(df.Name == name2) & (df.Park == park_name2)].values.tolist()

 plt.figure(figsize=(10,8))
 ax = plt.subplot()
 plt.plot(years1, ranks1, color = 'blue', label = '{} ({})'.format(name1, park_name1))
 plt.plot(years2, ranks2, color = 'red',  label = '{} ({})'.format(name2, park_name2))
 plt.title('{} and {} Yearly Rankings'.format(name1, name2))
 plt.xlabel('Years')
 plt.ylabel('Rank')
 ax.invert_yaxis()
 plt.legend()
 plt.show()

 return ranks1, years1, ranks2, years2

#rankings_2_roller_coasters('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood_rankings)
#plt.clf()

# write function to plot top n rankings over time here:
def top_n_rankings(n, df):
 top_n = df[df.Rank <= n]
 top_n_names = zip(top_n.Name, top_n.Park)
 top_n_names = list(set([i for i in top_n_names]))

 plt.figure(figsize=(10,8))
 ax = plt.subplot()
 for i in range(len(top_n_names)):
  ranks = top_n['Rank'][(top_n.Name == top_n_names[i][0]) & (top_n.Park == top_n_names[i][1])].values.tolist()
  years = top_n['Year of Rank'][(top_n.Name == top_n_names[i][0]) & (top_n.Park == top_n_names[i][1])].values.tolist()
  plt.plot(years, ranks, label = '{}'.format(top_n_names[i][0]), marker = 'o')

 plt.title('Rollercoaster rankings within the top {}'.format(n))
 plt.xlabel('Years')
 plt.ylabel('Rank')
 ax.set_yticks(range(1, n+1))
 ax.invert_yaxis()
 box = ax.get_position()
 ax.set_position([box.x0, box.y0, box.width*0.9, box.height])
 legend_x = 1
 legend_y = 0.2
 plt.legend(loc='center left', bbox_to_anchor=(legend_x, legend_y))
 plt.show()

 return top_n_names

#top_n_rankings(5, wood_rankings)
#plt.clf()

# load roller coaster data here:
roller_coaster_data = pd.read_csv('roller_coasters.csv')

# write function to plot histogram of column values here:
def plot_histogram(column_name, df):
 df[column_name] = df[column_name].dropna()
 plt.figure(figsize=(10,8))
 plt.hist(df[column_name], bins = 20)

 return plt.show()

heights = roller_coaster_data[roller_coaster_data['height'] <= 140]
#plot_histogram('height', heights)
#plt.clf()

# write function to plot inversions by coaster at a park here:
def number_inversions(park_string, df):
 data = df.sort_values('num_inversions', ascending = False)
 plt.bar(range(len(df.name)), data.num_inversions)

 return plt.show()

#number_inversions('Parc Asterix', roller_coaster_data)
#plt.clf()

# write function to plot pie chart of operating status here:
def status_pie(df):
 n_operating = df.status[df.status == 'status.operating'].count()
 n_closed = df.status[df.status == 'status.closed.definitely'].count()
# print(n_operating)
# print(n_closed)
 plt.pie([n_operating, n_closed])

 return plt.show()

#status_pie(roller_coaster_data)
#plt.clf()

# write function to create scatter plot of any two numeric columns here:
def scatter_plot(column1, column2, df):
 plt.scatter(df[column1], df[column2])

 return plt.show()

scatter_plot('height', 'speed', roller_coaster_data)
plt.clf()
