import pygame
import cv2
import random
import numpy as np
import tkinter as tk
import os
from screeninfo import get_monitors

def render_multiline_text_with_fading_stroke(text, font, text_color, stroke_color, screen, screen_width, line_height):
    lines = text.split("@")  # Split the text into lines
    y = screen.get_height() // 2 - (len(lines)-1) * line_height // 2  # Calculate starting y position



    for line in lines:
        text_surface = font.render(line, True, stroke_color)
        text_rect = text_surface.get_rect(center=(screen_width // 2, y))
        screen.blit(text_surface, (text_rect.x+3, text_rect.y+3))
        screen.blit(text_surface, (text_rect.x-3, text_rect.y-3))

        y += line_height  # Move y position down for the next line

    # Render the actual text over the stroke
    y = screen.get_height() // 2 - (len(lines)-1) * line_height // 2  # Reset y position
    for line in lines:
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(center=(screen_width // 2, y))
        screen.blit(text_surface, text_rect)
        y += line_height  # Move y position down for the next line


monitors = get_monitors()
second = None
    
# Initialize Pygame
pygame.init()

# Tkinter for detecting screen size
root = tk.Tk()
root.withdraw()

if len(monitors) > 1:
    second = monitors[1]
    screen_width = second.width
    screen_height = second.height
    second_screen_width = second.x  # Assuming the second screen is positioned to the right
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{second_screen_width},0"
else:
    screen_width = 1920
    screen_height = 1080
    
# Create the window on the second monitor
screen = pygame.display.set_mode((screen_width, screen_height),pygame.NOFRAME )
pygame.display.set_caption("Random Word Game")

# Load the video using OpenCV
video = cv2.VideoCapture('finalmc.MP4')
video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))

# Define some words to display
with open("words.txt", 'r', encoding='utf-8') as file:
    # Read lines from the file and strip any extra whitespace
    words = [line.strip() for line in file]



font_size = 100
font = pygame.font.Font("./Kanit-Medium.ttf", font_size)

current_word = "KEYWORD"

# Setup a clock
clock = pygame.time.Clock()

# Main loop flag
running = True
stop_word = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_SPACE:
                if stop_word :
                    stop_word = False
                else:
                    stop_word = True
                    if len(words) > 0:
                        words.remove(current_word)
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_k:
                current_word = "KEYWORD"
            elif event.key == pygame.K_UP:
                font_size += 10
                font = pygame.font.Font("./Kanit-Medium.ttf", font_size)
            elif event.key == pygame.K_DOWN:
                font_size -= 10
                font = pygame.font.Font("./Kanit-Medium.ttf", font_size)
        
    # Get the video frame
    ret, frame = video.read()
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Convert the video frame to Pygame format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)

    # Scale video to screen size
    frame = pygame.transform.scale(frame, (screen_width, screen_height))

    # Display the video frame
    screen.blit(frame, (0, 0))

    # Randomly change the word if not stopped 
    if not stop_word:
        if len(words) > 0:
            current_word = random.choice(words)
        else:
            current_word = "The End"

    # Render and display the word
    # text_shadow = font.render(current_word, True, (115, 115, 115))
    # text_shadow_rect = text_shadow.get_rect(center=(screen_width // 2+4, screen_height // 2-3))
    # screen.blit(text_shadow, text_shadow_rect)
    # render_text_with_stroke(current_word, font, "#000000", (40, 40, 40), screen, screen.get_width())
    
    
    # text = font.render(current_word, True, (255, 255, 255))
    # text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    # screen.blit(text, text_rect)
    
    
    text_color = (0, 0, 0)  # White color for the text
    line_height = font_size + 25
    # render_multiline_text(current_word, font, text_color, screen, screen.get_width(), line_height)
    render_multiline_text_with_fading_stroke(current_word, font, (255,255,255),text_color, screen, screen.get_width(), line_height)
    

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Clean up
video.release()
pygame.quit()
