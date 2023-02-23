import requests
from bs4 import BeautifulSoup
import re
from googlesearch import search

query = input("Please enter search criteria: ")
num_results = 10
email_addresses = set()

for url in search(query, num_results=num_results):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    email_regex = re.compile(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+")

    for email in soup.find_all("a", href=email_regex):
        email_address = email["href"].split(":")[1].strip()
        email_addresses.add(email_address)

while True:
    output_option = input("Do you want to save the email addresses to a file (F) or print them in the terminal (P)? ").lower()
    if output_option == "f":
        with open("addresses.txt", "w") as f:
            for email_address in email_addresses:
                f.write(email_address + "\n")
        print("Email addresses saved to addresses.txt.")
        break
    elif output_option == "p":
        if len(email_addresses) > 0:
            print("Email addresses found:")
            for email_address in email_addresses:
                print(email_address)
        else:
            print("No email addresses found.")
        break
    else:
        print("Invalid input. Please enter F to save to a file or P to print in the terminal.")
