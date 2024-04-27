import random
from datetime import datetime

async def generate_signal() -> (str, str):
    percent = random.randint(7000, 9500) / 100
    game = random.randint(19999, 99999)
    images = ['resources/signals/left.JPG', 'resources/signals/mid.JPG', 'resources/signals/right.JPG']
    img = random.choice(images)
    time = datetime.now().strftime("%d.%m.%Y %H:%M")
    signal_string = ""
    if img == 'resources/signals/left.JPG':
        signal_string = 'Caiu: Crânio Esquerdo'
    if img == 'resources/signals/mid.JPG':
        signal_string = "Caiu: Caveira no meioе"
    elif img == 'resources/signals/right.JPG':
        signal_string = "Caiu: Crânio Direito"
    result_string = (f"💀 Um jogo №{game}\n"
                     f"🕓 {time}\n"
                     f"{signal_string}\n\n"
                     f"Chance - {percent}%\n\n")

    return result_string, img


