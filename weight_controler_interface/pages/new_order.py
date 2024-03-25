import streamlit as st
from weight_controler_interface.api_interactions import get_product_list

st.header("New Order")

# Obtention de la liste des produits
product_list = get_product_list()

# Sélection du produit à commander à l'aide d'un menu déroulant
selected_product = st.selectbox("Sélectionnez un produit :", product_list)

# Ajout de la quantité
quantity = st.number_input("Quantité", min_value=1, step=1)

# Bouton pour envoyer la commande
if st.button("Envoyer la commande"):
    # Logique pour envoyer la commande...
    st.success(f"Commande de {quantity} de {selected_product} envoyée avec succès.")

# Bouton pour ajouter une nouvelle commande
if st.button("Ajouter une commande"):
    # Réinitialisation des champs pour ajouter une nouvelle commande
    st.session_state.new_order = True