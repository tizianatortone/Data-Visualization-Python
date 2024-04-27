"""
This module reads data from a CSV file and generates a plot from said data.
"""
import csv
import matplotlib.pyplot as plt

plt.style.use('dark_background')

def generates_dictionary(data_file):
    """Generates a Dictionary from the data inside the .csv file
       
       Following this structure:
       {
           "Continent1": {"population":[...], "years":[...]}
           "Continent2": {"population":[...], "years":[...]}
       }
    """
    output = {}

    with open(data_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])

            if continent not in output:
                output[continent] = {'population': [], 'years': []}

            output[continent]['population'].append(population)
            output[continent]['years'].append(year)

    return output


def generates_plot(population_dictionary):
    """Generates a plot from the dictionary created with the csv data"""

    for continent in population_dictionary:
        years = population_dictionary[continent]['years']
        population = population_dictionary[continent]['population']
        plt.plot(years, population, label=continent, marker='o')
        


    plt.title('Continental Internet Population')
    plt.xlabel('Year')
    plt.ylabel('Internet usersr (in billion)')
    plt.legend()
    plt.grid()

    plt.savefig('graph.png')

    plt.show()

data_file = 'data.csv'

continent_population = generates_dictionary(data_file)
generates_plot(continent_population)
