# py-transcribe
A python project to transcribe and generate srt subtitle files for foreign language videos powered by ffmpeg and [Whisper](https://github.com/openai/whisper). It transcribes two subtitle files: one matcing the original video language and another translated to english.

## Requirements
This project depends on `ffmpeg` and `openai-whisper`. `ffmpeg` binaries should be installed manually before running this project.

## Usage
Run the `main.py` file with the following arguments:

```sh
Required parameters:

VIDEO_FILE
    The path to the source video file to be transcribed.

Optional parameters:

-l LANGUAGE, --language LANGUAGE
    The language of the source video file to be transcribed. Defaults to English ('en').
-m MODEL, --model MODEL
    The whisper model to use for transcription. Options include 'tiny', 'base', 'small', 'medium', and 'large'. Defaults to 'small'.
```

### Example

```sh
python main.py -l ko /path/to/file
```

Here `ko` refers to Korean language aka Hanguel. Refer to [Whisper Tokenizer file](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py) for available languages and codes.

### Another example with output files

```sh
python main.py -l es -m large tv-01-09.mp4
```

This will output the following files in the source video folder:

```sh
tv-01-09.es.srt
tv-01-09.en.srt
```
