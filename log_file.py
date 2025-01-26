import logging

# Logging-Konfiguration
logging.basicConfig(
    level=logging.DEBUG,  # Log-Level einstellen
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log-Format
    handlers=[
        logging.FileHandler("app.log"),  # Logs in eine Datei schreiben
        logging.StreamHandler()  # Logs auf die Konsole ausgeben
    ]
)

logger = logging.getLogger(__name__)

def main():
    logger.debug("Dies ist eine Debug-Nachricht.")
    logger.info("Dies ist eine Info-Nachricht.")
    logger.warning("Dies ist eine Warnung.")
    logger.error("Dies ist ein Fehler.")
    logger.critical("Dies ist eine kritische Nachricht.")

if __name__ == "__main__":
    main()
