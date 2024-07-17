import requests 
import json
from PIL import Image
import base64

# Path to the image in the directory of the current notepad
image_path = 'Yield.PNG'
img = Image.open(image_path)

#  Convert image to base64 format
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# Make a request to Google Cloud Vision API
api_key = 'example'
url = f'test={api_key}'# <-- link api key based on account

headers = {'Content-Type': 'application/json'}
data = {
    "requests": [
        {
            "image": {
                "content": base64_image
            },
            "features": [
                {
                    "type": "TEXT_DETECTION"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

# Extract the text from the answer
text = result['responses'][0].get('fullTextAnnotation', {}).get('text', 'No text found')

# Save the data to a text file
with open('file.txt', 'w') as file:
    file.write(text)

print("Processing completed. Results saved to file file.txt")


# Read the input from file.txt
with open('file.txt', 'r') as file:
    input_text = file.read()

# Split the input text into lines
lines = input_text.split('\n')

# Initialize variables to store processed lines
processed_lines = []
result_line = ""

# Iterate over each line and process accordingly
for line in lines:
    if line.endswith(':'):
        if result_line:
            processed_lines.append(result_line.strip())
            result_line = line + " "
        else:
            result_line = line
    else:
        result_line += line

# Append the last processed line
if result_line:
    processed_lines.append(result_line.strip())

# Join all processed lines with newline characters
output_text = '\n'.join(processed_lines)

# Write the output to YieldWA.txt
with open('file2.txt', 'w') as file:
    file.write(output_text)

print("Processing completed. Results saved to file file2.txt")