# TTS-STT-python
This python program uses the *IBM watson servecies* to convert from speech to text and from text to speech. 

## The project contains three main files: 
1. **transcirbe.py**
2. **TTS.py**
3. **driver.py**

### Transcribe.py
It is responsible of recording a speech for specified period of seconds and convert it to text using *STT service* from *IBM* 

### TTS.py
Takes a string and convert it to spoken words/sounds using *TTS service* from *IBM* 

### Driver.py
This is the main engin of the code. It combines the two passed files in order to achieve the folloing scenario:
- record an audio using device microphone
- display the final version of the speech recorded on the screen
- convert the speech to text and save it in **output.txt** file
- then convert the text to speech and save it as an audio in **output.mp3** file
- read the converted speech

## How to use 
In order to use this program you will need to install some python packages first.

### Use the client library that is provided by **IBM** for Python.
```
pip install --upgrade "ibm-watson>=5.2.2"
```

### Packages needed for *transcribe.py*
- pyaudio
- websocket-client

installation for any operating system except **Windows** use:
```
pip install pyaudio
pip install websocket-client
```

installation for **Windows** use:
```
pipwin install pyaudio
pipwin install websocket-client
```
### Packages needed for *driver.py* to play the speech as an audio
- playsound

installation for any operating system except **Windows** use:
```
pip install playsound
```

To install for **Windows** use:
```
pipwin install playsound
```

## Run and Excute
Open the file **driver.py** from your terminal using this command
```
python driver.py -t [duration]
```
Note: the duration passed is in seconds

### Run Example
The following command will do recording for 10 seconds then will convert what it recorded to text and read it loudly as spoken words. 
```
python driver.py -t 10
```

