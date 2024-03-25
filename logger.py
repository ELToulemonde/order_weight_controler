import logging

# Configuration du logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Création d'un objet logger
logger = logging.getLogger(__name__)
