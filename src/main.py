import os

def read_input_file(filepath):
    """Reads the input file and returns its content."""
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        return None

def generate_variants(pattern):
    """Generate all variants (rotations and mirrors) of a pattern."""
    def rotate_90(pattern):
        return [''.join(row[i] for row in reversed(pattern)) for i in range(len(pattern[0]))]

    variants = [pattern]  # Original pattern
    current = pattern

    # Generate rotations
    for _ in range(3):
        current = rotate_90(current)
        variants.append(current)

    # Generate mirrored versions
    mirrored = [row[::-1] for row in pattern]
    variants.append(mirrored)

    current = mirrored
    for _ in range(3):
        current = rotate_90(current)
        variants.append(current)

    # Convert to a set of immutable tuples to remove duplicates
    unique_variants = set(tuple(map(tuple, v)) for v in variants)

    # Convert back to list of lists
    return [list(map(list, v)) for v in unique_variants]


def pattern_match_matrix(matrix, patterns):
    """Count the number of times multiple patterns appear in a matrix."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    match_positions = set()  # To store unique match positions

    # Helper function to match at a specific position
    def matches_at(matrix, pattern, start_row, start_col):
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0]) if pattern_rows > 0 else 0
        for p_i in range(pattern_rows):
            for p_j in range(pattern_cols):
                if pattern[p_i][p_j] != "." and matrix[start_row + p_i][start_col + p_j] != pattern[p_i][p_j]:
                    return False
        return True

    # Iterate through all patterns
    for base_pattern in patterns:
        pattern_variants = generate_variants(base_pattern)  # Generate all pattern variants

        for variant in pattern_variants:
            pattern_rows = len(variant)
            pattern_cols = len(variant[0]) if pattern_rows > 0 else 0

            # Scan through the matrix for the current pattern
            for i in range(rows - pattern_rows + 1):
                for j in range(cols - pattern_cols + 1):
                    if matches_at(matrix, variant, i, j):
                        match_positions.add((i, j))  # Track unique match position

    return len(match_positions)



def process_input(input_text):
    """Processes the input and performs pattern matching."""
    lines = input_text.splitlines()

    matrix = []  # To store the matrix
    patterns = []  # To store multiple patterns

    is_pattern_section = False
    is_matrix_section = False

    current_pattern = []

    for line in lines:
        line = line.strip()

        if line.startswith("pattern:"):
            # Start of a pattern section
            if current_pattern:
                patterns.append(current_pattern)  # Save the previous pattern
                current_pattern = []
            is_pattern_section = True
            is_matrix_section = False
            continue

        if line.startswith("matrix:"):
            # End of the pattern section and start of matrix section
            if current_pattern:
                patterns.append(current_pattern)  # Save the final pattern
                current_pattern = []
            is_pattern_section = False
            is_matrix_section = True
            continue

        # Process pattern section
        if is_pattern_section:
            if line:  # Ensure we don't process empty lines
                current_pattern.append(list(line))

        # Process matrix section
        elif is_matrix_section:
            if line:  # Ensure we don't process empty lines
                matrix.append(list(line))

    # Add the last pattern if it exists
    if current_pattern:
        patterns.append(current_pattern)

    # If both patterns and matrix are found, perform the pattern match
    if patterns and matrix:
        result = pattern_match_matrix(matrix, patterns)
        return f"Patterns found {result} times."
    else:
        return "Error: Patterns or matrix missing."


# Main program
if __name__ == "__main__":
    input_file = os.path.join("src", "input.txt")
    print(f"Looking for file: {input_file}")
    content = read_input_file(input_file)

    if content:
        print("File content:", content)
        print("Processing input...")
        result = process_input(content)
        print("Result:", result)
