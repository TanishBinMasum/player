# import everything we need
import pygame
import os
import time


# Define a dictionary to store song titles and their lyrics
lyrics_database = {
    
}


def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(2)  # Play the song thrice


def fetch_lyrics(song_name, music_directory):
    lyrics = lyrics_database.get(song_name, [])
    current_line = 0
    current_lyrics = []

    # Define song_path here
    song_path = os.path.join(music_directory, song_name)

    while True:  # Loop indefinitely
        pygame.mixer.music.play(0)  # Play the song once
        start_time = time.time()

        while True:  # Loop until the song ends
            elapsed_time = time.time() - start_time
            if current_line < len(lyrics) and elapsed_time >= lyrics[current_line]["time"]:
                current_lyrics.append(lyrics[current_line]["text"])
                current_line += 1
                print("\n".join(current_lyrics))

            # Check if the song has completed
            if not pygame.mixer.music.get_busy():
                break

            # Add a delay to reduce CPU usage
            time.sleep(0.1)


def main():
    # Replace with the path to your music directory
    music_directory = "/your/music/dir"
    os.chdir(music_directory)

    pygame.mixer.init()  # Initialize the mixer here

    while True:
        print("Available songs:")
        for root, dirs, files in os.walk(music_directory):
            for file in files:
                if file.endswith(".mp3"):
                    print(file)

        song_choice = input(
            "Enter the name of the song you want to play (or 'quit' to exit): ")

        if song_choice.lower() == 'quit':
            break

        song_path = os.path.join(music_directory, song_choice)

        if os.path.exists(song_path):
            # Load and play the music before fetching lyrics
            play_music(song_path)
            fetch_lyrics(song_choice, music_directory)
        else:
            print("Invalid song name. Try again.")

# Run main
if __name__ == "__main__":
    main()
