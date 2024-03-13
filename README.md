````markdown
# Bot Discord de Comandos

Este é um bot Discord desenvolvido em Python usando a biblioteca discord.py. O bot oferece vários comandos úteis para interação em um servidor do Discord.

## Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes Python)

## Instalação

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd seuprojeto
   ```

3. **Instale as dependências necessárias:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuração da variável de ambiente PATH

Para acessar o FFmpeg de qualquer lugar em seu sistema, é uma prática comum adicionar o diretório contendo o executável do FFmpeg ao caminho (PATH) do sistema. Isso permite que você execute o FFmpeg a partir de qualquer diretório sem precisar especificar o caminho completo para o executável.

1. **Localize o diretório do executável do FFmpeg**: Dependendo de como o FFmpeg foi instalado em seu sistema, o diretório do executável pode variar. Você pode encontrar o diretório executável usando o comando `which ffmpeg` no terminal.

2. **Adicione o diretório ao PATH do sistema**: Após identificar o diretório do executável do FFmpeg, você pode adicionar esse diretório ao PATH do sistema. Por exemplo, se o FFmpeg estiver instalado em `/usr/bin/ffmpeg`, você pode adicionar a seguinte linha ao seu arquivo `.bashrc` ou `.bash_profile`:

   ```bash
   export PATH=$PATH:/usr/bin
   ```

   Certifique-se de substituir `/usr/bin` pelo diretório real do executável do FFmpeg em seu sistema.

3. **Recarregue o arquivo de configuração do shell**: Depois de adicionar a linha ao seu arquivo de configuração do shell, recarregue o arquivo executando:

   ```bash
   source ~/.bashrc
   ```

   Isso garantirá que as alterações no PATH sejam aplicadas imediatamente.

4. **Verifique a configuração**: Para verificar se a configuração foi aplicada corretamente, você pode executar o seguinte comando no terminal:

   ```bash
   ffmpeg -version
   ```

   Isso deverá exibir a versão do FFmpeg instalada em seu sistema. Se você ver a versão do FFmpeg, significa que está instalado e configurado corretamente.

Certifique-se de realizar esses passos para garantir que o FFmpeg esteja configurado corretamente em seu sistema e acessível para uso em seu projeto.
``` 

Lembre-se de substituir `/usr/bin` pelo diretório real do executável do FFmpeg em seu sistema.

## Configuração

1. **Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:**

   ```plaintext
   ACESS_TOKEN=seu_token_do_discord
   PERSONAL_ID=seu_id_pessoal
   ```

   Substitua `seu_token_do_discord` pelo token do seu bot Discord e `seu_id_pessoal` pelo seu ID de usuário do Discord.

## Uso

1. **Inicie o bot executando o seguinte comando:**

   ```bash
   python bot.py
   ```

2. **O bot estará online e pronto para receber comandos no servidor do Discord.**

## Comandos Disponíveis

- **/comandos**: Mostra uma lista de todos os comandos disponíveis.
- **/traduzir texto**: Traduz o texto fornecido para o inglês ou português, dependendo do idioma detectado.
- **/perfil @usuário**: Mostra a foto de perfil do usuário mencionado.
- **/banir @usuário**: Bane o usuário mencionado do servidor.
- **/play link_do_youtube**: Toca o áudio do vídeo do YouTube no canal de voz do usuário.
- **/pause**: Pausa a reprodução de áudio atual.
- **/resume**: Continua a reprodução de áudio pausada.
- **/stop**: Para a reprodução de áudio e desconecta o bot do canal de voz.

## Contribuindo

Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma [issue] ou enviar uma [pull request]

