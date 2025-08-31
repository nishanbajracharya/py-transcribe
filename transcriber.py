import whisper
from whisper.utils import get_writer


def transcribe_audio(audio_file: str, lang: str = "en", directory: str = ".", modelName: str = "small"):
    """
    Transcribes a Original audio file and translates it to English,
    saving both as separate SRT files.

    Args:
        audio_file (str): The path to the audio file.
        lang (str): The language of the source audio file. Defaults to "en".
        directory (str): The directory to save the SRT files. Defaults to the current directory.
        modelName (str): The Whisper model to use for transcription. Defaults to "small".

    Returns:
        dict[str, str | list]: The full transcription/translation result dictionary.
    """
    try:
        # Load the small Whisper model.
        model = whisper.load_model(modelName)

        # Transcribe the audio in Original language.
        print("Transcribing in Original...")
        # verbose=False enables the progress bar during transcription
        original_language_result = model.transcribe(
            audio_file, language=lang, fp16=False, verbose=False
        )

        # Save the Original transcription as an SRT file.
        output_directory = directory
        original_srt_writer = get_writer("srt", output_directory)
        original_srt_writer(
            original_language_result, audio_file.replace(".wav", f".{lang}.srt")
        )


        if (lang == "en"):
            print("Source language is English. Skipping translation step.")
            return original_language_result

        # Translate the audio to English.
        print("Translating to English...")
        # verbose=False enables the progress bar during translation
        english_result = model.transcribe(
            audio_file, language=lang, fp16=False, task="translate", verbose=False
        )

        # Save the English translation as an SRT file.
        english_srt_writer = get_writer("srt", output_directory)
        english_srt_writer(english_result, audio_file.replace(".wav", ".en.srt"))

        return english_result
    except Exception as e:
        print(f"Error during transcription and translation: {e}")
        raise
