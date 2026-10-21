# Clara — Emotion-Aware AI Companion for Dementia Care

**A Mini Project for Personalized, Compassionate AI Communication**

## 1. Project Overview

Clara is an AI-powered companion designed to support people living with dementia through empathetic conversation and personalized voice interaction.

The project aims to combine a generative AI dialogue system with emotion recognition and personalized text-to-speech synthesis. The goal is to make interactions feel more familiar, supportive, and comfortable for users.

Clara is being developed as a modular system so that dialogue generation, emotion recognition, voice synthesis, and the user interface can be developed and tested independently.

## 2. Problem Statement

People living with dementia may experience memory difficulties, confusion, anxiety, and challenges recognizing or remembering everyday interactions. Familiar voices and calm, reassuring communication may help make conversations more comfortable.

Traditional voice assistants generally provide generic responses and may not adapt sufficiently to the user's emotional state or personal preferences.

Clara aims to address this challenge through:

- Emotion-aware conversational responses.
- Personalized speech using a consented caregiver or family voice sample.
- Supportive, simple, and reassuring language.
- A modular architecture that allows future integration of emotion recognition, memory, and a graphical user interface.

Clara is intended as a supportive companion, not a replacement for professional medical care or human caregivers.

## 3. Project Objectives

1. Develop an AI-based conversational response generator.
2. Generate empathetic responses using the user's message and detected emotional state.
3. Integrate a text-to-speech engine capable of personalized voice synthesis.
4. Explore caregiver or family voice personalization using Coqui XTTS-v2.
5. Handle API errors through a fallback response mechanism.
6. Develop a modular foundation for future integration with emotion recognition, memory, and a Streamlit interface.
7. Evaluate response quality and voice naturalness as development progresses.

## 4. System Architecture

Clara is planned as a modular pipeline:

1. **User Input:** The user communicates with Clara.
2. **Emotion Recognition:** The emotion recognition module identifies an emotional state.
3. **Dialogue Generation:** Gemini generates a supportive response using the user's message, detected emotion, and available contextual memories.
4. **Voice Synthesis:** XTTS-v2 converts the generated response into speech using a selected reference voice.
5. **User Interface:** A future integrated interface will connect these components and present the interaction to the user.

### Current implementation status

The Gemini dialogue-generation component has been integrated and tested. XTTS-v2 has also been tested separately for Hindi speech generation using a reference audio sample. The complete end-to-end pipeline has not yet been verified as an integrated application.

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Google Gemini API | AI-powered dialogue generation |
| `google-genai` | Python SDK for Gemini |
| Coqui XTTS-v2 | Multilingual text-to-speech and reference-voice conditioning |
| PyTorch | Machine learning framework used by the speech engine |
| `torchaudio` | Audio-related support for PyTorch |
| FFmpeg | Audio conversion and preprocessing |
| pytest | Automated testing |
| Git and GitHub | Version control and project collaboration |
| VS Code | Development environment |

**Planned integration:** Streamlit for the user interface, along with emotion recognition and conversational memory modules.

## 6. Work Completed So Far

### 6.1 Gemini API Integration

The Gemini API has been integrated into the dialogue-generation module.

The dialogue generator is designed to use:
- The user's message.
- The detected emotion supplied to the generator.
- Available conversational memories or context.
- Instructions intended to encourage simple, empathetic, and dementia-care-sensitive responses.

The API integration was tested successfully with a live Gemini request.

### 6.2 Error Handling and Fallback Responses

A fallback mechanism has been implemented to handle dialogue-generation failures.

When an API error occurs, Clara can return a predefined response rather than leaving the interaction without a reply. An automated test checks that the fallback response contains the expected reassuring language.

### 6.3 Automated Testing

Automated tests have been created for the dialogue component. The project development notes record that the existing dialogue tests passed after Gemini integration.

Testing includes mocked API behavior so that error-handling logic can be checked without relying on a successful live API request for every test.

### 6.4 XTTS-v2 Environment Setup

A separate Python environment was created for voice synthesis to keep the speech-generation dependencies isolated from the main Gemini environment.

The voice synthesis environment was configured with Python 3.11, PyTorch, Coqui TTS dependencies, and FFmpeg.

Additional dependency issues involving Transformers and TorchCodec were resolved so that the XTTS-v2 package could be imported successfully.

### 6.5 Audio Preprocessing

A voice sample recorded using Voice Memos was converted from M4A format into WAV format using FFmpeg.

