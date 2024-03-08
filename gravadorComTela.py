import pyaudio
import wave
import threading
import tkinter as tk

def start_recording():
    global recording
    recording = True
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    iniciando.config(text="Gravação iniciada...!")

    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)
    
    threading.Thread(target=_record, args=(stream,)).start()

def stop_recording():
    global recording
    recording = False
    filename = "output.wav"
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    iniciando.config(text="")
    confirmacao.config(text="Gravação concluída com sucesso!")  # Define o texto como "Gravação concluída" após parar a gravação
    

def _record(stream):
    global recording
    while recording:
        data = stream.read(1024)
        frames.append(data)

recording = False
frames = []
audio = pyaudio.PyAudio()


# Tela
janela = tk.Tk()
janela.title("GRAVADOR DE ÁUDIO")
janela.geometry("400x250")  # Definindo o tamanho da janela

start_button = tk.Button(janela, text="INICIAR GRAVAÇÃO", command=start_recording)
start_button.pack()
iniciando = tk.Label(janela, text="" , padx=10, pady=10)
iniciando.pack()

stop_button = tk.Button(janela, text="PARAR E SALVAR GRAVAÇÃO", command=stop_recording, state=tk.DISABLED)
stop_button.pack()

confirmacao = tk.Label(janela, text="" , padx=10, pady=10)
confirmacao.pack()

janela.mainloop()
