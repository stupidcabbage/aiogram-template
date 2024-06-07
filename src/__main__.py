import logging
import sys

import uvicorn

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvicorn.run("src.server:app", host="0.0.0.0", port=8000)
