"""
Ango → Label Studio converter for dense audio NER exports.

Input:  Ango JSON export (array of speaker tracks with utterances/words/tags)
Output: Label Studio JSON (one task per track, with audio NER pre-labels)

Usage:
    python ango_to_label_studio.py input.json output.json [--audio-url-prefix https://your-bucket/]

Label Studio config to use with this output (paste into your project's Labeling Config):

<View>
  <Audio name="audio" value="$audio_url" />
  <Labels name="label" toName="audio">
    <Label value="verbatim" background="#FFA39E"/>
    <Label value="um-ah" background="#FFD591"/>
  </Labels>
  <TextArea name="transcript" toName="audio" perRegion="true" value="$transcript"/>
</View>
"""

import json
import argparse
import sys
from pathlib import Path


def convert(input_path: str, output_path: str, audio_url_prefix: str = "") -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        tracks = json.load(f)

    ls_tasks = []

    for track in tracks:
        track_id = track.get("trackId", "unknown")
        participant_name = track.get("participantName", "unknown")
        utterances = track.get("utterances", [])

        # Flatten all words across utterances into a single list of regions
        regions = []
        region_id = 0

        for utt in utterances:
            words = utt.get("words", [])
            start_times = utt.get("startTimes", [])
            end_times = utt.get("endTimes", [])
            tags_list = utt.get("tags", [])

            # Pad tags_list if shorter than words (shouldn't happen but be safe)
            while len(tags_list) < len(words):
                tags_list.append([])

            for word, start, end, tags in zip(words, start_times, end_times, tags_list):
                if not tags:
                    continue  # Only emit pre-labels for tagged words

                for tag in tags:
                    region_id += 1
                    regions.append({
                        "id": f"region_{track_id}_{region_id}",
                        "from_name": "label",
                        "to_name": "audio",
                        "type": "labels",
                        "origin": "prediction",
                        "value": {
                            "start": round(start, 4),
                            "end": round(end, 4),
                            "labels": [tag],
                            "text": word.strip(),
                        },
                    })

        # Build a plain transcript string for reference
        all_words = []
        for utt in utterances:
            all_words.extend(utt.get("words", []))
        transcript = " ".join(w.strip() for w in all_words)

        task = {
            "data": {
                "audio_url": f"{audio_url_prefix}{track_id}.mp3",  # adjust extension as needed
                "track_id": track_id,
                "participant_name": participant_name,
                "transcript": transcript,
            },
            "predictions": [
                {
                    "model_version": "ango-export",
                    "score": 1.0,
                    "result": regions,
                }
            ],
        }

        ls_tasks.append(task)
        print(f"  ✓ {participant_name}: {len(regions)} labeled regions across {len(utterances)} utterances")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ls_tasks, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {len(ls_tasks)} tasks written to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert Ango audio NER export to Label Studio format")
    parser.add_argument("input", help="Path to Ango JSON export file")
    parser.add_argument("output", help="Path for Label Studio JSON output")
    parser.add_argument(
        "--audio-url-prefix",
        default="",
        help="URL prefix for audio files (e.g. https://my-bucket.s3.amazonaws.com/audio/). "
             "Track ID will be appended as the filename.",
    )
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Error: input file '{args.input}' not found", file=sys.stderr)
        sys.exit(1)

    print(f"Converting {args.input} → {args.output}")
    convert(args.input, args.output, args.audio_url_prefix)


if __name__ == "__main__":
    main()
