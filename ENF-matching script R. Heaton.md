https://github.com/robert/enf-matching

This Python script is a comprehensive example of processing an audio file to perform Electrical Network Frequency (ENF) analysis. It's designed to load audio files, extract the #ENF signal, and compare this signal with reference data to predict the timing of the recording. The script uses several libraries, such as `numpy`, `matplotlib`, and `scipy`, and involves signal processing techniques. I'll explain the key functions and flow of the script:

### Key Functions

1. **`load_wav(fpath)`:** 
   - Loads a WAV file from a given path `fpath`.
   - Uses the `wave` module to read the audio data and sample rate.
   - Returns a tuple containing the audio data and the sample rate (`fs`).

2. **`butter_bandpass_filter(data, locut, hicut, fs, order)`:**
   - Applies a Butterworth bandpass filter to the audio data.
   - Filters the data to retain frequencies between `locut` and `hicut`.
   - Useful for isolating the ENF signal within a specific frequency range.

3. **`stft(data, fs)`:**
   - Performs a Short-Time Fourier Transform (STFT) on the audio data.
   - This is used to analyze the frequency content of the audio data over time.
   - Returns the frequencies, time segments, and the STFT results.

4. **`enf_series(data, fs, nominal_freq, freq_band_size, harmonic_n)`:**
   - Extracts a series of ENF values from the audio data.
   - Applies the Butterworth filter and STFT to focus on the ENF signal.
   - Uses quadratic interpolation to refine the frequency estimation.
   - Returns a dictionary with various components of the analysis, including the ENF values.

5. **`pmcc(x, y)`:**
   - Calculates the Pearson Product-Moment Correlation Coefficient (PMCC) between two sets of data.
   - Useful for measuring the linear correlation between the target ENF data and reference data.

6. **`sorted_pmccs(target, references)`:**
   - Calculates PMCCs between target ENF data and multiple reference datasets.
   - Returns a sorted list of tuples containing reference indices and PMCC values.

7. **`search(target_enf, reference_enf)`:**
   - Performs a sliding window comparison of the target ENF data against a longer reference ENF series.
   - Uses PMCC to find the best match and predict the timing of the recording.

8. **`gb_reference_data(year, month, day)`:**
   - Fetches and caches reference ENF data from Great Britain's National Grid for a specific date.
   - This function is not used directly in the main script but is included for completeness.

9. **Plotting Functions (`plot_stft_ax`, `plot_series_ax`):**
   - These functions are used for visualizing the STFT results and ENF series.

### Main Script Flow

- The script begins by setting some parameters like `nominal_freq` and `freq_band_size`.
- It then loads a reference WAV file (`001_ref.wav`) and processes it to extract the reference ENF series.
- Another target WAV file (`001.wav`) is loaded and processed similarly to extract the target ENF series.
- The script then compares the target ENF series with the reference ENF series using the `search` function, which employs PMCC.
- The highest PMCC value and its corresponding index give the best estimate for when the target recording was made, compared to the reference data.
- Finally, the script visualizes the results using matplotlib plots, showing both the ENF series and the STFT analysis.

This script is a solid example of how to implement ENF analysis in #Python, demonstrating both signal processing and statistical correlation techniques to analyze and compare audio recordings.