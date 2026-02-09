import streamlit as st
import pandas as pd
import os
import plotly.express as px
import numpy as np # Nécessaire pour les données de secours

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Portfolio Clarisse DEBERDT", page_icon="👩‍💻", layout="wide")

# --- STYLE CSS AVANCÉ (TOUT REGROUPÉ ICI) ---
st.markdown("""
    <style>
    /* 1. FOND ET STRUCTURE */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Sidebar avec distinction visuelle */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #E9ECEF;
    }

    /* 2. PHOTO DE PROFIL ANIMÉE (Seulement la première image tout en haut) */
    [data-testid="stSidebar"] > div > div > div > div:first-of-type img {
        width: 180px !important;
        height: 180px !important;
        border-radius: 50%;
        object-fit: cover;
        transition: transform 0.4s ease-in-out, border-color 0.4s ease-in-out;
        border: 3px solid #E8DAEF; 
        padding: 5px;
    }
    [data-testid="stSidebar"] > div > div > div > div:first-of-type img:hover {
        transform: scale(1.05) rotate(2deg);
        border-color: #9b59b6;
    }

    /* 3. BOUTONS INTERACTIFS */
    div.stButton > button, div.stDownloadButton > button, .stLinkButton > a {
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
        border: 1px solid #E0E0E0 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
    }
    div.stButton > button:hover, div.stDownloadButton > button:hover, .stLinkButton > a:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 12px rgba(155, 89, 182, 0.2) !important;
        border-color: #9b59b6 !important;
        color: #9b59b6 !important;
    }
            
    /* 4. CARTES INTERACTIVES (Méthodologie) */
    .custom-card {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #F0F2F6;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        height: 200px !important; 
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    
    .custom-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        border: 1.5px solid #9b59b6;
    }

    .card-title {
        color: #2D3436;
        font-weight: 700;
        margin-bottom: 15px;
        font-size: 1.1em;
        display: block;
    }
    
    .custom-card p {
        text-align: left; 
    }
            
    /* 5. BADGES DE COMPÉTENCES */
    .skill-badge {
        background-color: #f0f2f6;
        color: #31333F;
        padding: 6px 12px;
        border-radius: 8px;
        margin: 4px;
        display: inline-block;
        font-size: 0.9em;
        font-weight: 500;
        transition: all 0.3s ease;
        border: 1px solid transparent; 
        cursor: default;
    }
    .skill-badge:hover {
        background-color: #FFFFFF !important;
        color: #9b59b6 !important;
        border: 1px solid #9b59b6 !important;
        transform: scale(1.1);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    /* 6. CARTES DE PROJETS (Effet d'élévation) */
    [data-testid="stVerticalBlock"] > div > div[style*="border: 1px solid"] {
        transition: all 0.4s ease;
        border-radius: 15px !important;
        border: 1px solid #F0F2F6 !important;
        padding: 20px !important;
    }
    [data-testid="stVerticalBlock"] > div > div[style*="border: 1px solid"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.08);
        border-color: #D7BDE2 !important;
    }

    /* 7. CONTEXTE BOX (Interactif style Hard Skills) */
    .context-box {
        background-color: #F8F9FA;
        color: #31333F;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        transition: all 0.3s ease;
        border: 1px solid transparent;
        cursor: default;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    .context-box:hover {
        background-color: #FFFFFF !important;
        color: #9b59b6 !important;
        border: 1px solid #9b59b6 !important;
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .context-box:hover b, .context-box:hover i {
        color: #9b59b6 !important;
    }

/* 8. SÉCURITÉ DIPLÔMES (CORRECTION) */
    /* On cible spécifiquement les images DANS les expanders de la sidebar */
    [data-testid="stSidebar"] [data-testid="stExpander"] div[data-testid="stImage"] img {
        border-radius: 4px !important;
        transition: none !important;
        box-shadow: none !important;
        border: none !important;
        transform: none !important;
        
        /* C'est ici que la magie opère pour l'affichage correct */
        object-fit: contain !important; /* Affiche l'image entière sans couper */
        height: auto !important;        /* Hauteur automatique selon le ratio */
        width: 100% !important;         /* Largeur max du conteneur */
        max-height: 100%;
    }
    
    /* On bloque l'interaction au survol */
    [data-testid="stSidebar"] [data-testid="stExpander"] img:hover {
        transform: none !important;
        box-shadow: none !important;
        border: none !important;
    }

    /* TYPOGRAPHIE GLOBALE */
    h1, h2, h3 { color: #2D3436 !important; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)


# --- FONCTION POUR LES TITRES ---
def section_title(titre):
    st.markdown(f"""
    <div style="
        display: flex; 
        align-items: center; 
        margin-top: 40px; 
        margin-bottom: 20px;
    ">
        <span style="
            display: inline-block; 
            width: 6px; 
            height: 35px; 
            background-color: #9b59b6; 
            margin-right: 15px; 
            border-radius: 3px;
        "></span>
        <h2 style="
            margin: 0; 
            color: #2D3436; 
            font-size: 32px; 
            font-weight: 700;
        ">{titre}</h2>
    </div>
    """, unsafe_allow_html=True)

# --- FONCTION DE CHARGEMENT DES DONNÉES ---
@st.cache_data
def load_data():
    csv_path = "survey_results_public.csv"
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path, usecols=['Country', 'LanguageHaveWorkedWith', 'DatabaseHaveWorkedWith'])
    else:
        # DONNÉES DE SECOURS
        data = {
            'Country': np.random.choice(['United States of America', 'Germany', 'India', 'United Kingdom', 'France', 'Canada', 'Brazil', 'Poland', 'Netherlands', 'Italy'], 1000),
            'LanguageHaveWorkedWith': np.random.choice(['Python;SQL;HTML/CSS', 'JavaScript;HTML/CSS', 'Python;R', 'Java;Kotlin', 'C#;SQL', 'TypeScript;JavaScript'], 1000),
            'DatabaseHaveWorkedWith': np.random.choice(['PostgreSQL;MySQL', 'MongoDB', 'Microsoft SQL Server', 'SQLite', 'Redis;PostgreSQL', 'DynamoDB'], 1000)
        }
        return pd.DataFrame(data)

# --- SIDEBAR ---
with st.sidebar:
    if os.path.exists("image_moi_linkedin.png"):
        st.image("image_moi_linkedin.png") 
    else:
        st.write("(Image de profil ici)")

    st.markdown("<h2 style='text-align: center; color: #9b59b6; margin-top: -10px;'>Clarisse DEBERDT</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.1em;'><b>🎓Future Etudiante Master Data Analytics<br><span style='color: #9b59b6;'>Septembre 2026</span></b></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.8;'>📍 Paris, France 🇫🇷</p>", unsafe_allow_html=True)
    
    st.link_button("✉️ Me contacter", "mailto:c.deberdt.lefebvre@gmail.com", use_container_width=True)
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/clarisse-deberdt/", use_container_width=True)
    st.link_button("🐙 GitHub", "https://github.com/clarissedeberdt", use_container_width=True)
    
    if os.path.exists("CV_Clarisse_Deberdt.pdf"):
        with open("CV_Clarisse_Deberdt.pdf", "rb") as pdf_file:
            st.download_button(label="📄 Télécharger mon CV", data=pdf_file, file_name="CV_Clarisse_Deberdt.pdf", mime="application/pdf", use_container_width=True)
    
    st.write("---")
    
    # --- SKILLS ---
    st.markdown("### 🛠️ Hard Skills")
    hard_skills = ["Python", "Excel", "PowerBI", "Looker Studio", "SQL", "LLMs", "Plotly", "Seaborn", "Matplotlib", "Pandas"]
    html_hard = "".join([f'<span class="skill-badge">{s}</span>' for s in hard_skills])
    st.markdown(html_hard, unsafe_allow_html=True)

    st.markdown("### 🧠 Soft Skills")
    soft_skills = ["Communication", "Curieuse", "Autonome", "Esprit d'analyse", "Rigueur", "Esprit d'équipe"]
    html_soft = "".join([f'<span class="skill-badge">{s}</span>' for s in soft_skills])
    st.markdown(html_soft, unsafe_allow_html=True)

    # --- LANGUES ---
    st.caption("🌐 **Anglais** (Niveau B2/C1)") 

    st.write("---")

    # --- DIPLÔMES ---
    st.subheader("🎓 Diplômes & Certifications")
    
    # IBM
    st.markdown("**IBM Data Analyst (déc. 2025)** 🔗 [Voir le certificat](https://www.coursera.org/account/accomplishments/specialization/HN9P6HM29J5Q)")
    
    if os.path.exists("certificat_IBM.png"):
        with st.expander("Voir la capture"):
            st.image("certificat_IBM.png")
    elif os.path.exists("certificat_IBM.jpg"):
        with st.expander("Voir la capture"):
            st.image("certificat_IBM.jpg")

    st.write("") 

    # KEDGE
    st.markdown("**Bachelor International - KEDGE Business School (2022 - 2025)**")
    
    if os.path.exists("Clarisse_Deberdt_Diplome_Kedge.png"):
        with st.expander("Voir le diplôme"):
            st.image("Clarisse_Deberdt_Diplome_Kedge.png")
    elif os.path.exists("Clarisse_Deberdt_Diplome_Kedge.jpg"):
        with st.expander("Voir le diplôme"):
            st.image("Clarisse_Deberdt_Diplome_Kedge.jpg")


# --- PAGE PRINCIPALE ---
st.markdown("""
    <h1>Hello, moi c'est <span style="background: linear-gradient(to right, #9b59b6, #dc2430); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Clarisse</span> ! 👋</h1>
    """, unsafe_allow_html=True)

st.markdown("""
**Ma conviction ?** Un tableau de bord que personne ne comprend, c'est comme s'il **n'existait pas**.

🚀 **Future Data / Business Analyst (Master Data)**, je ne me contente pas de créer des graphiques : je fais parler les données pour raconter leur histoire et anticiper l'avenir.

Alliant **rigueur technique**, **enthousiasme naturel** et **dynamisme** ☀️, je cherche à rejoindre une équipe bienveillante pour avoir un impact concret.

**📅 Objectif :** Alternance dès Septembre 2026 pour une durée de 24 mois.

<br>
<small style="color: #636E72;">PS : Le <b>sourire</b> et la <b>bonne humeur</b> font partie de ma façon de travailler 😄</small>
""", unsafe_allow_html=True)


st.write("---")

# --- MÉTHODOLOGIE ---
section_title("Ma Méthodologie")

cols = st.columns(4)
steps = [
    ("1. Cadrer 🎯", "Je définis la destination et les objectifs. Cela me permet de savoir où aller et comment explorer les données ensuite."),
    ("2. Nettoyer 🧹", "Ici, je prépare et nettoie les données avec Excel et Pandas (valeurs manquantes, formats, cohérence...)."),
    ("3. Analyser 🔎", "J'explore ensuite les données avec Python pour faire ressortir les tendances et comprendre ce que les chiffres racontent."),
    ("4. Restituer 📊", "Enfin, je transforme les analyses en visuels clairs avec différentes bibliothèques (Plotly, Seaborn, Matplotlib).")
]

for i, col in enumerate(cols):
    with col:
        st.markdown(f"""
        <div class="custom-card">
            <span class="card-title">{steps[i][0]}</span>
            <p style="font-size: 0.9em; color: #636E72; line-height: 1.4;">
                {steps[i][1]}
            </p>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

section_title("Mes Projets Data")

# --- CONTEXTE & DOWNLOAD ---
try:
    df = load_data()
    nb_lignes = df.shape[0]
    
    st.markdown(f"""
    <div class="context-box">
        <b>Contexte :</b> Les analyses suivantes sont basées sur le dataset public <i>StackOverflow Developer Survey</i> (64,000 lignes).
        L'objectif est de détecter les tendances du marché Tech actuel.
    </div>
    """, unsafe_allow_html=True)

    if os.path.exists("survey_data.zip"):
        with open("survey_data.zip", "rb") as file:
            st.download_button(
                label="📥 Télécharger les données sources (.zip)",
                data=file,
                file_name="survey_data.zip",
                mime="text/zip"
            )

except Exception as e:
    st.error(f"Erreur de chargement des données : {e}")

st.write("") 

# ==========================================
# PROJET 1 : LANGAGES
# ==========================================
with st.container(border=True):
    st.subheader("📊 Projet 1 : Tendances Tech par Pays")
    
    st.write("L'objectif est de comparer les langages utilisés dans les principaux hubs technologiques mondiaux pour orienter une stratégie de recrutement.")
    st.markdown("**❓ Question : Existe-t-il des spécificités géographiques dans l'adoption des langages Data ?**")

    if 'df' in locals():
        # TRAITEMENT PANDAS
        df_clean = df[['Country', 'LanguageHaveWorkedWith']].dropna()
        top_countries = df_clean['Country'].value_counts().nlargest(10).index
        df_filtered = df_clean[df_clean['Country'].isin(top_countries)].copy()
        df_filtered['Language'] = df_filtered['LanguageHaveWorkedWith'].str.split(';')
        df_exploded = df_filtered.explode('Language')
        top_langs = df_exploded['Language'].value_counts().nlargest(10).index
        df_final = df_exploded[df_exploded['Language'].isin(top_langs)]

        # --- PALETTE DE VIOLETS DOUX ---
        pastel_purples = [
            '#E0B0FF', '#D8BFD8', '#DDA0DD', '#DA70D6', '#BA55D3', 
            '#9932CC', '#9400D3', '#8A2BE2', '#800080', '#4B0082'
        ]

        # VISUALISATION PLOTLY
        fig1 = px.histogram(df_final, x='Country', color='Language', 
                            barmode='group', 
                            color_discrete_sequence=pastel_purples, 
                            title="Top 10 Langages par Pays")
        
        fig1.update_layout(xaxis_title="Pays", yaxis_title="Développeurs", plot_bgcolor="white")
        st.plotly_chart(fig1, use_container_width=True)
        
        with st.expander("👉 Voir le code Python (Plotly)"):
            st.code("""
# Étape 1 :  je me concentre sur l’essentiel 
df_filtered = df[df['Country'].isin(top_10_countries)]

# Étape 2 : je remets les données à plat 
df_final = df_filtered.assign(Language=df['LanguageHaveWorkedWith'].str.split(';')).explode('Language')

# Étape 3 : création d'une visualisation claire et interactive 
fig = px.histogram(df_final, x='Country', color='Language', barmode='group', title="Top 10 Langages par Pays")
fig.show()
            """, language="python")

    st.success("✅ **Insight :** Si le Web (HTML/JS) est partout, Python domine nettement aux USA, en Inde et en Allemagne, confirmant leur statut de leaders en IA.")


# ==========================================
# PROJET 2 : BASES DE DONNÉES
# ==========================================
with st.container(border=True):
    st.subheader("💾 Projet 2 : SQL vs NoSQL")
    
    st.write("Analyse des technologies de stockage pour déterminer si le SQL reste la norme incontournable.")
    st.markdown("**❓ Question : Quelles sont les bases de données les plus utilisées aujourd'hui ?**")

    if 'df' in locals():
        # TRAITEMENT
        database_counts = df['DatabaseHaveWorkedWith'].str.split(';', expand=True).stack().value_counts().head(15)
        df_db = database_counts.reset_index()
        df_db.columns = ['Base de Données', 'Nombre']

        # VISUALISATION PLOTLY
        fig2 = px.bar(df_db, x='Base de Données', y='Nombre', 
                      title="Top 15 Bases de Données",
                      color_discrete_sequence=['#B39DDB']) 
        
        fig2.update_layout(xaxis_title="Technologie", yaxis_title="Répondants", plot_bgcolor="white")
        st.plotly_chart(fig2, use_container_width=True)
        
        with st.expander("👉 Voir le code Python (Plotly)"):
            st.code("""
# Étape 1 : comprendre quelles bases de données sont les plus utilisées 
db_counts = df['DatabaseHaveWorkedWith'].str.split(';', expand=True).stack().value_counts().head(15)

# Étape 2 : préparation des données pour la visualisation 
df_db = db_counts.reset_index()

# Étape 3 : création d'un graphique clair et lisible 
fig = px.bar(df_db, x='Base de Données', y='Nombre', title="Top 15 Bases de Données")
fig.show()
            """, language="python")

    st.success("✅ **Insight :** Le SQL reste roi (PostgreSQL/MySQL > 45%). Cependant MongoDB s'impose comme la première alternative NoSQL majeure, confirmant son évolution croissante.")

st.write("")
st.write("")

# Titre Principal de la section
section_title("Mes Passions")

st.markdown("""
<div style="text-align: left; font-style: italic;">
    Lorsque je ne suis pas entrain de faire parler les données, je pars explorer le monde, faire du sport, ou écouter de la musique. Pour en apprendre un peu plus sur moi, voici un retour en images de mes passions sous formes de visualisations interactives.
</div>
""", unsafe_allow_html=True)

st.write("") # Espace

# CRÉATION DES ONGLETS (Voyage | Sport | Musique)
tab1, tab2, tab3 = st.tabs(["🌍 Data Trotter", "🏅 Sport Analytics", "🎵 Music Data"])

# --- ONGLET 1 : VOYAGE ---
with tab1:
    st.subheader("🗺️ Mapping de mes explorations")
    
    st.markdown("""
    <div style="text-align: left;">
        <p>
            Chaque point sur cette carte raconte une histoire. J'utilise ici une carte choroplèthe pour visualiser 
            mes voyages passés et... mes futures destinations. <b> Passe la souris dessus !😉</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 1. Préparation des données
    data_voyage = [
        {"Pays": "France", "Statut": "J'y vis 📍", "Détails": "France Métropolitaine (Paris, Bordeaux...)"},
        {"Pays": "French Polynesia", "Statut": "Visité 🎒", "Détails": "Tahiti, Moorea, Huahine, Bora Bora..."},
        {"Pays": "Guadeloupe", "Statut": "Visité 🎒", "Détails": "Pointe-à-Pitre et exploration de l'île"},
        {"Pays": "Martinique", "Statut": "Visité 🎒", "Détails": "Fort-de-France, St Pierre, St Anne"},
        {"Pays": "Spain", "Statut": "J'y ai vécu 🏠", "Détails": "Madrid (6 mois), Alicante"},
        {"Pays": "Italy", "Statut": "Visité 🎒", "Détails": "Palerme (Sicile)"},
        {"Pays": "Greece", "Statut": "Visité 🎒", "Détails": "Athènes, Égine"},
        {"Pays": "United Kingdom", "Statut": "Visité 🎒", "Détails": "Londres"},
        {"Pays": "Albania", "Statut": "Visité 🎒", "Détails": "Durres, Tirana"},
        {"Pays": "Switzerland", "Statut": "Road Trip Europe 👍", "Détails": "Zurich (Autostop - KET 2025)"},
        {"Pays": "Austria", "Statut": "Road Trip Europe 👍", "Détails": "Salzbourg (Autostop - KET 2025)"},
        {"Pays": "Czech Republic", "Statut": "Road Trip Europe 👍", "Détails": "Prague (Autostop - KET 2025)"},
        {"Pays": "Germany", "Statut": "Road Trip Europe 👍", "Détails": "Francfort (Autostop - KET 2025)"},
        {"Pays": "Netherlands", "Statut": "Road Trip Europe 👍", "Détails": "Amsterdam (Autostop - KET 2025)"},
        {"Pays": "Morocco", "Statut": "Visité 🎒", "Détails": "Tanger"},
        {"Pays": "Saint Lucia", "Statut": "Visité 🎒", "Détails": "Voyage aux Antilles"},
        {"Pays": "Dominica", "Statut": "Visité 🎒", "Détails": "Voyage aux Antilles"},
        {"Pays": "South Korea", "Statut": "Visité 🎒", "Détails": "Séoul"},
        {"Pays": "Japan", "Statut": "Visité 🎒", "Détails": "Kyoto, Hiroshima, Okinawa, Beppu, Miyajima..."},
        {"Pays": "Philippines", "Statut": "Prochainement ✈️", "Détails": "Objectif : Road trip de 3 mois"},
        {"Pays": "Indonesia", "Statut": "Prochainement ✈️", "Détails": "Objectif : Raja Ampat (env. 2 mois)"},
        {"Pays": "Canada", "Statut": "Prochainement ✈️", "Détails": "Objectif : Montréal"}
    ]

    df_voyage = pd.DataFrame(data_voyage)

    # 2. Carte Plotly
    fig_map = px.choropleth(
        df_voyage,
        locations="Pays",
        locationmode='country names',
        color="Statut", 
        hover_name="Pays",
        hover_data={"Statut": True, "Détails": True, "Pays": False}, 
        color_discrete_map={
            "J'y vis 📍": "#B39DDB",          # Violet Pastel
            "J'y ai vécu 🏠": "#D7BDE2",      # Mauve très clair
            "Visité 🎒": "#A9DFBF",           # Vert Menthe Pastel
            "Road Trip Europe 👍": "#AED6F1", # Bleu très pâle
            "Prochainement ✈️": "#F5B7B1"     # Corail Pastel (Futur)
        },
        projection="natural earth"
    )

    fig_map.update_geos(
        showcountries=True, countrycolor="#d1d1d1",
        showcoastlines=True, coastlinecolor="#d1d1d1",
        showland=True, landcolor="#f5f5f5", 
        showocean=True, oceancolor="#ffffff"
    )

    fig_map.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor='rgba(0,0,0,0)', 
        showlegend=True,
        legend=dict(y=0.05, x=0.05, bgcolor="rgba(255,255,255,0.9)", title=None),
        geo=dict(bgcolor='rgba(0,0,0,0)') 
    )

    st.plotly_chart(fig_map, use_container_width=True)
    
    with st.expander("🚙 Détails sur mon tour de l'Europe en auto-stop avec 1€/jour"):
        st.markdown("""
        <div style="text-align: left;">
            <p>
                <b>Le Challenge :</b> 8 jours, 6 pays traversés, et seulement 1€ par jour ! Inspiré de Pékin Express, 
                ce défi solidaire organisé par l'association <i>Adrénaline Kedge Bordeaux</i> m'a poussée dans mes retranchements.
            </p>
            <p>
                <b>L'itinéraire :</b> Bordeaux → Lyon → Zurich → Salzbourg → Prague → Amsterdam → Paris → Bordeaux.
            </p>
            <p>    
                <b>La Mission :</b> Nous avons avancé uniquement en auto-stop, 
                en négociant hébergement et nourriture chaque soir. Mais au-delà de l'aventure sportive, 
                ce projet était avant tout un <b>défi à but caritatif</b> : nous avons récolté des fonds pour <b>Life ONG</b> 
                afin de lutter contre la pauvreté.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("🚀 Clique ici afin de voir le récit complet de ce projet dingue ainsi que les photos (LinkedIn)", "https://www.linkedin.com/feed/update/urn:li:activity:7300911140312616960/")

# --- ONGLET 2 : SPORT ---
with tab2:
    st.subheader("🏅 Sport Analytics : Mon équilibre")
    
    st.markdown("""
    <div style="text-align: left;">
        <p>
            Le sport… le sport… le sport ! C'est bien plus qu'une activité, c'est ma façon de me dépasser, 
            de gérer le stress et la pression, et surtout d'apprendre l'esprit d'équipe. 
        </p>
    </div>
    """, unsafe_allow_html=True)

    data_sport = {
        'Sport': ['Handball 🤾‍♀️', 'Musculation 🏋️‍♀️', 'Course à pied 🏃‍♀️'],
        'Part': [50, 25, 25]
    }
    df_sport = pd.DataFrame(data_sport)

    fig_sport = px.pie(
        df_sport, 
        values='Part', 
        names='Sport',
        hole=0.5,
        color_discrete_sequence=['#B39DDB', '#A9DFBF', '#AED6F1']
    )

    fig_sport.update_traces(
        textinfo='percent',    
        textposition='inside', 
        textfont_size=14,      
        marker=dict(line=dict(color='#FFFFFF', width=2))
    )
    
    fig_sport.update_layout(
        showlegend=True,       
        legend=dict(
            orientation="h",   
            yanchor="bottom",
            y=-0.2,            
            xanchor="center",
            x=0.5
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin={"r":0,"t":20,"l":0,"b":50} 
    )

    st.plotly_chart(fig_sport, use_container_width=True)

    st.info("💡 **Le Handball** reste ma discipline de cœur, celle qui m'a appris l'esprit d'équipe et la stratégie. La musculation et la course viennent compléter ma préparation physique.")

# --- ONGLET 3 : MUSIQUE ---
with tab3:
    st.subheader("🎵 Analyse de ma Rétrospective Spotify 2025")
    
    st.markdown("""
    <div style="text-align: left;">
        <p>
            Avec près de <b>80 000 minutes</b> d'écoute cette année, la musique est vraiment mon moteur. 
            Besoin de me concentrer ? J'écoute du Néo-classique. Besoin de dynamisme ? J'écoute de l'Électro et de la Pop pour donner le rythme à ma journée.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temps d'écoute", "79 865 min", "soit 55 jours 🤯")
    col2.metric("Artistes Uniques", "2 886", "Découverte")
    col3.metric("Top Artiste", "L. Einaudi", "Top 0.03% Monde")
    col4.metric("Titres Uniques", "4 826", "Diversité")

    st.write("---")

    c1, c2 = st.columns([1, 1])

    with c1:
        st.markdown("**🎹 Top 5 Genres : L'équilibre Focus / Énergie**")
        df_genres = pd.DataFrame({
            'Genre': ['Néo-classique', 'Électro', 'Pop-rap', 'Pop française', 'Pop'],
            'Classement': [1, 2, 3, 4, 5],
            'Importance': [90, 75, 60, 50, 40] 
        })

        fig_genre = px.bar(
            df_genres, 
            x='Importance', 
            y='Genre', 
            orientation='h',
            text='Genre',
            color='Genre',
            color_discrete_sequence=['#B39DDB', '#FFAB91', '#AED6F1', '#A9DFBF', '#F9E79F'] 
        )
        
        fig_genre.update_layout(
            showlegend=False,
            xaxis_visible=False, 
            yaxis_visible=False, 
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=250
        )
        fig_genre.update_traces(textposition='inside', textfont_size=14)
        st.plotly_chart(fig_genre, use_container_width=True)

    with c2:
        st.markdown("**🏆 La part de Ludovico Einaudi**")
        ludo_min = 8343
        total_min = 79865
        autres_min = total_min - ludo_min
        
        df_ludo = pd.DataFrame({
            'Artiste': ['Ludovico Einaudi', 'Autres Artistes'],
            'Minutes': [ludo_min, autres_min]
        })

        fig_ludo = px.pie(
            df_ludo, 
            values='Minutes', 
            names='Artiste', 
            hole=0.6,
            color_discrete_sequence=['#4B0082', '#E0E0E0'] 
        )

        fig_ludo.update_layout(
            showlegend=True,
            legend=dict(orientation="h", y=-0.1),
            margin=dict(l=0, r=0, t=20, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=250,
            annotations=[dict(text=f"{int(ludo_min/total_min*100)}%", x=0.5, y=0.5, font_size=20, showarrow=False)]
        )
        st.plotly_chart(fig_ludo, use_container_width=True)

    st.write("")
    with st.expander("👉 Derrière les chiffres : comment SQL m’a permis de trouver mon artiste préféré"):
        st.write("""
        Pour obtenir mon temps d'écoute total et identifier mon artiste n°1, j'utilise ici les fondamentaux de l'analyse SQL : 
        l'agrégation (`SUM`, `COUNT`) et le regroupement (`GROUP BY`).
        """)
        
        st.code("""
-- Objectif : Trouver l'artiste le plus écouté et le temps total
SELECT 
    artist_name,
    COUNT(track_id) AS nombre_titres,
    SUM(duration_ms) / 60000 AS minutes_totales
FROM listen_history
WHERE year = 2025
GROUP BY artist_name
ORDER BY minutes_totales DESC
LIMIT 1;
        """, language="sql")
        
        st.caption("Une requête simple mais efficace pour extraire des tendances à partir de données brutes.")

# ==========================================
# FOOTER (Message personnel)
# ==========================================
st.write("---")

st.markdown("""
<div style="text-align: center; color: #636E72; font-size: 0.9em; font-style: italic;">
    <p>
        Ce portfolio a été codé avec passion, en alliant mes compétences techniques, ma curiosité autodidacte et l'assistance de l'Intelligence Artificielle. 🦾💜<br>
        Une preuve que l'humain et la machine peuvent collaborer pour créer de belles choses.
    </p>
    <p>
        © 2025 Clarisse Deberdt · Fait avec ❤️.
    </p>
</div>
""", unsafe_allow_html=True)