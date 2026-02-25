import sys
import os
from pathlib import Path

try:
    from moviepy import VideoFileClip  # moviepy 2.x
except ImportError:
    try:
        from moviepy.editor import VideoFileClip  # moviepy 1.x fallback
    except ImportError:
        print("Error: moviepy is not installed. Run: pip install moviepy")
        sys.exit(1)


def convert_file(input_path, output_path=None):
    input_path = Path(input_path)

    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        return

    if output_path is None:
        output_path = input_path.with_suffix(".mp3")
    else:
        output_path = Path(output_path)

    print(f"Converting: {input_path} -> {output_path}")
    with VideoFileClip(str(input_path)) as video:
        video.audio.write_audiofile(str(output_path))
    print(f"Done: {output_path}\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Convert a specific file
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_file(input_file, output_file)
    else:
        # Convert all .mp4 files in the current directory
        mp4_files = list(Path(".").glob("*.mp4"))

        if not mp4_files:
            print("No .mp4 files found in the current directory.")
            print(f"Usage: python {sys.argv[0]} [input.mp4] [output.mp3]")
            sys.exit(1)

        for file in mp4_files:
            convert_file(file)

        print("All conversions complete.")
