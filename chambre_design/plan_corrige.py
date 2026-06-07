#!/usr/bin/env python3
"""Chambre 1 - PLAN MEUBLE corrige (forme validee).
Pente mansardee sur long mur HAUT (0.9m -> 2.5m). Fenetre pleine hauteur au fond.
Passage imperatif le long du mur HAUT. 2 lits en enfilade sous la pente.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch
import numpy as np

C = {"floor":"#f6efe2","slope":"#e6d6bd","wall":"#2f3640","win":"#bfe3f0",
     "bed":"#cdbfe0","bedf":"#b7a6d4","draw":"#e3c9a0","ward":"#9cc0d9",
     "ok":"#2e7d52","ink":"#2f3640","pass":"#dff0e6"}

W, L = 1.73, 5.6
fig, ax = plt.subplots(figsize=(14,5.2))
fig.patch.set_facecolor("#faf6ef"); ax.set_facecolor("#faf6ef")

# contour + decroche d'entree (coin bas-gauche)
outline=[(0,0),(0,W),(L,W),(L,0),(1.0,0),(1.0,-0.55),(0,-0.55)]
ax.add_patch(Polygon(outline, closed=True, facecolor=C["floor"],
            edgecolor=C["wall"], lw=5, zorder=2))

# bande basse de la pente (mur HAUT) en degrade
for i in range(30):
    yy=W-0.75+0.75*i/30
    ax.add_patch(Rectangle((0,yy),L,0.75/30, facecolor=C["slope"],
                 alpha=0.9-0.6*i/30, edgecolor="none", zorder=2.5))
ax.text(L/2, W-0.18, "◤  MUR EN PENTE — plafond 0,9 m ici (lits / rangements bas seulement)  ◥",
        ha="center", fontsize=9, color="#7a6a4f", fontweight="bold", zorder=8)

# couloir / passage le long du mur HAUT
ax.add_patch(Rectangle((1.0,0.0),L-1.0,0.62, facecolor=C["pass"],
             edgecolor=C["ok"], lw=1.2, ls=(0,(4,3)), zorder=3))
ax.text(3.3,0.31,"◀  PASSAGE LIBRE  ~0,75 m  (on est debout ici)  ▶",
        ha="center", fontsize=9, color=C["ok"], fontweight="bold", zorder=8)

def bloc(x,y,w,h,fc,ec,label,fs=8.5,tc="#2f3640",lw=2,z=5):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012,rounding_size=0.04",
                 facecolor=fc,edgecolor=ec,lw=lw,zorder=z))
    ax.text(x+w/2,y+h/2,label,ha="center",va="center",fontsize=fs,
            color=tc,fontweight="bold",zorder=z+1)

# 2 lits en enfilade contre la pente (0.9 large x 1.9 long)
bloc(1.65,0.80,1.90,0.90,C["bed"],C["bedf"],"LIT 1\n90×190",z=5)
bloc(3.62,0.80,1.90,0.90,C["bed"],C["bedf"],"LIT 2\n90×190",z=5)
# tete cote fenetre pour lit 2
ax.text(5.45,1.25,"☀",ha="center",fontsize=11,zorder=6)

# commode basse sous la pente, cote porte (sous 0.9m, h~0.5)
bloc(0.18,1.05,1.35,0.62,C["draw"],"#c79b5e","COMMODE BASSE\n(sous la pente)",fs=7.5,z=5)

# penderie haute, coin HAUT cote fenetre (plafond 2.5m)
bloc(4.95,0.04,0.58,0.60,C["ward"],"#5f93b3","PENDERIE\n(coin haut)",fs=7,tc="#234",z=5)

# bureau rabattable sur mur haut (n'empiete pas: 0.30 prof)
bloc(1.15,0.0,0.95,0.30,"#f0e2c8","#c9a96b","bureau rabattable",fs=7,z=4)

# fenetre pleine hauteur au fond
ax.add_patch(Rectangle((L-0.02,0.55),0.16,0.75, facecolor=C["win"],
             edgecolor=C["wall"], lw=2, zorder=7))
ax.text(L+0.42,0.92,"FENÊTRE\npleine hauteur\n(pas de pente)",ha="center",
        va="center",fontsize=7.5,color="#3a6b80",fontweight="bold")
# porte / entree decroche
ax.add_patch(Rectangle((0,-0.55),1.0,0.55, facecolor="#efe6d6",
             edgecolor=C["wall"], lw=2, ls=":", zorder=3))
ax.text(0.5,-0.28,"entrée\n(décroché)",ha="center",va="center",fontsize=7,
        color="#8a7860",zorder=4)
ax.annotate("",xy=(1.05,-0.27),xytext=(1.7,-0.27),
            arrowprops=dict(arrowstyle="->",color="#8a7860",lw=1.4))

# cotes
ax.annotate("",xy=(0,W+0.28),xytext=(L,W+0.28),
            arrowprops=dict(arrowstyle="<->",color=C["ink"],lw=1.2))
ax.text(L/2,W+0.40,"5,60 m",ha="center",fontsize=9,color=C["ink"])
ax.annotate("",xy=(L+0.62,0),xytext=(L+0.62,W),
            arrowprops=dict(arrowstyle="<->",color=C["ink"],lw=1.2))
ax.text(L+0.78,W/2,"1,73 m",rotation=90,va="center",fontsize=9,color=C["ink"])

ax.set_xlim(-0.6,L+1.25); ax.set_ylim(-0.95,W+0.7)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("CHAMBRE 1 — plan corrigé : passage libre + 2 lits sous la pente  (9,83 m²)",
             fontsize=13.5,fontweight="bold",color=C["ink"],loc="left",pad=12)
plt.savefig("/home/user/ella-caisse/chambre_design/plan_corrige.png",
            dpi=145,facecolor="#faf6ef",bbox_inches="tight")
print("OK plan_corrige.png")
