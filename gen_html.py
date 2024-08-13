import os

# Define the root directory where your GIF files are located
root_dir = './'  # Change this if your root directory is different

# Collect all the files
files = {}
for subdir, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.gif'):
            subfolder = os.path.basename(subdir)
            file_key = os.path.splitext(filename)[0]  # Get the file name without the extension
            if file_key not in files:
                files[file_key] = []
            files[file_key].append((subfolder, os.path.join(subdir, filename)))

print("files: ", files)
sorted_files = {key: sorted(value) for key, value in files.items()}
print("sorted files: ", sorted_files)
files = sorted_files

# Generate the HTML content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GIF Gallery</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
"""

for file_name, subfolders in files.items():
    html_content += f"""        <section class="relation-section">
            <h1 class="relation">{file_name}</h1>
"""
    for subfolder, file_path in subfolders:
        html_content += f"""            <div class="model-section">
                <h2 class="model">{subfolder}</h2>
                <img class="animation" src="{file_path}" alt="{file_name} in {subfolder}">
            </div>
"""
    html_content += "            <hr>\n        </section>\n"

html_content += """    </main>
</body>
</html>
"""

# Save the HTML to a file
with open("gallery.html", "w") as file:
    file.write(html_content)

print("HTML file generated successfully.")
