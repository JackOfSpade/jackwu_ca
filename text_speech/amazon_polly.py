"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
from google.cloud import storage
from google.cloud.exceptions import NotFound
import random

def amazon_polly(text, voice, speed):
    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    try:
        session = Session(profile_name="default")
        polly = session.client("polly")
    except Exception as e:
        return "Session authentication exception: " + str(e)

    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text='<speak><prosody rate="' + speed + '%">' + text + "</prosody></speak>", TextType="ssml", OutputFormat="mp3",
                                           VoiceId=voice)
    except (BotoCoreError, ClientError) as error:
        return "The service returned an error"

    try:
        os.remove("speech.mp3")
    except OSError:
        pass

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
                return "Could not write to file: " + str(error)
    else:
        return "No AudioStream in response object."

    seed = str(random.random())[2:]

    return upload_to_bucket("speech" + seed + ".mp3", "speech.mp3", "jackwu.ca")

def upload_to_bucket(blob_name, path_to_file, bucket_name):
    storage_client = storage.Client.from_service_account_json("service_account_key.json")
    bucket = storage_client.get_bucket(bucket_name)

    try:
        blobs = bucket.list_blobs(prefix="speech_files")
        for blob in blobs:
            blob.delete()
    except:
        pass

    # Name of the object to be stored in the bucket
    blob = bucket.blob("speech_files/" + blob_name)
    # Name of the object in local file system
    blob.upload_from_filename(path_to_file)

    # returns a public url
    return blob.public_url