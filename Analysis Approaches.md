Extracting Electric Network Frequency (ENF) features from audio recordings involves a series of steps to transition from the raw sound to a time series of frequency measurements. This process is integral to ENF analysis in audio forensics. Here's a breakdown of the process and the necessary vocabulary:
## 1 - Preprocessing
Preprocessing of sound data, especially in the context of audio analysis or forensics like Electric Network Frequency (ENF) analysis, involves several key steps to prepare the raw audio data for effective analysis. These steps are essential for enhancing the quality of the data and ensuring the accuracy of subsequent analyses. Here's an overview of common preprocessing steps:

**Metadata / Exif Data**
first, as much information as possible should be squeezed out of the file. 
- framerate
* camera settings like timezone, time, language etc

### **Sampling**: 
The raw audio signal, which is typically analog, is converted into a digital format through a process called sampling. This involves measuring the amplitude of the sound wave at regular intervals (the sample rate) and representing these measurements in a digital form.
- Input: Analog audio signal.
- Output: Digital representation of the audio signal.
- Effect: It's crucial to choose an appropriate sampling rate. A rate that's too low might lead to loss of relevant ENF information (aliasing), while a very high rate could result in unnecessarily large files without added value for ENF analysis.
Certainly! Sampling is a fundamental process in digital signal processing where an analog signal is converted into a digital signal by measuring its amplitude at regular intervals. The pseudocode for sampling an audio signal in Python, along with general requirements, is as follows:

#### General Requirements:
1. **Analog-to-Digital Converter (ADC)**: A hardware device or software component that converts the continuous analog audio signal into discrete digital values.
2. **Sampling Rate**: The number of samples taken per second, often measured in Hertz (Hz). The choice of sampling rate depends on the highest frequency present in the audio signal (according to Nyquist Theorem, it should be at least twice the highest frequency).
3. **Python Libraries**: Libraries like `wave` for reading audio files, and `numpy` for numerical operations.

#### Pseudocode:

```python
import wave
import numpy as np

def read_audio_file(file_path):
    # Open the audio file
    with wave.open(file_path, 'r') as wave_file:
        # Extract parameters
        frame_rate = wave_file.getframerate()  # Sampling rate
        n_frames = wave_file.getnframes()      # Total number of frames
        audio_data = wave_file.readframes(n_frames)

    # Convert audio data to numpy array
    audio_signal = np.frombuffer(audio_data, dtype=np.int16)

    return audio_signal, frame_rate

# Example usage
file_path = 'path/to/audio_file.wav'
audio_signal, frame_rate = read_audio_file(file_path)
```

- **`read_audio_file` Function**: This function reads an audio file using the `wave` library and extracts the audio data.
- **`frame_rate`**: Represents the sampling rate of the audio file.
- **`n_frames`**: The total number of frames (samples) in the audio file.
- **`audio_data`**: The raw audio data is read from the file.
- **`np.frombuffer`**: Converts the raw audio data into a numpy array for easier manipulation. The `dtype` (data type) should match the bit depth of the audio file (e.g., `np.int16` for 16-bit audio).
- **`audio_signal`**: The digital representation of the audio signal, which can now be processed further.

**Note:**
- This pseudocode assumes a simple mono audio file. For stereo or multi-channel files, additional steps are needed to handle multiple channels.
- The chosen sampling rate when recording the audio initially should be suitable for the content of the audio. For example, a standard CD-quality audio has a sampling rate of 44.1 kHz, which is more than sufficient for human speech and music.

### **Normalization**: 
This step adjusts the amplitude of the audio signal so that it falls within a standard range, often to avoid clipping and to maintain consistent volume levels across different audio samples.
- Input: Digital audio with varying amplitude levels.
- Output: Audio signal with standardized amplitude.
- Effect: Normalization might not significantly affect ENF analysis, as ENF extraction focuses on frequency rather than amplitude. However, excessive normalization can sometimes introduce artifacts or distortions.
-Normalization of audio data in Python involves adjusting the amplitude of the audio signal so that it fits within a certain range, often to prevent clipping and to maintain a consistent level across different audio samples. This process can also help to improve the Signal-to-Noise Ratio (SNR) for further processing.

#### General Requirements:
1. **Audio Data**: The digital audio data, usually represented as a NumPy array.
2. **Python Libraries**: `numpy` for numerical operations.

