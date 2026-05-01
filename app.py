import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import random

# Configuration
st.set_page_config(page_title="Vœux 1er Mai - SCSM Group", page_icon="💡")

# --- FONCTIONS DE GÉNÉRATION ---

def generer_poeme(label, theme):
    templates = {
        "Scientifique": [
            f"Dans l'algorithme du succès, {label} calcule votre bonheur.",
            "Que vos efforts convergent vers une réussite exponentielle.",
            "L'excellence est une constante, votre travail en est la variable clé."
        ],
        "Inspirant": [
            f"Bâtir l'avenir avec {label}, c'est transformer chaque effort en victoire.",
            "Le travail est le pinceau qui dessine les plus beaux lendemains.",
            "À vous qui forgez le monde, recevez notre plus profonde gratitude."
        ]
    }
    return random.choice(templates[theme])

def creer_carte_visuelle(label, destinataire, message):
    # Création d'une image simple (800x400)
    img = Image.new('RGB', (800, 450), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Couleurs du groupe (Bleu et Gris)
    d.rectangle([0, 0, 800, 10], fill="#2E86C1") # Barre décorative
    
    # Ajout du texte (Note : Pour des polices spécifiques, il faudrait charger un .ttf)
    try:
        d.text((50, 80), f"Fête du Travail 2026", fill="#2E86C1")
        d.text((50, 150), f"À l'attention de : {destinataire}", fill="black")
        d.text((50, 220), f"\"{message}\"", fill="#555555")
        d.text((50, 350), f"Signé : {label} (SCSM Group)", fill="#2E86C1")
    except:
        d.text((50, 80), "Bonne fête du Travail !", fill="black")

    # Sauvegarde en mémoire
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im

# --- INTERFACE UTILISATEUR ---

st.title("🎨 Générateur de Vœux Lab_Math & Co")

col1, col2 = st.columns(2)

with col1:
    label_choisi = st.selectbox("Émetteur :", ["Lab_Math", "SCSM Group", "CIE", "Doloprint"])
    nom_dest = st.text_input("Destinataire :", "Cher Collaborateur")

with col2:
    style = st.radio("Style du poème :", ["Scientifique", "Inspirant"])

if st.button("Générer mon message et ma carte"):
    poeme = generer_poeme(label_choisi, style)
    
    # Affichage du poème
    st.info(f"**Votre message personnalisé :** \n\n {poeme}")
    
    # Création et affichage du visuel
    img_data = creer_carte_visuelle(label_choisi, nom_dest, poeme)
    st.image(img_data, caption="Aperçu de votre carte de vœux")
    
    # Bouton de téléchargement
    st.download_button(
        label="📥 Télécharger la carte (PNG)",
        data=img_data,
        file_name=f"Voeux_1erMai_{label_choisi}.png",
        mime="image/png"
    )

st.markdown("---")
st.caption("Propulsé par Lab_Math | Excellence & Innovation 2026")