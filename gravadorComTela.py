import pyaudio
import wave
import threading
import tkinter as tk 

def iniciar_gravacao():
    global gravando
    gravando = True
    botao_iniciar.config(state=tk.DISABLED)
    botao_parar.config(state=tk.NORMAL)
    msg_gravacao_iniciada.config(text="Gravando...") # mensagem inicial

    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)
    
    threading.Thread(target=_gravar, args=(stream,)).start()

def parar_gravacao():
    global gravando
    gravando = False
    nome_arquivo = "audio_capturado.wav"
    wf = wave.open(nome_arquivo, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

    botao_iniciar.config(state=tk.NORMAL)
    botao_parar.config(state=tk.DISABLED)
    msg_gravacao_finalizada.config(text="Gravação concluída com sucesso!")  # mensagem final
    

def _gravar(stream):
    global gravando
    while gravando:
        dados = stream.read(1024)
        frames.append(dados)

gravando = False
frames = []
audio = pyaudio.PyAudio()

janela = tk.Tk() #tela
janela.title("GRAVADOR DE ÁUDIO - PYTHON")
janela.geometry("400x250")

botao_iniciar = tk.Button(janela, text="INICIAR GRAVAÇÃO", command=iniciar_gravacao)
botao_iniciar.pack()
msg_gravacao_iniciada = tk.Label(janela, text="" , padx=10, pady=10)
msg_gravacao_iniciada.pack()

botao_parar = tk.Button(janela, text="PARAR E SALVAR GRAVAÇÃO", command=parar_gravacao, state=tk.DISABLED)
botao_parar.pack()
msg_gravacao_finalizada = tk.Label(janela, text="" , padx=10, pady=10)
msg_gravacao_finalizada.pack()

janela.mainloop()
