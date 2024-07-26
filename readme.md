# Voice Recognition AI Assistant

This is a simple voice recognition AI assistant implemented in Python. It uses the `speech_recognition` library for voice recognition, `gtts` for text-to-speech conversion, and a simple rule-based response system. The assistant can recognize voice commands and respond with a male voice. It can also close the application when the user says "close".

## Features

- Voice recognition using Google's Web Speech API
- Text-to-speech conversion using Google Text-to-Speech (GTTS)
- Simple rule-based responses
- Closes the application when the user says "close"
- Handles wait time errors and other exceptions gracefully

## Prerequisites

- Python 3.6 or higher
- A working microphone and speaker setup

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/voice-recognition-ai-assistant.git
    cd voice-recognition-ai-assistant
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```bash
    python voice_recg_with_audio_resp.py
    ```

2. Speak into the microphone. The assistant will recognize your voice and respond accordingly.

3. To close the application, say "close".

## Example

AI Voice Assistant is running...
Listening...
Recognizing...
User said: hello
AI: Hello! How can I help you today?
Listening...
Recognizing...
User said: close
AI: Goodbye!
Closing the application...

