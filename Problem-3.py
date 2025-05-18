import csv

def load_database():
    titles_dict = {}
    artists_dict = {}
    with open('songs_database.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            song = {
                'title': row[0],
                'artist': row[1],
                'album': row[2],
                'genre': row[3],
                'duration': row[4]
            }
            title_lower = song['title'].lower()
            artist_lower = song['artist'].lower()
            if title_lower not in titles_dict:
                titles_dict[title_lower] = []
            titles_dict[title_lower].append(song)
            if artist_lower not in artists_dict:
                artists_dict[artist_lower] = []
            artists_dict[artist_lower].append(song)
    return titles_dict, artists_dict

def search_by_title(titles_dict, title):
    print(f"Searching for songs with title: '{title}'")
    title_lower = title.lower()
    if title_lower in titles_dict:
        for song in titles_dict[title_lower]:
            print(f"Found: '{song['title']}' by {song['artist']} (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
    else:
        print(f"Song title '{title}' does not exist in the database.")

def search_by_artist(artists_dict, artist):
    print(f"Searching for songs by artist: '{artist}'")
    artist_lower = artist.lower()
    if artist_lower in artists_dict:
        for song in artists_dict[artist_lower]:
            print(f"Found: '{song['title']}' (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
    else:
        print(f"No songs found for artist '{artist}'.")

def main():
    titles_dict, artists_dict = load_database()
    while True:
        print("--- User Menu ---")
        print("1. Search for a Song by Title")
        print("2. Search for All Songs by an Artist")
        print("3. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            title = input("Enter the song title to search: ").strip()
            search_by_title(titles_dict, title)
        elif choice == '2':
            artist = input("Enter the artist's name to search: ").strip()
            search_by_artist(artists_dict, artist)
        elif choice == '3':
            print("Exiting the Songs Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
