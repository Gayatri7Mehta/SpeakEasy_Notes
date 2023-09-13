import pyttsx3
def text_to_speech(text, rate=150):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', rate)
    speaker.say(text)
    speaker.runAndWait()
def main():
    print("Welcome to the Text-to-Speech for Visually Impaired Students!")

    # Prompt faculty to upload a text file
    file_path = input(
        "Faculty, please upload a text file containing the notes you want to be read aloud (e.g., notes.txt):\n")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            faculty_notes = file.read()

        rate = int(input("Enter the speech rate (default is 150): "))

        text_to_speech(faculty_notes, rate)
    except FileNotFoundError:
        print("File not found. Please make sure the file path is correct.")


if __name__ == "__main__":
    main()
