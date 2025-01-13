import math


def add_echo(data, sample_rate, delay, attenuation):
    delay_samples = int(sample_rate * delay)
    echo_data = bytearray(len(data) + delay_samples)
    
    # Copiar o som original
    for i in range(len(data)):
        echo_data[i] = data[i]
    
    # Adicionar eco
    for i in range(len(data)):
        if i + delay_samples < len(echo_data):
            # Adicionar o som atenuado, garantindo que o valor esteja no intervalo [0, 255]
            original_value = echo_data[i + delay_samples]
            attenuated_value = int(data[i] * attenuation)
            echo_data[i + delay_samples] = min(255, max(0, original_value + attenuated_value))

    return echo_data

def add_reverb(data, sample_rate, delay, attenuation):
    delay_samples = int(sample_rate * delay)
    reverb_data = bytearray(len(data) + delay_samples)
    
    # Copiar o som original
    for i in range(len(data)):
        reverb_data[i] = data[i]
    
    # Adicionar reverb
    for i in range(len(data)):
        if i + delay_samples < len(reverb_data):
            # Adicionar o som atenuado, garantindo que o valor esteja no intervalo [0, 255]
            original_value = reverb_data[i + delay_samples]
            attenuated_value = int(data[i] * attenuation)
            reverb_data[i + delay_samples] = min(255, max(0, original_value + attenuated_value))

    return reverb_data

def add_distortion(data, gain):
    distorted_data = bytearray(len(data))
    
    for i in range(len(data)):
        # Amplificar o som, garantindo que o valor esteja no intervalo [0, 255]
        distorted_value = int(data[i] * gain)
        distorted_data[i] = min(255, max(0, distorted_value))

    return distorted_data

def add_tremolo(data, sample_rate, frequency, depth):
    tremolo_data = bytearray(len(data))
    
    for i in range(len(data)):
        # Modulação senoidal
        tremolo_value = int(data[i] * (1 + depth * math.sin(2 * math.pi * frequency * i / sample_rate)))
        tremolo_data[i] = min(255, max(0, tremolo_value))

    return tremolo_data

# fade_out_last_seconds: duração do fade out em segundos
def add_fade_out(data: bytearray, fade_out_duration: int, sample_rate: int) -> bytearray:
    fade_out_samples = int(sample_rate * fade_out_duration)
    faded_data = bytearray(len(data))

    for i in range(len(data)):
        if i >= len(data) - fade_out_samples:
            # Aplicar fade out
            faded_data[i] = int(data[i] * (1 - (i - (len(data) - fade_out_samples)) / fade_out_samples))
        else:
            faded_data[i] = data[i]

    return faded_data