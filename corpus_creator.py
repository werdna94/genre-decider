import lyricscorpora as lc
import csv
import time

# To add more to this list, look at billboard.charts() and find charts that end in '-songs' (for now)
GENRES = ['country', 'rock', 'pop', 'r-b-hip-hop', 'alternative']


def get_genre(genre, csv_writer):
    print('Getting ' + genre + ' music...')
    songs = []
    start = time.time()
    music = lc.Genre(genre).artist_list
    end = time.time()
    print('{} seconds'.format(end - start))
    for artist in music:
        songs += artist.get_song_list()

    written = 0
    print('Writing to csv...')
    start = time.time()
    for song in songs:
        print('lyrics for {}'.format(song.title))
        lyrics = song.get_lyrics()
        if lyrics is not None or lyrics is not "" or lyrics is not "Instrumental":
            csv_writer.writerow([song.title, song.artist.name, lyrics, genre])
            written += 1
    end = time.time()
    print('{} seconds'.format(end - start))

    return written


class CorporaCreator:

    # TODO add parameter for number of weeks back to get?
    def __init__(self, filename):
        total_songs = 0
        csv_columns = ['Song Name', 'Artist', 'Lyrics', 'Genre']
        csv_file = open('./corpora/' + filename, 'a')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_columns)

        for genre in GENRES:
            total_songs += get_genre(genre, csv_writer)

        print('Got {} songs total!'.format(total_songs))
        pass
