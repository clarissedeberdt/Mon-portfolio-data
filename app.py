import streamlit as st
import pandas as pd
import os
import plotly.express as px

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Portfolio Clarisse DEBERDT", page_icon="👩‍💻", layout="wide")

# --- STYLE CSS (Minimaliste) ---
import streamlit as st
import os

# --- STYLE CSS ---
st.markdown("""
    <style>
    /* Fond blanc pour l'application et la sidebar */
    .stApp { background-color: #FFFFFF !important; }
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; }
    
    /* 1. CIBLAGE DE LA PHOTO DE PROFIL UNIQUEMENT */
    /* On vise la première image de la sidebar pour la mettre en rond et centrée */
    [data-testid="stSidebar"] > div > div > div > div:first-of-type img {
        border-radius: 50%;
        object-fit: cover; 
        aspect-ratio: 1 / 1;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* 2. CIBLAGE DES CERTIFICATS (DANS LES EXPANDERS) */
    /* On force les images dans les menus déroulants à rester rectangulaires */
    [data-testid="stSidebar"] [data-testid="stExpander"] img {
        border-radius: 5px !important; /* Juste des coins légèrement arrondis */
        object-fit: contain !important; /* Affiche l'image entière sans couper */
        aspect-ratio: auto !important;
    }

    h1, h2, h3, p, li { color: #2D3436 !important; }
    
    /* Style context box */
    .context-box {
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #E9ECEF;
        margin-bottom: 20px;
        color: #636E72;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    # --- PROFIL (CENTRÉ) ---
    st.image("https://media.licdn.com/dms/image/v2/D4E35AQEMFKPL7yzGLQ/profile-framedphoto-shrink_400_400/B4EZtpe9faIUAc-/0/1767001282768?e=1767607200&v=beta&t=bOdj3kRoVQKPDZnjvE5GEVcB5aE54QMZX08QpFvQHFw", width=180) 
    
    # Texte centré via HTML comme demandé
    st.markdown("<h2 style='text-align: center; color: #0083B0;'>Clarisse DEBERDT</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><b>Future Data Analyst 📊<br>Recherche d'une alternance pour Septembre 2026 !</b></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>📍Paris, France 🇫🇷</p>", unsafe_allow_html=True)
    
    # Boutons (prennent la largeur, donc "centrés" visuellement)
    st.link_button("✉️ Me contacter", "mailto:c.deberdt.lefebvre@gmail.com", use_container_width=True)
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/clarisse-deberdt/", use_container_width=True)
    st.link_button("🐙 GitHub", "https://github.com/clarissedeberdt", use_container_width=True)
    
    # BOUTON CV (Indispensable)
    with open("CV_Clarisse_Deberdt.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Télécharger mon CV",
            data=pdf_file,
            file_name="CV_Clarisse_Deberdt.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    st.write("---")
    
    # --- HARD SKILLS (ALIGNÉS À GAUCHE) ---
    # Retour à l'alignement par défaut (gauche) pour la lisibilité
    st.markdown("### 🛠️ Compétences Techniques")
    
    st.write("🐍 Python · 🐼 Pandas")
    st.write("💾 SQL · 💚 Excel")
    st.write("📊 PowerBI · ⚙️ Automatisation")
    st.write("📈 Plotly · 🎨 Seaborn")
    
    st.write("---")

    # --- SOFT SKILLS (ALIGNÉS À GAUCHE) ---
    st.markdown("### 🧠 Soft Skills")
    st.write("🗣️ Communication")
    st.write("🧐 Esprit Analytique & Résolution de problèmes")
    st.write("💡 Curiosité & Rigueur")

    st.write("")

    # --- LANGUES ---
    st.caption("🌐 **Anglais** (Niveau B2/C1)") 

    st.write("---")

    # --- DIPLÔMES ---
    st.subheader("🎓 Diplômes & Certifications")
    
    # IBM
    st.markdown("**IBM Data Analyst (déc. 2025)**")
    st.link_button("Voir le certificat", "https://www.coursera.org/account/accomplishments/specialization/HN9P6HM29J5Q", use_container_width=True)
    
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
# --- CHARGEMENT DES DONNÉES ---
@st.cache_data
def load_data():
    return pd.read_csv("survey_data.zip", compression='zip')

# --- PAGE PRINCIPALE ---
st.title("Hello, moi c'est Clarisse ! 👋")
st.markdown("""
**Future étudiante en Master Data**, je construis mon parcours avec une conviction précise : 
la donnée n'a de valeur que si elle est utile aux humains qui l'utilisent.

Ce qui m'anime aujourd'hui, c'est **l'envie d'avoir un impact concret**. Je ne cherche pas seulement à produire des graphiques, 
mais à faire parler les données pour offrir des **recommandations claires**. Mon but est de transformer des données complexes 
en réponses simples, afin de permettre à l'entreprise de se développer et de pérenniser son activité.

Au-delà de la technique, je considère que la réussite d'un projet passe aussi par l'ambiance de travail. 
D'un naturel **enthousiaste et positive**, j'ai à cœur d'apporter ma bonne humeur au sein d'une équipe, 
car je suis persuadée qu'on travaille mieux dans un environnement bienveillant. ☀️

🚀 *Actuellement en auto-formation, je prépare le terrain pour rejoindre une entreprise en **alternance dès septembre 2026**.*
""")

st.write("---")

# ==========================================
# MÉTHODOLOGIE (Titres ajustés)
# ==========================================

st.header("⚙️ Ma Méthodologie")

# Mise en page en 4 colonnes
step1, step2, step3, step4 = st.columns(4)

with step1:
    # J'ai remplacé "####" par "#####" pour réduire la taille
    st.markdown("##### 1. Cadrer 🎯")
    st.caption("Comprendre le besoin métier et définir les objectifs avant de foncer dans le code.")

with step2:
    st.markdown("##### 2. Nettoyer 🧹")
    st.caption("Préparation des données (Excel/Pandas), gestion des valeurs manquantes et formatage.")

with step3:
    st.markdown("##### 3. Analyser 🔎")
    st.caption("Exploration (SQL/Python) pour faire émerger les tendances et les patterns cachés.")

with step4:
    st.markdown("##### 4. Restituer 📊")
    st.caption("Visualisation claire (Plotly) et storytelling pour faciliter la prise de décision.")

st.write("---")

st.header("📂 Mes Projets Data")

# --- CONTEXTE & DOWNLOAD ---
try:
    df = load_data()
    nb_lignes = df.shape[0]
    
    st.markdown(f"""
    <div class="context-box">
        <b>Contexte :</b> Les analyses suivantes sont basées sur le dataset public <i>StackOverflow Developer Survey</i> ({nb_lignes:,} lignes).
        L'objectif est de détecter les tendances du marché Tech actuel.
    </div>
    """, unsafe_allow_html=True)

    with open("survey_data.zip", "rb") as file:
        st.download_button(
            label="📥 Télécharger les données sources (.zip)",
            data=file,
            file_name="survey_data.zip",
            mime="text/zip"
        )

except Exception as e:
    st.error(f"Erreur de chargement : {e}")

st.write("") 

# ==========================================
# PROJET 1 : LANGAGES (Palette Violette)
# ==========================================
with st.container(border=True):
    st.subheader("📊 Projet 1 : Tendances Tech par Pays")
    
    st.write("L'objectif est de comparer les langages utilisés dans les principaux hubs technologiques mondiaux pour orienter une stratégie de recrutement.")
    st.markdown("**❓ Question : Existe-t-il des spécificités locales dans l'adoption des langages Data ?**")

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
                            color_discrete_sequence=pastel_purples, # On applique le violet
                            title="Top 10 Langages par Pays")
        
        fig1.update_layout(xaxis_title="Pays", yaxis_title="Développeurs", plot_bgcolor="white")
        st.plotly_chart(fig1, use_container_width=True)
        
        # LE VRAI CODE DE GÉNÉRATION EXPLIQUÉ
        with st.expander("👉 Voir le code Python (Plotly)"):
            st.code("""
# 1. Préparation des données (Pandas)
# On filtre d'abord pour ne garder que les 10 pays principaux
df_filtered = df[df['Country'].isin(top_10_countries)]

# Transformation clé : .explode()
# Une cellule contenant "Python;SQL" est divisée en deux lignes distinctes.
# Cela permet de compter chaque langage individuellement.
df_final = df_filtered.assign(Language=df['LanguageHaveWorkedWith'].str.split(';')).explode('Language')

# 2. Création du graphique interactif (Plotly Express)
# barmode='group' permet de comparer les langages côte à côte pour chaque pays
fig = px.histogram(
    df_final, 
    x='Country', 
    color='Language', 
    barmode='group',
    color_discrete_sequence=pastel_purples, # Palette personnalisée
    title="Top 10 Langages par Pays"
)

# Amélioration du design (fond blanc propre)
fig.update_layout(plot_bgcolor="white")
fig.show()
            """, language="python")

    st.success("✅ **Insight :** Si le Web (HTML/JS) est partout, Python domine nettement aux USA, en Inde et en Allemagne, confirmant leur statut de leaders en IA.")


# ==========================================
# PROJET 2 : BASES DE DONNÉES (Minimaliste)
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

        # VISUALISATION PLOTLY (SANS ETIQUETTES)
        fig2 = px.bar(df_db, x='Base de Données', y='Nombre', 
                      title="Top 15 Bases de Données",
                      color_discrete_sequence=['#B39DDB']) # Violet Pastel unique
        
        # Suppression des étiquettes (text_auto retiré) et fond blanc
        fig2.update_layout(xaxis_title="Technologie", yaxis_title="Répondants", plot_bgcolor="white")
        st.plotly_chart(fig2, use_container_width=True)
        
        # LE VRAI CODE DE GÉNÉRATION EXPLIQUÉ
        with st.expander("👉 Voir le code Python (Plotly)"):
            st.code("""
# 1. Calcul des fréquences (Pandas)
# La colonne brute contient des listes : "MySQL;PostgreSQL;MongoDB"
# .stack() empile toutes les valeurs pour les mettre dans une seule colonne
# .value_counts() compte ensuite chaque occurrence unique
db_counts = df['DatabaseHaveWorkedWith'].str.split(';', expand=True).stack().value_counts().head(15)

# On remet l'index à plat pour que Plotly puisse lire les colonnes X et Y
df_db = db_counts.reset_index()
df_db.columns = ['Base de Données', 'Nombre']

# 2. Création du graphique (Plotly Express)
# On choisit un Bar Chart simple avec une couleur unique pour la clarté
fig = px.bar(
    df_db, 
    x='Base de Données', 
    y='Nombre', 
    color_discrete_sequence=['#B39DDB'], # Violet Pastel
    title="Top 15 Bases de Données"
)

# Nettoyage de l'interface (axes et fond)
fig.update_layout(xaxis_title="Technologie", plot_bgcolor="white")
fig.show()
            """, language="python")

    st.success("✅ **Insight :** Le SQL reste roi (PostgreSQL/MySQL > 45%). Cependant MongoDB s'impose comme la première alternative NoSQL majeure, confirmant son évolution croissante.")

    # ==========================================
# SECTION PASSIONS (AVEC ONGLETS)
# ==========================================
st.write("---")

# Titre Principal de la section
st.header("❤️ Mes Passions")

# Phrase d'intro "Jeu de mots"
st.markdown("""
<div style="text-align: justify; font-style: italic;">
    La curiosité est le moteur de tout bon Data Analyst. Quand je ne suis pas en train de faire parler des datasets, 
    je pars explorer le monde, faire du sport ou écouter de la musique. 
    J'ai voulu appliquer mes compétences de visualisation à ce qui me fait vibrer au quotidien.
</div>
""", unsafe_allow_html=True)

st.write("") # Espace

# CRÉATION DES ONGLETS (Voyage | Sport | Musique)
tab1, tab2, tab3 = st.tabs(["🌍 Data Trotter", "🏅 Sport Analytics", "🎵 Music Data"])

# --- ONGLET 1 : VOYAGE ---
with tab1:
    st.subheader("🗺️ Mapping de mes explorations")
    
    st.markdown("""
    <div style="text-align: justify;">
        <p>
            Chaque point sur cette carte raconte une histoire. J'utilise ici une carte choroplèthe pour visualiser 
            mes voyages passés et... mes futures destinations. <b> Passe la souris dessus !😉</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 1. Préparation des données
    data_voyage = [
        # --- FRANCE & DOM-TOM ---
        {"Pays": "France", "Statut": "J'y vis 📍", "Détails": "France Métropolitaine (Paris, Bordeaux...)"},
        {"Pays": "French Polynesia", "Statut": "Visité 🎒", "Détails": "Tahiti, Moorea, Huahine, Bora Bora..."},
        {"Pays": "Guadeloupe", "Statut": "Visité 🎒", "Détails": "Pointe-à-Pitre et exploration de l'île"},
        {"Pays": "Martinique", "Statut": "Visité 🎒", "Détails": "Fort-de-France, St Pierre, St Anne"},
        
        # --- EUROPE ---
        {"Pays": "Spain", "Statut": "J'y ai vécu 🏠", "Détails": "Madrid (6 mois), Alicante"},
        {"Pays": "Italy", "Statut": "Visité 🎒", "Détails": "Palerme (Sicile)"},
        {"Pays": "Greece", "Statut": "Visité 🎒", "Détails": "Athènes, Égine"},
        {"Pays": "United Kingdom", "Statut": "Visité 🎒", "Détails": "Londres"},
        {"Pays": "Albania", "Statut": "Visité 🎒", "Détails": "Durres, Tirana"},
        
        # --- ROAD TRIP EUROPE (Autostop - KET 2025) ---
        {"Pays": "Switzerland", "Statut": "Road Trip Europe 👍", "Détails": "Zurich (Autostop - KET 2025)"},
        {"Pays": "Austria", "Statut": "Road Trip Europe 👍", "Détails": "Salzbourg (Autostop - KET 2025)"},
        {"Pays": "Czech Republic", "Statut": "Road Trip Europe 👍", "Détails": "Prague (Autostop - KET 2025)"},
        {"Pays": "Germany", "Statut": "Road Trip Europe 👍", "Détails": "Francfort (Autostop - KET 2025)"},
        {"Pays": "Netherlands", "Statut": "Road Trip Europe 👍", "Détails": "Amsterdam (Autostop - KET 2025)"},

        # --- RESTE DU MONDE ---
        {"Pays": "Morocco", "Statut": "Visité 🎒", "Détails": "Tanger"},
        {"Pays": "Saint Lucia", "Statut": "Visité 🎒", "Détails": "Voyage aux Antilles"},
        {"Pays": "Dominica", "Statut": "Visité 🎒", "Détails": "Voyage aux Antilles"},
        {"Pays": "South Korea", "Statut": "Visité 🎒", "Détails": "Séoul"},
        # Modification ici : Japon passé en "Visité" standard
        {"Pays": "Japan", "Statut": "Visité 🎒", "Détails": "Kyoto, Hiroshima, Okinawa, Beppu, Miyajima..."},
        
        # --- FUTUR ---
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
        
        # --- PALETTE PASTEL DOUCE ---
        color_discrete_map={
            "J'y vis 📍": "#B39DDB",          # Violet Pastel
            "J'y ai vécu 🏠": "#D7BDE2",      # Mauve très clair
            "Visité 🎒": "#A9DFBF",           # Vert Menthe Pastel (Japon est ici maintenant)
            "Road Trip Europe 👍": "#AED6F1", # Bleu très pâle
            "Prochainement ✈️": "#F5B7B1"     # Corail Pastel (Futur)
        },
        projection="natural earth"
    )

    # Mise en forme Monde Entier + Fond Gris
    fig_map.update_geos(
        showcountries=True, countrycolor="#d1d1d1",
        showcoastlines=True, coastlinecolor="#d1d1d1",
        showland=True, landcolor="#f5f5f5", # FOND GRIS CLAIR
        showocean=True, oceancolor="#ffffff"
    )

    fig_map.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor='rgba(0,0,0,0)', # <-- LA LIGNE MAGIQUE (Fond global transparent)
        showlegend=True,
        legend=dict(y=0.05, x=0.05, bgcolor="rgba(255,255,255,0.9)", title=None),
        geo=dict(bgcolor='rgba(0,0,0,0)') # (Fond de la zone geo transparent)
    )

    st.plotly_chart(fig_map, use_container_width=True)
    
    # 3. Détail du Road Trip avec Lien LinkedIn
    with st.expander("🚙 Détails sur mon tour de l'Europe : Le défi KET 2025 (1€/jour)"):
        st.markdown("""
        <div style="text-align: justify;">
            <p>
                <b>Le Challenge :</b> 8 jours, 6 pays traversés, et seulement 1€ par jour ! Inspiré de Pékin Express, 
                ce défi solidaire organisé par l'association <i>Adrénaline Kedge Bordeaux</i> m'a poussée dans mes retranchements.
            </p>
            <p>
                <b>La Mission :</b> De Bordeaux à Paris (Bordeaux → Lyon → Zurich → Salzbourg → Prague → Amsterdam → Paris), nous avons avancé uniquement en auto-stop, 
                en négociant hébergement et nourriture chaque soir. Au-delà de l'aventure sportive, nous avons collecté des fonds 
                pour <b>Life ONG</b> afin de lutter contre la pauvreté. Une véritable école de la débrouillardise et de la négociation !
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("🚀 Voir le récit complet et les photos sur LinkedIn", "https://www.linkedin.com/feed/update/urn:li:activity:7300911140312616960/")

# --- ONGLET 2 : SPORT ---
with tab2:
    st.subheader("🏅 Sport Analytics : Mon équilibre")
    
    st.markdown("""
    <div style="text-align: justify;">
        <p>
            Le sport est essentiel à mon équilibre mental et physique. Il m'apprend la persévérance, 
            la gestion de l'effort et l'esprit d'équipe. Voici la répartition de mon temps sportif !
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 1. Données
    data_sport = {
        'Sport': ['Handball 🤾‍♀️', 'Musculation 🏋️‍♀️', 'Course à pied 🏃‍♀️'],
        'Part': [50, 25, 25] # 50% Hand, 25% Muscu, 25% Run
    }
    df_sport = pd.DataFrame(data_sport)

    # 2. Création du Donut Chart
    fig_sport = px.pie(
        df_sport, 
        values='Part', 
        names='Sport',
        hole=0.5, # Crée le trou au milieu (Donut Chart)
        color_discrete_sequence=['#B39DDB', '#A9DFBF', '#AED6F1'] # Violet (Hand), Vert (Muscu), Bleu (Run)
    )

    # 3. Customisation
    fig_sport.update_traces(
        textinfo='percent+label', # Affiche le % et le nom
        textposition='outside',   # Texte à l'extérieur pour la lisibilité
        marker=dict(line=dict(color='#FFFFFF', width=2)) # Bordure blanche autour des parts
    )
    
    fig_sport.update_layout(
        showlegend=False, # On cache la légende car les labels sont déjà sur le graphique
        paper_bgcolor='rgba(0,0,0,0)', # Fond transparent
        plot_bgcolor='rgba(0,0,0,0)',
        margin={"r":0,"t":40,"l":0,"b":0} # Marges ajustées
    )

    st.plotly_chart(fig_sport, use_container_width=True)

    # Petit texte explicatif
    st.info("💡 **Le Handball** reste ma discipline de cœur, celle qui m'a appris l'esprit d'équipe et la stratégie. La musculation et la course viennent compléter ma préparation physique.")

# --- ONGLET 3 : MUSIQUE ---
with tab3:
    # Titre simplifié comme demandé
    st.subheader("🎵 Analyse de ma Rétrospective Spotify 2025")
    
    st.markdown("""
    <div style="text-align: justify;">
        <p>
            Avec près de <b>80 000 minutes</b> d'écoute cette année, la musique est mon moteur. 
            On remarque une corrélation directe entre mes styles d'écoute et mes phases de travail : 
            du <b>Néo-classique</b> pour la concentration (Deep Work) et de l'<b>Électro/Pop</b> pour le dynamisme.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 1. LES KPIs (Gros Chiffres)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temps d'écoute", "79 865 min", "soit 55 jours 🤯")
    col2.metric("Artistes Uniques", "2 886", "Découverte")
    col3.metric("Top Artiste", "L. Einaudi", "Top 0.03% Monde")
    col4.metric("Titres Uniques", "4 826", "Diversité")

    st.write("---")

    # 2. VISUALISATIONS (2 Colonnes)
    c1, c2 = st.columns([1, 1])

    with c1:
        st.markdown("**🎹 Top 5 Genres : L'équilibre Focus / Énergie**")
        # Données Genres
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
        # Calcul : 8343 min sur 79865 min
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
            color_discrete_sequence=['#4B0082', '#E0E0E0'] # Indigo vs Gris
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

    # 3. LE COIN TECHNIQUE (SQL)
    st.write("")
    with st.expander("👩‍💻 Tech Corner : La requête SQL derrière ces chiffres"):
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
        Ce portfolio a été conçu avec passion, en alliant mes compétences techniques, ma curiosité autodidacte et l'assistance de l'Intelligence Artificielle. 🦾💜<br>
        Une preuve que l'humain et la machine peuvent collaborer pour créer de belles choses.
    </p>
    <p>
        © 2025 Clarisse Deberdt · Fait avec ❤️.
    </p>
</div>
""", unsafe_allow_html=True)
 