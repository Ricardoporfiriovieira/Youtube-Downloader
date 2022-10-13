# Youtube Downloader Documentação

Esse é um projeto que tem como Objetivo Baixar arquivos Mp3 e Mp4 no seu computador.

# Guia de Instalação

* **Primeiro Utilize o comando:**

    ```

        git clone https://github.com/Ricardoporfiriovieira/Youtube-Downloader

    ```
  * para baixar todos os arquivos necessários, após isso baixe todas as dependências do projeto.

<hr>

* **Baixando as dependências do projeto**
  
  * Todas as dependências do Projeto estão listadas em um arquivo chamado **requirements.txt** Utilize o comando:
  
    ```

      pip install -r requirements.txt 

    ```
  
  * para baixar todas as dependências.

  * Esse comando serve principalmente para adicionar as bibliotecas Pysimplegui e Pytube ao seu computador.

<hr>

* # Como Usar a Aplicação:

  * Após completar todos os passos anteriores com sucesso Você precisa apenas ir no terminal e digitar o comando:

    ```
      python baixar.py
    ```

  * esse comando irá abrir a interface do programa que irá solicitar a **URL** de um vídeo do youtube.

  * <p align="center">
    <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_1.png" alt="imagem demonstrativa 1">
    </p>

  * após inserir a url do vídeo desejado, a interface irá mostrar 2 checkbox Com as opções **MP3** e **MP4** Escolha em qual formato você deseja baixar a mídia em questão e clique no botão **Download**.

  * <p align="center">
      <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_4.png" alt="imagem demonstrativa 3">
    </p>

  * A mídia em questão Será baixada na mesma pasta Onde o Arquivo **baixar.py** se encontra.




# Sobre o projeto
<p>
  Para começar, eu utilizei 2 bibliotecas principais o pytube, que será responsável por o que acontece no backend e o pysimplegui que é responsável pelo front end.
</p>
<p>
  O pysimplegui poderia ter sido substituído pelo tkinter que é uma biblioteca de interface gráfica muito mais completa, porém como o próprio nome já diz o pysimplegui é bem simples além do fato da sua documentação ser ótima o que é um ponto muito importante pra mim que estou aprendendo a usar a biblioteca enquanto desenvolvo esse projeto.
</p>
<p align="center">
 <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/PySimpleGUI_logo.png" alt="pysimplegui icone"> 
 <img src="https://warehouse-camo.ingress.cmh1.psfhosted.org/42d43def1c8634a6c158def4846894bc2afd542b/68747470733a2f2f6173736574732e6e69636b666963616e6f2e636f6d2f67682d7079747562652e6d696e2e737667" alt="pytube icone">
</p> <br>

 <p>
Primeiro construi a interface gráfica utilizando o pysimplegui, essa biblioteca é bem intuitiva e o princípio é bem simples, basicamente para cada janela que você deseja utilizar será criada uma função, dentro dessa função será criada uma lista com todos os elementos contidos na janela, na linha 9 adicionei um texto para guiar o usuário, na linha 10 adicionei uma área para o usuário adicionar uma informação e nessa área eu defini uma "key" uma espécie de apelido para mais tarde conseguir referenciar esse input com mais facilidade, na linha 11 eu defini 2 botões.
</p> 
<p align="center">
  <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_1.png" alt="imagem demonstrativa 1">
</p>

<p>
  dentro dessa primeira janela, é possível observar pelo menos 2 tipos de dados recebidos segundo a biblioteca do pysimplegui, o primeiro tipo são os "values" são dados que a janela recebe pela área de input, e o segundo tipo são os "events", nesse caso os botões:  "Continuar", "Sair" e o botão de fechar a janela que o próprio pysimplegui já cria automaticamente nomeado de "WINDOWS_CLOSED" que fica localizado no canto superior direito da tela.
</p>

<p align="center">
  <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_3.png" alt="imagem demonstrativa 2">
</p>
<p>
  após tudo isso eu usei o recurso "Window" , na linha 7 eu adicionei o recurso "theme" para poder mudar a cor tema da janela pois acho o tema escuro mais agradável aos olhos.
</p>
<p>
  Na função "janela2" o processo se repete mas com duas diferenças a primeira é a adição de um objeto de texto na linha 19 a função desse texto é a de mostrar o título do vídeo que será baixado, isso será feito através do método ".title" que acontece na linha 39 e para conseguir mudar o conteúdo desse texto eu utilizei o método ".upgrade" além disso eu também adicionei 2 checkbox eles são considerados como eventos pelo pysimplegui e retornam os valores "True" para quando está marcado e "False" para quando está desmarcado eles serão utilizados pelo programa para identificar se o usuário deseja instalar apenas o mp3, apenas o mp4 ou se ele deseja fazer o download dos 2.
