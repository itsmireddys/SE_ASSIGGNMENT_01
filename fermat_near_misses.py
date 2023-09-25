import itertools  # Import itertools for count function

# Program Title: Fermat's Last Theorem Near Misses
# File Name: fermat_near_misses.py
# External Files Needed: itertools
# External Files Created: None
# Programmers: Vidya Sagar Reddy Mukkala, sai krishna
# Course: Software Engineering 001
# Date Completed: 2023-09-24
# Program Explanation: This program searches for near misses of Fermat's Last Theorem for given n and k values.
# It calculates and displays the smallest relative miss and related information.
# Resources Used: None

def calculate_miss(x, y, z, n):
    """
    Calculate the miss for a given x, y, z, and n.
    
    Args:
    x (int): The value of x.
    y (int): The value of y.
    z (int): The value of z.
    n (int): The power in the equation.

    Returns:
    float: The relative miss as a percentage.
    """
    xn_yn = x**n + y**n
    zn = z**n
    znp1 = (z + 1)**n
    miss1 = abs(xn_yn - zn)
    miss2 = abs(znp1 - xn_yn)
    return min(miss1, miss2) / xn_yn

def find_near_misses(n, k):
    """
    Find near misses of Fermat's Last Theorem for a given n and k.
    
    Args:
    n (int): The power in the equation.
    k (int): The upper limit for x, y, and z.

    Returns:
    tuple: The best x, y, z, n, miss, and smallest_relative_miss values.
    """
    smallest_relative_miss = float('inf')
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            for z in itertools.count(1):
                relative_miss = calculate_miss(x, y, z, n)
                if relative_miss < smallest_relative_miss:
                    smallest_relative_miss = relative_miss
                    best_x, best_y, best_z = x, y, z
                    miss = min(x**n + y**n - z**n, (z + 1)**n - x**n - y**n)
                else:
                    break
    return best_x, best_y, best_z, n, miss, smallest_relative_miss

def main():
    # Input n and k from the user
    n = int(input("Enter the value of n (2 < n < 12): "))
    k = int(input("Enter the value of k (k > 10): "))

    smallest_relative_miss = float('inf')  # Initialize with positive infinity

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            for z in range(1, k + 1):
                xn_yn = x ** n + y ** n
                zn = z ** n

                # Check for near misses
                if abs(xn_yn - zn) < smallest_relative_miss:
                    smallest_relative_miss = abs(xn_yn - zn)
                    current_x, current_y, current_z = x, y, z

    relative_miss_percentage = (smallest_relative_miss / (current_x ** n + current_y ** n)) * 100

    print("Smallest Relative Miss:")
    print(f"x = {current_x}, y = {current_y}, z = {current_z}")
    print(f"Actual Miss: {smallest_relative_miss}")
    print(f"Relative Miss Percentage: {relative_miss_percentage}%")

if __name__ == "__main__":
    main()
