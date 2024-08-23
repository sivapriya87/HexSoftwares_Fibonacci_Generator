from matplotlib import pyplot as plt

def fibonacci(n):
    """Generate Fibonacci sequence up to the nth term."""
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

def golden_ratio(sequence):
    """Calculate the ratio of consecutive Fibonacci numbers."""
    ratios = [sequence[i] / sequence[i - 1] for i in range(2, len(sequence))]
    return ratios

def plot_fibonacci(sequence, ratios):
    """Plot the Fibonacci sequence and the golden ratio."""
    plt.figure(figsize=(12, 6))

    # Plot Fibonacci Sequence
    plt.subplot(1, 2, 1)
    plt.plot(sequence, marker='o')
    plt.title('Fibonacci Sequence')
    plt.xlabel('Index')
    plt.ylabel('Fibonacci Number')

    # Plot Golden Ratio Convergence
    plt.subplot(1, 2, 2)
    plt.plot(ratios, marker='o', color='orange')
    plt.axhline(y=1.618, color='red', linestyle='--', label='Golden Ratio (≈ 1.618)')
    plt.title('Convergence to the Golden Ratio')
    plt.xlabel('Index')
    plt.ylabel('Ratio')

    plt.tight_layout()
    plt.show()

def main():
    print("Fibonacci Sequence Project")
    
    # User input for the number of Fibonacci terms
    n = int(input("Enter the number of Fibonacci terms to generate: "))
    
    # Generate Fibonacci sequence
    fib_sequence = fibonacci(n)
    
    # Display the Fibonacci sequence
    print(f"\nThe first {n} terms of the Fibonacci sequence are:\n{fib_sequence}")

     # Calculate the Golden Ratio
    ratios = golden_ratio(fib_sequence)
    
          # Display the Golden Ratio calculations
    print(f"\nThe ratios between consecutive Fibonacci numbers are:\n{ratios}")
    
         # Plot the sequence and the ratio convergence
    plot_fibonacci(fib_sequence, ratios)

if __name__ == "__main__":
    main()