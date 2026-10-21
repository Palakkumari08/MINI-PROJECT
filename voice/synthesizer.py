
from TTS.api import TTS


MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"


def generate_speech(
    text,
    reference_audio,
    output_audio="clara_response.wav",
    language="hi",
):
    """Generate speech for Clara's response using XTTS-v2."""

    tts = TTS(MODEL_NAME, gpu=False)

    tts.tts_to_file(
        text=text,
        speaker_wav=reference_audio,
        language=language,
        file_path=output_audio,
    )

    return output_audio
