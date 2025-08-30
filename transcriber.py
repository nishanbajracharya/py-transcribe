import whisper
from whisper.utils import get_writer


def transcribe_audio(audio_file: str, lang: str):
    """
    Transcribes a Original audio file and translates it to English,
    saving both as separate SRT files.

    Args:
        audio_file (str): The path to the audio file.
        lang (str): The language of the source audio file

    Returns:
        tuple: A tuple containing the English text (str), the
               Original text (str) and the full transcription/translation
               result dictionary (dict).
    """
    try:
        # Load the small Whisper model.
        model = whisper.load_model("small")

        # Transcribe the audio in Original language.
        print("Transcribing in Original...")
        # verbose=False enables the progress bar during transcription
        original_language_result = model.transcribe(
            audio_file, language=lang, fp16=False, verbose=False
        )
        original_language_text = original_language_result["text"]

        # Translate the audio to English.
        print("Translating to English...")
        # verbose=False enables the progress bar during translation
        english_result = model.transcribe(
            audio_file, language=lang, fp16=False, task="translate", verbose=False
        )
        english_text = english_result["text"]

        # Save the Original transcription as an SRT file.
        output_directory = "./"
        original_srt_writer = get_writer("srt", output_directory)
        original_srt_writer(
            original_language_result, audio_file.replace(".wav", "-" + lang)
        )

        # Save the English translation as an SRT file.
        english_srt_writer = get_writer("srt", output_directory)
        english_srt_writer(english_result, audio_file.replace(".wav", "-en"))

        return english_text, original_language_text, english_result
    except Exception as e:
        print(f"Error during transcription and translation: {e}")
        raise
