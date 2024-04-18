import numpy as np

# Step 1: Read the input signal x(t) from the text file
def read_signal(file_path):
    with open(file_path, 'r') as file:
        signal = [float(line.strip()) for line in file]
    return np.array(signal)

# Step 2: Read the output signal y(t) from the text file
x_t = read_signal('input_signal.txt')
y_t = read_signal('output_signal.txt')

# Step 3: Implement the filters
def low_pass_filter(signal):
    # Implement your low pass filter
    filtered_signal = np.convolve(signal, np.ones(10)/10, mode='same')  # Example: Moving average filter
    return filtered_signal

def high_pass_filter(signal):
    # Implement your high pass filter
    return signal - low_pass_filter(signal)

def band_pass_filter(signal):
    # Implement your band pass filter
    return high_pass_filter(low_pass_filter(signal))

# Step 4: Convolve each filter with the input signal
def convolve(signal, kernel):
    N = len(signal)
    M = len(kernel)
    output = np.zeros(N + M - 1)
    for n in range(N + M - 1):
        for k in range(M):
            if n - k >= 0 and n - k < N:
                output[n] += signal[n - k] * kernel[k]
    return output

ylp_t = low_pass_filter(x_t)
yhp_t = high_pass_filter(x_t)
ybp_t = band_pass_filter(x_t)

# Step 5: Calculate correlation with the output signal
def correlation(x, y):
    N = len(x)
    M = len(y)
    correlation_result = np.zeros(N + M - 1)
    for n in range(N + M - 1):
        for k in range(M):
            if n - k >= 0 and n - k < N:
                correlation_result[n] += x[n - k] * y[k]
    return correlation_result

correlation_ylp = correlation(y_t, ylp_t)
correlation_yhp = correlation(y_t, yhp_t)
correlation_ybp = correlation(y_t, ybp_t)

# Step 6: Identify the best match based on correlation result
best_match = np.argmax([np.max(correlation_ylp), np.max(correlation_yhp), np.max(correlation_ybp)])

if best_match == 0:
    print("Low pass filter best matches the output signal.")
elif best_match == 1:
    print("High pass filter best matches the output signal.")
else:
    print("Band pass filter best matches the output signal.")
