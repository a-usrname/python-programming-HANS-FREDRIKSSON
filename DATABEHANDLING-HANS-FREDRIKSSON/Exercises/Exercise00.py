import random
import pandas as pd

#exercise00 Cities in Sweden

# create Dataframe
cities_dataset = {
            'Kommun': ["Malmö", "Stockholm", "Uppsala", "Göteborg"],
            'Population':[347949, 975551, 233839,583056]
}

# a) use your DataFrame to print out all the cities
cities_in_Sweden_df = pd.DataFrame(cities_dataset)
print(cities_in_Sweden_df)

# Select only the row that contains Göteborg. Do this by using the name Göteborg.
#refer to the named index: some error       loc = locate
print(cities_in_Sweden_df.loc[3]) #funkar
#print(cities_in_Sweden_df.loc["Göteborg"]) #funkar ej ? key error
