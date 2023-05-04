import os
import openai

def whisper_transcribe(
    infile,
    outfile='whisper-transcription.txt',
    response_format='text',
    language='pt'
):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    with open(infile, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            file = audio_file,
            model = "whisper-1",
            response_format=response_format,
            language=language
        )

    with open(outfile, "w") as text_file:
        text_file.write(transcript)

    return transcript
    