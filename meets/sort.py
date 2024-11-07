import os

# Get all HTML files in the current directory
meet_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Function to extract the meet name (ignores specifics like "men", "women", etc.)
def get_meet_name(file_name):
    parts = file_name.replace("_", " ").replace(".html", "").split()
    return " ".join(parts[:2]).title()  # Assumes the meet name is the first two words

# Group files by their meet names
meet_dict = {}
for file in meet_files:
    meet_name = get_meet_name(file)
    if meet_name not in meet_dict:
        meet_dict[meet_name] = []
    meet_dict[meet_name].append(file)

# Sort the meet names
sorted_meet_names = sorted(meet_dict.keys())

# Generate the HTML code
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skyline Meets</title>
</head>
<body>
    <div>
"""

# Append the sorted meet links to the HTML
for meet_name in sorted_meet_names:
    html_content += f"""
        <ul> {meet_name}
    """
    for file in sorted(meet_dict[meet_name]):
        html_content += f"""
            <li><a href="{file}">{file.replace("_", " ").replace(".html", "").title()}</a></li>
        """
    html_content += "</ul>"

# Close the div and body tags
html_content += """
    </div>
</body>
</html>
"""

# Save the generated HTML to a file
with open("index.html", "w") as file:
    file.write(html_content)

print("HTML file 'index.html' generated successfully.")
