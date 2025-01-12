import struct

"""
    RIFF (Resource Interchange File Format) é um formato de arquivo de áudio digital padrão para arquivos de áudio não compactados.
    Cada arquivo WAV é composto por um cabeçalho RIFF seguido por dois sub-chunks: "fmt " e "data".
    O sub-chunk "fmt " contém informações sobre o formato do áudio, como taxa de amostragem, número de canais, etc.
    O sub-chunk "data" contém os dados do áudio.
    Exemplo de cabeçalho RIFF:
    - RIFF: 4 bytes 
    - Tamanho do arquivo: 4 bytes (36 + tamanho dos dados)
    - WAVE: 4 bytes 
    Exemplo de sub-chunk "fmt ":
    - fmt : 4 bytes
    - Tamanho do subchunk: 4 bytes (16 para PCM) PCM = Pulse Code Modulation
    - Formato do áudio: 2 bytes (1 = PCM, 3 = IEEE float)
    - Número de canais: 2 bytes (1 = Mono, 2 = Stereo)
    - Taxa de amostragem: 4 bytes (Hz)
    - Byte rate: 4 bytes (taxa de amostragem * canais * bits/8) 
    - Alinhamento de blocos: 2 bytes (canais * bits/8)
    - Bits por amostra: 2 bytes (8, 16, 24, 32)
    Exemplo de sub-chunk "data":
    - data: 4 bytes
    - Tamanho dos dados: 4 bytes (n bytes)
    - Dados do áudio: n bytes (amostras)
    Referência: https://en.wikipedia.org/wiki/WAV
"""
def write_wav_file(filename, data, sample_rate):
    with open(filename, 'wb') as f:
        # Cabeçalho RIFF
        f.write(b'RIFF')
        f.write(struct.pack('<I', 36 + len(data)))  # Tamanho do arquivo
        f.write(b'WAVE')

        # Subchunk "fmt "
        f.write(b'fmt ')
        f.write(struct.pack('<I', 16))  # Tamanho do subchunk
        f.write(struct.pack('<H', 1))  # Formato do áudio (1 = PCM)
        f.write(struct.pack('<H', 1))  # Número de canais (1 = Mono)
        f.write(struct.pack('<I', sample_rate))  # Taxa de amostragem
        f.write(struct.pack('<I', sample_rate * 1))  # Byte rate (sample_rate * canais * bits/8)
        f.write(struct.pack('<H', 1))  # Alinhamento de blocos (canais * bits/8)
        f.write(struct.pack('<H', 8))  # Bits por amostra

        # Subchunk "data"
        f.write(b'data')
        f.write(struct.pack('<I', len(data)))  # Tamanho dos dados
        f.write(data)  # Dados do áudio
