<h1>Gravador de audio em python com Interface Gráfica</h1>
<h2> Bibliotecas utilizadas</h2>
<li> threading </li>
<li> pyaudio </li>
<h2> Sobre execução</h2>
<h3>Nesse código, duas threads são executadas</h3>
<p>
A primeira thread é a thread principal do programa, que é responsável por executar o loop principal do Tkinter (janela.mainloop()). Essa thread lida com a interface gráfica do usuário e responde às interações do usuário, como clicar nos botões "INICIAR GRAVAÇÃO" e "PARAR E SALVAR GRAVAÇÃO".

A segunda thread é criada quando a função iniciar_gravacao() é chamada. Dentro desta função, uma nova thread é iniciada com a chamada threading.Thread(target=_gravar, args=(stream,)).start(). Esta nova thread executa a função _gravar(stream), que captura continuamente os dados de áudio enquanto a gravação está em andamento.

Portanto, durante a gravação, há duas threads em execução: a thread principal do Tkinter e a thread que executa a função _gravar(stream) para capturar os dados de áudio em tempo real.

</p>


<h3>Como é iniciada a nova thread? </h3>
<p>
  threading.Thread: Esta é uma classe da biblioteca threading em Python que permite criar e manipular threads. Ao instanciar um objeto Thread, estamos preparando uma nova thread para executar uma determinada função.

start(): Este é um método que inicia a execução da thread. Uma vez que uma thread é criada com os detalhes especificados (alvo e argumentos), chamamos start() para iniciar a execução dessa thread. Quando este método é chamado, a função _gravar começará a ser executada em paralelo com a thread principal.

Resumindo, essa linha de código cria uma nova thread que executa a função _gravar(stream) com o argumento stream, permitindo que a gravação de áudio ocorra em paralelo com outras operações do programa.
</p>
