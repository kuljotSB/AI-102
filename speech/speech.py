#importing important libraries and utilities
import os 
import requests
import json
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

#loading the environment variables
load_dotenv()
speech_key=os.getenv('SPEECH_KEY')
speech_region=os.getenv('SPEECH_REGION')

def recognize_speech(): # speech to text
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    
    print("recognised: {}" .format(speech_recognition_result.text))
    
def speak_text(): #text to speech
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
 speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
 audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

 # The language of the voice that speaks.
 speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

 speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
 
 # Get text from the console and synthesize to the default speaker.
 print("Enter some text that you want to speak >")
 text = input()

 speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

 if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
 elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
            
