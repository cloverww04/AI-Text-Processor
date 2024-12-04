import os
from tasks.arithmetic import add_numbers, subtract_numbers, multiply_numbers, average, factorial
from tasks.strings import reverse_string

# Print the current working directory for debugging
print("Current working directory:", os.getcwd())

def read_input_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        return None

# Task dispatcher function
def task_dispatcher(task_type, *args):
    task_mapping = {
        "add": add_numbers,
        "subtract": subtract_numbers,
        "multiply": multiply_numbers,
        "reverse": reverse_string,
        "average": average,
        "factorial": factorial
    }

    # If task_type is in the mapping, call the corresponding function
    if task_type in task_mapping:
        if task_type == "reverse":
            return task_mapping[task_type](*args)
        elif task_type == "factorial":
            return task_mapping[task_type](args[0])
        else:
            return task_mapping[task_type](args)
    else:
        return f"Error: Unrecognized task '{task_type}'"

def process_input(input_text):
    results = []
    lines = input_text.splitlines()

    for line in lines:
        line = line.strip().lower()

        if line.startswith("task:"):
            line = line.replace("task:", "").strip()
            parts = line.split()

            task_type = parts[0]  # First word is the task type
            params = [int(param) for param in parts[1:] if param.isdigit()]  # Extract numbers from the remaining parts

            # Check for missing parameters for tasks that require numbers
            if task_type in ["add", "subtract", "multiply", "average", "factorial"] and not params:
                results.append(f"Error: Missing numbers for task '{task_type}'")
            else:
                # Dispatch the task
                result = task_dispatcher(task_type, *params) if params else task_dispatcher(task_type, line)  # No params for reverse task
                results.append(result)
        else:
            results.append(f"Error: Unrecognized task '{line}'")

    return results


if __name__ == "__main__":
    input_file = os.path.join("src", "input.txt")
    print(f"Looking for file: {input_file}")
    content = read_input_file(input_file)
    if content:
        print("File content:", content)
        print("Processing input...")
        results = process_input(content)
        for result in results:
            print("Result:", result)
