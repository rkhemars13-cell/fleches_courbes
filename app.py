import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuration de la page
st.set_page_config(page_title="Mécanismes Réactionnels", layout="centered")
st.title("⚗️ Atelier Interactif : Mécanismes Réactionnels")
st.write("Exercez-vous à tracer les flèches courbes représentant le mouvement des doublets d'électrons.")

# Création des trois onglets (Exemples)
onglet1, onglet2, onglet3 = st.tabs([
    "💧 1. Substitution Nucléophile", 
    "🧪 2. Addition Électrophile", 
    "🔋 3. Réaction Acido-Basique"
])

# -----------------------------------------------------------------
# ONGLET 1 : SUBSTITUTION NUCLÉOPHILE (CH3Br + HO-)
# -----------------------------------------------------------------
with onglet1:
    st.header("Exemple 1 : Synthèse du Méthanol")
    st.write("On étudie l'attaque de l'ion hydroxyde $\\text{{HO}}^-$ sur le bromométhane $\\text{{CH}}_3\\text{{Br}}$.")
    
    # Formulaire de choix pour l'élève
    st.subheader("✍️ Paramétrez votre flèche courbe :")
    col1, col2 = st.columns(2)
    donneur1 = col1.selectbox("Le doublet part du site donneur (Nucléophile) :", 
                             ["Choisir...", "Liaison C-H", "Doublet non liant de l'Oxygène (O-)", "Atome de Brome (Br)"], key="d1")
    accepteur1 = col2.selectbox("Le doublet arrive sur le site accepteur (Électrophile) :", 
                               ["Choisir...", "Atome de Carbone (δ+)", "Atome d'Hydrogène", "Ion Hydroxyde"], key="a1")
    
    # Bouton de validation
    valider1 = st.button("Valider le mécanisme 1")
    
    # Graphique de la réaction
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.set_xlim(-2, 10)
    ax1.set_ylim(-3, 3)
    ax1.axis('off')
    
    # Dessin de HO-
    ax1.text(0, 0, r"$\mathbf{HO^-}$", fontsize=16, color='blue', ha='center', va='center')
    ax1.text(0.3, 0.5, "••\n••", fontsize=10, color='blue', ha='center') # Doublets
    
    # Signe +
    ax1.text(2, 0, "+", fontsize=16, ha='center', va='center')
    
    # Dessin de CH3Br
    ax1.text(4, 0, r"$\mathbf{C}$", fontsize=16, color='black', ha='center', va='center')
    ax1.text(4, -0.4, r"$\delta+$", fontsize=10, color='red', ha='center')
    # Liaisons H
    ax1.plot([4, 4], [0.4, 1.2], 'k-', linewidth=2)
    ax1.text(4, 1.4, "H", fontsize=14, ha='center')
    ax1.plot([4, 3.3], [-0.3, -1], 'k-', linewidth=2)
    ax1.text(3.1, -1.2, "H", fontsize=14, ha='center')
    ax1.plot([4, 4.7], [-0.3, -1], 'k-', linewidth=2)
    ax1.text(4.9, -1.2, "H", fontsize=14, ha='center')
    # Liaison Br
    ax1.plot([4.4, 5.8], [0, 0], 'k-', linewidth=2)
    ax1.text(6.3, 0, r"$\mathbf{Br}$", fontsize=16, color='darkgreen', ha='center', va='center')
    ax1.text(6.3, -0.4, r"$\delta-$", fontsize=10, color='blue', ha='center')
    
    # Tracé dynamique de la flèche si l'élève fait un choix
    if donneur1 == "Doublet non liant de l'Oxygène (O-)" and accepteur1 == "Atome de Carbone (δ+)":
        # Flèche courbe correcte
        arrow = patches.FancyArrowPatch((0.2, 0.2), (3.8, 0), connectionstyle="arc3,rad=-0.4",
                                        arrowstyle="->", mutation_scale=15, color='red', linewidth=2.5, linestyle='-')
        ax1.add_patch(arrow)
        
    st.pyplot(fig1)
    
    # Correction pédagogique
    if valider1:
        if donneur1 == "Doublet non liant de l'Oxygène (O-)" and accepteur1 == "Atome de Carbone (δ+)":
            st.success("🎉 **Excellent travail !** La flèche courbe part bien d'un des doublets non liants de l'atome d'oxygène (riche en électrons, chargé négativement) et pointe vers l'atome de carbone électrophile (pauvre en électrons à cause de la polarisation de la liaison C-Br).")
            st.markdown("**Étape suivante du mécanisme :** La formation de la liaison O-C provoque simultanément la rupture de la liaison C-Br. Le brome emporte le doublet et devient l'ion bromure $\\text{Br}^-$.")
        else:
            st.error("❌ **Ce n'est pas correct.** Rappelez-vous la règle fondamentale : la flèche courbe représente le mouvement des électrons. Elle doit TOUJOURS partir d'un site riche en électrons (nucléophile) et arriver sur un site pauvre en électrons (électrophile). Réessayez !")

