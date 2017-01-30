import fresh_tomatoes
import media


def start():
    movies = [media.Movie('The Great Gatsby',
                          'https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxNTk1ODcxNl5BMl5BanBnXkFtZTcwMDI1OTMzOQ@@._V1_SY1000_SX666_AL_.jpg',  # NOQA
                          'https://www.youtube.com/watch?v=rARN6agiW7o',
                          'A writer and wall street trader, Nick, finds himself drawn to the past and lifestyle of his '
                          'millionaire neighbor, Jay Gatsby.'),
              media.Movie('The Aviator',
                          'https://images-na.ssl-images-amazon.com/images/M/MV5BZTYzMjA2M2EtYmY1OC00ZWMxLThlY2YtZGI3MTQzOWM4YjE3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg',  # NOQA
                          'https://www.youtube.com/watch?v=zikFDK4cuQA',
                          'A biopic depicting the early years of legendary director and aviator Howard Hughes\' career '
                          'from the late 1920s to the mid-1940s.'),
              media.Movie('The Wolf of Wall Street',
                          'https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg',  # NOQA
                          'https://www.youtube.com/watch?v=iszwuX1AK6A',
                          'Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living '
                          'the high life to his fall involving crime, corruption and the federal government.'),
              media.Movie('Interstellar',
                          'https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg',  # NOQA
                          'https://www.youtube.com/watch?v=2LqzF5WauAw',
                          'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s '
                          'survival.')]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    start()
