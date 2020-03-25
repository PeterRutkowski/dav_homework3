import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# countries closest to Poland in 1971
# ascending order in terms of population

# import data
data = pd.read_csv("data/data_I_C.csv")
labels = np.asarray(data['country'])
data = np.asarray(data.drop(['country'], axis=1))

def plot(population, labels, year):
    # build the plot
    fig, ax = plt.subplots()

    index = np.arange(len(labels))
    index_y = np.arange(11)*10000000
    labels_y = []
    for i in range(len(index_y)):
        labels_y.append(np.round((i)*10,1))

    plt.text(0.75, 93000000.0, str(year), size=30,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1.0, 1.0, 1.0),
                       fc=(1.0, 1.0, 1.0),
                       )
             )

    colors = ['dodgerblue', 'orchid', 'green', 'darkorange', 'brown']

    bars = plt.bar(index, population, color=colors)

    for i in range(len(bars)):
        yval = bars[i].get_height()
        plt.text(bars[i].get_x()+0.25, yval + 1000000, labels[i])

    plt.ylabel('Population [million]')
    plt.xticks([])
    plt.title('The evolution of populations of countries that were most \n' +
              'similar population-wise to Poland in 1971')
    plt.yticks(index_y, labels_y)
    plt.ylim(0, 105000000)
    plt.tight_layout()
    plt.savefig('plots/I_CA/' + str(year)  + '.png', dpi=200)
    plt.close(fig)

# sorting plot bars in ascending order
last_index = len(data[0]) - 1
last_input = []
for i in range(5):
    last_input.append(data[i][58])

indices = [] # order of bars in the plot
indices = np.argsort(last_input)

sorted_pop = []
sorted_lab = []

for i in range(len(indices)):
    sorted_lab.append(labels[indices[i]])

population = []

for i in range(59):
    for j in range(5):
        population.append(data[j][i])
    for k in range(len(indices)):
        sorted_pop.append(population[indices[k]])

    plot(sorted_pop, sorted_lab, i+1960)

    population = []
    sorted_pop = []