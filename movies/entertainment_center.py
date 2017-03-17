import media
import fresh_tomatoes

toy_story = media.movie("Toy story",
                        "A story of a boy and his toys in life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.movie("Avatar", "A marine of alien planet",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#toy_story.show_trailer()

martian = media.movie("Martian", "This is story of an astronaut who is mistakenly presumed dead and left behind on Mars. The film depicts his struggle to survive and others' efforts to rescue him.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://youtu.be/ej3ioOneTy8?t=19s")

got = media.movie("Game of Thrones", "", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM5OTQ1MTY5Nl5BMl5BanBnXkFtZTgwMjM3NzMxODE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                    "https://www.youtube.com/watch?v=s7L2PVdrb_8")

mentalist  = media.movie("The Mentalist", "", "http://www.impawards.com/tv/posters/mentalist.jpg",
                            "https://www.youtube.com/watch?v=nn2Q69pSC_M")

homeland = media.movie("Homeland", "", "http://screencrush.com/files/2015/07/homeland-season-5.jpg",
                        "https://www.youtube.com/watch?v=6EBmdbsWTNE")
#martian.show_trailer()
movies = [got, mentalist,  homeland, martian, avatar, toy_story ]
fresh_tomatoes.open_movies_page(movies)
