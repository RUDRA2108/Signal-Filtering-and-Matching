# -*- coding: utf-8 -*-
"""signal_filtering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qXsZtfwOBF6CM14te8Ca4obWea_Bz0cw
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the input signal x(t) from the text file
def read_signal(file_path):
    with open(file_path, 'r') as file:
        signal = [float(line.strip()) for line in file]
    return np.array(signal)

# Step 3: Implement the filters
def low_pass_filter(signal):
    return np.convolve(signal, np.ones(10)/10, mode='same')  # Example: Moving average filter

def high_pass_filter(signal):
    return signal - low_pass_filter(signal)

def band_pass_filter(signal):
    return high_pass_filter(low_pass_filter(signal))

# Step 6: Calculate mean normalized correlation for each filter
def mean_normalized_correlation(signal, filtered_signal):
    corr = np.correlate(signal, filtered_signal, mode='same')
    return np.mean(corr / (np.sqrt(np.sum(signal*2)) * np.sqrt(np.sum(filtered_signal*2))))

# Step 7: Plot input signal, actual output signal, and filtered output signal
def plot_signals(input_signal, output_signal, filtered_signal, filter_name):
    plt.figure(figsize=(10, 6))
    plt.plot(input_signal, label='Input Signal')
    plt.plot(output_signal, label='Actual Output Signal')
    plt.plot(filtered_signal, label=f'{filter_name} Filtered Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Comparison of Input, Actual Output, and Filtered Output')
    plt.legend()
    plt.grid(True)
    plt.show()

# Step 8: Print input signal
def print_input_signal(signal):
    print("Input Signal:")
    print(signal)

# Step 9: Print actual output signal
def print_output_signal(signal):
    print("Actual Output Signal:")
    print(signal)

# Step 10: Print filtered output signal
def print_filtered_signal(signal, filter_name):
    print(f"{filter_name} Filtered Signal:")
    print(signal)

# Read input and output signals from files
x_t = read_signal('INPUT-SIGNAL-X(t).txt')
y_t = read_signal('OUTPUT-SIGNAL-Y(t).txt')

# Convolve each filter with the input signal
ylp_t = low_pass_filter(x_t)
yhp_t = high_pass_filter(x_t)
ybp_t = band_pass_filter(x_t)

# Calculate mean normalized correlation for each filter
mean_corr_ylp = mean_normalized_correlation(y_t, ylp_t)
mean_corr_yhp = mean_normalized_correlation(y_t, yhp_t)
mean_corr_ybp = mean_normalized_correlation(y_t, ybp_t)

# Print mean normalized correlation for each filter
print(f"Mean normalized correlation for Low Pass Filter: {mean_corr_ylp}")
print(f"Mean normalized correlation for High Pass Filter: {mean_corr_yhp}")
print(f"Mean normalized correlation for Band Pass Filter: {mean_corr_ybp}")

# Identify the best match based on correlation result
best_match = np.argmax([mean_corr_ylp, mean_corr_yhp, mean_corr_ybp])

if best_match == 0:
    print("Low pass filter best matches the output signal.")
    print_input_signal(x_t)
    print_output_signal(y_t)
    print_filtered_signal(ylp_t, 'Low Pass')
    plot_signals(x_t, y_t, ylp_t, 'Low Pass')
elif best_match == 1:
    print("High pass filter best matches the output signal.")
    print_input_signal(x_t)
    print_output_signal(y_t)
    print_filtered_signal(yhp_t, 'High Pass')
    plot_signals(x_t, y_t, yhp_t, 'High Pass')
else:
    print("Band pass filter best matches the output signal.")
    print_input_signal(x_t)
    print_output_signal(y_t)
    print_filtered_signal(ybp_t, 'Band Pass')
    plot_signals(x_t, y_t, ybp_t, 'Band Pass')

