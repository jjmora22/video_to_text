# Video to Text Converter

## 📌 Project Overview
This script extracts audio from a video file and transcribes it into a text document using **MoviePy** for audio extraction and **Whisper (OpenAI)** for speech-to-text transcription.

---

## 🔹 How It Works
1. **Extracts audio** from a given video file (`video.mp4` by default).
2. **Transcribes the extracted audio** into text using the Whisper AI model.
3. **Saves the transcription** to a text file (`transcription.txt`).
4. **Deletes the temporary audio file** once the process is complete.

---

## 🔹 Requirements
Ensure you have the following dependencies installed:

```bash
pip install moviepy openai-whisper
```

You may also need `ffmpeg`, which can be installed via Homebrew (for macOS users):

```bash
brew install ffmpeg
```

---

## 🔹 Usage
1. Place your video file in the same directory as `video2txt.py`.
2. Run the script with:

```bash
python3 video2txt.py
```

3. The transcribed text will be saved in `transcription.txt`.

4. To use a different video file, modify the line:

```python
txt_file = process_video("video.mp4")
```
Replace `"video.mp4"` with your actual file name.

---

## 🔹 Configuration
- You can change the **Whisper model** used by modifying:

```python
model = whisper.load_model("base")
```

Available models:
- `tiny`
- `base`
- `small`
- `medium`
- `large`

Larger models provide better accuracy but require more computational resources.

---

## 🔹 Example Output
```
Extrayendo audio...
Transcribiendo audio...
Guardando transcripción...
Transcripción guardada en transcription.txt
```

---

## 🔹 Notes
- The script automatically deletes the temporary audio file (`temp_audio.wav`) after transcription.
- If you experience issues with `ffmpeg`, ensure it is installed and available in your system path.

---

## 🔹 License
This script is free to use and modify. Attribution is appreciated.

---

## 🔹 Author
- **GitHub:** [jjmora22](https://github.com/jjmora22)  
- **Email:** jjmora22@gmail.com *(replace with your actual email if desired)*

