import argparse
import scipy.signal as signal
import numpy as np
import wave

# ... [Rest of your functions like read_wave_file, stft, etc.]
def load_wav(fpath):
    """Loads a .wav file and returns the data and sample rate.

    :param fpath: the path to load the file from
    :returns: a tuple of (wav file data as a list of amplitudes, sample rate)
    """
    with wave.open(fpath) as wav_f:
        wav_buf = wav_f.readframes(wav_f.getnframes())
        data = np.frombuffer(wav_buf, dtype=np.int16)
        fs = wav_f.getframerate()

        clip_len_s = len(data) / fs
        print(f"Loaded .wav file, n_samples={len(data)} len_s={clip_len_s}")

        return (data, fs)

def main():
    parser = argparse.ArgumentParser(description='Process an audio file with STFT.')
    parser.add_argument('-p', '--path', type=str, help='Path to the audio file', required=True)

    args = parser.parse_args()
    input_file = args.path

    # Process the file
    frequencies, times, stft_matrix = process_stft(input_file)
    # You can now use 'frequencies', 'times', and 'stft_matrix' for further analysis
    print(f"Processed {input_file} with STFT.")

if __name__ == "__main__":
    main()
