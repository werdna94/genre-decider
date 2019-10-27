import lyricscorpora as lc
import csv

# To add more to this list, look at billboard.charts() and find charts that end in '-songs' (for now)
GENRES = ['dance-electronic', 'country', 'rock', 'pop', 'r-b-hip-hop', 'alternative']

class CorporaCreator:

    # TODO add parameter for number of weeks back to get?
    def __init__(self, filename):
        total_songs = 0
        csv_columns = ['Song Name', 'Artist', 'Lyrics', 'Genre']
        csv_file = open('./corpora/' + filename, 'a')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_columns)

        for genre in GENRES:
            total_songs += self.get_genre(genre, csv_writer)

        print('Got {} songs total!'.format(total_songs))
        pass

    def get_genre(self, genre, csv_writer):
        print('Getting ' + genre + ' music...')
        songs = []
        music = lc.Genre(genre).artist_list
        for artist in music:
            songs += artist.get_song_list()

        print('Writing to csv...')
        for song in songs:
            lyrics = song.get_lyrics()
            if lyrics is not None or lyrics is not '':
                csv_writer.writerow([song.title, song.artist.name, lyrics, genre])

        return len(songs)
