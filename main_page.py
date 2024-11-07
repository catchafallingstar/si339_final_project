import os

# Specify the directory containing the HTML files
directory = 'meets'  # Replace with your folder path

# Create/open the index.html file for writing
with open(os.path.join(directory, 'index.html'), 'w', encoding='utf-8') as index_file:
    # Write the basic structure of index.html
    index_file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <title>Meets Gallery</title>
   
</head>
<body>
    <h1>Skyline Highschool Meets</h1>
    <nav>
        <table>
            <tr>
                <th>Meets</th>
                <th>Link</th>
            </tr>
''')

    # Loop through the files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an HTML file and not the index.html itself
        if filename.endswith('.html') and filename != 'index.html':
            index_file.write(f'            <tr><td class = " meet-column ">{filename}</td><td class = " link-column "><a href="meets/{filename}">Open</a></td></tr>\n')

    # Close the table and body structure
    index_file.write('''        </table>
    </nav>
</body>
</html>
''')

print(f"index.html created successfully in {directory}")
