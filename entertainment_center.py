import media
import fresh_tomatoes


# Movie instances

thematrix = media.Movie("The Matrix",
                        "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

hackers = media.Movie("Hackers",
                      "This movie is about hackers who are blamed for making a virus that will capsize 5 oil tankers.",
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
                      "https://www.youtube.com/watch?v=Ql1uLyuWra8")

wargames = media.Movie("War Games",
                       "A young man finds a back door into a military central computer in which reality is confused with game-playing, possibly starting World War III.",
                       "https://upload.wikimedia.org/wikipedia/en/2/29/Wargames.jpg",
                       "https://www.youtube.com/watch?v=tAcEzhQ7oqA")

antitrust = media.Movie("AntiTrust",
                        "A computer programmer's dream job at a hot Portland-based firm turns nightmarish when he discovers his boss has a secret and ruthless means of dispatching anti-trust problems.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2a/Antitrust_poster.jpg",
                        "https://www.youtube.com/watch?v=eS1EOjO9sgw")

thenet = media.Movie("The Net",
                     "A computer programmer stumbles upon a conspiracy, putting her life and the lives of those around her in great danger.",
                     "https://upload.wikimedia.org/wikipedia/en/0/0d/Netposter1995.jpg",
                     "https://www.youtube.com/watch?v=46qKHq7REI4")

transcendence = media.Movie("Transcendence",
                            "A scientist's drive for artificial intelligence, takes on dangerous implications when his consciousness is uploaded into one such program.",
                            "https://upload.wikimedia.org/wikipedia/en/e/ef/Transcendence2014Poster.jpg",
                            "https://www.youtube.com/watch?v=VCTen3-B8GU")


# Movies list

movies = [thematrix, hackers, wargames, antitrust, thenet, transcendence]


# Open movies function

fresh_tomatoes.open_movies_page(movies)