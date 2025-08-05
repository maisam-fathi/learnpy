# Exercise: Movie Rating Analyzer

# You are given a list of movies, each represented as a tuple:
# (movie_title, release_year, rating)
# For example:
# movies = [
#     ("Inception", 2010, 8.8),
#     ("The Godfather", 1972, 9.2),
#     ("The Dark Knight", 2008, 9.0),
#     ("The Room", 2003, 3.7),
#     ("Interstellar", 2014, 8.6),
#     ("Cats", 2019, 2.7),
#     ("Pulp Fiction", 1994, 8.9),
#     ("Sharknado", 2013, 3.3)
# ]
movies = [
    ("Inception", 2010, 8.8),
    ("The Godfather", 1972, 9.2),
    ("The Dark Knight", 2008, 9.0),
    ("The Room", 2003, 3.7),
    ("Interstellar", 2014, 8.6),
    ("Cats", 2019, 2.7),
    ("Pulp Fiction", 1994, 8.9),
    ("Sharknado", 2013, 3.3)
]
# Task 1: Define a lambda function called `double_rating` that doubles a movie's rating.
double_rating = list(map(lambda rating: rating[2] * 2, movies))
print('Double Rating: ', double_rating)

# Task 2: Use `map` and `double_rating` to create a new list where all ratings are doubled.
#         (The format should still be (title, year, new_rating).)
double_rating = list(map(lambda movie: (movie[0], movie[1], movie[2] * 2), movies))
print('Double Rating + Movie Detail: ', double_rating)

# Task 3: Use `filter` and a lambda function to create a list of only "good" movies,
#         where the original rating is 6.0 or higher.
good_movies = list(filter(lambda movie: movie[2] >= 6, movies))
print('Good movies Filter: ', good_movies)

# Task 4: Use `map` and a lambda function to label each movie as "classic" if the year is before 2000,
#         or "modern" otherwise. The new format should be (title, label)
label_movies = list(map(lambda movie: (movie[0], 'classic' if movie[1] < 2000 else 'modern'), movies))
print('Modern and Classic Movies: ', label_movies)

# Task 5: Sort the original `movies` list by rating (descending), using `lambda` in `sort`.
movies.sort(key=lambda movie: movie[2], reverse=True)
print('Rating (descending) Sort: ', movies)

# Task 6: Print out all the results for each step.

# Optional Challenge: Combine `filter` and `map` in one line to:
# - get titles of movies rated below 5.0
# - and prefix them with "Bad Movie: "
bad_movies = list(map((lambda movie: movie[0]), (filter(lambda movie: movie[2] < 5, movies))))
print('Bad Movies: ', bad_movies)

# Write clean, readable code and test each part step by step.