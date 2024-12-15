import random
import time
import heapq
import matplotlib.pyplot as plt

# Simulate real-time stock data
def generate_stock_data():
    stock_id = random.randint(1, 100)
    price = random.uniform(10.0, 500.0)  # Random stock price between 10 and 500
    timestamp = time.time()  # Current time as timestamp
    return (stock_id, price, timestamp)

# Sorting Algorithms

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[1] < arr[j][1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# QuickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[1] < pivot[1]]
    middle = [x for x in arr if x[1] == pivot[1]]
    right = [x for x in arr if x[1] > pivot[1]]
    return quick_sort(left) + middle + quick_sort(right)

# HeapSort
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# MergeSort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# TimSort (Python's built-in method)
def tim_sort(arr):
    return sorted(arr, key=lambda x: x[1])  # Sorting based on stock price

# Get Top N Stock Prices
def get_top_n_prices(arr, n):
    return sorted(arr, key=lambda x: x[1], reverse=True)[:n]

# Function to visualize the real-time top N stock prices
def visualize_top_n_prices(top_n):
    prices = [stock[1] for stock in top_n]
    stock_ids = [stock[0] for stock in top_n]
    
    plt.figure(figsize=(10, 5))
    plt.bar(stock_ids, prices)
    plt.xlabel('Stock ID')
    plt.ylabel('Stock Price')
    plt.title('Top N Stock Prices in Real-Time')
    plt.show()

# Main function to simulate the system
def simulate_stock_trading_system():
    stock_data_stream = []
    num_iterations = 100  # Number of stock price updates to simulate
    top_n = 5  # Number of top prices to track
    
    sorting_algorithms = {
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Merge Sort": merge_sort,
        "Tim Sort": tim_sort
    }
    
    for algo_name, sort_algo in sorting_algorithms.items():
        print(f"\nTesting with {algo_name}:")
        start_time = time.time()
        
        # Simulate real-time data stream
        for i in range(num_iterations):
            new_stock = generate_stock_data()
            stock_data_stream.append(new_stock)
            
            # Sort the stock data based on the current algorithm
            sorted_data = sort_algo(stock_data_stream.copy())  # Sort a copy of the data
            top_n_stocks = get_top_n_prices(sorted_data, top_n)  # Get the top N prices
            
            # Optionally, visualize the current top N stock prices
            if i % 20 == 0:  # Visualize every 20th iteration
                visualize_top_n_prices(top_n_stocks)
            
            # Simulate real-time delay between data arrivals (e.g., every 0.1 second)
            time.sleep(0.1)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total time for sorting {num_iterations} stock prices with {algo_name}: {elapsed_time:.4f} seconds")
        
# Execute the system simulation
simulate_stock_trading_system()