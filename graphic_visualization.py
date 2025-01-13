import matplotlib.pyplot as plt
import wave
import numpy as np

def plot_audio_waveform(file_path):
    # Abrir o arquivo WAV
    with wave.open(file_path, 'rb') as wav_file:
        # Informações básicas
        sample_rate = wav_file.getframerate()
        n_samples = wav_file.getnframes()
        n_channels = wav_file.getnchannels()
        print (sample_rate, n_samples, n_channels)

        # Ler os dados do arquivo WAV
        raw_data = wav_file.readframes(n_samples)
        audio_data = np.frombuffer(raw_data, dtype=np.uint8)  # Para áudio de 8 bits
        time = np.linspace(0, n_samples / sample_rate, num=n_samples)

        # Se for estéreo, separar os canais
        if n_channels > 1:
            audio_data = audio_data.reshape(-1, n_channels)

        # Plotar o gráfico
        plt.figure(figsize=(10, 4))
        if n_channels == 1:
            plt.plot(time, audio_data, label="Canal único")
        else:
            plt.plot(time, audio_data[:, 0], label="Canal esquerdo")
            plt.plot(time, audio_data[:, 1], label="Canal direito")

        plt.title("Forma de Onda do Áudio")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.tight_layout()
        plt.show()

# Exemplo de uso
plot_audio_waveform("happy_birthday_to_you.wav")
