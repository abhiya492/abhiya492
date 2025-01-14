import datetime

# Define the placeholder in your README
PLACEHOLDER = "<!-- DYNAMIC-CONTENT -->"

# Read the current README file
with open("README.md", "r") as file:
    content = file.read()

# Generate dynamic content
last_updated = f"📆 **Last Updated:** {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"
dynamic_content = f"""
{last_updated}

💡 *Here's a motivational quote for you:*
> "The best way to predict the future is to create it." — Peter Drucker
"""

# Replace the placeholder with dynamic content
updated_content = content.replace(PLACEHOLDER, dynamic_content)

# Write the updated content back to the README
with open("README.md", "w") as file:
    file.write(updated_content)

print("README updated successfully!")
