import math

# A onda senoidal é a forma de onda mais simples e pura, e é definida pela função sin(x).
def generate_sine_wave(frequency: int, duration: int, sample_rate: int = 44100) -> bytearray:
    samples = int(sample_rate * duration)
    data = bytearray()
    for i in range(samples):
        amplitude = int(127 * math.sin(2 * math.pi * frequency * i / sample_rate)) 
        data.append(amplitude & 0xFF) # Dar um AND com 0xFF para obter somente os 8 bits menos significativos
    return data

# A característica da onda quadrada é que ela possui um ciclo de trabalho de 50%, ou seja, a metade do tempo o sinal é alto e a outra metade é baixo.
def generate_square_wave(frequency: int, duration: int, sample_rate: int = 44100) -> bytearray:
    samples = int(sample_rate * duration)
    data = bytearray()
    for i in range(samples):
        amplitude = int(127 * math.sin(2 * math.pi * frequency * i / sample_rate))
        if amplitude > 0:
            data.append(127)
        else:
            data.append(-127)
    return data

# A onda triangular é uma onda que varia linearmente entre -1 e 1, e é definida pela função abs(sin(x)).
def generate_triangle_wave(frequency: int, duration: int, sample_rate: int = 44100) -> bytearray:
    samples = int(sample_rate * duration)
    data = bytearray()
    for i in range(samples):
        amplitude = int(127 * (2 / math.pi) * math.asin(math.sin(2 * math.pi * frequency * i / sample_rate)))
        data.append(amplitude & 0xFF)
    return data

# A onda dente de serra é uma onda que varia linearmente entre -1 e 1, e é definida pela função sin(x).
def generate_sawtooth_wave(frequency: int, duration: int, sample_rate: int = 44100) -> bytearray:
    samples = int(sample_rate * duration)
    data = bytearray()
    for i in range(samples):
        amplitude = int(127 * (2 / math.pi) * (math.pi / 2 - math.asin(math.sin(2 * math.pi * frequency * i / sample_rate))))
        data.append(amplitude & 0xFF)
    return data