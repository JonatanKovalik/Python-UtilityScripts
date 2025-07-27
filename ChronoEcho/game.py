import pygame
import sys
import json
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

MUSIC_ENDED = pygame.USEREVENT + 1 


def load_settings():
    file_path = "settings.json"
    try:
        with open(file_path, 'r') as f:
            settings_dict = json.load(f)
            print(f"Settings loaded for game from {file_path}")
            return settings_dict
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Settings file '{file_path}' not found or corrupted for game. Using default game settings.")
        return {
            "music_volume": 0.75
        }


def run_game():
    game_settings = load_settings()
    music_volume = game_settings.get("music_volume", 0.75)

    pygame.init()
    pygame.mixer.init()

    screen_width = 1200
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("ChronoEcho: The Temporal Labyrinth - The Game")

    music_tracks = [
        resource_path(os.path.join("Assets", "Audio", "BackgroundMusic01.mp3")),
        resource_path(os.path.join("Assets", "Audio", "BackgroundMusic02.mp3"))
    ]
    
    current_track_index = 0 

    def play_next_track():
        nonlocal current_track_index
        
        if current_track_index >= len(music_tracks):
            current_track_index = 0 
        
        music_file_to_play = music_tracks[current_track_index]
        
        try:
            pygame.mixer.music.load(music_file_to_play)
            pygame.mixer.music.set_volume(music_volume)
            pygame.mixer.music.set_endevent(MUSIC_ENDED) 
            pygame.mixer.music.play(0)
            print(f"Now playing: {music_file_to_play}")
            current_track_index += 1
        except pygame.error as e:
            print(f"ERROR: Could not load or play music track {music_file_to_play}: {e}")
            current_track_index += 1
            play_next_track()
    play_next_track()

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MUSIC_ENDED:
                play_next_track()
        
        screen.fill((50, 50, 50))
        pygame.draw.circle(screen, (255, 255, 255), (screen_width // 2, screen_height // 2), 20)

        pygame.display.flip()
        clock.tick(120)

    pygame.quit()
    sys.exit()