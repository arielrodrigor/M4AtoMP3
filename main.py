# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from pydub import AudioSegment

def convert_m4a_to_mp3(m4a_filepath, mp3_filepath):
    audio = AudioSegment.from_file(m4a_filepath, format='m4a')
    audio.export(mp3_filepath, format='mp3')

def main():
    # Usa la función para convertir un archivo
    convert_m4a_to_mp3('test.m4a', 'output.mp3')

if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
