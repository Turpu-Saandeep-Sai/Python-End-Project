def load_data():
    filename = input("Enter the file name to load songs: ").strip()
    try:
        with open(filename, "r") as file:
            songs = {}
            for line in file:
                fields = [field.strip('"').strip() for field in line.strip().split(",")]
                if len(fields) != 5:
                    continue
                title, artist, album, genre, duration = fields
                song_dict = {"title": title, "album": album, "genre": genre, "duration": duration}
                if artist in songs:
                    songs[artist].append(song_dict)
                else:
                    songs[artist] = [song_dict]
            if not songs:
                print(f"No valid songs found in {filename}.")
            else:
                print(f"Songs loaded from {filename}.")
            return songs
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return {}

def view_database(songs):
    if not songs:
        print("No data loaded.")
        return
    print("Songs Database:")
    print("Title                          Artist                       Genre")
    print("=============================================================")
    for artist, song_list in sorted(songs.items()):
        for song in song_list:
            title = song["title"]
            genre = song["genre"]
            quoted_title = f'"{title}"'
            quoted_artist = f'"{artist}"'
            quoted_genre = f'"{genre}"'
            print(f"{quoted_title:<30} {quoted_artist:<25} {quoted_genre}")

def delete_song(songs):
    artist = input("Enter the artist's name of the song to delete: ").strip().strip('"')
    title = input("Enter the title of the song to delete: ").strip().strip('"')
    if artist in songs:
        for song in songs[artist][:]:  # Iterate over a copy
            if song["title"] == title:
                songs[artist].remove(song)
                if not songs[artist]:
                    del songs[artist]
                print(f'Deleted "{title}" by "{artist}" from the database.')
                return
    print("Song not found.")

def modify_song(songs):
    artist = input("Enter the artist's name of the song to modify: ").strip().strip('"')
    title = input("Enter the title of the song to modify: ").strip().strip('"')
    if artist in songs:
        for song in songs[artist]:
            if song["title"] == title:
                print(f'Current details:\nTitle: "{song["title"]}", Album: "{song["album"]}", Genre: "{song["genre"]}", Duration: "{song["duration"]}"')
                new_album = input("Enter new album (or press Enter to keep current): ").strip()
                new_genre = input("Enter new genre (or press Enter to keep current): ").strip()
                new_duration = input("Enter new duration (or press Enter to keep current): ").strip()
                if new_album:
                    song["album"] = new_album
                if new_genre:
                    song["genre"] = new_genre
                if new_duration:
                    song["duration"] = new_duration
                print(f'Modified "{title}" by "{artist}".')
                return
    print("Song not found.")

def main():
    songs = {}
    while True:
        print("\nDeveloper Menu:")
        print("1. Load Song Data")
        print("2. View Songs Database")
        print("3. Delete a Song")
        print("4. Modify a Song")
        print("5. Exit")
        option = input("\nSelect an option: ").strip()
        if option == "1":
            songs = load_data()
        elif option == "2":
            view_database(songs)
        elif option == "3":
            delete_song(songs)
        elif option == "4":
            modify_song(songs)
        elif option == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
