from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text

with SB(uc=True, test=True) as sb:

    if True:
        url = "https://kick.com/brutalles"
        sb.uc_open_with_reconnect(url, 5)
        sb.uc_gui_click_captcha()
        sb.sleep(1)
        sb.uc_gui_handle_captcha()
        sb.sleep(1)
        if sb.is_element_present('button:contains("Accept")'):
            sb.uc_click('button:contains("Accept")', reconnect_time=4)
        if sb.is_element_visible('#injected-channel-player'):
            acasf = sb.get_new_driver(undetectable=True)
            acasf.uc_open_with_reconnect(url, 5)
            acasf.uc_gui_click_captcha()
            acasf.uc_gui_handle_captcha()
            sb.sleep(10)
            if acasf.is_element_present('button:contains("Accept")'):
                acasf.uc_click('button:contains("Accept")', reconnect_time=4)
            while sb.is_element_visible('#injected-channel-player'):
                sb.sleep(10)
            sb.quit_extra_driver()
    sb.sleep(1)
    if is_stream_online("brutalles"):
        url = "https://www.twitch.tv/brutalles"
        sb.uc_open_with_reconnect(url, 5)
        if sb.is_element_present('button:contains("Accept")'):
            sb.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            acasf = sb.get_new_driver(undetectable=True)
            acasf.uc_open_with_reconnect(url, 5)
            sb.sleep(10)
            if acasf.is_element_present('button:contains("Accept")'):
                acasf.uc_click('button:contains("Accept")', reconnect_time=4)
            while sb.is_element_visible(input_field):
                sb.sleep(10)
            sb.quit_extra_driver()
    sb.sleep(1)

