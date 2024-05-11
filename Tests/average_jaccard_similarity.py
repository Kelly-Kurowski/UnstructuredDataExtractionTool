with open('extracted_text_results_second_run.txt', 'r') as file:
    # Initialize variables to store the sum of Jaccard similarities
    total_similarity = 0

    # Iterate through each line in the file
    for line in file:
        # Check if the line contains Jaccard similarity information
        if "Jaccard similarity:" in line:
            # Extract the Jaccard similarity value
            similarity = float(line.split(":")[-1].strip())
            # Add it to the total
            total_similarity += similarity

# Calculate the average jaccard similarity
average_similarity = total_similarity / 181
print(f"The average jaccard similarity over 181 documents is: {average_similarity:.3f}")