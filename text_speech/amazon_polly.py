"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
from playsound import playsound


def amazon_polly(text, voice, speed):
    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    session = Session(profile_name="default")
    polly = session.client("polly")

    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text='<speak><prosody rate="' + speed + '%">' + text + "</prosody></speak>", TextType="ssml", OutputFormat="mp3",
                                           VoiceId=voice)
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    os.remove("speech.mp3")

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output = "speech.mp3"

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file
                return "Could not write to file: " + str(error)
    else:
        # The response didn't contain audio data
        return "No AudioStream in response object."

    # Play the audio using the platform's default player
    # Test
    # playsound("speech.mp3")