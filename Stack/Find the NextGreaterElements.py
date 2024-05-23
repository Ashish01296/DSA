class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        results = []
        n = len(arr)
        
        for index in indices:
            current_element = arr[index]
            count = 0
            
            for i in range(index + 1, n):
                if arr[i] > current_element:
                    count += 1
            
            results.append(count)
        
        return results

# Main function
def main():
    # Example input
    arr = [3, 4, 2, 7, 5, 8, 10, 6]
    queries = 2
    indices = [0, 5]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the count_NGEs method
    output = solution.count_NGEs(len(arr), arr, queries, indices)
    
    # Print the output
    print(output)  # Output should be [6, 1]

if __name__ == "__main__":
    main()
