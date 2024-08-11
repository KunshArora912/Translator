# Translator

# Voice Assistant with Translation

This project is a simple voice assistant application that allows you to interact with it through voice commands. It can recognize speech, translate spoken Hindi to English, and provide audio output. The project uses the `pyttsx3` library for text-to-speech, `speech_recognition` for capturing and recognizing voice input, and `googletrans` for translation.

## Features

- **Voice Recognition**: Captures voice input using your microphone.
- **Text-to-Speech**: Converts text to speech using various voices.
- **Translation**: Translates spoken Hindi sentences to English.
  
## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Translator.git
    cd Translator
    ```

2. **Install the required packages**:
    You need to have Python installed. Install the dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` should include:
    ```text
    pyttsx3
    SpeechRecognition
    googletrans==4.0.0-rc1
    ```
    
    You may also need to install additional dependencies for `pyttsx3` depending on your system.

3. **Run the application**:
    ```bash
    python Translator.py
    ```

## Usage

Once the application is running:

1. **Voice Input**: The application will listen for your voice input when prompted.
2. **Translation**: It will prompt you to speak in Hindi, then translate your speech into English.
3. **Text-to-Speech**: The translated text will be spoken back to you.

## Project Structure

- `Translator.py`: The main script that runs the application.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.

## Customization

- **Changing Voices**: You can customize the voice used by editing the `getvoices()` function in `main.py`.
- **Translation Language**: The translation is currently set to translate from Hindi to English. You can change this by modifying the `language` parameter in the `Translator` object.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- The `pyttsx3` library for text-to-speech functionality.
- The `speech_recognition` library for voice input.
- The `googletrans` library for translation services.

