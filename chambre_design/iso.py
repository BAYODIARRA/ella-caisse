#!/usr/bin/env python3
"""Vue d'ambiance isometrique coloree - Chambre 1."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.patches as mpatches
import numpy as np

C = {
    "floor":  "#e7c9a0", "floor_d":"#d8b487",
    "wall_l": "#f3ede3", "wall_r": "#c8893a", "wall_rd":"#b07a31",
    "slope":  "#e8e2d6",
    "bunk_t": "#7ba0d0", "bunk_f":"#6c8ebf", "bunk_s":"#5a79a3",
    "bed_t":  "#a9c08c", "bed_f":"#9cb380", "bed_s":"#86a063",
    "ward_t": "#e3a187", "ward_f":"#d98e73", "ward_s":"#bf755c",
    "desk_t": "#edc46f", "desk_f":"#e6b85c", "desk_s":"#cfa244",
    "box_t":  "#a3c6b6", "box_f":"#8fb9a8", "box_s":"#79a08f",
    "matt":   "#cdd6df", "lin":"#dfe7ec",
    "ink":    "#3a3f47", "white":"#ffffff",
}

# --- projection isometrique ---
ax_a = np.radians(30)
def iso(x, y, z):
    sx = (x - y) * np.cos(ax_a)
    sy = (x + y) * np.sin(ax_a) + z
    return sx, sy

def quad(ax, pts3d, color, ec="white", lw=1.2, z=5, alpha=1):
    pts = [iso(*p) for p in pts3d]
    ax.add_patch(Polygon(pts, closed=True, facecolor=color,
                 edgecolor=ec, lw=lw, zorder=z, alpha=alpha,
                 joinstyle="round"))

def box(ax, x, y, z, dx, dy, dz, ct, cf, cs, z0=5, ec="white", lw=1.4):
    """Dessine un pave 3D (top, face avant -y, face droite +x)."""
    # top
    quad(ax, [(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)],
         ct, ec, lw, z0+2)
    # face avant (vers -y, cote observateur)
    quad(ax, [(x,y,z),(x+dx,y,z),(x+dx,y,z+dz),(x,y,z+dz)], cf, ec, lw, z0+1)
    # face droite (+x)
    quad(ax, [(x+dx,y,z),(x+dx,y+dy,z),(x+dx,y+dy,z+dz),(x+dx,y,z+dz)],
         cs, ec, lw, z0)

def label(ax, x, y, z, txt, fs=11, color="white", weight="bold"):
    sx, sy = iso(x, y, z)
    ax.text(sx, sy, txt, ha="center", va="center", fontsize=fs,
            color=color, fontweight=weight, zorder=60,
            path_effects=None)

fig, ax = plt.subplots(figsize=(13,10))
fig.patch.set_facecolor("#faf6ef")
ax.set_facecolor("#faf6ef")
ax.set_aspect("equal"); ax.axis("off")

# dimensions piece (x=largeur 2.6, y=longueur 5.6, h=2.5)
W, L, H = 2.6, 5.6, 2.5

# ---- SOL ----
quad(ax, [(0,0,0),(W,0,0),(W,L,0),(0,L,0)], C["floor"], "#cdb188", 1.5, 1)
# planches parquet
for i in range(1,7):
    yy = L*i/7
    p1=iso(0,yy,0); p2=iso(W,yy,0)
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]], color="#d8b487", lw=0.8, zorder=2)

# ---- MUR GAUCHE (pente) : ocre rappel photo, en pente ----
# mur arriere droit (ocre) plein
quad(ax, [(W,0,0),(W,L,0),(W,L,H),(W,0,H)], C["wall_r"], "#a06f2c", 1.5, 3)
# mur gauche en pente (haut incline)
quad(ax, [(0,0,0),(0,L,0),(0,L,H*0.55),(0,0,H*0.55)], C["wall_l"], "#ddd5c8",1.2,3)
# pan de toit incline (de 0.55H a H en allant vers la droite)
quad(ax, [(0,0,H*0.55),(0,L,H*0.55),(0.9,L,H),(0.9,0,H)], C["slope"],"#d8d0c2",1.2,3, alpha=0.95)

# ---- LITS SUPERPOSES (mur ocre, droit) ----
bx, by = 1.55, 3.3
box(ax, bx, by, 0.25, 0.95, 2.0, 0.55, C["bunk_t"],C["bunk_f"],C["bunk_s"], z0=20)  # lit bas
box(ax, bx, by, 1.25, 0.95, 2.0, 0.55, C["bunk_t"],C["bunk_f"],C["bunk_s"], z0=24)  # lit haut
# montants
for (mx,my) in [(bx,by),(bx+0.95,by),(bx,by+2.0),(bx+0.95,by+2.0)]:
    box(ax, mx-0.04,my-0.04,0.25,0.08,0.08,1.65, C["bunk_s"],C["bunk_s"],C["bunk_s"],z0=26,lw=0.5)
# matelas + linge
box(ax, bx+0.05, by+0.05, 0.8, 0.85, 1.9, 0.12, C["lin"],C["matt"],C["matt"],z0=23,lw=0.6)
box(ax, bx+0.05, by+0.05, 1.8, 0.85, 1.9, 0.12, C["lin"],C["matt"],C["matt"],z0=27,lw=0.6)
label(ax, bx+0.5, by+1.0, 2.25, "LITS\nSUPERPOSÉS", fs=11)
label(ax, bx+0.5, by+1.0, 1.55, "(2 enfants)", fs=8, weight="normal")

# ---- LIT 120x200 invite (cote pente) ----
gx, gy = 0.45, 3.1
box(ax, gx, gy, 0.1, 0.9, 2.2, 0.35, C["bed_t"],C["bed_f"],C["bed_s"], z0=14)
box(ax, gx+0.04, gy+0.04, 0.45, 0.82, 2.1, 0.14, C["lin"],C["matt"],C["matt"],z0=15,lw=0.6)
# oreiller
box(ax, gx+0.1, gy+0.1, 0.55, 0.6, 0.4, 0.12, C["white"],"#eef2f5","#dde4e9",z0=16,lw=0.6)
label(ax, gx+0.45, gy+1.3, 0.9, "LIT 120×200\n(invité)", fs=10, color=C["ink"])

# ---- BUREAU sous fenetre ----
dx0, dy0 = 0.55, 4.95
box(ax, dx0, dy0, 0, 1.0, 0.45, 0.62, C["desk_t"],C["desk_f"],C["desk_s"], z0=10)
label(ax, dx0+0.5, dy0+0.2, 0.7, "BUREAU", fs=9, color=C["ink"])

# ---- PENDERIE pleine hauteur (mur ocre, pres porte) ----
px, py = 1.75, 0.35
box(ax, px, py, 0, 0.75, 1.6, 2.1, C["ward_t"],C["ward_f"],C["ward_s"], z0=18)
# poignees
for hy in (0.55,1.05):
    box(ax, px-0.02, py+hy, 0.9, 0.03,0.12,0.25, "#fff","#f0d9cd","#e3c3b2",z0=20,lw=0.4)
label(ax, px+0.37, py+0.8, 1.15, "PENDERIE\npleine\nhauteur", fs=9.5)

# ---- CAISSONS sous pente ----
cx, cy = 0.5, 0.4
box(ax, cx, cy, 0, 0.45, 1.5, 0.5, C["box_t"],C["box_f"],C["box_s"], z0=12)
label(ax, cx+0.22, cy+0.75, 0.62, "caissons", fs=7.5, color=C["ink"])

# ---- TAPIS ----
quad(ax, [(0.75,1.6,0.02),(1.6,1.6,0.02),(1.6,2.7,0.02),(0.75,2.7,0.02)],
     "#bcc6cf","#ffffff",1.5, 4)
label(ax, 1.17, 2.15, 0.05, "tapis", fs=8, color="#5a6470", weight="normal")

# ---- FENETRE DE TOIT (sur la pente) ----
quad(ax, [(0.18,2.0,H*0.78),(0.62,2.0,H*0.78),(0.62,3.4,H*0.78),(0.18,3.4,H*0.78)],
     "#bfe3f0","#ffffff",1.5, 5)
label(ax, 0.4, 2.7, H*0.80, "fenêtre\nde toit", fs=7.5, color="#3a6b80", weight="normal")

# Titre + legende
ax.set_title("CHAMBRE 1 — vue d'ambiance  (lits superposés + lit invité)",
             fontsize=15, fontweight="bold", color=C["ink"], pad=10)
handles = [
    mpatches.Patch(color=C["bunk_f"], label="Lits superposés — 2 garçons"),
    mpatches.Patch(color=C["bed_f"],  label="Lit 120×200 — invité (2 pers.)"),
    mpatches.Patch(color=C["ward_f"], label="Penderie pleine hauteur"),
    mpatches.Patch(color=C["desk_f"], label="Bureau"),
    mpatches.Patch(color=C["box_f"],  label="Caissons sous-pente"),
]
ax.legend(handles=handles, loc="lower center", ncol=3, fontsize=9.5,
          frameon=False, bbox_to_anchor=(0.5,-0.04))

ax.text(0.5,0.965,"Mur ocre conservé (rappel de votre déco) • parquet clair • palette douce",
        transform=ax.transAxes, ha="center", fontsize=9, color="#8a7860", style="italic")

ax.autoscale_view()
ax.margins(0.05)
plt.tight_layout()
plt.savefig("/home/user/ella-caisse/chambre_design/vue_ambiance.png",
            dpi=140, facecolor="#faf6ef", bbox_inches="tight")
print("OK vue_ambiance.png")
