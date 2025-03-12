import random
import argparse

def generate_webhook_url():

    id1 = "".join(random.choices("0123456789", k=20))
    id2 = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_", k=69))

    return f"https://discord.com/api/webhooks/{id1}/{id2}"

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="The number to generate", default=1, type=int)

args = parser.parse_args()

for _ in range(args.number):
    print(generate_webhook_url())
