def function_with_improved_error_handling(data):
    if not data:
        return []

    result = []
    errors = []  # Keep track of errors encountered
    for item in data:
        try:
            processed_item = process_item(item)
            result.append(processed_item)
        except Exception as e:
            error_message = f"Error processing item {item}: {e}"
            errors.append(error_message) 
            # Log the error more robustly (e.g., to a file, database, or logging system)
            # print(error_message) 
    
    if errors:
        print("Errors encountered:")
        for error in errors:
            print(error)
            # Consider raising a custom exception here to signal significant problems
    return result

#The process_item function remains unchanged
def process_item(item):
    # Simulate side effect (modifying external state or file I/O)
    # ... some code ...
    return item * 2