import requests
import csv
import os
import time

output_folder = "output" 
os.makedirs(output_folder, exist_ok=True)

# list of chain_id values to replace
chain_ids = [
    'ETH', 'OPT', 'CRO', 'BSC', 'OKT', 'DAI', 'VEL', 'FUS', 'POL', 'FTM',
    'BOB', 'ERA', 'PZE', 'MOO', 'MOR', 'BAS', 'EVM', 'ARB', 'CEL', 'AVA',
    'AUR', 'ONE', 'LNA'
]

# common parameters for the URL without fromChain and toChain
base_url = ("https://partner-test.li.quest/v1/quote?fromToken=USDC&toToken=USDC&"
            "fromAddress=0xe0ebeDea0991EFc546F6a9D65a4fff883AeA8EB0&fromAmount=1000000000&order=RECOMMENDED")

headers = {"accept": "application/json"}

# create and write the responses to a single CSV file
csv_filename = os.path.join(output_folder, "target_merged_responses_usdc.csv")

with open(csv_filename, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["fromChain", "toChain", "response"])

    for from_chain in chain_ids:
        for to_chain in chain_ids:
            # create the URL with the current from_chain and to_chain values
            url = f"{base_url}&fromChain={from_chain}&toChain={to_chain}"

            # send the request
            response = requests.get(url, headers=headers)

            # write the response to the CSV file
            writer.writerow([from_chain, to_chain, response.text])

            print(f"Response for fromChain={from_chain} & toChain={to_chain} has been added to the merged CSV file")
            print("\n")

            time.sleep(1)

print(f"All responses have been merged into {csv_filename}")