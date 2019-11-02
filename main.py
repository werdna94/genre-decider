from corpus_creator import CorporaCreator
import csv


class Song:
    def __init__(self, title, artist, lyrics, genre):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.genre = genre


def get_corpus_info(songs):
    # Unique artists
    print('Unique artists')
    artists = []
    for song in songs:
        if not artists.__contains__(song.artist):
            artists.append(song.artist)
            print('{} {}'.format(song.artist, song.genre))

    # Genre counts
    country_count = 0
    rock_count = 0
    pop_count = 0
    alt_count = 0
    r_b_count = 0
    empty_songs = 0
    instrumentals = 0
    for song in songs:
        genre = song.genre
        if genre == 'country':
            country_count += 1
        elif genre == 'alternative':
            alt_count += 1
        elif genre == 'pop':
            pop_count += 1
        elif genre == 'rock':
            rock_count += 1
        elif genre == 'r-b-hip-hop':
            r_b_count += 1

        if song.lyrics == '':
            empty_songs += 1
        if song.lyrics == 'Instrumental' or song.lyrics == 'instrumental':
            instrumentals += 1

    print('Country: {}'.format(country_count))
    print('Rock: {}'.format(rock_count))
    print('Pop: {}'.format(pop_count))
    print('Alternative: {}'.format(alt_count))
    print('R & B: {}\n'.format(r_b_count))

    print('{} empty songs'.format(empty_songs))
    print('{} instrumentals'.format(instrumentals))


def remove_empty_and_instrumentals(songs):
    columns = ['Song Name', 'Artist', 'Lyrics', 'Genre']
    new_file = open('./corpora/clean_corpus_1.csv', 'a')
    writer = csv.writer(new_file)
    writer.writerow(columns)

    num_songs = 0
    for song in songs:
        if song.lyrics != '' and song.lyrics != 'Instrumental' and song.lyrics != 'instrumental':
            writer.writerow([song.title, song.artist, song.lyrics, song.genre])
            num_songs += 1

    print('{} songs passed the test'.format(num_songs))

def main():
    # creator = CorporaCreator('corpus_1.csv')

    # Read in the corpus
    songs = []
    corpus_csv = open('./corpora/corpus_1.csv')
    reader = csv.reader(corpus_csv)
    for row in reader:
        songs.append(Song(row[0], row[1], row[2], row[3]))

    get_corpus_info(songs)

    # Create cleaner corpus

    remove_empty_and_instrumentals(songs)

    # Remove songs with "unfortunately we can't..."

    # Remove words from between parens?

    # Manually relabel some of the songs or artists


if __name__ == '__main__':
    main()
