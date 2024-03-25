import streamlit as st

from weight_controler_interface.api_interactions import get_command_list, send_control_command, get_employee_list

st.title("Vérification des commandes")
command_list = get_command_list()

selected_command_id = st.selectbox("Sélectionnez une commande ID :", command_list)

employee_list = get_employee_list()
selected_employee_id = st.selectbox("Sélectionnez un ID salarié :", employee_list)

if st.button("Vérifier"):
    result_status = send_control_command(selected_command_id, selected_employee_id)

    if result_status == "OK !":
        st.success("La commande a été vérifiée avec succès.")
    elif result_status == "NOT OK !":
        st.error("La vérification de la commande a échoué.")
    else:
        st.error("Erreur lors de la vérification de la commande.")
