from presence import DiscordPresence, Button
from time import sleep

presence = DiscordPresence("client_id")
presence.connect()

presence.update(
    details="Пример",
    start=None,
    large_image="photo",
    buttons=[
        Button(label="Пример", url="https://google.com")
    ]
)

while True:
    sleep(30)