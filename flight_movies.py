def can_movies_fit_flight(flight_length, movie_lengths):

    # NICE. Constant lookup in a set
    movies_seen = set()

    for first_movie_length in movie_lengths:
        second_movie_length = flight_length - first_movie_length
        if(second_movie_length in movies_seen):
            return True
        movies_seen.add(first_movie_length)
    return False


print(can_movies_fit_flight(3, [1, 9, 1, 5, 6]))
