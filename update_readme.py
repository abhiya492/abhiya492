import datetime
import random

# Define the placeholder in your README
PLACEHOLDER = "<!-- DYNAMIC-CONTENT -->"

# Define a list of motivational quotes
quotes = [
    "The best way to predict the future is to create it. — Peter Drucker",
    "Your time is limited, so don’t waste it living someone else’s life. — Steve Jobs",
    "The only way to do great work is to love what you do. — Steve Jobs",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. — Jim Rohn",
    "Success is not in what you have, but who you are. — Bo Bennett"
]

# Read the current README file
with open("README.md", "r") as file:
    content = file.read()

# Generate dynamic content
last_updated = f"📆 **Last Updated:** {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"
random_quote = random.choice(quotes)
dynamic_content = f"""
{last_updated}

💡 *Here's a motivational quote for you:*
> "{random_quote}"
"""

# Replace the placeholder with dynamic content
updated_content = content.replace(PLACEHOLDER, dynamic_content)

# Write the updated content back to the README
with open("README.md", "w") as file:
    file.write(updated_content)

print("README updated successfully!")
