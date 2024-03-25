import requests
import streamlit as st

from weight_controler_api.command_status import CommandStatus

# Fonction pour faire l'appel API et retourner le résultat
def call_api(command_id):
    url = f"http://0.0.0.0:8000/control?command_id={command_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["message"]
    else:
        return "Erreur lors de la requête API"

# Fonction pour faire l'appel API et récupérer la liste des command_ids
def get_command_ids():
    url = "http://0.0.0.0:8000/list_command"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[-4:]
    else:
        return []

# Fonction pour créer une nouvelle commande
def create_new_command():
    url = "http://0.0.0.0:8000/new_command"
    response = requests.post(url)


# Définition de l'application Streamlit
def main():
    st.title("Vérification de commande via API")

    # Onglets dans la sidebar
    app_mode = st.sidebar.radio("Choisissez une option", ["Vérifier une commande", "Créer une nouvelle commande"])

    if app_mode == "Vérifier une commande":
        # Récupérer la liste des command_ids
        command_ids = get_command_ids()

        # Selectbox pour choisir un command_id
        selected_command_id = st.sidebar.selectbox("Commande ID", command_ids)

        if st.sidebar.button("Vérifier"):
            if selected_command_id:
                status = call_api(selected_command_id)
                if status == CommandStatus.ok:
                    st.success("Commande OK")
                elif status == CommandStatus.not_ok:
                    st.error("Commande Pas OK")
                else:
                    st.warning("Statut inconnu")
            else:
                st.warning("Veuillez entrer un ID de commande valide")

    elif app_mode == "Créer une nouvelle commande":
        if st.sidebar.button("Créer une nouvelle commande") :

            create_new_command()

if __name__ == "__main__":
    main()
