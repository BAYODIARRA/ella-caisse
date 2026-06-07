#!/usr/bin/env python3
"""Plans d'amenagement colores - Chambre 1 (enfants + invites)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, Circle, FancyArrow
from matplotlib.path import Path
import matplotlib.patches as mpatches
import numpy as np

# ---- Palette douce / enfantine ----
COL = {
    "wall":   "#2f3640",
    "floor":  "#f3e9da",   # parquet clair
    "slope":  "#e9d9c2",   # zone sous-pente
    "ochre":  "#c8893a",   # mur ocre (rappel photo)
    "bed_g":  "#9cb380",   # vert sauge (lit invite)
    "bunk":   "#6c8ebf",   # bleu (lits superposes)
    "bunk2":  "#4f6f9f",
    "ward":   "#d98e73",   # penderie terracotta
    "desk":   "#e6b85c",   # bureau jaune
    "rug":    "#b9c4cf",
    "box":    "#8fb9a8",   # caissons vert d'eau
    "text":   "#2f3640",
    "white":  "#ffffff",
    "win":    "#bfe3f0",
}

def room_outline(ax):
    """Contour trapezoidal approx. de la Chambre 1 (vue de dessus).
    Echelle: 1 unite = 1 m. Long ~5.6m (vertical), large ~2.6m."""
    # Coordonnees (x = largeur, y = longueur)
    pts = [(0,0),(2.6,0),(2.6,3.0),(2.6,5.6),(0.0,5.6),(0,0)]
    poly = Polygon([(0,0),(2.6,0),(2.6,5.6),(0,5.6)], closed=True,
                   facecolor=COL["floor"], edgecolor=COL["wall"], lw=6, zorder=1)
    ax.add_patch(poly)
    # Mur en pente a gauche (bande sous-pente)
    ax.add_patch(Rectangle((0,0),0.55,5.6, facecolor=COL["slope"],
                 edgecolor="none", zorder=2, alpha=0.9))
    ax.text(0.27,2.8,"sous-pente 0.9m", rotation=90, ha="center", va="center",
            fontsize=7, color="#8a7860", style="italic")

def furn(ax, x, y, w, h, color, label, sub="", fs=9, lc="white", rot=0, round=0.06):
    box = FancyBboxPatch((x,y), w, h,
            boxstyle=f"round,pad=0.01,rounding_size={round}",
            facecolor=color, edgecolor="white", lw=2, zorder=5)
    ax.add_patch(box)
    cx, cy = x+w/2, y+h/2
    if rot == 90:
        # texte vertical : les 2 lignes se separent horizontalement
        dmain, dsub = (0.11, -0.13) if sub else (0, 0)
        ax.text(cx+dmain, cy, label, ha="center", va="center",
                fontsize=fs, color=lc, fontweight="bold", rotation=rot, zorder=6)
        if sub:
            ax.text(cx+dsub, cy, sub, ha="center", va="center",
                    fontsize=fs-2, color=lc, rotation=rot, zorder=6)
    else:
        ax.text(cx, cy+(0.12 if sub else 0), label, ha="center", va="center",
                fontsize=fs, color=lc, fontweight="bold", rotation=rot, zorder=6)
        if sub:
            ax.text(cx, cy-0.16, sub, ha="center", va="center",
                    fontsize=fs-2, color=lc, rotation=rot, zorder=6)

def window(ax):
    ax.add_patch(Rectangle((0.7,5.5),1.2,0.18, facecolor=COL["win"],
                 edgecolor=COL["wall"], lw=2, zorder=7))
    ax.text(1.3,5.82,"FENÊTRE DE TOIT", ha="center", fontsize=7,
            color=COL["wall"], fontweight="bold")

def door(ax, x, y):
    ax.add_patch(mpatches.Wedge((x,y),0.7,180,270, facecolor="none",
                 edgecolor="#b0a99f", lw=1.4, ls="--", zorder=4))
    ax.text(x-0.05,y-0.18,"porte", ha="center", fontsize=6.5, color="#8a7860")

def zone_tag(ax, y, txt, color):
    ax.text(-0.18, y, txt, ha="right", va="center", fontsize=8.5,
            color="white", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc=color, ec="none", alpha=0.95),
            zorder=8)

# ============ FIGURE ============
fig, axes = plt.subplots(1,2, figsize=(15,9))
fig.patch.set_facecolor("#faf6ef")

titles = [
    "PHASE 1 — Aujourd'hui (3 ans + 8 mois)",
    "PHASE 2 — Dans 1-2 ans (enfants plus grands)",
]

for idx, ax in enumerate(axes):
    ax.set_xlim(-2.2, 3.3)
    ax.set_ylim(-0.6, 6.3)
    ax.set_aspect("equal")
    ax.axis("off")
    room_outline(ax)
    window(ax)
    door(ax, 2.45, 0.35)

    # Salle de bain (decroche en haut a droite, mur)
    ax.add_patch(Rectangle((2.6,3.0),0.0,2.6, facecolor="none"))

    if idx == 0:
        # --- PHASE 1 ---
        # Lit superpose contre mur droit (aine en bas, haut libre)
        furn(ax, 1.55, 3.4, 1.0, 2.0, COL["bunk"], "LITS",
             "superposés", fs=10, rot=0)
        ax.text(2.05,3.85,"aîné (bas)\nhaut libre", ha="center", va="center",
                fontsize=6.5, color="white", style="italic", zorder=7)
        # Lit 120x200 invite/bebe cote pente
        furn(ax, 0.55, 3.1, 0.85, 2.3, COL["bed_g"], "LIT 120×200",
             "bébé + invité", fs=9, rot=90)
        # Bureau sous fenetre
        furn(ax, 0.6, 4.9, 1.0, 0.45, COL["desk"], "bureau", "", fs=8)
        # Penderie pres porte mur droit
        furn(ax, 1.75, 0.25, 0.8, 1.7, COL["ward"], "PENDERIE",
             "habits enfants", fs=8.5, rot=90)
        # Caissons sous pente bas
        furn(ax, 0.55, 0.3, 0.5, 1.6, COL["box"], "caissons", "bas", fs=7, rot=90)
        # Tapis jeu
        ax.add_patch(Circle((1.55,1.9),0.55, facecolor=COL["rug"],
                     edgecolor="white", lw=2, zorder=3))
        ax.text(1.55,1.9,"tapis\njeu", ha="center", va="center", fontsize=7,
                color="#5a6470", zorder=4)
        zone_tag(ax,5.05,"☀ jour / jeu", COL["desk"])
        zone_tag(ax,4.4,"☾ nuit enfants", COL["bunk"])
        zone_tag(ax,0.9,"▤ rangement", COL["ward"])
    else:
        # --- PHASE 2 ---
        furn(ax, 1.55, 3.4, 1.0, 2.0, COL["bunk2"], "LITS",
             "superposés", fs=10)
        ax.text(2.05,3.85,"aîné (haut)\ncadet (bas)", ha="center", va="center",
                fontsize=6.5, color="white", style="italic", zorder=7)
        # 120 redevient lit invite seul
        furn(ax, 0.55, 3.1, 0.85, 2.3, COL["bed_g"], "LIT 120×200",
             "invité (2 pers.)", fs=9, rot=90)
        furn(ax, 0.6, 4.9, 1.0, 0.45, COL["desk"], "bureau", "rabattable", fs=8)
        furn(ax, 1.75, 0.25, 0.8, 1.7, COL["ward"], "PENDERIE",
             "+ linge invité", fs=8.5, rot=90)
        furn(ax, 0.55, 0.3, 0.5, 1.6, COL["box"], "caissons", "bas", fs=7, rot=90)
        ax.add_patch(Circle((1.55,1.9),0.55, facecolor=COL["rug"],
                     edgecolor="white", lw=2, zorder=3))
        ax.text(1.55,1.9,"tapis", ha="center", va="center", fontsize=7,
                color="#5a6470", zorder=4)
        zone_tag(ax,5.05,"☀ bureau / jour", COL["desk"])
        zone_tag(ax,4.4,"☾ nuit enfants", COL["bunk2"])
        zone_tag(ax,0.9,"▤ rangement", COL["ward"])

    ax.set_title(titles[idx], fontsize=13, fontweight="bold",
                 color=COL["text"], pad=14)

# Legende commune
handles = [
    mpatches.Patch(color=COL["bunk"], label="Lits superposés (2 enfants)"),
    mpatches.Patch(color=COL["bed_g"], label="Lit 120×200 (invité)"),
    mpatches.Patch(color=COL["ward"], label="Penderie pleine hauteur"),
    mpatches.Patch(color=COL["desk"], label="Bureau"),
    mpatches.Patch(color=COL["box"], label="Caissons sous-pente"),
    mpatches.Patch(color=COL["rug"], label="Tapis de jeu"),
]
fig.legend(handles=handles, loc="lower center", ncol=3, fontsize=10,
           frameon=False, bbox_to_anchor=(0.5,-0.01))
fig.suptitle("CHAMBRE 1  —  2 garçons + couchage invité  (vue de dessus)",
             fontsize=16, fontweight="bold", color=COL["text"], y=0.99)
plt.tight_layout(rect=[0,0.05,1,0.96])
plt.savefig("/home/user/ella-caisse/chambre_design/plan_dessus.png",
            dpi=140, facecolor="#faf6ef", bbox_inches="tight")
print("OK plan_dessus.png")
