import sys
import time

from kik_unofficial.kikclient import KikClient
from kik_unofficial.utilities import Utilities


def main():
    username, password = "your_username", "your_password"
    kik_client = KikClient(username, password)
    user_info = kik_client.get_user_info()

    # getting information of chat partners
    chat_partners = []
    for username in user_info["chat_list"]:
        print("[+] Fetching info for friend '"+username+"'...")
        jid_info = kik_client.get_info_for_node(username)
        chat_partners.append(jid_info)
        Utilities.print_dictionary(jid_info)

    # let's talk
    username = "other_username"
    kik_client.send_is_typing(username, "true")
    time.sleep(0.5)
    kik_client.send_is_typing(username, "false")
    kik_client.send_message(username, "hi from bot!")

    print("[+] Done!")
    kik_client.close()


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3!!")
    try:
        main()
    except KeyboardInterrupt:
        print("[!] User stopped execution.")
