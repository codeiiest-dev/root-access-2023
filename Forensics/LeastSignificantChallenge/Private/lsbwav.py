import wave

def hide_message_in_audio(audio_file, message):
    with wave.open(audio_file, mode='rb') as wav:
        n_frames = wav.getnframes()
        n_channels = wav.getnchannels()
        sampwidth = wav.getsampwidth()
        framerate = wav.getframerate()
        compname = wav.getcompname()
        comptype = wav.getcomptype()
        frames = bytearray(wav.readframes(n_frames))
        ascii_codes = [ord(char) for char in message]
        binary_text = ''.join([format(code, '08b') for code in ascii_codes])
        for i in range((168), (168) + len(binary_text)):
            frames[i] = (frames[i] & ~1) | int(binary_text[i-(168)])
    with wave.open('leastSignificantChallenge.wav', mode='wb') as wav:
        wav.setnchannels(n_channels)
        wav.setsampwidth(sampwidth)
        wav.setframerate(framerate)
        wav.setcomptype(comptype,compname)
        wav.setparams(wav.getparams())
        wav.writeframes(frames)

def retrieve_message_from_audio(audio_file):
    with wave.open(audio_file, mode='rb') as wav:
        n_frames = wav.getnframes()
        frames = wav.readframes(n_frames)
        message_binary = ''
        for i in range(n_frames * wav.getnchannels()):
            message_binary += str(frames[i] & 1)
        ascii_text = ''
        for i in range(0, len(message_binary), 8):
            ascii_code = int(message_binary[i:i+8], 2)
            ascii_text += chr(ascii_code)
        
        return ascii_text[ascii_text.find("accessdenied"):ascii_text.find("accessdenied")+40]

hide_message_in_audio('theme.wav', 'accessdenied{15b_!s_re@11y_us3fu1}')

message = retrieve_message_from_audio('stego_audio.wav')
print('Retrieved message:', message)
