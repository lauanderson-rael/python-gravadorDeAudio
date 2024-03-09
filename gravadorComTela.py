import pyaudio
import wave
import threading
import tkinter as tk

def start_recording():
    global recording
    recording = True
    botao_iniciar.config(state=tk.DISABLED)
    botao_parar.config(state=tk.NORMAL)
    msg_gravacao_iniciada.config(text="Gravando...")

    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)
    
    threading.Thread(target=_record, args=(stream,)).start()

def stop_recording():
    global recording
    recording = False
    filename = "audio_capturado.wav"
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

    botao_iniciar.config(state=tk.NORMAL)
    botao_parar.config(state=tk.DISABLED)
    msg_gravacao_iniciada.config(text="")
    msg_gravacao_finalizada.config(text="Gravação concluída com sucesso!")  # Define o texto como "Gravação concluída" após parar a gravação
    

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
janela.title("GRAVADOR DE ÁUDIO - PYTHON")
janela.geometry("400x250")  # Definindo o tamanho da janela

botao_iniciar = tk.Button(janela, text="INICIAR GRAVAÇÃO", command=start_recording)
botao_iniciar.pack()
msg_gravacao_iniciada = tk.Label(janela, text="" , padx=10, pady=10)
msg_gravacao_iniciada.pack()

botao_parar = tk.Button(janela, text="PARAR E SALVAR GRAVAÇÃO", command=stop_recording, state=tk.DISABLED)
botao_parar.pack()
msg_gravacao_finalizada = tk.Label(janela, text="" , padx=10, pady=10)
msg_gravacao_finalizada.pack()

janela.mainloop()
