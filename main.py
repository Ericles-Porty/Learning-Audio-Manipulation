from audio_generator import generate_sine_wave, generate_variable_frequency_sine_wave
from audio_effects import add_echo
from audio_writer import write_wav_file

# Configuração
frequency = 440.0  # Frequência em Hz
sample_rate = 44100  # Taxa de amostragem
duration = 2  # Duração em segundos

# Gerar onda senoidal
sine_wave = generate_sine_wave(frequency, sample_rate, duration)

# Aplicar efeito de eco
sine_wave_with_echo = add_echo(sine_wave, sample_rate, delay=0.5, attenuation=0.5)

# Gerar onda senoidal variável

variable_sine_wave = generate_variable_frequency_sine_wave([440.0, 880.0], sample_rate, duration)

# Escrever arquivos de áudio
write_wav_file("sine_wave.wav", sine_wave, sample_rate)
write_wav_file("sine_wave_with_echo.wav", sine_wave_with_echo, sample_rate)
write_wav_file("variable_sine_wave.wav", variable_sine_wave, sample_rate)

print("Arquivos WAV gerados:")
print("1. Onda Senoidal: sine_wave.wav")
print("2. Onda Senoidal com Eco: sine_wave_with_echo.wav")
print("3. Onda Senoidal Variável: variable_sine_wave.wav")
