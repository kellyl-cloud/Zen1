# How to Validate Transcriptions

Use this guide to validate an audio transcription in Label Studio.

---

## Basic Concepts

**Transcription:** A written record automatically generated from recorded audio.

**Utterance:** Transcriptions are broken into utterances — typically less than 30 seconds of audio from a single track.

**Segment:** An utterance has one or more segments. A segment is a single labeled span, typically equal to one word. In this document, segments are shown as ⟨angle⟩ ⟨brackets⟩.

> *A transcript contains many utterances made up of one or more segments.*

---

## Overview

Validation has three parts:

1. **Part One:** Validate the Labels
2. **Part Two:** Add or Remove Segments
3. **Part Three:** Adjust Segment Boundaries

---

## Part One: Labels

### What You're Doing

A transcription has been automatically generated. Your job is to check each segment to make sure it matches the word spoken in the audio.

### Basic Concepts

**Segment Label:** The written text that corresponds to the spoken word (or part of a word) in the segment.

### How to Check Label Accuracy

- Verify that the word you hear matches the segment label.
- Check that the capitalization is correct.
- Check that any needed punctuation is present.
- Transcriptions should be in the target language, using standard spelling and punctuation for that language variety.
- If the host or a guest occasionally uses another language and it is not more than 10% of speech, transcribe as:
  - `[New Language]` — if you do not know what the language is
  - `[Language Name]` — when you know (e.g., `[Spanish]`)
- 🚫 Do not let the transcription "correct" grammar or pronunciation.
  - Don't change "a umbrella" → "an umbrella" or "I runned" → "I ran".
- If they *significantly* mispronounce a word (e.g., "kind of" as /kwaində/), transcribe what they said (e.g., ⟨quinda⟩).

### Punctuation

#### Placement

- **Trailing punctuation** (commas, periods, question marks, hyphens, closing quotes, etc.) goes in the segment that **precedes** it.
- **Preceding punctuation** (open quotes, etc.) goes in the segment that **follows** it.

Examples:
```
⟨Hello,⟩ ⟨there.⟩
⟨"Hello,⟩ ⟨there,"⟩ ⟨Ben⟩ ⟨replied.⟩
⟨I⟩ ⟨asked,⟩ ⟨"How⟩ ⟨do⟩ ⟨you⟩ ⟨know?"⟩
```

#### Oxford Comma

Preferred but not required: ⟨red,⟩ ⟨white,⟩ ⟨and⟩ ⟨blue⟩

#### Titles

Use quotation marks anywhere you would normally italicize a title:
```
⟨Welcome⟩ ⟨to⟩ ⟨another⟩ ⟨episode⟩ ⟨of⟩ ⟨"Pots⟩ ⟨and⟩ ⟨Pans."⟩
```

#### Ellipses

Use *very rarely* to indicate trailing off:
```
⟨It⟩ ⟨all⟩ ⟨came⟩ ⟨down⟩ ⟨to…⟩ ⟨Anyway,⟩ ⟨let's⟩ ⟨go.⟩
```

- Use a comma if the speaker corrects themselves or continues.
- Use a period if the speaker ends their sentence.
- 🚫 Don't use ellipses for long pauses — timecodes supply that information.

---

## Part Two: Segments

### What You're Doing

Your job is to check that each segment matches a word in the audio, and that each word in the audio has a segment.

### Removing Segments

#### Unmatched Segments