# -----------------------------------------------------------------
# ONGLET 2 : ADDITION ÉLECTROPHILE (ALCÈNE + H+)
# -----------------------------------------------------------------
with onglet2:
    st.header("Exemple 2 : Étape d'initiation d'une hydratation d'alcène")
    st.write("On étudie l'attaque entre l'éthène $\\text{{C}}_2\\text{{H}}_4$ et un ion hydrogène $\\text{{H}}^+$.")
    
    st.subheader("✍️ Paramétrez votre flèche courbe :")
    col1, col2 = st.columns(2)
    donneur2 = col1.selectbox("Le doublet part du site donneur (Nucléophile) :", 
                             ["Choisir...", "Liaison simple C-H", "Double liaison C=C (liaison pi)", "Ion H+"], key="d2")
    accepteur2 = col2.selectbox("Le doublet arrive sur le site accepteur (Électrophile) :", 
                               ["Choisir...", "Un atome de Carbone", "L'ion H+ (lacune électronique)"], key="a2")
    
    valider2 = st.button("Valider le mécanisme 2")
    
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.set_xlim(-2, 10)
    ax2.set_ylim(-3, 3)
    ax2.axis('off')
    
    # Dessin Éthène
    ax2.text(2, 0, r"$\mathbf{C = C}$", fontsize=18, color='black', ha='center', va='center')
    # Liaisons H gauches et droites
    ax2.plot([1.3, 0.5], [0.2, 1], 'k-', linewidth=2)
    ax2.plot([1.3, 0.5], [-0.2, -1], 'k-', linewidth=2)
    ax2.plot([2.7, 3.5], [0.2, 1], 'k-', linewidth=2)
    ax2.plot([2.7, 3.5], [-0.2, -1], 'k-', linewidth=2)
    
    # Signe +
    ax2.text(5, 0, "+", fontsize=16, ha='center', va='center')
    
    # Dessin H+
    ax2.text(6.5, 0, r"$\mathbf{H^+}$", fontsize=16, color='red', ha='center', va='center')
    # Petit rectangle pour symboliser la lacune
    rect = patches.Rectangle((6.2, 0.4), 0.6, 0.4, linewidth=1, edgecolor='red', facecolor='none', linestyle='--')
    ax2.add_patch(rect)
    ax2.text(6.5, 0.9, "Lacune", color='red', fontsize=8, ha='center')
    
    if donneur2 == "Double liaison C=C (liaison pi)" and accepteur2 == "L'ion H+ (lacune électronique)":
        arrow2 = patches.FancyArrowPatch((2.0, 0.2), (6.3, 0.2), connectionstyle="arc3,rad=0.4",
                                         arrowstyle="->", mutation_scale=15, color='red', linewidth=2.5)
        ax2.add_patch(arrow2)
        
    st.pyplot(fig2)
    
    if valider2:
        if donneur2 == "Double liaison C=C (liaison pi)" and accepteur2 == "L'ion H+ (lacune électronique)":
            st.success("🎉 **Parfait !** La double liaison carbone-carbone contient une liaison $\\pi$ riche en électrons, mobile, constituant un excellent site donneur. L'ion $\\text{H}^+$ présente une lacune électronique totale, c'est le site accepteur idéal.")
            st.markdown("**Résultat :** Cela va former un **carbocation** intermédiaire (un des carbones se lie au H, l'autre carbone perd un électron et récupère une charge positive).")
        else:
            st.error("❌ **Erreur d'analyse.** L'ion $\\text{H}^+$ a une charge positive, il ne possède aucun électron disponible : il ne peut pas être le donneur ! Cherchez la zone de forte densité électronique.")

