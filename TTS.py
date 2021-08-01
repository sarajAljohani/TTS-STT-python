from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(text,audio):
    authenticator = IAMAuthenticator('7-KyTRyrBXQSuRQO7wazH5Q-Q_5QzDs6R0qOZqD1hyu6')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )
    text_to_speech.set_service_url('https://api.us-east.text-to-speech.watson.cloud.ibm.com')
    audio_file = open(audio, 'wb')
    res = text_to_speech.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
    audio_file.close()


if __name__ == "__main__":
    main('In order to get a final response from STT we send a stop, this will force a final=True return message.','./output.mp3')