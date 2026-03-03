import logging
from pathlib import Path

def setup_logging(log_file = "/logs/app.log"):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # To avoid duplicate logs :
    if logger.handlers:
        logger.handlers.clear()
    
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    file = logging.FileHandler(log_file, encoding='utf-8')
    file.setLevel(logging.WARNING)
    
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    
    console.setFormatter(fmt)
    file.setFormatter(fmt)
    
    logger.addHandler(console)
    logger.addHandler(file)
