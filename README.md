# ASR Validation Pipeline

A toolkit for converting dense audio NER exports from Ango into [Label Studio](https://labelstud.io/) for high-throughput ASR transcription validation.

## Why This Exists

Ango lags significantly when a single audio file has 1,000+ NER segments (one per word). This repo provides:

- A converter from Ango's JSON export format → Label Studio's JSON import format
- A Label Studio labeling config for audio NER validation
- Annotator guidelines for transcription validation
- Sample data for testing

---

## Quickstart

### 1. Install Label Studio

```bash
pip install label-studio
label-studio start
```

### 2. Convert your Ango export

```bash
python scripts/ango_to_label_studio.py your_ango_export.json output.json \
  --audio-url-prefix https://your-bucket.s3.amazonaws.com/audio/
```

### 3. Set up your Label Studio project

1. Create a new project in Label Studio
2. Go to **Settings → Labeling Interface**
3. Paste the contents of [`label_studio_config.xml`](label_studio_config.xml)
4. Go to **Import** and upload `output.json`

All pre-labels from Ango will load as predictions — annotators just review and correct.

---

## Repository Structure

```
asr-validation-pipeline/
├── scripts/
│   └── ango_to_label_studio.py   # Ango → Label Studio converter
├── samples/
│   ├── sample_ango_input.json    # Example Ango export (3 speakers, ~50 words)
│   └── sample_ls_output.json     # Expected Label Studio output
├── docs/
│   └── annotation_guide.md       # Annotator guidelines for transcription validation
├── label_studio_config.xml       # Label Studio labeling interface config
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml                # Validates converter runs cleanly on sample data
└── README.md
```

---

## Converter Details

### Input format (Ango)

```json
[
  {
    "trackId": "abc123",
    "participantName": "Speaker 1",
    "utterances": [
      {
        "words": ["Hello", "world"],
        "startTimes": [1.0, 1.5],
        "endTimes": [1.4, 2.0],
        "tags": [["verbatim"], ["um-ah"]]
      }
    ]
  }
]
```

### Output format (Label Studio)

```json
[
  {
    "data": {
      "audio_url": "https://your-bucket/abc123.mp3",
      "participant_name": "Speaker 1",
      "transcript": "Hello world"
    },
    "predictions": [
      {
        "model_version": "ango-export",
        "result": [
          {
            "type": "labels",
            "value": { "start": 1.0, "end": 1.4, "labels": ["verbatim"], "text": "Hello" }
          }
        ]
      }
    ]
  }
]
```

### CLI options

| Flag | Default | Description |
|------|---------|-------------|
| `input` | required | Path to Ango JSON export |
| `output` | required | Path for Label Studio JSON output |
| `--audio-url-prefix` | `""` | URL prefix for audio files. Track ID is appended as filename. |

---

## Supported NER Tags

| Tag | Description |
|-----|-------------|
| `verbatim` | Word transcribed exactly as spoken |
| `um-ah` | Filler/hesitation word |

To add new tags, update both the converter's output and `label_studio_config.xml`.

---

## Contributing

1. Fork the repo
2. Add your changes
3. Run the CI check locally: `python scripts/ango_to_label_studio.py samples/sample_ango_input.json /tmp/test_out.json`
4. Open a PR
