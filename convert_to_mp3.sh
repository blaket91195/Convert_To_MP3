#!/bin/bash

# Convert MP4 files to MP3
# Usage: ./convert_to_mp3.sh [input.mp4] [output.mp3]
#        ./convert_to_mp3.sh              (converts all .mp4 files in current directory)

if ! command -v ffmpeg &> /dev/null; then
    echo "Error: ffmpeg is not installed. Install it with: sudo apt install ffmpeg"
    exit 1
fi

convert_file() {
    local input="$1"
    local output="${2:-${input%.mp4}.mp3}"

    echo "Converting: $input -> $output"
    ffmpeg -i "$input" -vn -acodec libmp3lame -q:a 2 "$output" -loglevel error
    echo "Done: $output"
}

if [ "$1" != "" ]; then
    # Convert a specific file
    convert_file "$1" "$2"
else
    # Convert all MP4 files in the current directory
    shopt -s nullglob
    mp4_files=(*.mp4)

    if [ ${#mp4_files[@]} -eq 0 ]; then
        echo "No .mp4 files found in the current directory."
        echo "Usage: $0 [input.mp4] [output.mp3]"
        exit 1
    fi

    for file in "${mp4_files[@]}"; do
        convert_file "$file"
    done

    echo "All conversions complete."
fi
