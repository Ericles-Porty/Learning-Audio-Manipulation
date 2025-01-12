import math

def generate_sine_wave(frequency, sample_rate, duration):
    samples = int(sample_rate * duration)
    data = bytearray()
    for i in range(samples):
        amplitude = int(127 * math.sin(2 * math.pi * frequency * i / sample_rate))
        data.append(amplitude & 0xFF)  # Cada amostra é um byte
    return data

def generate_variable_frequency_sine_wave(frequencies, sample_rate, duration):
    samples = int(sample_rate * duration)
    data = bytearray()
    for i in range(samples):
        amplitude = 0
        for frequency in frequencies:
            amplitude += int(127 * math.sin(2 * math.pi * frequency * i / sample_rate))
        data.append(amplitude & 0xFF)  # Cada amostra é um byte
    return data
