# 8-6
def city_country(city, country):
    val = f"{city}, {country}"
    return val

print(city_country('hk', 'hk'))
print(city_country('tokyo', 'japan'))
print(city_country('sydney', 'australia'))

def make_album(artist_name, album_title, songs=None):
    album = {}
    album['artist_name'] = artist_name
    album['album_title'] = album_title
    if songs:
        album['songs'] = songs

    return album


album1 = make_album('pricilla chan', 'autum', 11)
album2 = make_album('jackey cheung', 'pilot jacket')
album3 = make_album('Lupa', 'lalala')
print(album1, album2, album3)

active = True
while active:
    artist = input("Please enter artist (to quit press q): ")
    if artist == 'q':
        break
    album = input("Please enter album (to quit press q): ")
    if artist == 'q':
        break
    new_album = make_album(artist, album)
    print(new_album)

