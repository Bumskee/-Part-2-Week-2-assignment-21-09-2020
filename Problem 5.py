"""Problem 5 calculating the wavelength from a data of speed and frequency"""

#A function that assigns values to waveVelocity and waveFrequency respectively and then printing the values of speed, frequency, and wavelength
def FindWaveLength(wave_velocity, wave_frequency):
    global waveLength, waveVelocity, waveFrequency
    waveVelocity = wave_velocity
    waveFrequency = wave_frequency
    waveLength = wave_velocity / wave_frequency
    print("Speed =", str(waveVelocity), "m/s")
    print("Frequency =", str(waveFrequency), "Hz")
    print("wave Length =", str(waveLength), "m")

#Calls the function
FindWaveLength(343, 256)