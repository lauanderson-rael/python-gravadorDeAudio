import pyaudio
import wave
import threading

class Recorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.recording = False
        self.stream = None
        self.frames = []

    def start_recording(self):
        self.recording = True

        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=44100,
                                      input=True,
                                      frames_per_buffer=1024)
        self.frames = []
        threading.Thread(target=self._record).start()
        
    def _record(self):
        while self.recording:
            data = self.stream.read(1024)
            self.frames.append(data)

    def stop_recording(self):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()

    def save_recording(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()

# Aqui é Exemplo de uso:
recorder = Recorder()

recorder.start_recording() # Iniciar gravação

input("Pressione Enter para parar a gravação...") # Aguardar alguns segundos...

recorder.stop_recording() # Parar gravação

# Salvar gravação
filename = "output.wav"
recorder.save_recording(filename)
print(f"Gravação salva em {filename}")
