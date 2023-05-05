import numpy as np
import simpleaudio as sa
import wave


def to_numpy(wav_file:str) -> np.ndarray:
    '''
    nchannels = num channels
    sampwidth = num bytes per sample (one sample per channel)
    framerate = how many frames (or samples) per second. One frame for all channels
    nframes = number frames in sound signal

    sample       sample              sample
    frame 0      frame 1             frame N
    _____ _____ _____ _____         _____ _____
    | ch1 | ch2 | ch1 | ch2 | . . . | ch1 | ch2 |
    |_____|_____|_____|_____|       |_____|_____|
     _____
    |     | = one sample point
    |_____|

    https://stackoverflow.com/questions/20677390/python-wave-byte-data
    '''    
    wr = wave.open(wav_file,'rb')
    nchannels, sampwidth, framerate, nframes, comptype, compname =  wr.getparams()
    frames = wr.readframes(nframes-1) #(nframes-1)
    audio = np.zeros(((nframes-1),nchannels))
    for frame_idx in range(nframes-1):
        start_idx = frame_idx*(nchannels*sampwidth)
        end_idx = (frame_idx+1)*(nchannels*sampwidth)
        frame_data = frames[start_idx:end_idx]
        for channel in range(nchannels):
            channel_start_idx = channel*sampwidth
            channel_end_idx = (channel+1)*sampwidth
            channel_data = frame_data[channel_start_idx:channel_end_idx]
            audio[frame_idx][channel] = int.from_bytes(channel_data, byteorder='little', signed=True)          
    return audio

def play_wav(wav_file:str) -> None:
    wave_obj = sa.WaveObject.from_wave_file(wav_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def play_np(audio:np.ndarray, num_channels:int, bytes_per_sample:int, sample_rate:int) -> None:
    audio = audio * (2**15 - 1) / np.max(np.abs(audio))
    audio = audio.astype(np.int16) # Convert to 16-bit data
    play_obj = sa.play_buffer(audio, num_channels, bytes_per_sample, sample_rate)
    play_obj.wait_done()    
