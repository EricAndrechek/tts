#!/usr/local/bin/python3

from google.cloud import texttospeech
import click
import os
import webbrowser
import sys

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
path = os.path.dirname(os.path.abspath(__file__))

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--voice', default='en-US-Wavenet-H', help="Choose a voice to speak with. For a list of voices, visit https://cloud.google.com/text-to-speech/docs/voices", 
    show_default=True)
@click.option('-r', '--rate', type=float, default=1.0, help="Optional. Speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by \
    the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values < 0.25 or > 4.0 will return an error.",
    show_default=True)
@click.option('-p', '--pitch', type=float, default=0.0, help="Optional. Speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the \
    original pitch. -20 means decrease 20 semitones from the original pitch.", show_default=True)
@click.option('-d', '--decibels', type=float, default=0.0, help="Optional. Volume gain (in dB) of the normal native volume supported by the specific \
    voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at \
    approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal \
    native signal amplitude. Strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.", show_default=True)
@click.option('-i', '--input-file', type=click.File('r'), default=None, help="Optional. Choose a file to read from and convert to speech. If this parameter is not provided or is unable \
    to be read from, read from standard input.", show_default=False)
@click.option('-o', '--output-file', type=click.Path(), default=None, help="Optional. Specify a file path for an audio file to be written to in the MP3 filetype.", show_default=False)
@click.argument('text', default='')
def init(voice, rate, pitch, decibels, input_file, output_file, text):
    """
    Google Cloud Text-to-Speech CLI - A more powerful version of 'say' or 'espeak'
    commands that brings modern text-to-speech technology to the command line.

    To use this tool, you will need to generate a Service Account and enable this API
    in the Cloud Console.

    This CLI is able to run 300 TTS processes per minute before hitting Google's quota,
    although it is possible to apply for extensions to this limit.

    To avoid any charges while using this service, stay under 4 million characters per 
    when month using non-wavenet voices, and under 1 million characters per month when
    using wavenet voices. More details including pricing when you exceed this limit are
    avaliable at: https://cloud.google.com/text-to-speech/pricing#pricing_table
    """

    if input_file is not None:
        text = input_file.read()
    if text == '':
        text = sys.stdin.read()
    run(voice, rate, pitch, decibels, output_file, text)
    
def run(voice, rate, pitch, decibels, output_file, text):
    client = texttospeech.TextToSpeechClient.from_service_account_json(os.path.join(path, 'TTSCreds.json'))
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    build_voice = texttospeech.VoiceSelectionParams(
        language_code=''.join(voice.split('-')[:1]),
        name=voice
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=rate,
        pitch=pitch,
        volume_gain_db=decibels,

    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=build_voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    if output_file is not None:
        with open(output_file, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
    else:
        with open(os.path.join(path, 'output.mp3'), "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
        os.system('mplayer ' + os.path.join(path, 'output.mp3') + ' >/dev/null 2>&1')
        

if __name__ == '__main__':
    init()