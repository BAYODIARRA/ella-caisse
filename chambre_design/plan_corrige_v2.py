#!/usr/bin/env python3
"""Chambre 1 - plan corrige v2. Pente DANS LA LONGUEUR:
porte (gauche) = HAUT 2.5m, fenetre (droite) = BAS 0.9m.
2 enfants en lits superposes (tete cote porte) + lit gigogne invite.
Fenetre NON bloquee. Passage le long d'un mur."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch
import numpy as np

C={"floor":"#f6efe2","wall":"#2f3640","win":"#bfe3f0","bunk":"#cdbfe0",
   "bunkf":"#b7a6d4","gig":"#f3d9a6","ward":"#9cc0d9","desk":"#f0e2c8",
   "ok":"#2e7d52","ink":"#2f3640","bench":"#d8c6a8"}
W,L=1.73,5.6
hi,lo=2.5,0.9
def h(x): return hi-(hi-lo)*x/L

fig=plt.figure(figsize=(13.5,7.4)); fig.patch.set_facecolor("#faf6ef")
gs=fig.add_gridspec(2,1,height_ratios=[1.55,1],hspace=0.42)

# ---------- TOP VIEW ----------
ax=fig.add_subplot(gs[0]); ax.set_facecolor("#faf6ef")
outline=[(0,0),(0,W),(L,W),(L,0),(1.0,0),(1.0,-0.55),(0,-0.55)]
ax.add_patch(Polygon(outline,closed=True,facecolor=C["floor"],
            edgecolor=C["wall"],lw=5,zorder=2))
# degrade plafond haut(gauche)->bas(droite)
for i in range(60):
    x0=L*i/60
    al=0.05+0.5*(x0/L)
    ax.add_patch(Rectangle((x0,0),L/60,W,facecolor="#caa46a",
                 alpha=al*0.6,edgecolor="none",zorder=2.3))
ax.text(0.55,W+0.18,"côté PORTE\nHAUT 2,5 m",ha="center",fontsize=8.5,
        color=C["ok"],fontweight="bold")
ax.text(L-0.55,W+0.18,"côté FENÊTRE\nBAS 0,9 m",ha="center",fontsize=8.5,
        color="#b07a31",fontweight="bold")
ax.annotate("le plafond descend  ▶",xy=(L-1.4,W-0.18),xytext=(1.4,W-0.18),
            fontsize=9,color="#7a6a4f",fontweight="bold",
            arrowprops=dict(arrowstyle="->",color="#7a6a4f",lw=1.5),va="center")

def bloc(x,y,w,h_,fc,ec,label,fs=8,tc="#2f3640",lw=2,z=5,ls="solid"):
    ax.add_patch(FancyBboxPatch((x,y),w,h_,boxstyle="round,pad=0.012,rounding_size=0.04",
                 facecolor=fc,edgecolor=ec,lw=lw,zorder=z,linestyle=ls))
    ax.text(x+w/2,y+h_/2,label,ha="center",va="center",fontsize=fs,
            color=tc,fontweight="bold",zorder=z+1)

# superposes tete cote porte (mur haut du plan)
bloc(0.12,0.80,1.90,0.90,C["bunk"],C["bunkf"],
     "LITS SUPERPOSÉS\n2 enfants · tête côté porte (2,5 m)",fs=8,z=6)
# gigogne deploye (tire au sol, milieu) - dashed
bloc(2.10,0.80,1.90,0.90,C["gig"],"#cda44e",
     "lit GIGOGNE invité\n(rangé dessous, tiré le soir)",fs=7.5,z=4,ls=(0,(5,3)))
# penderie coin porte haut (bas du plan)
bloc(0.12,0.04,0.62,0.62,C["ward"],"#5f93b3","PENDERIE",fs=7.5,tc="#234",z=6)
# bureau zone debout
bloc(0.95,0.0,0.95,0.50,C["desk"],"#c9a96b","bureau",fs=7.5,z=5)
# coffre bas sous fenetre (NE BLOQUE PAS)
bloc(4.35,0.95,1.15,0.72,C["bench"],"#b39a72","coffre / banc bas\n(sous la pente)",fs=7,z=5)
# passage
ax.add_patch(Rectangle((2.05,0.0),L-2.05-0.05,0.70,facecolor="#dff0e6",
             edgecolor=C["ok"],lw=1.2,ls=(0,(4,3)),zorder=3))
ax.text(3.6,0.34,"◀ PASSAGE LIBRE ▶",ha="center",fontsize=8.5,
        color=C["ok"],fontweight="bold",zorder=7)
# fenetre NON bloquee
ax.add_patch(Rectangle((L-0.02,0.45),0.16,0.85,facecolor=C["win"],
             edgecolor=C["wall"],lw=2,zorder=7))
ax.text(L+0.40,0.88,"FENÊTRE\ndégagée ✓",ha="center",va="center",
        fontsize=8,color="#3a6b80",fontweight="bold")
# entree decroche
ax.add_patch(Rectangle((0,-0.55),1.0,0.55,facecolor="#efe6d6",
             edgecolor=C["wall"],lw=2,ls=":",zorder=3))
ax.text(0.5,-0.28,"entrée\n(décroché)",ha="center",va="center",fontsize=7,
        color="#8a7860",zorder=4)
ax.set_xlim(-0.6,L+1.1); ax.set_ylim(-0.95,W+0.55)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("CHAMBRE 1 — vue de dessus : 2 enfants (superposés) + invité (gigogne)",
             fontsize=12.5,fontweight="bold",color=C["ink"],loc="left")

# ---------- LONGITUDINAL SECTION ----------
ax2=fig.add_subplot(gs[1]); ax2.set_facecolor("#faf6ef")
prof=[(0,0),(L,0),(L,lo),(0,hi)]
ax2.add_patch(Polygon(prof,closed=True,facecolor="#eef3ef",
              edgecolor=C["wall"],lw=3,zorder=2))
# zone debout h>=1.9 -> x<=2.1
xs=L*(hi-1.9)/(hi-lo)
ax2.add_patch(Polygon([(0,0),(xs,0),(xs,1.9),(0,hi)],closed=True,
              facecolor=C["ok"],alpha=0.16,zorder=3))
ax2.axvline(xs,color=C["ok"],ls="--",lw=1.1,zorder=4)
ax2.text(0.9,0.4,"debout OK",ha="center",fontsize=8,color=C["ok"],fontweight="bold")
# superpose schema cote porte
ax2.add_patch(Rectangle((0.12,0),1.9,0.55,facecolor=C["bunk"],edgecolor=C["bunkf"],lw=1.5,zorder=5))
ax2.add_patch(Rectangle((0.12,1.25),1.9,0.18,facecolor=C["bunkf"],edgecolor=C["bunkf"],lw=1,zorder=5))
ax2.text(1.05,1.55,"lit haut",ha="center",fontsize=7,color="#5b4b78",zorder=6)
ax2.text(1.05,0.27,"lit bas + gigogne",ha="center",fontsize=7,color="#5b4b78",zorder=6)
# window
ax2.add_patch(Rectangle((L-0.05,0.15),0.08,0.6,facecolor=C["win"],edgecolor=C["wall"],lw=1.5,zorder=6))
ax2.annotate("2,5 m",xy=(0,hi),xytext=(-0.45,hi-0.3),fontsize=8,
             arrowprops=dict(arrowstyle="->",lw=1),ha="center")
ax2.annotate("0,9 m",xy=(L,lo),xytext=(L+0.45,lo-0.1),fontsize=8,
             arrowprops=dict(arrowstyle="->",lw=1),ha="center")
ax2.text(L/2,-0.35,"longueur 5,60 m  (porte ◀  ▶ fenêtre)",ha="center",fontsize=8,color=C["ink"])
ax2.set_xlim(-0.7,L+0.8); ax2.set_ylim(-0.6,2.9)
ax2.set_aspect("equal"); ax2.axis("off")
ax2.set_title("Coupe dans la LONGUEUR — la pente descend vers la fenêtre",
              fontsize=11.5,fontweight="bold",color=C["ink"],loc="left")

plt.savefig("/home/user/ella-caisse/chambre_design/plan_corrige_v2.png",
            dpi=145,facecolor="#faf6ef",bbox_inches="tight")
print("OK plan_corrige_v2.png")
