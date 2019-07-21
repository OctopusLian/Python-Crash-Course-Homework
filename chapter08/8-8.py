def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

print("Enter 'quit' at any time to stop.")

while True:
    title = raw_input(title_prompt)
    if title == 'quit':
        break
    
    artist = raw_input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")