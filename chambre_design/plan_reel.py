#!/usr/bin/env python3
"""Plan AUX VRAIES DIMENSIONS - Chambre 1 etroite : 1.73 x 5.6 m (9.83 m2).
Pente (0.9m) a GAUCHE en entrant. Fenetre de toit au fond. Porte cote escalier.
Vue de dessus, piece dessinee horizontalement (longueur = x).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, Circle
import matplotlib.patches as mpatches

C = {
    "floor":"#f3e9da","slope":"#e3d3ba","wall":"#2f3640",
    "bunk":"#6c8ebf","bed":"#9cb380","ward":"#d98e73",
    "desk":"#e6b85c","box":"#8fb9a8","rug":"#b9c4cf","win":"#bfe3f0",
    "ink":"#2f3640","warn":"#c0392b","ok":"#2e7d52",
}
W, L = 1.73, 5.6   # largeur, longueur

def base(ax):
    ax.add_patch(Polygon([(0,0),(L,0),(L,W),(0,W)], closed=True,
                 facecolor=C["floor"], edgecolor=C["wall"], lw=5, zorder=1))
    # bande sous-pente le long du mur BAS (= gauche en entrant), basse 0.9m
    ax.add_patch(Rectangle((0,0),L,0.45, facecolor=C["slope"], zorder=2))
    ax.text(L/2,0.22,"◣ mur en pente — sous-pente 0,9 m  (seulement meubles bas / lit)",
            ha="center", va="center", fontsize=7.5, color="#8a7860", style="italic", zorder=3)
    # mur haut = mur droit (vertical, ~2,5 m) -> meubles hauts ok
    ax.text(L/2,W-0.12,"mur droit (plus haut, ~2,5 m) — meubles hauts ici",
            ha="center", va="center", fontsize=7.5, color="#8a7860", style="italic", zorder=3)
    # fenetre de toit (fond, x=L)
    ax.add_patch(Rectangle((L-0.02,0.5),0.16,0.8, facecolor=C["win"],
                 edgecolor=C["wall"], lw=2, zorder=6))
    ax.text(L+0.32,0.9,"fenêtre\nde toit", ha="center", va="center",
            fontsize=7, color="#3a6b80", fontweight="bold")
    # porte (cote escalier, x=0)
    ax.add_patch(mpatches.Wedge((0.1,W-0.1),0.7,270,360, facecolor="none",
                 edgecolor="#b0a99f", lw=1.4, ls="--", zorder=4))
    ax.text(0.05,W+0.18,"porte", ha="left", fontsize=7, color="#8a7860")

def furn(ax, x, y, w, h, color, label, sub="", fs=8.5, lc="white"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,
        boxstyle="round,pad=0.01,rounding_size=0.05",
        facecolor=color, edgecolor="white", lw=2, zorder=5))
    ax.text(x+w/2,y+h/2+(0.10 if sub else 0),label, ha="center", va="center",
            fontsize=fs, color=lc, fontweight="bold", zorder=6)
    if sub:
        ax.text(x+w/2,y+h/2-0.13,sub, ha="center", va="center",
                fontsize=fs-2, color=lc, zorder=6)

def passage(ax, x, y0, y1, txt, good=True):
    col = C["ok"] if good else C["warn"]
    ax.annotate("", xy=(x,y1), xytext=(x,y0),
                arrowprops=dict(arrowstyle="<->", color=col, lw=1.6), zorder=8)
    ax.text(x+0.06,(y0+y1)/2,txt, fontsize=7.5, color=col, fontweight="bold",
            va="center", zorder=8)

fig, axes = plt.subplots(2,1, figsize=(13,8.6))
fig.patch.set_facecolor("#faf6ef")

# ============ OPTION A (recommandee) ============
ax = axes[0]
base(ax)
# Superposes contre mur haut, cote fenetre
furn(ax, 3.55, 0.83, 1.9, 0.9, C["bunk"], "LITS SUPERPOSÉS", "2 garçons (haut+bas)", fs=9)
# Tiroir gigogne (invite) qui sort vers le bas
ax.add_patch(Rectangle((3.65,0.45),1.7,0.36, facecolor="none",
             edgecolor=C["bunk"], lw=1.5, ls="--", zorder=5))
ax.text(4.5,0.63,"tiroir gigogne = couchage invité (se range le jour)",
        ha="center", fontsize=6.8, color="#4f6f9f", style="italic", zorder=6)
# Penderie mur haut
furn(ax, 1.55, 1.13, 1.7, 0.6, C["ward"], "PENDERIE pleine hauteur", "habits + linge invité", fs=8)
# Bureau cote pente sous fenetre
furn(ax, 4.75, 0.05, 0.7, 0.42, C["desk"], "bureau", "", fs=7.5)
# Caissons sous pente
furn(ax, 0.25, 0.05, 1.2, 0.42, C["box"], "caissons bas", "", fs=7.5)
# passage
passage(ax, 2.6, 0.47, 0.81, "0,83 m\nlibre", good=True)
ax.text(L/2, W+0.45, "OPTION A  —  RECOMMANDÉE  ·  passage dégagé partout (0,83 m)",
        ha="center", fontsize=11.5, fontweight="bold", color=C["ok"])
ax.text(L/2, -0.55, "Les 2 garçons dorment dans les superposés • l'invité dort sur le tiroir gigogne "
        "• penderie + caissons règlent le rangement", ha="center", fontsize=8, color="#6a6a6a")

# ============ OPTION B ============
ax = axes[1]
base(ax)
furn(ax, 3.55, 0.83, 1.9, 0.9, C["bunk"], "LITS SUPERPOSÉS", "2 garçons", fs=9)
# lit 120 le long de la pente
furn(ax, 1.0, 0.05, 2.0, 1.2, C["bed"], "LIT 120×200 (invité, 2 pers.)", "", fs=8.5, lc="white")
# penderie cote porte
furn(ax, 0.15, 1.13, 0.75, 0.6, C["ward"], "PENDERIE", "", fs=7.5)
# passage etroit au niveau du lit 120
passage(ax, 3.15, 1.25, 1.71, "0,48 m\nTRÈS étroit", good=False)
passage(ax, 0.95, 0.83, 1.71, "0,88 m", good=True)
ax.text(L/2, W+0.45, "OPTION B  —  garde le lit 120  ·  mais passage très serré (0,48 m) le long du lit",
        ha="center", fontsize=11.5, fontweight="bold", color=C["ink"])
ax.text(L/2, -0.55, "Permet 2 invités sur le 120×200, MAIS on se faufile le long du lit "
        "(0,48 m) → peu pratique au quotidien dans une pièce si étroite", ha="center",
        fontsize=8, color="#6a6a6a")

for ax in axes:
    ax.set_xlim(-0.4, L+0.9)
    ax.set_ylim(-0.7, W+0.7)
    ax.set_aspect("equal"); ax.axis("off")

# legende
handles=[
    mpatches.Patch(color=C["bunk"], label="Lits superposés (2 garçons)"),
    mpatches.Patch(color=C["bed"], label="Lit 120×200 (invité)"),
    mpatches.Patch(color=C["ward"], label="Penderie"),
    mpatches.Patch(color=C["desk"], label="Bureau"),
    mpatches.Patch(color=C["box"], label="Caissons sous-pente"),
]
fig.legend(handles=handles, loc="lower center", ncol=5, fontsize=9,
           frameon=False, bbox_to_anchor=(0.5,-0.02))
fig.suptitle("CHAMBRE 1 — VRAIES DIMENSIONS : 1,73 m × 5,6 m (9,83 m²) — pièce étroite",
             fontsize=14, fontweight="bold", color=C["ink"], y=1.0)
plt.tight_layout(rect=[0,0.04,1,0.97])
plt.savefig("/home/user/ella-caisse/chambre_design/plan_reel.png",
            dpi=140, facecolor="#faf6ef", bbox_inches="tight")
print("OK plan_reel.png")
