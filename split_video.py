#!/usr/bin/env python3
"""Split video into two equal parts"""
import sys
sys.path.insert(0, 'C:\\Users\\x\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages')

from moviepy.editor import VideoFileClip

# Load video
input_file = 'evidence/videos/TV-20260328-1359-1300_Thilo_Maack_webxxl.mp4'
output_part1 = 'evidence/videos/TV-20260328-1359-1300_Thilo_Maack_webxxl_part1.mp4'
output_part2 = 'evidence/videos/TV-20260328-1359-1300_Thilo_Maack_webxxl_part2.mp4'

print(f'Loading video: {input_file}')
clip = VideoFileClip(input_file)
duration = clip.duration
half = duration / 2

print(f'Video duration: {duration:.2f}s')
print(f'Splitting at: {half:.2f}s')

# Split into two parts
clip1 = clip.subclip(0, half)
clip2 = clip.subclip(half, duration)

print('Writing part 1...')
clip1.write_videofile(output_part1, codec='libx264', audio_codec='aac', verbose=False, logger=None)

print('Writing part 2...')
clip2.write_videofile(output_part2, codec='libx264', audio_codec='aac', verbose=False, logger=None)

clip.close()
print('Split complete!')
print(f'Part 1: {output_part1}')
print(f'Part 2: {output_part2}')
