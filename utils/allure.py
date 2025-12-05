import os
import requests
import allure
from dotenv import load_dotenv


load_dotenv()


def attach_bstack_video_android(session_id):

    bstack_session = requests.get(
        f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
        auth=(os.getenv("USER_NAME_BSTACK"), os.getenv("ACCESS_KEY_BSTACK")),
    ).json()

    video_url = bstack_session["automation_session"]["video_url"]

    allure.attach(
        "<html><body>"
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        "</video>"
        "</body></html>",
        name="video recording",
        attachment_type=allure.attachment_type.HTML,
    )
