import argparse
import subprocess

# Custom host header
custom_host = "tg"

# Output file name
output_file = "output.txt"

# Create a command-line argument parser
parser = argparse.ArgumentParser(description="Subdomain Recon Tool")
parser.add_argument("subdomains_file", help="Path to the subdomains file")

# Parse the command-line arguments
args = parser.parse_args()

# Read subdomains from the specified file
with open(args.subdomains_file, "r") as file:
    subdomains = [line.strip() for line in file.readlines()]

# Open the output file for writing
with open(output_file, "w") as file:
    for subdomain in subdomains:
        # Construct the curl command
        curl_command = f"curl -H 'host:{custom_host}' {subdomain}"
        
        try:
            # Run the curl command and capture the output
            result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Write the output to the file
            file.write(f"Subdomain: {subdomain}\n")
            file.write(result.stdout)
            file.write("\n")
            
            # Print the result to the console
            print(f"Subdomain: {subdomain}")
            print(result.stdout)
            print("-" * 20)
        
        except Exception as e:
            # Handle any errors that occur during the curl command
            print(f"Error processing {subdomain}: {str(e)}")
