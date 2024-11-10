import os
import subprocess

def download_song(song_name, artist):
    # Construct the search query
    query = f"{song_name} {artist}"
    print(f"Searching for: {query}")
    
    # Use yt-dlp to search and download the song as mp3
    try:
        # The command will download audio only and convert it to mp3
        output_path = "/storage/emulated/0/Download/%(title)s.%(ext)s"  # Save to phone's Download folder
        subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '--audio-quality', '0', '--output', output_path, f'ytsearch:{query}'], check=True)
        print("Download complete! Check your Downloads folder.")
    except subprocess.CalledProcessError:
        print("Error downloading the song. Please try again.")

if __name__ == "__main__":
    print("Welcome to the music downloader! Type 'exit' to quit.")
    
    while True:
        # Ask user for song name and artist
        song_name = input("Enter the song name: ")
        if song_name.lower() == "exit":
            print("Goodbye!")
            break
        
        artist = input("Enter the artist name: ")
        
        # Call the function to download the song
        download_song(song_name, artist)
