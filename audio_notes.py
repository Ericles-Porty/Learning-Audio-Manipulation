from audio_effects import add_fade_out
from audio_generator import *
from audio_writer import write_wav_file

# Notas musicais
C = 261.63  # Dó
C_SHARP = D_FLAT = 277.18  # Dó sustenido / Ré bemol
D = 293.66  # Ré
D_SHARP = E_FLAT = 311.13  # Ré sustenido / Mi bemol
E = 329.63  # Mi
F = 349.23  # Fá
F_SHARP = G_FLAT = 369.99  # Fá sustenido / Sol bemol
G = 392.00  # Sol
G_SHARP = A_FLAT = 415.30  # Sol sustenido / Lá bemol
A = 440.00  # Lá
A_SHARP = B_FLAT = 466.16  # Lá sustenido / Si bemol
B = 493.88  # Si
SILENCE = 0

def get_upper_octave(note: float) -> float:
    return note * 2

def get_lower_octave(note: float) -> float:
    return note / 2

# Função para obter a duração de cada nota musical
def get_note_duration(bpm: int = 160) -> dict:
    # Duração de uma batida em segundos
    beat_duration = 60 / bpm
    return {
        "longa": beat_duration * 16,  # 16 tempos
        "breve": beat_duration * 8,  # 8 tempos
        "semibreve": beat_duration * 4,  # 4 tempos
        "mínima": beat_duration * 2,     # 2 tempos
        "semínima": beat_duration * 1,  # 1 tempo
        "colcheia": beat_duration / 2,  # Meio tempo
        "semicolcheia": beat_duration / 4,  # Um quarto de tempo
        "fusa": beat_duration / 8,  # Um oitavo de tempo
        "semifusa": beat_duration / 16  # Um décimo sexto de tempo
    }

# Função para gerar uma nota com duração
def generate_note(frequency: int, duration: int, sample_rate: int = 44100):
    return generate_sine_wave(frequency, duration, sample_rate)

# Função para salvar uma melodia em um arquivo
def save_melody(filename: int, melody: int, sample_rate: int = 44100):
    # Gera as ondas de áudio para todas as notas e as combina
    combined_waves = b"".join([generate_note(note, duration, sample_rate) for note, duration in melody])

    # Adiciona um fade out no final da melodia
    faded_out_waves = add_fade_out(data = combined_waves, fade_out_duration = 4, sample_rate = sample_rate)

    write_wav_file(filename, faded_out_waves, sample_rate)
    print(f"Arquivo WAV gerado: {filename}")


# Melodia de "Parabéns pra você"
def happy_birthday_to_you():
    BPM = 160
    duration = get_note_duration(BPM)

    melody = [
        (get_lower_octave(G), duration["semínima"]), 
        (get_lower_octave(G), duration["semínima"]), 
        (get_lower_octave(A), duration["mínima"]), 
        (get_lower_octave(G), duration["mínima"]),
        (C, duration["mínima"]), 
        (get_lower_octave(B), duration["semibreve"]),

        (get_lower_octave(G), duration["semínima"]), 
        (get_lower_octave(G), duration["semínima"]), 
        (get_lower_octave(A), duration["mínima"]), 
        (get_lower_octave(G), duration["mínima"]),
        (D, duration["mínima"]), 
        (C, duration["semibreve"]), 

        (get_lower_octave(G), duration["semínima"]), 
        (get_lower_octave(G), duration["semínima"]),
        (G, duration["mínima"]), 
        (E, duration["mínima"]),
        (C, duration["mínima"]),
        (get_lower_octave(B), duration["mínima"]),
        (get_lower_octave(A), duration["semibreve"]),

        (F, duration["semínima"]),
        (F, duration["semínima"]),
        (E, duration["mínima"]),
        (C, duration["mínima"]),
        (D, duration["mínima"]),
        (C, duration["breve"])
    ]

    save_melody("happy_birthday_to_you.wav", melody)


happy_birthday_to_you()
