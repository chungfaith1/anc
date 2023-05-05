import anc.simpleaudio as sa
import numpy as np

if __name__ == "__main__":
    wav_file = "/Users/faith/Desktop/Projects/anc/anc/data/radiator.wav"
    #sa.play_wav(wav_file=wav_file)

    '''
    frequency = 100  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    audio = np.sin(frequency * t * 2 * np.pi)#+np.sin(frequency * t * 9 * np.pi)
    sa.play_np(audio=audio, num_channels=1, bytes_per_sample=2, sample_rate=fs)
    '''

    wav_file = "/Users/faith/Desktop/Projects/anc/anc/data/radiator.wav"
    data = sa.to_numpy(wav_file=wav_file)
    sa.play_np(audio = data[:,0], num_channels=1, bytes_per_sample=2, sample_rate=44100)
    sa.play_np(audio = data[:,1], num_channels=1, bytes_per_sample=2, sample_rate=44100)    
    sa.play_wav(wav_file=wav_file)

    