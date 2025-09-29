import pygame
from pathlib import Path


# def init_audio():
#     pygame.mixer.init()       # Initialize audio
#     pygame.init()             # Good practice: initialize pygame generally

# # init_audio()

# def play_game_music():
#     # Use mixer.music for longer tracks
#     music_path = Path("assets/synth-decay-loop.wav")

#     pygame.mixer.music.load(music_path)       # Load music
#     pygame.mixer.music.set_volume(0.5)        # 0.0 – 1.0
#     pygame.mixer.music.play(loops=-1)         # Loop forever

#     # Keep the program running so you can hear it
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#     pygame.quit()

ASSETS = Path(__file__).resolve().parent / "assets"
_SFX = {}

def init_audio():
    # Low-ish buffer for snappy playback; increase if you hear crackles.
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(16)  # plenty for overlapping sfx

    # Preload SFX
    _SFX["eat"] = pygame.mixer.Sound(str(ASSETS / "crunch.wav"))
    _SFX["pain"] = pygame.mixer.Sound(str(ASSETS / "pain.wav"))
    _SFX["eat"].set_volume(0.5)
    _SFX["pain"].set_volume(0.5)

def play_game_music(volume=0.5):
    music_path = ASSETS / "synth-decay-loop.wav"   # or .ogg
    pygame.mixer.music.load(str(music_path))
    pygame.mixer.music.set_volume(volume)          # 0.0–1.0
    pygame.mixer.music.play(loops=-1)              # loop forever

def play_sfx(name: str):
    snd = _SFX.get(name)
    if snd:
        snd.play()                                 # does NOT interrupt mixer.music

def stop_music(fade_ms=500):
    pygame.mixer.music.fadeout(fade_ms)