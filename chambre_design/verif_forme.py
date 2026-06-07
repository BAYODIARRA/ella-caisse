#!/usr/bin/env python3
"""Chambre 1 - VERIFICATION de la forme (vide) + coupe de la mansarde.
A faire valider par l'utilisateur avant de meubler.
Dim: ~1.73 large x 5.6 long, 9.83 m2. Pente mansardee sur un long mur (0.9->2.5m).
Fenetre = mur du fond pleine hauteur. Porte = cote oppose, avec decroche.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyArrow
import matplotlib.patches as mpatches
import numpy as np

C = {"floor":"#f3e9da","slopezone":"#e3d3ba","wall":"#2f3640","win":"#bfe3f0",
     "ok":"#2e7d52","warn":"#c0392b","ink":"#2f3640","hi":"#9cb380","accent":"#6c8ebf"}

fig = plt.figure(figsize=(13,8))
fig.patch.set_facecolor("#faf6ef")
gs = fig.add_gridspec(2,1, height_ratios=[1.7,1], hspace=0.35)

# ============ 1) VUE DE DESSUS (vide) ============
ax = fig.add_subplot(gs[0]); ax.set_facecolor("#faf6ef")
W, L = 1.73, 5.6
# contour avec petit decroche d'entree pres de la porte (coin bas-gauche)
outline = [(0.0,0.0),(0.0,W),(L,W),(L,0.0),(1.0,0.0),(1.0,-0.55),(0.0,-0.55)]
ax.add_patch(Polygon(outline, closed=True, facecolor=C["floor"],
             edgecolor=C["wall"], lw=5, zorder=2))
# zone basse de la pente (le long du mur du HAUT ici = un long mur), degrade
n=40
for i in range(n):
    t=i/n
    # de y=W (mur haut, le plus bas 0.9m) vers le bas (remonte)
    yy = W - 0.7*(1-t)   # bande de 0.7m de profondeur sous la pente
    col = (0.89-0.06*t, 0.83-0.04*t, 0.73-0.02*t)
    ax.add_patch(Rectangle((0,W-0.7+ (0.7*i/n)), L, 0.7/n,
                 facecolor=C["slopezone"], alpha=0.9-0.5*t, edgecolor="none", zorder=3))
ax.text(L/2, W-0.32, "◤  MUR EN PENTE  ·  bas 0,9 m ici, puis ça REMONTE vers le bas du plan  ◥",
        ha="center", va="center", fontsize=9, color="#7a6a4f", fontweight="bold", zorder=6)
# fleche \"ca remonte\"
ax.annotate("ça remonte\n(jusqu'à ~2,5 m)", xy=(L/2,0.25), xytext=(L/2,W-0.9),
            ha="center", fontsize=8, color="#7a6a4f",
            arrowprops=dict(arrowstyle="->", color="#7a6a4f", lw=1.5), zorder=6)
# mur haut (cote bas du plan) = mur droit
ax.text(L/2, 0.12, "côté HAUT (~2,5 m) — c'est ici qu'on peut se tenir debout / passage",
        ha="center", fontsize=8, color="#2e7d52", fontweight="bold", zorder=6)
# fenetre pleine hauteur au fond (x=L)
ax.add_patch(Rectangle((L-0.02,0.45),0.16,0.85, facecolor=C["win"],
             edgecolor=C["wall"], lw=2, zorder=7))
ax.text(L+0.35,0.88,"FENÊTRE\n(mur pleine\nhauteur,\nPAS de pente)",
        ha="center", va="center", fontsize=7.5, color="#3a6b80", fontweight="bold")
# porte avec decroche (l'entree fait un tour)
ax.add_patch(Rectangle((0.0,-0.55),1.0,0.55, facecolor="#efe6d6",
             edgecolor=C["wall"], lw=2, ls=":", zorder=4))
ax.text(0.5,-0.28,"entrée\n(décroché —\nla porte fait\nun tour)", ha="center",
        va="center", fontsize=7, color="#8a7860", zorder=5)
ax.annotate("", xy=(1.0,-0.27), xytext=(1.7,-0.27),
            arrowprops=dict(arrowstyle="->",color="#8a7860",lw=1.4))
ax.set_xlim(-0.6, L+1.2); ax.set_ylim(-0.9, W+0.5)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("1) VUE DE DESSUS  —  est-ce la bonne forme ?  (chambre vide)",
             fontsize=12, fontweight="bold", color=C["ink"], loc="left")

# ============ 2) COUPE (mansarde) sur la largeur 1.73 m ============
ax2 = fig.add_subplot(gs[1]); ax2.set_facecolor("#faf6ef")
# profil: mur bas a gauche (0.9m), remonte a droite (2.5m)
prof = [(0,0),(1.73,0),(1.73,2.5),(0,0.9)]
ax2.add_patch(Polygon(prof, closed=True, facecolor="#eef3ef",
              edgecolor=C["wall"], lw=3, zorder=2))
# zone debout (h>=1.9): x tel que 0.9+0.925x>=1.9 -> x>=1.08
xd=1.08
ax2.add_patch(Polygon([(xd,0),(1.73,0),(1.73,2.5),(xd,0.9+0.925*xd)],
              closed=True, facecolor=C["ok"], alpha=0.18, zorder=3))
ax2.axvline(xd, color=C["ok"], ls="--", lw=1.2, zorder=4)
ax2.text(1.4,0.35,"debout OK\n(passage)", ha="center", fontsize=8,
         color=C["ok"], fontweight="bold", zorder=5)
ax2.text(0.5,0.35,"zone basse\n(lit / rangt bas\nseulement)", ha="center",
         fontsize=8, color="#b07a31", fontweight="bold", zorder=5)
# cotes
ax2.annotate("0,9 m", xy=(0,0.9), xytext=(-0.32,0.45), fontsize=8, color=C["ink"],
             arrowprops=dict(arrowstyle="->",lw=1), ha="center")
ax2.annotate("~2,5 m", xy=(1.73,2.5), xytext=(2.05,1.6), fontsize=8, color=C["ink"],
             arrowprops=dict(arrowstyle="->",lw=1), ha="center")
ax2.annotate("", xy=(0,-0.18), xytext=(1.73,-0.18),
             arrowprops=dict(arrowstyle="<->",color=C["ink"],lw=1.2))
ax2.text(0.86,-0.36,"largeur 1,73 m", ha="center", fontsize=8, color=C["ink"])
ax2.set_xlim(-0.6,2.4); ax2.set_ylim(-0.55,2.9)
ax2.set_aspect("equal"); ax2.axis("off")
ax2.set_title("2) COUPE de la pente (sur la largeur)  —  on n'est debout qu'à droite",
              fontsize=12, fontweight="bold", color=C["ink"], loc="left")

fig.suptitle("CHAMBRE 1 — vérification de la forme avant de meubler  (1,73 × 5,6 m)",
             fontsize=14, fontweight="bold", color=C["ink"], y=0.98)
plt.savefig("/home/user/ella-caisse/chambre_design/verif_forme.png",
            dpi=140, facecolor="#faf6ef", bbox_inches="tight")
print("OK verif_forme.png")