Remove segments that have no matching audio. This can happen when:
- Short words like "to," "yeah," etc. get duplicate segments. (Check that the duplicate doesn't belong somewhere later in the transcript before deleting.)
- The ASR system mistakes a non-speech sound (breath, cough) for a word.

#### Contractions

- If the speaker **enunciates each word**, transcribe grammatically with separate segments:
  - going to → ⟨going⟩ ⟨to⟩
  - should have → ⟨should⟩ ⟨have⟩
- If the speaker **contracts the words**, transcribe phonetically with a single segment:
  - gonna → ⟨gonna⟩
  - shoulda → ⟨should've⟩

| If they pronounce… | Like this… | Transcribe as… |
|--------------------|------------|----------------|
| about | 'bout | ⟨about⟩ |
| all right | alright | ⟨alright⟩ |
| because | 'cause | ⟨'cause⟩ |
| don't know | dunno | ⟨dunno⟩ |
| give me | gimme | ⟨gimme⟩ |
| going to | gonna | ⟨gonna⟩ |
| it was | iwwuz | ⟨it⟩ ⟨was⟩ |
| kind of | kinda | ⟨kind⟩ ⟨of⟩ |
| let me | lemme | ⟨lemme⟩ |
| lot of | lotta | ⟨lot⟩ ⟨of⟩ |
| probably | prolly | ⟨prolly⟩ |
| saying | sayin' | ⟨saying⟩ |
| should've | shoulda | ⟨should've⟩ |
| sort of | sorta | ⟨sort⟩ ⟨of⟩ |
| them | 'em | ⟨them⟩ |
| want to | wanna | ⟨wanna⟩ |
| what are | what're | ⟨what're⟩ |
| you know | y'know | ⟨you⟩ ⟨know⟩ |

### Adding Segments

Add segments when the transcription misses a word, or when a single segment covers several words.

#### Very Fast Speech

Break longer segments into smaller ones:
```
I'mgonnawanna → ⟨I'm⟩ ⟨gonna⟩ ⟨wanna⟩
```

#### Mumbled Speech

Listen carefully to any sound on the waveform without associated segments — it may be quiet speech that needs transcribing.

#### Filler

Set off from surrounding segments with punctuation:
```
I uh know → ⟨I,⟩ ⟨uh,⟩ ⟨know.⟩
it's you know good → ⟨It's,⟩ ⟨you⟩ ⟨know,⟩ ⟨good.⟩
```

- Capitalize the first letter at the beginning of a sentence.
- 🚫 Don't add extra letters to indicate length: ~~⟨Ooooooh⟩~~

**Spelling conventions for American English fillers:**

| Spelling | Usage |
|----------|-------|
| ah | relief, confusion, understanding, wonder |
| ah-ha | realization, recognition, surprise (usually followed by !) |
| aw | disappointment, affection (🚫 not "awe") |
| hmm | thinking, surprise |
| huh | doubt, confusion, amusement |
| mm-hmm | agreement or affirmation (not "mhm") |
| mmm | satisfaction, thought, confusion |
| nuh-uh | disagreement |
| oh | surprise, wonder, understanding, annoyance, etc. |
| ooh | awe, pain, enthusiastic interest |
| uh | hesitation, uncertainty, holding the floor |
| uh-huh | agreement |
| uh-uh | disagreement |
| um | hesitation, uncertainty, searching for the next thought |

#### Dysfluencies, Repetitions, and Corrections

Set off with commas:
```
I I I think that → ⟨I,⟩ ⟨I,⟩ ⟨I⟩ ⟨think⟩ ⟨that⟩
I was ten was eleven then → ⟨I⟩ ⟨was⟩ ⟨ten,⟩ ⟨was⟩ ⟨eleven⟩ ⟨then⟩
```

#### False Starts and Self-interruptions

Transcribe as much of the word as you hear, followed by an em dash:
```
it's a misunderst a mistake → ⟨It's⟩ ⟨a⟩ ⟨misunderst—,⟩ ⟨a⟩ ⟨mistake.⟩
```

#### Numbers & Letters

Spell out numbers; each spoken word gets its own segment:
```
⟨one⟩ ⟨thousand⟩ ⟨three⟩ ⟨hundred⟩ ⟨forty⟩ ⟨five⟩ ⟨percent⟩
```

Use single letters, not letter names:
- ✅ ⟨fits⟩ ⟨you⟩ ⟨to⟩ ⟨a⟩ ⟨T⟩
- 🚫 ⟨fits⟩ ⟨you⟩ ⟨to⟩ ⟨a⟩ ⟨tee⟩

#### Proper Nouns

Separate personal and place names into separate words:
```
⟨Judy⟩ ⟨Smith⟩    ⟨Los⟩ ⟨Angeles⟩
```

Use official rendering for organizational names:
```
⟨eBay⟩    ⟨FedEx⟩    ⟨3four3⟩
```

#### Hyphenated Compounds

Split each word into its own segment; place hyphens at the end of appropriate segments:
```
tippity-tippity-top → ⟨tippity-⟩ ⟨tippity-⟩ ⟨top⟩
```

Don't split bound morphemes: ⟨re-record⟩, ⟨un-American⟩

#### Non-speech Events

Always use English labels regardless of the transcription's language:

| Label | When to use |
|-------|-------------|
| `[Laughter]` | Laughter (often missed by ASR) |
| `[Unintelligible]` | Speech you can hear but cannot make out (last resort) |
| `[Error]` | Utterances with no legitimate segments |
| `[Error: Noise]` | Segment is just noise |
| `[Error: Silence]` | Segment is just silence |
| `[Error: Unnecessary Segment]` | Duplicate segments from the previous utterance |
| `[Crosstalk Participant: ___]` | Speech from another participant |
| `[Crosstalk Background: ___]` | Speech from someone not in the conversation |
| `[Cough]` | Coughing |
| `[Sigh]` | Sighing |
| `[Humming]` | Humming (not "hmm" or "um") |
| `[Beatboxing]` | Beatboxing |

🚫 Don't use `[Error]` if any legitimate segments exist in the utterance — just delete the illegitimate ones.

---

## Part Three: Boundaries

### What You're Doing

Boundaries marking where each word starts and ends have already been placed automatically. Your job is to listen, check if they're accurate, and adjust any that are not.

### Basic Concepts

**Waveform:** A visual representation of loudness over time.

**Spectrogram:** A visual representation of frequency content over time.

**Boundary:** The vertical line marking where one word ends and the next begins.

### How to Validate a Boundary

Listen for these problems:

- Does it sound like the labeled word and *only* that word?
- Is any part of the word cut off at the beginning or end?
- Is there extra sound from the previous word at the beginning?
- Do multiple segments cover the same sounds?

🚨 **Above all, ensure that segments do not contain any parts of sounds from adjacent words.**

#### Building Up and Tapering Off

Include prevocalizations and aspirations within the segment's boundaries, but not in its label:
```
"mmmmbig" (as emphasis) → ⟨big⟩, but include the "mmmm" within the initial boundary
"take your pickHHH" → ⟨take⟩ ⟨your⟩ ⟨pick⟩, but include the /ʰ/ in ⟨pick⟩'s final boundary
```

- It's better to make segments too big than too small.
- 🚫 Don't include silence.
- 🚫 Don't include part of an adjacent segment.

---

## Notes for Languages Other than English

### Filler Speech and Contractions

Use conventionalized spellings in the target language for:
- Placeholders (um, uh in English)
- Backchanneling (hmm, mm-hmm, huh, yeah, etc.)
- Conventionalized contractions in informal writing (gonna, wanna, etc.)

### Punctuation

Use standard punctuation for the target language, except:
- Follow these guidelines for false starts and stutters/repetitions.

### Non-speech Events

Use the English words for labels like `[Laughter]`. Do not translate into the transcription's language.
