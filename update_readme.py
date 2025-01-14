import datetime

# Read the README content
with open("README.md", "r") as file:
    content = file.read()

# Insert the dynamic content
last_updated = f"📆 **Last Updated:** {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"
content = content.replace("<!-- DYNAMIC-CONTENT -->", last_updated)

# Write back the README
with open("README.md", "w") as file:
    file.write(content)
