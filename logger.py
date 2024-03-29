import logging

# Configuration du logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(module)s - %(message)s')

# Création d'un logger
logger = logging.getLogger(__name__)
