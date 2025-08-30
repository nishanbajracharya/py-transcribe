# py-transcribe
A python project to transcribe and generate srt subtitle files for foreign language videos powered by ffmpeg and [Whisper](https://github.com/openai/whisper). It transcribes two subtitle files: one matcing the original video language and another translated to english.

## Requirements
This project depends on `ffmpeg` and `openai-whisper`. `ffmpeg` binaries should be installed manually before running this project.

## Usage
Run the `main.py` file with the following arguments:

```sh
positional arguments:
  video_file  The path to the source video file to be transcribed.
  language    The language of the source video file to be transcribed.
```

### Example

```sh
python main.py /path/to/file ko
```

Here `ko` refers to Korean language aka Hanguel. Refer to [Whisper Tokenizer file](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py) for available languages and codes.

### Another example with output files

```sh
python main.py tv-01-09.mp4 es
```

This will output the following files in the project folder:

```sh
tv-01-09.es.srt
tv-01-09.en.srt
```
