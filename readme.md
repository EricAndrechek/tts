# TTS CLI
The new-and-improved command line text-to-speech program aiming to bring modern tts technology to the command line.

This program utilizing the Google Cloud Text-to-Speech API with a easy-to-use CLI that mimics Apple's "say" CL tool.

## Setup
1. In the Cloud Console, on the project selector page, select or create a Cloud project. 

    [Go to the project selector page](https://console.cloud.google.com/projectselector2/home/dashboard)

2. Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm billing is enabled for your project.](https://cloud.google.com/billing/docs/how-to/modify-project)

3. Enable the Cloud Text-to-Speech API.
    
    [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=texttospeech.googleapis.com)

4. Set up authentication:

    a. In the Cloud Console, go to the **Create service account key** page.
        
    [Go to the Create Service Account Key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey)


    b. From the **Service account** list, select **New service account**.
    
    c. In the **Service account name** field, enter a name.
    
    d. Don't select a value from the **Role** list. No role is required to access this service.
    
    e. Click **Create**. A note appears, warning that this service account has no role.
    
    d. Click **Create without role**. A JSON file that contains your key downloads to your computer.

5. Save your JSON file into the same directory this project is downloaded in and name it `TTSCreds.json`

6. To optimize the ease of use of running the command, it is advised that you `sudo chmod +x tts.py` so that it can be run directly. 

7. Lastly, to add this script as an alias, run `nano ~/.zshrc` (or whatever other shell you run) and add `alias tts={{direct path to tts.py}}`. Finally, press CTRL X >> y >> [ENTER], and then type `source ~/.zshrc` into terminal and hit enter. Now, no matter where you are, `tts` should run this python script.

## Usage

Usage: tts.py [OPTIONS] [TEXT]

  Google Cloud Text-to-Speech CLI - A more powerful version of 'say' or
  'espeak' commands that brings modern text-to-speech technology to the
  command line.

  To use this tool, you will need to generate a Service Account and enable
  this API in the Cloud Console.

  This CLI is able to run 300 TTS processes per minute before hitting
  Google's quota, although it is possible to apply for extensions to this
  limit.

  To avoid any charges while using this service, stay under 4 million
  characters per  when month using non-wavenet voices, and under 1 million
  characters per month when using wavenet voices. More details including
  pricing when you exceed this limit are avaliable at:
  https://cloud.google.com/text-to-speech/pricing#pricing_table

Options:
  -v, --voice TEXT           Choose a voice to speak with. For a list of
                             voices, visit https://cloud.google.com/text-to-
                             speech/docs/voices  [default: en-US-Wavenet-H]

  -r, --rate FLOAT           Optional. Speaking rate/speed, in the range
                             [0.25, 4.0]. 1.0 is the normal native speed
                             supported by     the specific voice. 2.0 is twice
                             as fast, and 0.5 is half as fast. If unset(0.0),
                             defaults to the native 1.0 speed. Any other
                             values < 0.25 or > 4.0 will return an error.
                             [default: 1.0]

  -p, --pitch FLOAT          Optional. Speaking pitch, in the range [-20.0,
                             20.0]. 20 means increase 20 semitones from the
                             original pitch. -20 means decrease 20 semitones
                             from the original pitch.  [default: 0.0]

  -d, --decibels FLOAT       Optional. Volume gain (in dB) of the normal
                             native volume supported by the specific
                             voice, in the range [-96.0, 16.0]. If unset, or
                             set to a value of 0.0 (dB), will play at normal
                             native signal amplitude. A value of -6.0 (dB)
                             will play at     approximately half the amplitude
                             of the normal native signal amplitude. A value of
                             +6.0 (dB) will play at approximately twice the
                             amplitude of the normal     native signal
                             amplitude. Strongly recommend not to exceed +10
                             (dB) as there's usually no effective increase in
                             loudness for any value greater than that.
                             [default: 0.0]

  -i, --input-file FILENAME  Optional. Choose a file to read from and convert
                             to speech. If this parameter is not provided or
                             is unable     to be read from, read from standard
                             input.

  -o, --output-file PATH     Optional. Specify a file path for an audio file
                             to be written to in the MP3 filetype.

  -h, --help                 Show this message and exit.