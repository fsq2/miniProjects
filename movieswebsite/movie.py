import webbrowser
import fresh_tomatoes


class Movie():
    def __init__(self, movietitle, story, moviepoaster, movietrailer):
        self.title = movietitle
        self.storyLine = story
        self.poaster = moviepoaster
        self.trilar = movietrailer


jonwick = Movie('Jhon wick ', 'An ex-hit-man comes out of retirement to track down the gangsters that killed his dog and took everything from him.', 'https://images-na.ssl-images-amazon.com/images/I/41i2SoUoRjL.jpg',
                'https://www.youtube.com/watch?v=RllJtOw0USI')

TheShawshankRedemption = Movie('The Shawshank Redemption ',
                               'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=BXUEUwwgIyU')

TheGodfather = Movie(
    'The Godfather', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=sY1S34973zA')


TheDarkKnight = Movie('The Dark Knight', 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                      'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=_PZpmTj1Q8Q')


Inception = Movie('Inception', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
                  'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=8hP9D6kZseM')

films = [jonwick, TheShawshankRedemption,
         TheGodfather, TheDarkKnight, Inception]
fresh_tomatoes.open_movies_page(films)
