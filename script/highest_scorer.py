import requests
import argparse


SLEEPER_API = "https://docs.sleeper.com/"

def get_call():
    x = requests.get('https://w3schools.com')
    league_info = requests.get('https://api.sleeper.app/v1/league/872554216374337536/')
    league_users = requests.get('https://api.sleeper.app/v1/league/872554216374337536/users')
    print(league_users.text)




def main():
    print("HELLO")
    get_call()