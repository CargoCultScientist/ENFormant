import math

def temporal_discrete_median_filter(input_signal, window_order, threshold):
    """
    This function applies a Temporal Discrete Median Filter (TDMF) to a given signal. 
    TDMF is a method used in signal processing to remove spikes or outliers from the signal.
    
    The process involves moving a 'window' across the signal, computing the median of the values
    in that window, and then comparing each value in the window to this median. If a value is 
    too different from the median (beyond a specified 'threshold'), it is replaced by the median.
    This smooths out the signal by removing abrupt changes (spikes).
    
    Parameters:
    input_signal (list): The original signal (list of numerical values) that you want to smooth.
    window_order (int): The size of the 'window' - how many values around each point are considered to calculate the median.
    threshold (float): A value that determines how different a point must be from the median to be considered a spike.
    
    Returns:
    list: The smoothed signal with spikes and outliers reduced.
    """

    # Length of the input signal
    input_length = len(input_signal)

    # Initialize arrays to store the median-filtered signal and the final output signal
    median_filtered_signal = [None] * input_length
    output_signal = [None] * input_length

    # Calculate the padding length required on each side of the signal
    padding_length = int((window_order - 1) / 2)

    # Create padding for the start and end of the signal.
    # This is done to ensure the window has enough values at the edges of the signal.
    start_padding = [input_signal[0]] * padding_length
    end_padding = [input_signal[-1]] * padding_length

    # Combine the padding and original signal into a single, padded signal
    padded_signal = start_padding + input_signal + end_padding

    # Calculate the median for each window position in the signal
    for i in range(input_length):
        # Extract the window of values from the padded signal
        window = padded_signal[i: i + window_order]
        # Sort the values in the window to find the median
        window.sort()
        # The median is the middle value in the sorted window
        median_filtered_signal[i] = window[math.ceil((window_order - 1) / 2)]

    # Calculate the difference between the median-filtered signal and the original signal
    detrended_signal = [median_filtered_signal[i] - input_signal[i] for i in range(input_length)]

    # Apply the threshold to each value in the signal
    for i in range(input_length):
        # If the difference between the original signal and the median is within the threshold,
        # keep the original value. Otherwise, replace it with the median.
        if abs(detrended_signal[i]) <= threshold:
            output_signal[i] = input_signal[i]
        else:
            output_signal[i] = median_filtered_signal[i]

    # Return the smoothed signal
    return output_signal
