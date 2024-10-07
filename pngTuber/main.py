import pygame
import pyaudio
import numpy as np

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PNG Tuber")

# Load PNG images
character_idle = pygame.image.load('assets/spriteClosed.png')
character_speaking = pygame.image.load('assets/spriteOpen.png')

# Initialize audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

def get_audio_level():
    data = np.frombuffer(stream.read(1024), dtype=np.int16)
    return np.abs(data).mean()

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # White background

    # Check for events like window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update character image based on audio level
    audio_level = get_audio_level()
    if audio_level > 500:  # Adjust threshold as needed
        screen.blit(character_speaking, (100, 100))
    else:
        screen.blit(character_idle, (100, 100))

    pygame.display.flip()

pygame.quit()
stream.stop_stream()
stream.close()
p.terminate()
