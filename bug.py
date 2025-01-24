def function_with_uncommon_error(data):
    if not data:
        return []  # Handle empty input

    result = []
    for item in data:
        try:
            processed_item = process_item(item) # Assume process_item has side effects
            result.append(processed_item)
        except Exception as e:
            print(f"Error processing item {item}: {e}")
            # In a real-world scenario, consider logging this error to a file or system
            # Instead of just printing it
            # Implement proper error handling to avoid partial data corruption
            continue  # Continue processing remaining items despite an error

    return result

# Example of a function that might have side-effects
def process_item(item):
    # Simulate side effect (modifying external state or file I/O)
    # ... some code ...
    return item * 2 # Or some other processing