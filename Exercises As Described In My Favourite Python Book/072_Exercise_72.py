# Question :-
""" Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.Add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album's dictionary. Make at least one new function call that includes the number of tracks on an album."""

# First Version
 
def make_album(artist , title):
    music_album = {artist : title}
    return music_album

album = make_album("Hawayien" , "Arijit Singh")
print(album)

album = make_album("Soch na sake" , "Arijit Singh")
print(album)

album = make_album("Raabta" , "Arijit Singh")
print(album)

# Second Version

def make_album(artist , title , tracks = 0):
    music_album = {artist : title}
    
    if tracks:
        music_album["tracks"] = tracks

    return music_album

album = make_album("Hawayien" , "Arijit Singh")
print(album)

album = make_album("Soch na sake" , "Arijit Singh")
print(album)

album = make_album("Raabta" , "Arijit Singh")
print(album)

album = make_album("Tera Yaar Hoon Mein" , "Arijit Singh" , tracks=10)
print(album)