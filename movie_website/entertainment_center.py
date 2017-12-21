import media
import fresh_tomatoes


def main():
    #Star Wars: title, description, poster link, trailer link
    star_wars = media.Movie(
        "Star Wars: Episode V - The Empire Strikes Back",
        "After the rebels are overpowered by the Empire on their newly "
        "established base, Luke Skywalker begins Jedi training with Yoda. "
        "His friends accept shelter from a questionable ally as Darth Vader "
        "hunts them in a plan to capture Luke.",
        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",  #NOQA
        "https://www.youtube.com/watch?v=Ft9a-CfdZi8"
        )

    #Star Wars: title, description, poster link, trailer link
    nightmare_before_christmas = media.Movie(
        "The Nightmare Before Christmas",
        "Jack Skellington, king of Halloween Town, discovers Christmas Town, "
        "but his attempts to bring Christmas to his home cause confusion.",
        "https://upload.wikimedia.org/wikipedia/en/9/9a/The_nightmare_before_christmas_poster.jpg",  #NOQA
        "https://www.youtube.com/watch?v=wr6N_hZyBCk"
        )

    #Star Wars: title, description, poster link, trailer link
    wristcutters = media.Movie(
        "Wristcutters: A Love Story",
        "A film set in a strange afterlife way station that has been reserved"
        " for people who have committed suicide.",
        "https://resizing.flixster.com/vKBlXtUpqD2tpyGP33zNAglUpD0=/206x305/v1.bTsxMTI5NjI2MjtqOzE3NTkwOzEyMDA7MTIwMDsxNjAw",  #NOQA
        "https://www.youtube.com/watch?v=NHAQW2ko6yI"
        )

    #Star Wars: title, description, poster link, trailer link
    lazer_team = media.Movie(
        "Lazer Team",
        "Four losers are thrust into the position of saving the world when "
        "they stumble upon a UFO crash site and become genetically equipped "
        "to the battle suit on board.",
        "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Theatrical_poster_of_Lazer_Team.jpg/220px-Theatrical_poster_of_Lazer_Team.jpg",  #NOQA
        "https://www.youtube.com/watch?v=TI455Z37o30"
        )

    #Star Wars: title, description, poster link, trailer link
    wreck_it_ralph = media.Movie(
        "Wreck It Ralph",
        "A video game villain wants to be a hero and sets out to fulfill his"
        " dream, but his quest brings havoc to the whole arcade where he "
        "lives.",
        "https://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg",  #NOQA
        "https://www.youtube.com/watch?v=87E6N7ToCxs"
        )

    #Star Wars: title, description, poster link, trailer link
    forrest_gump = media.Movie(
        "Forrest Gump",
        "JFK, LBJ, Vietnam, Watergate, and other history unfold through the "
        "perspective of an Alabama man with an IQ of 75.",
        "https://i.ytimg.com/vi/EtYNngO7eq4/movieposter.jpg",
        "https://www.youtube.com/watch?v=bLvqoHBptjg"
        )

    #Set the movies that will be passed to the media file
    movies = [
        wristcutters,
        forrest_gump,
        wreck_it_ralph,
        nightmare_before_christmas,
        lazer_team,
        star_wars
        ]
    fresh_tomatoes.open_movies_page(movies)
if __name__ == '__main__':
    main()