#### Pseudocode:

```python
import numpy as np

def normalize_audio(audio_signal):
    # Convert audio signal to floating point values
    audio_signal = audio_signal.astype(float)

    # Find the maximum absolute amplitude in the audio signal
    max_amplitude = np.max(np.abs(audio_signal))

    # Normalize the audio signal
    normalized_signal = audio_signal / max_amplitude

    return normalized_signal

# Example usage
# Assume 'audio_signal' is the digital representation of your audio data
normalized_audio = normalize_audio(audio_signal)
```

- **`normalize_audio` Function**: This function takes an audio signal as input and normalizes it.
- **Convert to Float**: The audio signal is converted to floating point values to avoid integer division.
- **Find Maximum Amplitude**: The maximum absolute amplitude is found using `np.max` and `np.abs`. This step ensures that the normalization process considers both positive and negative peaks.
- **Normalize**: The audio signal is normalized by dividing each sample by the maximum absolute amplitude. This scales the signal so that the peak amplitude is exactly 1.0 (or -1.0 for negative peaks).
- **Normalized Signal**: The output is a normalized audio signal where the peak amplitude fits within the range [-1.0, 1.0].

**Note:**
- The pseudocode assumes a mono audio signal. For stereo or multi-channel signals, you might need to handle each channel separately or together, depending on the desired outcome.
- Normalization is useful when dealing with multiple audio files recorded at different levels, but care should be taken to avoid introducing artifacts or distortions, especially in signals with very low amplitudes.

### **Noise Reduction**: 
Background noise and interference are common in audio recordings. Noise reduction techniques are applied to filter out unwanted sounds and reduce noise levels, improving the Signal-to-Noise Ratio (SNR) of the recording.
- Input: Audio signal with background noise.
- Output: Cleaner audio signal with reduced noise.
- Effect: If not carefully implemented, noise reduction can inadvertently filter out parts of the ENF signal, especially if the noise frequencies overlap with the ENF frequencies.
Noise reduction in audio processing involves the removal or reduction of unwanted background noise from an audio signal. This can be a complex task, depending on the type of noise and the quality of the original recording. For effective noise reduction in Python, you can use libraries like `scipy` for signal processing and `noisereduce`, a library specifically designed for noise reduction.

#### General Requirements:
1. **Audio Data**: Digital audio data, typically a NumPy array.
2. **Python Libraries**: `noisereduce` for noise reduction, `librosa` for audio loading, and `numpy` for numerical operations.

#### Python Pseudocode:

First, install the required packages:
```bash
pip install noisereduce librosa numpy
```

Then, we can use the following pseudocode for noise reduction:

```python
import noisereduce as nr
import librosa
import numpy as np

def reduce_noise(audio_signal, sr):
    # Perform noise reduction
    reduced_noise_signal = nr.reduce_noise(y=audio_signal, sr=sr)
    return reduced_noise_signal

# Example usage
file_path = 'path/to/your/audio_file.wav'
# Load audio file (librosa automatically normalizes audio to [-1, 1])
audio_signal, sr = librosa.load(file_path, sr=None) # sr=None ensures original sampling rate is used
noise_reduced_signal = reduce_noise(audio_signal, sr)
```

- **Libraries**: `librosa` is used for loading the audio file. It automatically normalizes the audio, but you can disable normalization if needed. `noisereduce` performs the noise reduction.
- **`reduce_noise` Function**: This function takes the audio signal and its sampling rate as inputs and applies noise reduction.
- **Noise Reduction**: `nr.reduce_noise` automatically estimates the noise profile from the audio signal and reduces the noise. It's also possible to provide a specific noise profile if you have a segment of audio that contains only the background noise.

**Recommendations:**
- **Noise Profile**: For better results, if you have a segment of the recording where only the background noise is present (without the desired signal), you can use that as a noise profile for more effective noise reduction.
- **Parameter Tuning**: `noisereduce` offers various parameters to fine-tune the noise reduction process. Adjusting these parameters can lead to better results depending on the specific characteristics of the audio.
- **Complex Noise**: If the noise is complex or varies significantly throughout the recording, advanced techniques or manual intervention might be necessary for optimal noise reduction.
- **Quality Preservation**: While noise reduction can significantly improve the clarity of an audio recording, it's important to strike a balance to avoid removing essential parts of the signal or introducing artifacts. 

