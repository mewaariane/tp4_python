from mewa import DiscordClient
import os
from dotenv import load_dotenv
import logging

from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
    parser.add_argument(
        "-l", "--logfile", help="Log file", required=True
    )
    return parser.parse_args()

def main():
    parser = parse_args()
    load_dotenv(dotenv_path=parser.config)
    logging.basicConfig(
        filename=parser.logfile,
        format='%(asctime)s -- %(message)s --',
        datefmt='%m/%d/%Y %I:%M:%S',
        encoding='utf-8', 
        level=logging.WARN
    )
    client = DiscordClient()
    client.run(os.getenv("TOKEN"))    

if __name__ == "__main__":
    main()