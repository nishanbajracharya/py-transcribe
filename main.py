import argparse
import os
import sys
from audio_extractor import extract_audio
from transcriber import transcribe_audio


def main():
    """
    Main function to parse arguments and run the transcription process.
    """
    # Create an argument parser to handle command-line arguments
    parser = argparse.ArgumentParser(
        description="Transcribe a video file to text using FFmpeg and Whisper."
    )
    parser.add_argument(
        "video_file", help="The path to the source video file to be transcribed."
    )
    parser.add_argument(
        "language", help="The language of the source video file to be transcribed."
    )

    # Parse the arguments provided by the user
    args = parser.parse_args()
    video_file: str = args.video_file
    lang: str = args.language or "en"

    # Check if the video file exists
    if not os.path.exists(video_file):
        print(f"Error: The video file '{video_file}' was not found.")
        sys.exit(1)

    print(f"Starting transcription for '{video_file}'...")

    # Generate a temporary audio file name based on the video file's name
    base_name = os.path.splitext(os.path.basename(video_file))[0]
    audio_file = f"{base_name}.wav"

    try:
        # Step 1: Extract audio from the video file
        # audio_file = "temp_audio.wav"
        extract_audio(video_file, audio_file)

        # Step 2: Transcribe the extracted audio using Whisper
        print("Transcribing audio...")
        transcribe_audio(audio_file, lang)

        # Step 3: Print that final transcription is completed
        print("\n--- Transcription Completed ---")
        # print(transcription_result)

        # Step 4: Clean up the temporary audio file
        os.remove(audio_file)
        print("\nTemporary audio file removed.")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Clean up the audio file if it was created
        if os.path.exists(audio_file):
            os.remove(audio_file)
            print("Temporary audio file was cleaned up.")


if __name__ == "__main__":
    main()
