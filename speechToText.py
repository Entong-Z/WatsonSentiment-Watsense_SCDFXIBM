import sys
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(sys.argv[1])
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url(sys.argv[2])

with open(join(dirname(__file__), './.', sys.argv[3]),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        # content_type='audio/wav',
        # word_alternatives_threshold=0.9,
        # keywords=['colorado', 'tornado', 'tornadoes'],
        # keywords_threshold=0.5
    ).get_result()
f = open("transcribed.txt", "w")
f.write(speech_recognition_results["results"][0]["alternatives"][0]["transcript"])
f.close()