# -----------------------------------------------------------------
# ONGLET 3 : RÉACTION ACIDO-BASIQUE (NH3 + H+)
# -----------------------------------------------------------------
with onglet3:
    st.header("Exemple 3 : Formation de l'ion Ammonium")
    st.write("On étudie la réaction entre l'ammoniac $\\text{{NH}}_3$ (une base) et un acide libérant un ion $\\text{{H}}^+$.")
    
    st.subheader("✍️ Paramétrez votre flèche courbe :")
    col1, col2 = st.columns(2)
    donneur3 = col1.selectbox("Le doublet part du site donneur (Nucléophile) :", 
                             ["Choisir...", "Liaison simple N-H", "Doublet non liant de l'Azote (N)", "Ion H+"], key="d3")
    accepteur3 = col2.selectbox("Le doublet arrive sur le site accepteur (Électrophile) :", 
                               ["Choisir...", "L'atome d'Azote", "L'ion H+"], key="a3")
    
    valider3 = st.button("Valider le mécanisme 3")
    
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    ax3.set_xlim(-2, 10)
    ax3.set_ylim(-3, 3)
    ax3.axis('off')
    
    # Dessin NH3
    ax3.text(2, 0, r"$\mathbf{N}$", fontsize=18, color='darkblue', ha='center', va='center')
    ax3.text(2, 0.4, "••", fontsize=12, color='darkblue', ha='center') # Doublet non liant
    # Liaisons H
    ax3.plot([2, 2], [-0.4, -1.2], 'k-', linewidth=2)
    ax3.plot([1.6, 0.8], [-0.2, -0.7], 'k-', linewidth=2)
    ax3.plot([2.4, 3.2], [-0.2, -0.7], 'k-', linewidth=2)
    
    # Signe +
    ax3.text(4.5, 0, "+", fontsize=16, ha='center', va='center')
    
    # Dessin H+
    ax3.text(6, 0, r"$\mathbf{H^+}$", fontsize=16, color='red', ha='center', va='center')
    
    if donneur3 == "Doublet non liant de l'Azote (N)" and accepteur3 == "L'ion H+":
        arrow3 = patches.FancyArrowPatch((2.0, 0.5), (5.8, 0.1), connectionstyle="arc3,rad=0.3",
                                         arrowstyle="->", mutation_scale=15, color='red', linewidth=2.5)
        ax3.add_patch(arrow3)
        
    st.pyplot(fig3)
    
    if valider3:
        if donneur3 == "Doublet non liant de l'Azote (N)" and accepteur3 == "L'ion H+":
            st.success("🎉 **Félicitations, c'est tout à fait ça !** L'azote possède un doublet non liant disponible (site donneur) qu'il va partager avec l'ion $\\text{H}^+$ (site accepteur) pour former une liaison covalente dative. On obtient l'ion tétraédrique ammonium $\\text{NH}_4^+$.")
        else:
            st.error("❌ **Faux.** Souvenez-vous qu'une liaison $\\text{N-H}$ existante est stable et ne va pas céder ses électrons spontanément. Regardez plutôt au-dessus de l'atome d'Azote.")
