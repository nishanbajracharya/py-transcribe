import subprocess
import sys


def extract_audio(input_video: str, output_audio: str):
    """
    Extracts audio from a video file using FFmpeg and saves it as a WAV file.

    Args:
        input_video (str): The path to the input video file.
        output_audio (str): The desired path for the output WAV file.
    """
    # The FFmpeg command to extract audio.
    # The command is defined as a list of strings to avoid shell injection issues.
    command = [
        "ffmpeg",
        "-i",
        input_video,  # Input file
        "-vn",  # Disable video recording
        "-acodec",
        "pcm_s16le",  # Set audio codec to PCM signed 16-bit little-endian
        "-ar",
        "44100",  # Set audio sample rate to 44100 Hz
        "-ac",
        "2",  # Set audio channels to 2 (stereo)
        output_audio,  # Output file
    ]

    try:
        # Run the FFmpeg command.
        # 'check=True' will raise an exception if the command returns a non-zero exit code.
        subprocess.run(
            command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
        )
        print(f"Successfully extracted audio to: {output_audio}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing FFmpeg command. Details:")
        print(e.output.decode())
        print("Make sure FFmpeg is installed and available in your system's PATH.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: FFmpeg command not found.")
        print(
            "Please ensure FFmpeg is installed and its location is in your system's PATH."
        )
        sys.exit(1)
