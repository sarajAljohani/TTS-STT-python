import transcribe
import TTS
from playsound import playsound

if __name__ == "__main__": 
    # Speech To Text
    speech = transcribe.main()
    fhand = open("C:\\Users\Dell\\Desktop\\sara\\STT\\watson-streaming-stt\\output.txt","w")
    fhand.write(speech)
    fhand.close
    
    # Text To Speech 
    audio = 'C:\\Users\\Dell\\Desktop\\sara\\STT\\watson-streaming-stt\\output.mp3'
    TTS.main(speech,audio)
    playsound(audio)
 