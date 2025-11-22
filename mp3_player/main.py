import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"   # Hide the pygame support prompt
import pygame
def main():
    try:
        pygame.mixer.init()
        print("Pygame mixer initialized successfully.")
        # Additional code for the MP3 player would go here
    except Exception as e:
        print(f"Error initializing pygame mixer: {e}")
    folder='music'
    if not os.path.isdir(folder):
        print(f"Music folder '{folder}' does not exist.")
    mp3_files=[file for file in os.listdir(folder) if file.endswith('.mp3')]
    #print(mp3_files)
    if not mp3_files:
        print("No MP3 files found in the music folder.")
    while True:
        print('****MP3 PLAYER****')
        print('My songs list:')
        for index, file in enumerate(mp3_files):
            print(f"{index + 1}. {file}")
        #break
        choice_input=input("Enter the song number to play or 0 to exit: ")
        try:
            choice=int(choice_input)
            if choice==0:
                print("Exiting the MP3 player.")
                break
            elif 1 <= choice <= len(mp3_files):
                current_index= choice - 1  # Set current index to the chosen song
                 # Load and play the selected song
                song_path=os.path.join(folder, mp3_files[choice - 1])
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
                print(f"Playing: {mp3_files[choice - 1]}")
                print("Press 's' to stop playback.")
                print("Press 'n' to play next song.")
                while True:
                    command=input()
                    if command.lower()=='s':
                        pygame.mixer.music.stop()
                        print("Playback stopped.")
                        break
                    if command.lower()=='n':
                         # Advance to the next track in the list. Wrap to start when the end is reached.
                        current_index = (current_index + 1) % len(mp3_files)
                        song_path = os.path.join(folder, mp3_files[current_index])
                        pygame.mixer.music.load(song_path)
                        pygame.mixer.music.play()
                        print(f"Playing: {mp3_files[current_index]}")
                        # continue listening for 's' or 'n'
                    # ignore empty input and other commands, continue loop
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
if __name__=="__main__":
    main()

