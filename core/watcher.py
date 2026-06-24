from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from core.processor import processar_json
from utils.utils import esperar_arquivo_pronto


class MonitorHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.src_path.endswith(".json"):
            print(f"[NOVO JSON] {event.src_path}")
            
            esperar_arquivo_pronto(event.src_path)
            processar_json(event.src_path)


def iniciar_monitoramento(pasta):
    observer = Observer()
    handler = MonitorHandler()

    observer.schedule(handler, pasta, recursive=False)
    observer.start()

    print("Monitorando pasta de JSONs...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
