<h1> Gravador de audio em python</h1>
<h2> Bibliotecas utilizadas</h2>
<li> threading </li>
<li> pyaudio </li>

<h2> Sobre execução</h2>
<p>
As threads estão executando simultaneamente durante o período em que a gravação está ocorrendo. Quando você chama recorder.start_recording(), uma nova thread é iniciada para executar a função _record. Enquanto a gravação estiver ativa (self.recording == True), esta thread estará executando o loop de gravação em paralelo com a thread principal do programa.

Enquanto isso, a thread principal pode continuar executando outras tarefas, como aguardar a entrada do usuário através de input("Pressione Enter para parar a gravação...").

Portanto, durante o período em que a gravação está ativa e a espera pelo input do usuário está ocorrendo, as duas threads estão executando em paralelo, permitindo que a gravação continue enquanto o programa aguarda a entrada do usuário.
</p>