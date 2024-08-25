Fibonacci Sequence and Golden Ratio Visualization
This Python project generates the Fibonacci sequence up to a specified number of terms and visualizes the convergence of the ratio of consecutive Fibonacci numbers to the Golden Ratio (approximately 1.618). The project uses Matplotlib to plot the sequence and the ratio convergence.

Features
Fibonacci Sequence Generation: Generate the Fibonacci sequence up to the user-defined number of terms.
Golden Ratio Calculation: Compute the ratio between consecutive Fibonacci numbers to observe the convergence to the Golden Ratio.
Data Visualization: Visualize the Fibonacci sequence and the convergence to the Golden Ratio using Matplotlib.
Requirements
Python 3.x
Required Python packages:
matplotlib
Install the required package using pip:

bash
Copy code
pip install matplotlib
Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/sivapriya87/HexSoftwares_Fibonacci_Generator.git
cd fibonacci-golden-ratio
Run the Script:

Execute the Python script to start the program.

bash
Copy code
python fibonacci_golden_ratio.py
Input the Number of Terms:

When prompted, enter the number of terms for the Fibonacci sequence generation. The program will generate the sequence, calculate the Golden Ratio, and display the results.

View the Plot:

After the calculations, the program will display two plots:

Fibonacci Sequence: Shows the sequence of Fibonacci numbers.
Golden Ratio Convergence: Illustrates how the ratio of consecutive Fibonacci numbers converges to the Golden Ratio.
Example
If you input 10, the program will output:

mathematica
Copy code
Fibonacci Sequence Project
Enter the number of Fibonacci terms to generate: 10

The first 10 terms of the Fibonacci sequence are:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

The ratios between consecutive Fibonacci numbers are:
[2.0, 1.5, 1.6666666666666667, 1.6, 1.625, 1.6153846153846154, 1.619047619047619, 1.6176470588235294]

The program will then display plots of the Fibonacci sequence and the convergence to the Golden Ratio.

How It Works
fibonacci(n): Generates the Fibonacci sequence up to the nth term.
golden_ratio(sequence): Calculates the ratio of each term to its predecessor in the Fibonacci sequence.
plot_fibonacci(sequence, ratios): Visualizes the Fibonacci sequence and the convergence to the Golden Ratio using Matplotlib.
Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a pull request

Acknowledgments
Fibonacci sequence and the Golden Ratio concepts.
