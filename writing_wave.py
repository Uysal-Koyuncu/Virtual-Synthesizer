import wave, random, struct, math

sampleRate = 44100.0 # Hertz
duration = 1.0 # Seconds
frequency = 440.0 # Hertz
freq_C = 261.0 # Hertz

write_wave = wave.open("Twisted Center C.wav", "w")
write_wave.setnchannels(1)
write_wave.setsampwidth(2)
write_wave.setframerate(sampleRate)
for i in range(44100 * 10):
    value = int(math.sin(i * 261 * 2 * math.pi / 44100) * math.sin(i * 0.1 * 2 * math.pi / 44100) * 20000)
        # First freq., second sine is amplitude control
    data = struct.pack("<h", value)
    write_wave.writeframesraw(data)
write_wave.close()