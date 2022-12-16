from datetime import datetime
from fastapi import Request


def log(tag="MyApp", message="no message", request: Request = None):
    with open("log.txt", "a+") as log:
        log.write(f"[{datetime.now()}] {tag}: {message}\n")
        log.write(f"\t{request.url}\n")
