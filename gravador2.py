import pyaudio
import wave
import threading

class Recorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.recording = False
        self.frames = []

    def _record(self, stream):
        while self.recording:
            data = stream.read(1024)
            self.frames.append(data)

    def start_recording(self):
        
        self.recording = True

        stream = self.audio.open(format=pyaudio.paInt16,
                                 channels=1,
                                 rate=44100,
                                 input=True,
                                 frames_per_buffer=1024)
        
        threading.Thread(target=self._record, args=(stream,)).start()

    def stop_recording(self):
        self.recording = False

    def save_recording(self, filename):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))

# Exemplo de uso:
recorder = Recorder()

recorder.start_recording()
input("Pressione Enter para parar a gravação...") 
recorder.stop_recording()

filename = "gravacao_finalizada.wav"
recorder.save_recording(filename)
print(f"Gravação salva em {filename}")
