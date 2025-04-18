import os
import pydub
from pydub import AudioSegment

def generate_typing_audio(essay_file, keystroke_dir, output_file):
    try:
        with open(essay_file, 'r') as f:
            essay = f.read().lower()
    except FileNotFoundError:
        print(f"Error: Essay file '{essay_file}' not found.")
        return

    keystrokes = {}
    for filename in os.listdir(keystroke_dir):
        if filename.endswith(".wav"):
            char = filename.split(".")[0]
            keystrokes[char] = AudioSegment.from_wav(os.path.join(keystroke_dir, filename))

    typing_audio = AudioSegment.silent(duration=0)
    general_pause = AudioSegment.silent(duration=300)

    for char in essay:
        if char.isalpha():
            typing_audio += keystrokes[char] + general_pause
        else:
            typing_audio += general_pause

    typing_audio.export(output_file, format="mp3")
    print(f"Typing audio generated and saved to '{output_file}'.")


essay_file = "text.txt"
keystroke_dir = r"C:\keyboard strokes"
output_file = "password.mp3"


generate_typing_audio(essay_file, keystroke_dir, output_file)