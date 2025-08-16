# YouTube para MP3 Downloader

Um programa simples em Python para baixar vídeos do YouTube e convertê-los para formato MP3.

## 📋 Pré-requisitos

1. **Python 3.7+** instalado
2. **FFmpeg** instalado no sistema
3. **Biblioteca yt-dlp**

## 🚀 Instalação

### 1. Instalar dependências Python
```bash
pip install -r requirements.txt
```

### 2. Instalar FFmpeg

#### Windows:
- Baixe o FFmpeg de: https://ffmpeg.org/download.html
- Extraia os arquivos
- Adicione a pasta `bin` ao PATH do sistema

#### macOS:
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg
```

## 💻 Como usar

1. Execute o programa:
```bash
python mp3.py
```

2. Escolha a opção "1" para baixar um vídeo

3. Cole a URL do vídeo do YouTube

4. O arquivo MP3 será salvo na pasta `downloads/`

## ✨ Funcionalidades

- ✅ Download de vídeos únicos
- ✅ Conversão automática para MP3
- ✅ Qualidade de áudio configurável (192kbps)
- ✅ Interface simples e intuitiva
- ✅ Criação automática da pasta de downloads

## 🔧 Configurações

O programa usa as seguintes configurações padrão:
- Formato de áudio: Melhor qualidade disponível
- Formato de saída: MP3
- Qualidade: 192kbps
- Pasta de destino: `downloads/`

## 📁 Estrutura de arquivos

```
├── mp3.py          # Programa principal
├── requirements.txt # Dependências Python
├── README.md       # Este arquivo
└── downloads/      # Pasta onde os MP3s são salvos
```

## ⚠️ Observações importantes

- Respeite os direitos autorais dos vídeos
- Use apenas para conteúdo que você tem permissão para baixar
- O programa requer conexão com a internet
- Alguns vídeos podem ter restrições de download

## 🐛 Solução de problemas

### Erro: "FFmpeg não encontrado"
- Instale o FFmpeg seguindo as instruções acima
- Verifique se está no PATH do sistema

### Erro: "yt-dlp não instalado"
- Execute: `pip install yt-dlp`

### Download falha
- Verifique se a URL do YouTube é válida
- Teste sua conexão com a internet
- Alguns vídeos podem ter restrições de download