Using libraries like `noisereduce` simplifies the process of noise reduction, but understanding the nature of the noise and the characteristics of the desired signal is crucial for effective results.
**Bandpass Filtering**: This process involves filtering the signal to keep only a specific range of frequencies that are relevant to the analysis. For ENF analysis, a bandpass filter might be used to isolate the frequency band around the expected ENF signal (e.g., around 50 Hz or 60 Hz).
- Input: Audio signal with a wide range of frequencies.
- Output: Audio signal focused on a specific frequency range.
- Effect: This is beneficial for ENF analysis as it isolates the frequency band around the expected ENF signal, reducing irrelevant frequency components.

### **Segmentation**: 
The audio signal is often divided into shorter segments or frames. This is particularly important for analyses that require examining how features of the audio signal vary over time.
- Input: Continuous audio signal.
- Output: Series of shorter audio segments.
- Effect: Essential for ENF analysis, as it allows for the examination of how the ENF signal changes over time. The length of segments must be chosen to balance temporal resolution with frequency accuracy.
Segmentation of audio data in Python involves dividing the audio signal into smaller, manageable segments or frames. This is a common step in many audio processing tasks, such as feature extraction, speech recognition, and noise reduction. Here's how you can perform segmentation along with the necessary requirements:
#### Trade-offs of Window Size

1. **Frequency Resolution vs. Time Resolution**:
    
    - Larger Window Size: Increases frequency resolution as more cycles of lower frequencies fit into the window. This is helpful for accurately identifying and analyzing lower frequencies. However, it reduces time resolution, meaning that changes in the audio signal over time are less precisely captured.
    - Smaller Window Size: Improves time resolution, allowing for better tracking of rapid changes in the signal over time. But, it decreases frequency resolution, making it harder to distinguish closely spaced frequencies, especially lower ones.
2. **Signal Stationarity**:
    
    - Audio signals are often assumed to be stationary (i.e., their statistical properties do not change over time) within a small window. A smaller window size is more likely to satisfy this assumption, especially in signals with rapid changes, like speech. Larger windows might encompass non-stationary characteristics, potentially leading to inaccuracies in frequency analysis.
3. **Computational Load**:
    
    - Larger windows contain more samples and, therefore, require more computational resources for processing. Conversely, smaller windows reduce computational demand but increase the number of segments to be processed.
#### General Requirements:
1. **Audio Data**: The digital audio signal, typically represented as a NumPy array.
2. **Python Libraries**: Basic Python libraries like `numpy` are sufficient for segmentation.

#### Python Pseudocode:

```python
import numpy as np

def segment_audio(audio_signal, frame_size, hop_length):
    # Number of segments
    num_segments = 1 + int((len(audio_signal) - frame_size) / hop_length)

    # Initialize segments
    segments = np.zeros((num_segments, frame_size))

    for i in range(num_segments):
        start = i * hop_length
        end = start + frame_size
        segments[i] = audio_signal[start:end]

    return segments

# Example usage
frame_size = 1024  # Frame size in samples
hop_length = 512  # Hop length in samples

# Assume 'audio_signal' is the digital representation of your audio data
segments = segment_audio(audio_signal, frame_size, hop_length)
```

- **`segment_audio` Function**: This function takes an audio signal and splits it into segments of a specified frame size and hop length.
- **Frame Size**: The number of samples in each segment.
- **Hop Length**: The number of samples to move ahead between segments. A smaller hop length increases the overlap between segments.
- **Segmentation Loop**: The audio signal is looped over, and each segment is extracted based on the frame size and hop length.
- **Segments**: The output is a 2D NumPy array where each row represents a segment of the audio signal.

**Notes and Recommendations**
- **Overlap**: In many audio processing applications, segments often overlap. This is controlled by the hop length. Overlapping can help in maintaining the continuity of the audio signal, especially in tasks like speech processing.
- **Windowing**: After segmentation, it's common to apply a window function (like Hamming or Hanning) to each segment to minimize the discontinuities at the edges of each frame.
- **Frame Size and Hop Length Selection**: The choice of frame size and hop length depends on the specific application and the characteristics of the audio signal. For example, speech signals often use smaller frame sizes (20-40 ms) to capture the rapidly changing characteristics of speech.
- **Memory Efficiency**: For very large audio files, consider using more memory-efficient approaches like generators or processing the segments in a loop without storing them all in memory at once.

