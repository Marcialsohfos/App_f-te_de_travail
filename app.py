import streamlit as st
import random
from datetime import datetime
import base64

# Configuration de la page
st.set_page_config(
    page_title="Bonne Fête du Travail - Lab_Math",
    page_icon="👷",
    layout="centered"
)

# CSS personnalisé pour le style
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .wish-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        animation: fadeIn 0.8s ease-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .team-badge {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 10px 20px;
        border-radius: 50px;
        display: inline-block;
        margin: 5px;
    }
    h1 {
        text-align: center;
        color: white;
        font-size: 3em;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .footer {
        text-align: center;
        color: white;
        margin-top: 50px;
        padding: 20px;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Titre
st.markdown("<h1>👷‍♂️ Bonne Fête du Travail 👷‍♀️</h1>", unsafe_allow_html=True)

# Carte principale
with st.container():
    st.markdown("""
    <div class="wish-card">
        <div style="text-align: center; margin-bottom: 20px;">
            <span class="team-badge">📊 Lab_Math</span>
            <span class="team-badge">🏢 SCSM Group</span>
            <span class="team-badge">🔬 CIE</span>
            <span class="team-badge">🖨️ Doloprint</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Liste des souhaits
    wishes = [
        "🌟 Que ce 1er mai vous apporte reconnaissance et fierté pour tout ce que vous construisez chaque jour. Votre travail est la pierre angulaire de notre succès collectif.",
        "💡 Au-delà des algorithmes et des modèles, c'est votre passion qui fait la différence. Bonne fête du travail à toute l'équipe !",
        "⚡ Chaque ligne de code, chaque calcul, chaque innovation mérite d'être célébrée. Merci pour votre engagement exceptionnel !",
        "🎯 Le travail n'est pas seulement une activité, c'est une contribution au progrès. Bravo pour votre dévouement au quotidien.",
        "🌺 En ce 1er mai, prenez le temps de reconnaître la valeur de votre travail. Vous êtes l'énergie qui fait avancer Lab_Math et SCSM Group.",
        "🔬 Des modèles mathématiques aux réalisations concrètes, votre travail transforme les idées en réalité. Bonne fête à tous !"
    ]
    
    # Session state pour garder le souhait actuel
    if 'current_wish' not in st.session_state:
        st.session_state.current_wish = random.choice(wishes)
    
    # Affichage du souhait
    st.markdown(f"""
    <div style="text-align: center; font-size: 1.3em; line-height: 1.6; color: #555; margin: 30px 0;">
        <span style="font-size: 2em; color: #764ba2;">"</span><br>
        {st.session_state.current_wish}<br>
        <span style="font-size: 2em; color: #764ba2;">"</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Boutons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✨ Nouveau souhait", use_container_width=True):
            st.session_state.current_wish = random.choice(wishes)
            st.rerun()
    with col2:
        if st.button("📤 Partager", use_container_width=True):
            st.info("Sélectionnez et copiez le texte ci-dessus pour le partager !")
    with col3:
        st.markdown(f"""
        <div style="text-align: center;">
            <span style="font-size: 2em;">🎉</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Pied de page
st.markdown("""
<div class="footer">
    <hr style="border-color: rgba(255,255,255,0.3);">
    🌟 Merci à tous les travailleurs pour votre dévouement 🌟<br>
    <small>© 2024 SCSM Group - Lab_Math - CIE - Doloprint | 1er Mai</small>
</div>
""", unsafe_allow_html=True)

# Affichage de la date
current_date = datetime.now().strftime("%d %B %Y")
st.sidebar.success(f"📅 {current_date}")
st.sidebar.info("""
### À tous les travailleurs,

Prenez un moment pour célébrer vos accomplissements.
Votre travail a de la valeur et fait la différence !

💪 **Continuez à innover**  
🎯 **Restez passionnés**  
🌟 **Soyez fiers de vous**

---
*L'équipe Lab_Math*
""")