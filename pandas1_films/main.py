import pandas as pd

filePath = r'Files/filmy.csv'

myData = pd.read_csv(filePath)

# Task 1 (print columns names)
print(list(myData.columns))

# Task 2 (print first five rows)
print(myData.head(5))

# Task 3 (print all surnames of film directors)
surnames = []

for el in myData['director_name']:
    director = str(el)
    if director != 'nan':
        surname = director.split(' ')
        list_len = len(surname)
        surnames.append(surname[list_len - 1])

print(surnames)

# Task 4 (using crosstab function print movie_title depends on director_name) ???
print(pd.crosstab(myData.movie_title, myData.director_name))

# Task 5 (print all James Cameron films)
print(list(myData[myData['director_name'] == 'James Cameron']['movie_title']))

# Task 6 (print all polish film in polish language) 'language', 'country'
for film in myData[(myData['country'] == 'Poland') & (myData['language'] == 'Polish')]['movie_title'].unique():
    film_str = str(film).strip()
    print(film_str, end='; ')

# Task 7 (how many American films had a budget of more than $ 250 million)
print(len(list(myData[(myData['budget'] > 250000000) & (myData['country'] == 'USA')]['movie_title'].unique())))

# Task 8 (most expensive polish film)
print(myData[(myData['country'] == 'Poland')]['budget'].max())

# Task 9 (print the 10 film that had the most likes on Facebook)
print(myData.sort_values('movie_facebook_likes', ascending=False)[['movie_title', 'movie_facebook_likes']].head(10))

# Task 10 (in which country was shot the most films in color) ???
print(myData[myData['color'] == 'Color']['country'][0])

# Task 11 (sort data in ascending order by title_year)
print(myData.sort_values('title_year', ascending=True)[['movie_title', 'title_year']].head(20))

# Task 12 (name all the films starring Leonardo DiCaprio or Johnny Depp)
print(myData[(myData['actor_1_name'] == 'Leonardo DiCaprio') |
             (myData['actor_1_name'] == 'Johnny Depp') |
             (myData['actor_2_name'] == 'Leonardo DiCaprio') |
             (myData['actor_2_name'] == 'Johnny Depp') |
             (myData['actor_3_name'] == 'Leonardo DiCaprio') |
             (myData['actor_3_name'] == 'Johnny Depp')]
      [['movie_title', 'actor_1_name']].tail(20))
