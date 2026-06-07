#!/usr/bin/env python3
"""Chambre 1 - planche d'ambiance couleur facon photo d'inspiration (mansarde verte,
lune + etoiles, lit bois naturel, linge gris). + palette + plan couleur."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, FancyBboxPatch, Wedge
import numpy as np

# ---- palette ----
GREEN="#3c564d"; GREEN_D="#33493f"; WHITE="#f3efe6"; WOOD="#c89b6b"; WOOD_D="#b07f4f"
GREY="#9aa0a3"; GREY_L="#c4c8ca"; TERRA="#c0714f"; SAGE="#a7b79d"; INK="#2f3640"
MOON="#d9d9d2"; STAR="#f2ead0"

L,Htop,Hlow=5.6,2.55,0.95

fig=plt.figure(figsize=(13,9)); fig.patch.set_facecolor("#faf6ef")
gs=fig.add_gridspec(2,1,height_ratios=[2.05,1],hspace=0.22)

# ============ HERO : elevation ambiance ============
ax=fig.add_subplot(gs[0]); ax.set_facecolor("#faf6ef")
# rampant blanc (lambris) au-dessus de la ligne de pente
ax.add_patch(Polygon([(0,Htop),(L,Hlow),(L,2.95),(0,2.95)],closed=True,
            facecolor=WHITE,edgecolor="#ddd6c6",lw=1,zorder=2))
for k in np.linspace(0.0,1.0,9):  # lignes lambris paralleles a la pente
    y0=Htop+k*(2.95-Htop); y1=Hlow+k*(2.95-Hlow)
    ax.plot([0,L],[y0,y1],color="#e3ddcd",lw=0.8,zorder=2.1)
# mur vert (sous la pente)
ax.add_patch(Polygon([(0,0),(L,0),(L,Hlow),(0,Htop)],closed=True,
            facecolor=GREEN,edgecolor=GREEN_D,lw=2,zorder=2.5))
# plinthe blanche
ax.add_patch(Rectangle((0,0),L,0.08,facecolor=WHITE,edgecolor="none",zorder=2.6))
# sol bois
ax.add_patch(Rectangle((0,-0.45),L,0.45,facecolor=WOOD,edgecolor="none",zorder=2))
for xx in np.arange(0.0,L,0.55):
    ax.plot([xx,xx-0.18],[0,-0.45],color=WOOD_D,lw=0.7,alpha=0.5,zorder=2.1)
ax.plot([0,L],[-0.22,-0.22],color=WOOD_D,lw=0.6,alpha=0.4,zorder=2.1)

# --- LUNE lumineuse + cordon ---
mx,my=1.05,1.92
ax.add_patch(Circle((mx,my),0.40,facecolor=MOON,edgecolor="#bcbcb2",lw=2,zorder=4))
for (cx,cy,cr) in [(-0.12,0.10,0.07),(0.14,0.06,0.05),(0.02,-0.15,0.09),(0.18,-0.12,0.04),(-0.16,-0.10,0.05)]:
    ax.add_patch(Circle((mx+cx,my+cy),cr,facecolor="#c7c7bf",edgecolor="none",zorder=4.1))
ax.add_patch(Circle((mx,my),0.40,facecolor="none",edgecolor="#fff7e0",lw=4,alpha=0.25,zorder=3.9))
ax.plot([mx,mx-0.05],[my-0.40,0.0],color="#eee",lw=1.2,zorder=3.8)
# --- ETOILES ---
def star(x,y,s,c=STAR):
    ang=np.linspace(0,2*np.pi,11)+np.pi/2
    r=np.where(np.arange(11)%2==0,s,s*0.4)
    ax.add_patch(Polygon(np.c_[x+r*np.cos(ang),y+r*np.sin(ang)],closed=True,
                 facecolor=c,edgecolor="none",zorder=4))
for (sx,sy,ss) in [(2.0,2.05,0.10),(2.45,1.75,0.07),(0.45,1.45,0.08),(1.75,1.5,0.06),
                   (2.3,2.25,0.05),(0.35,2.15,0.06),(1.4,2.2,0.05),(2.7,1.35,0.06),
                   (0.8,1.25,0.05),(2.05,1.15,0.05)]:
    star(sx,sy,ss)
for (sx,sy) in [(1.6,1.95),(2.6,2.0),(0.6,1.85),(2.2,1.55),(1.2,1.6)]:
    ax.add_patch(Circle((sx,sy),0.018,facecolor=STAR,edgecolor="none",zorder=4))

# --- petit singe (decal) bas gauche ---
sgx,sgy=0.38,0.30
ax.add_patch(Circle((sgx,sgy+0.05),0.20,facecolor="#8a5a3c",edgecolor="none",zorder=4))  # corps
ax.add_patch(Circle((sgx,sgy+0.30),0.15,facecolor="#9c6846",edgecolor="none",zorder=4.1)) # tete
ax.add_patch(Circle((sgx,sgy+0.27),0.10,facecolor="#d8b48c",edgecolor="none",zorder=4.2)) # face
for ex in (-0.13,0.13):
    ax.add_patch(Circle((sgx+ex,sgy+0.33),0.05,facecolor="#9c6846",edgecolor="none",zorder=4.2)) # oreilles
for ex in (-0.04,0.04):
    ax.add_patch(Circle((sgx+ex,sgy+0.30),0.012,facecolor="#3a2a1a",edgecolor="none",zorder=4.3)) # yeux

# --- LIT bas bois naturel avec barrieres ---
bx0,bx1=0.15,2.55; bt=0.40  # hauteur matelas
ax.add_patch(Rectangle((bx0,0),bx1-bx0,0.20,facecolor=WOOD,edgecolor=WOOD_D,lw=1.5,zorder=5))     # sommier
ax.add_patch(Rectangle((bx0,0.20),bx1-bx0,bt-0.20,facecolor=GREY_L,edgecolor=GREY,lw=1.2,zorder=5.1)) # matelas gris
# barriere tete (gauche) + montants
for px in np.linspace(bx0+0.05,bx0+0.05,1):
    pass
ax.add_patch(Rectangle((bx0,bt),0.05,0.42,facecolor=WOOD,edgecolor=WOOD_D,lw=1,zorder=5.3))  # montant tete
ax.add_patch(Rectangle((bx1-0.05,bt),0.05,0.42,facecolor=WOOD,edgecolor=WOOD_D,lw=1,zorder=5.3)) # montant pied
ax.add_patch(Rectangle((bx0,bt+0.38),bx1-bx0,0.05,facecolor=WOOD,edgecolor=WOOD_D,lw=1,zorder=5.3)) # rail haut
for bxx in np.arange(bx0+0.18,bx1-0.1,0.22): # barreaux
    ax.add_patch(Rectangle((bxx,bt),0.035,0.40,facecolor=WOOD,edgecolor=WOOD_D,lw=0.6,zorder=5.2))
# oreillers + plush
ax.add_patch(FancyBboxPatch((bx0+0.10,bt),0.55,0.16,boxstyle="round,pad=0.02,rounding_size=0.05",
             facecolor="#e9e9e6",edgecolor=GREY,lw=1,zorder=5.4))
ax.add_patch(Circle((1.55,bt+0.12),0.12,facecolor="#b9907a",edgecolor="none",zorder=5.4)) # plush ours
ax.add_patch(Circle((1.55,bt+0.22),0.09,facecolor="#c89e87",edgecolor="none",zorder=5.4))
ax.add_patch(FancyBboxPatch((1.95,bt),0.16,0.16,boxstyle="round,pad=0.01,rounding_size=0.08",
             facecolor=TERRA,edgecolor="none",zorder=5.4)) # coussin terracotta accent
# couverture pliee vert fonce facon photo
ax.add_patch(Rectangle((0.85,0.20),0.5,0.05,facecolor=GREEN_D,edgecolor="none",zorder=5.25))

ax.text(L-0.15,2.35,"rampant\nlambris blanc",ha="right",va="center",fontsize=8,
        color="#8a8470",style="italic",zorder=6)
ax.text(3.7,0.95,"mur vert sapin",ha="center",fontsize=10,color="#dfeae3",
        fontweight="bold",zorder=6)
ax.text(mx+0.55,my+0.2,"lune\nlumineuse",ha="left",va="center",fontsize=8.5,
        color="#f0ead8",fontweight="bold",zorder=6)

ax.set_xlim(-0.25,L+0.25); ax.set_ylim(-0.5,3.0); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("CHAMBRE 1 — ambiance « mansarde étoilée »  (façon ta photo d'inspiration)",
             fontsize=14,fontweight="bold",color=INK,loc="left",pad=8)

# ============ PALETTE + deco list ============
ax2=fig.add_subplot(gs[1]); ax2.set_facecolor("#faf6ef"); ax2.axis("off")
ax2.set_xlim(0,10); ax2.set_ylim(0,3)
swatches=[(GREEN,"Vert sapin\n(mur principal)"),(WHITE,"Blanc cassé\n(rampant/lambris)"),
          (WOOD,"Bois naturel\n(lit, étagères)"),(GREY,"Gris doux\n(linge de lit)"),
          (TERRA,"Terracotta\n(touches déco)"),(SAGE,"Sauge\n(alternative mur)")]
for i,(c,lab) in enumerate(swatches):
    x=0.3+i*1.62
    ax2.add_patch(FancyBboxPatch((x,1.55),1.35,1.1,boxstyle="round,pad=0.02,rounding_size=0.08",
                 facecolor=c,edgecolor="#cfc8b8",lw=1.5))
    ax2.text(x+0.675,1.25,lab,ha="center",va="top",fontsize=8,color=INK,fontweight="bold")
ax2.text(0.3,2.95,"PALETTE",fontsize=11,fontweight="bold",color=INK)
deco=("DÉCO petit budget :  • peinture vert sapin sur le mur du fond + lambris/rampant blanc"
      "   • stickers lune lumineuse + étoiles + 1 animal (singe)\n"
      "• parure de lit gris  • 1 coussin terracotta + guirlande lumineuse"
      "   • étagères bois + panier osier  • tapis doux clair")
ax2.text(0.3,0.85,deco,fontsize=8.7,color="#4a4a44",va="top",wrap=True)

plt.savefig("/home/user/ella-caisse/chambre_design/ambiance_chambre1.png",
            dpi=145,facecolor="#faf6ef",bbox_inches="tight")
print("OK ambiance_chambre1.png")
