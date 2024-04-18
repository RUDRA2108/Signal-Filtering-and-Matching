
---

# Signal Filtering and Matching


This Python script is designed to infer the type of filtering (Low Pass, High Pass, or Band Pass) that has been applied to an input signal based on a given output signal. It implements convolution and correlation techniques to compare the filtered outputs with the given output signal.

## Usage

### Prerequisites
- Python 3.x
- NumPy

### Installation
1. Clone or download the repository to your local machine.
2. Ensure that you have Python 3.x installed.
3. Install the required dependencies by running the following command:
   ```
   pip install numpy
   ```

### Running the Script
1. Place the input signal (`input_signal.txt`) and the output signal (`output_signal.txt`) files in the same directory as the script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script and input files.
4. Run the script using the following command:
   ```
   python signal_filtering.py
   ```

### Output
- The script will analyze the input and output signals, apply low-pass, high-pass, and band-pass filters, and determine which filter best matches the given output signal.
- The output will be printed to the console, indicating whether the low-pass, high-pass, or band-pass filter best matches the output signal.