with open('Data Resume/extracted_text_resumes_fourth_run.txt', 'r', encoding="utf-8") as file:
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
average_similarity = total_similarity / 400
print(f"The average jaccard similarity over 400 documents is: {average_similarity:.3f}")