</p>

<p align="center">
  <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_4.png" alt="imagem demonstrativa 3">
   <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_5.png" alt="imagem demonstrativa 4">
</p>

<p>
Então na linha 27 do programa será invocado a função "janela1" para poder dar início ao programa, e logo após será gerado um looping indeterminado, sem esse looping as janelas seriam fechadas após qualquer interação do usuário com o programa, na linha 30 eu vou ler todos os dados que as janelas receberam e vou alocar nas variáveis "window" essa variável vai receber jn1 ou jn2 ela será necessária para saber de onde aquele dado veio, na variável "event" serão alocados os valores recebidos por botões e checkbox e o values receberá o valor do input após isso eu sempre irei verificar se o usuário clicou em algum botão para sair do programa caso isso seja falso o programa vai verificar se window é igual a jn1 aqui eu estou verificando se a última interação do usuário aconteceu na primeira janela e após isso eu vou verificar se o botão "Continuar" foi clicado, caso essas premissas sejam verdadeiras eu vou guardar o valor do input em uma variável vou invocar a função janela2 abrindo assim a minha segunda janela e vou fechar a primeira janela com o método ".hide()" após isso eu vi após isso vou alterar o valor do objeto de texto já mencionado anteriormente a linha 40 é dedicada ao botão voltar, basicamente se o usuário clicar nesse botão eu irei invocar a primeira janela e fechar a segunda mas caso isso não aconteça nós iremos para na linha 43 do nosso código, aqui é onde a mágica realmente acontece, primeiro nós iremos verificar se o usuário clicou no botão "Download" se ele clicou então nós iremos verificar os checkboxes começando primeiro pelo "mp4" se esse primeiro checkbox estiver marcado então eu irei pegar a variável link que guarda a minha url e irei jogar isso dentro do objeto "YouTube" e colocarei tudo isso dentro da var youtube seguindo assim as recomendações da bilbioteca do pytube,após isso vou utilizar o método ".streams.get_highest_resolution()"
</p>

<p align="center">
  <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_6.png" alt="imagem demonstrativa 5">
</p>

<p>
  Onde o programa irá escolher a resolução do vídeo que ele irá pegar "360", "480", "720" e por aí vai, após isso eu vou utilizar o método ".download" para realmente baixar o vídeo após isso na linha 49 eu renomeio o arquivo para não acabar tendo problemas com a instalação de um arquivo duplicado e nas linhas 51, 52 e 53 eu crio uma pequena barra de progresso para poder dar um feedback visual para o usuário de que o primeiro download foi executado.
</p>

<p align="center">
  <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_7.png" alt="imagem demonstrativa 6">
  <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_9.png" alt="imagem demonstrativa 7">
</p>

<p>
  Na linha 55 o processo se repete mas com a diferença de que na linha 57 eu uso a especificação "only_audio=true" com essa especificação eu faço o download de um arquivo em mp4, porém esse mp4 não terá nada além de uma imagem preta e o áudio, por isso que na linha 62 eu faço a renomeação do arquivo, eu tiro a extensão ".mp4" e adiciono a extensão "mp3" após isso nas linhas 63, 64 e 65 eu mostro outra barra de progresso para mostrar ao usuário que o download foi executado com sucesso, após tudo isso o programa irá colocar os arquivos baixados na mesma pasta onde o programa está localizado.
</p>

<p align="center">
  <img src="https://github.com/Ricardoporfiriovieira/imagens-youtubedownloader/blob/main/print_8.png" alt="imagem demonstrativa ">
</p>

# Conclusões:
Com esse projeto eu consegui a minha primeira experiência com interfaces gráficas e ao concluir uma aplicação onde eu trabalhei tanto com o frontend quanto com o backend eu sinto que estou um passo mais próximo de me tornar um bom desenvolvedor full stack, eu pretendo adicionar algumas funções a mais nesse projeto como por exemplo a opção de baixar mp3 e mp4 por play list dessa forma o usuário conseguiria baixar vários arquivos do youtube com o mínimo de esforço, além disso eu pretendo criar uma versao mobile dessa aplicação mas eu gostaria de desenvolver essa versão em kotlin, eu criei essa plicação com o objetivo de me desenvolver na programação e o de conseguir criar uma ferramenta útil para as pessoas, o meu maior desejo  desenvolver coisas que façam a diferença na sociedade, por isso caso alguém tenha alguma sugestão de mudança eu ficaria feliz em escutar eu quero poder melhorar cada vez mais.