Segmentation is a versatile and essential preprocessing step in various audio analysis and processing tasks, allowing for the detailed and efficient analysis of audio signals.

**Windowing**: 
Each segment of the audio signal might be multiplied by a window function to minimize edge effects in the spectral analysis. Windowing functions, like the Hamming or Hanning window, help in reducing spectral leakage when applying Fourier Transform.
- Input: Segmented audio signals.
- Output: Smoothed segments to minimize edge effects.
- Effect: Important for spectral analysis to reduce spectral leakage. However, the choice of window function and size can influence the resolution of the frequency analysis.

**Detrending**: This involves removing any trends or slow-moving components from the signal that are not relevant to the analysis, which can be especially important for stable frequency analysis like ENF extraction.
- Input: Audio signal with potential trends or slow-moving components.
- Output: More stationary audio signal.
- Effect: Generally, not very relevant for ENF analysis, as ENF signals are expected to be relatively stable and any slow trends might actually be part of the ENF information.

**Feature Extraction**: Relevant features are extracted from the preprocessed audio signal. This can include spectral features (like energy in specific frequency bands), temporal features (like zero-crossing rate), and others depending on the goal of the analysis.
- Input: Preprocessed audio signal.
- Output: Extracted features relevant to the analysis (e.g., frequency measurements).
- Effect: Critical for ENF analysis. The method of feature extraction will determine the accuracy and reliability of ENF frequency measurement.

**Data Augmentation** (if applicable): For machine learning applications, data augmentation might be used to artificially expand the dataset by creating modified versions of the audio data, such as changing the speed or pitch.
- Input: Original dataset of audio recordings.
- Output: Expanded dataset with modified versions of the original recordings.
- Effect: Not typically used in ENF analysis, as the authenticity of the original recording is crucial. Artificial modifications could distort the ENF signal.


### Bandpass Filter
In order to isolate the 50Hz component (and its harmonics), several methods have been proposed, the simplest of which is a direct fourier transform. 
E

1. **Audio Signal**: The starting point is the raw audio signal, which is a recording that may contain ENF information. ENF signatures can be embedded in recordings due to electrical network hum.

2. **Spectrum Analysis**: The audio signal is analyzed in the frequency domain using spectrum analysis. This involves transforming the audio signal from the time domain to the frequency domain, usually through a Fourier Transform (like the Fast Fourier Transform - FFT). 

3. **Frequency Spectrum**: The result of the Fourier Transform is a frequency spectrum that shows the energy (or power) present at different frequencies within the audio signal.

4. **ENF Signal Detection**: Within this frequency spectrum, the ENF signal needs to be identified. The ENF is typically a very steady frequency close to a nominal value (like 50 Hz or 60 Hz, depending on the region) with slight fluctuations over time.

5. **Peak Detection**: To precisely determine the ENF frequency at any given moment, peak detection in the spectrum is used. This involves identifying the frequency at which the power (energy) of the signal is the highest near the expected ENF value. This peak represents the ENF at that particular moment.

6. **Time Series of Frequency Measurement**: By repeatedly analyzing short segments of the audio signal over time and detecting the ENF peak in each segment, a time series of frequency measurements is created. This time series reflects how the ENF fluctuates over time.

7. **Signal-to-Noise Ratio (SNR)**: This is an important factor in ENF analysis. The quality and reliability of the frequency measurement depend on the SNR. Higher SNR means the ENF signal is clearer and more distinguishable from background noise.

8. **Filtering and Enhancement**: Various filtering techniques, like low-pass filters, may be used to enhance the ENF signal by reducing noise and interference. This step is crucial for accurate frequency measurement, especially in low SNR conditions.

9. **ENF Feature Extraction**: Finally, from the time series of frequency measurements, various features can be extracted for analysis. These features can include the mean frequency, fluctuations over time, and patterns in frequency changes.

This process of extracting ENF features from audio signals is fundamental in forensic audio analysis, where the aim is to determine the authenticity of a recording or to establish its time and location of origin. The precision in measuring the ENF frequency and understanding its fluctuations over time are key to effective audio forensics.
## 2 - Feature Extraction

Here, we can already write out some meaningful data. How much of the signal is actually there? Is the signal usable? What's the SNR? (What would be an acceptable SNR?)

The goal of this step is to arrive at a time series that's consists high resolution frequency