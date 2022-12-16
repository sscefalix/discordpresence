from presence import DiscordPresence, Button
from time import sleep

presence = DiscordPresence("1053209886898532362")
presence.connect()

presence.update(
    details="Я влюбился в неё..",
    start=None,
    large_image="photo",
    buttons=[
        Button(label='Иди нахуй', url="https://google.com")
    ]
)

while True:
    sleep(30)