The resulting reference audio was approximately 20.5 seconds long, mono-channel, and sampled at 22,050 Hz.

The original recording was preserved separately.

### 6.6 Hindi Speech Generation

XTTS-v2 was downloaded and tested locally.

A Hindi sentence was synthesized into a WAV audio file using the reference audio and the Hindi language setting (`language="hi"`). The generation script completed successfully and saved the output audio.

This verifies that the local XTTS-v2 setup can generate Hindi speech. The quality and similarity of the generated voice still require systematic evaluation.

### 6.7 GitHub Version Control

The project is maintained in the following repository:

https://github.com/Palakkumari08/MINI-PROJECT

The Gemini integration and the updated `.gitignore` have been committed and pushed to the `main` branch.

The `.gitignore` excludes virtual environments, local audio recordings, generated voice files, model checkpoints, environment files, and other local development artifacts from normal Git tracking.

## 7. Project Structure

The main files currently identified in the repository include:

```text
MINI-PROJECT/
├── README.md
├── requirements.txt
├── dialogue/
│   ├── __init__.py
│   └── generator.py
├── voice/
│   ├── __init__.py
│   └── synthesizer.py
├── tests/
│   └── test_dialogue.py
└── .gitignore
```

Local development scripts such as `check_gemini_manual.py` and `test_xtts.py` are also being used during development. They are not part of the committed project structure listed above.

## 8. Development Environment

The development setup uses two separate Python environments:

- **Main environment:** Python 3.12, used for the Gemini dialogue component and its associated dependencies.
- **Voice environment:** Python 3.11, used for Coqui XTTS-v2 and its speech-generation dependencies.

Keeping the environments separate helps avoid dependency conflicts between the dialogue system and the voice synthesis engine.

The Gemini API key is read from the `GEMINI_API_KEY` environment variable rather than being written directly into the source code.

For security, API keys, personal voice recordings, and generated audio samples should not be committed to the public repository.

## 9. Current Limitations

The project is still under development. The following work remains incomplete or requires further validation:

- Integrating emotion recognition with the dialogue and voice modules.
- Connecting Gemini dialogue generation and XTTS-v2 in one end-to-end workflow.
- Completing the Streamlit user interface.
- Implementing and validating conversational memory.
- Improving voice naturalness, pronunciation, and similarity to the reference speaker.
- Testing different emotional speaking styles and prosody.
- Evaluating generated speech using a structured listening test and Mean Opinion Score (MOS).
- Testing the system with a wider range of messages, emotions, and failure scenarios.
- Conducting usability and safety evaluation before any real-world care deployment.

## 10. Voice Personalization, Consent, and Safety

Voice personalization is intended to use a reference recording supplied with the appropriate consent of the speaker.

Before using or sharing a cloned voice, the project should establish clear permission for voice cloning and specify how recordings and generated audio may be stored and used.

The system should provide a fallback voice if personalized synthesis fails. Generated responses should remain calm, respectful, and supportive. Clara should not be presented as a diagnostic or medical decision-making system.

**Licensing note:** The Coqui XTTS-v2 model is distributed under the Coqui Public Model License (CPML). Its terms must be reviewed before redistributing the model, distributing a product using it, or using it commercially.

## 11. Future Scope

Planned improvements include:

1. Integrating the emotion recognition module.
2. Connecting dialogue generation to personalized speech synthesis.
3. Developing the Streamlit application.
4. Adding conversational memory and context management.
5. Supporting emotion-aware prosody and speaking style.
6. Evaluating voice naturalness and speaker similarity, with a target MOS of at least 3.5/5.
7. Adding a backup voice and robust error handling.
8. Improving privacy, consent management, and testing.
9. Evaluating the application with appropriate safeguards before real-world use.

## 12. Conclusion

Clara is being developed as a personalized AI companion for dementia care. The initial development has established a working Gemini-based dialogue component with fallback handling and a separate local XTTS-v2 environment capable of generating Hindi speech from a reference audio sample.

These components provide a foundation for the next development phase: integrating emotion recognition, dialogue generation, personalized speech synthesis, conversational memory, and the user interface into a single application.

The complete system, voice quality, and care-related effectiveness still require integration and evaluation.

---

**Project Repository:** https://github.com/Palakkumari08/MINI-PROJECT

**Project Status:** In Development

**Current Focus:** Gemini dialogue generation completed and tested; XTTS-v2 Hindi speech generation tested separately; end-to-end integration and remaining modules pending.
