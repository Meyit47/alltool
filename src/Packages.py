from time import sleep
from rich.console import Console

console = Console()
tasks = [f"veri {n}" for n in range(1, 3)]

with console.status("[koyu yeşil]Görevi ben gerçekleştiriyorum ...[/koyu yeşil]") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(0.4)
        console.log(f"{task} Tamamlandı!")
