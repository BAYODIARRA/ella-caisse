#!/usr/bin/env python3
"""Chambre 1 - plan avec le LIT ACTUEL 120x200 (pas de nouveau lit).
Pente dans la longueur: porte=HAUT 2.5m, fenetre=BAS 0.9m.
Lit tete cote porte. Reste de la piece = passage + appoint invite. Fenetre degagee."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch

C={"floor":"#f6efe2","wall":"#2f3640","win":"#bfe3f0","bed":"#cdbfe0",
   "bedf":"#b7a6d4","ward":"#9cc0d9","bench":"#d8c6a8","ok":"#2e7d52","ink":"#2f3640"}
W,L=1.73,5.6
fig,ax=plt.subplots(figsize=(14,5.0)); fig.patch.set_facecolor("#faf6ef"); ax.set_facecolor("#faf6ef")

outline=[(0,0),(0,W),(L,W),(L,0),(1.0,0),(1.0,-0.55),(0,-0.55)]
ax.add_patch(Polygon(outline,closed=True,facecolor=C["floor"],edgecolor=C["wall"],lw=5,zorder=2))
# degrade plafond haut(gauche)->bas(droite)
for i in range(60):
    ax.add_patch(Rectangle((L*i/60,0),L/60,W,facecolor="#caa46a",
                 alpha=(0.05+0.5*(i/60))*0.6,edgecolor="none",zorder=2.3))
ax.text(0.55,W+0.18,"PORTE · HAUT 2,5 m",ha="center",fontsize=8.5,color=C["ok"],fontweight="bold")
ax.text(L-0.55,W+0.18,"FENÊTRE · BAS 0,9 m",ha="center",fontsize=8.5,color="#b07a31",fontweight="bold")
ax.annotate("le plafond descend  ▶",xy=(L-1.4,W-0.16),xytext=(1.6,W-0.16),fontsize=9,
            color="#7a6a4f",fontweight="bold",arrowprops=dict(arrowstyle="->",color="#7a6a4f",lw=1.5),va="center")

def bloc(x,y,w,h_,fc,ec,label,fs=8,tc="#2f3640",lw=2,z=5,ls="solid"):
    ax.add_patch(FancyBboxPatch((x,y),w,h_,boxstyle="round,pad=0.012,rounding_size=0.04",
                 facecolor=fc,edgecolor=ec,lw=lw,zorder=z,linestyle=ls))
    ax.text(x+w/2,y+h_/2,label,ha="center",va="center",fontsize=fs,color=tc,fontweight="bold",zorder=z+1)

# LIT 120x200 tete cote porte, contre le mur du haut
bloc(0.08,0.46,2.00,1.20,C["bed"],C["bedf"],"TON LIT  120 × 200\n(tête côté porte, 2,5 m)",fs=9,z=6)
ax.text(0.35,1.05,"☰\ntête",ha="center",va="center",fontsize=7,color="#5b4b78",zorder=7)
# penderie coin haut porte (bas-gauche, plafond 2.5)
bloc(0.10,0.02,0.66,0.40,C["ward"],"#5f93b3","penderie",fs=7.5,tc="#234",z=6)
# coffre bas sous fenetre (NE bloque pas)
bloc(4.45,0.50,1.05,1.15,C["bench"],"#b39a72","coffre /\nbanc bas",fs=7.5,z=5)
# zone libre / passage / appoint invite
ax.add_patch(Rectangle((2.15,0.0),2.15,W,facecolor="#dff0e6",edgecolor=C["ok"],lw=1.3,ls=(0,(4,3)),zorder=3))
ax.text(3.2,0.95,"ESPACE LIBRE\npassage + jeu\n(matelas d'appoint\ninvité possible ici)",
        ha="center",va="center",fontsize=8.5,color=C["ok"],fontweight="bold",zorder=7)
# fenetre degagee
ax.add_patch(Rectangle((L-0.02,0.55),0.16,0.75,facecolor=C["win"],edgecolor=C["wall"],lw=2,zorder=7))
ax.text(L+0.40,0.92,"FENÊTRE\ndégagée ✓",ha="center",va="center",fontsize=8,color="#3a6b80",fontweight="bold")
# entree decroche
ax.add_patch(Rectangle((0,-0.55),1.0,0.55,facecolor="#efe6d6",edgecolor=C["wall"],lw=2,ls=":",zorder=3))
ax.text(0.5,-0.28,"entrée\n(décroché)",ha="center",va="center",fontsize=7,color="#8a7860",zorder=4)
# cotes
ax.annotate("",xy=(0,W+0.42),xytext=(L,W+0.42),arrowprops=dict(arrowstyle="<->",color=C["ink"],lw=1.2))
ax.text(L/2,W+0.52,"5,60 m",ha="center",fontsize=9,color=C["ink"])
ax.annotate("",xy=(L+0.62,0),xytext=(L+0.62,W),arrowprops=dict(arrowstyle="<->",color=C["ink"],lw=1.2))
ax.text(L+0.80,W/2,"1,73 m",rotation=90,va="center",fontsize=9,color=C["ink"])

ax.set_xlim(-0.6,L+1.25); ax.set_ylim(-0.95,W+0.75); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("CHAMBRE 1 — plan avec TON lit actuel (120×200) · fenêtre dégagée · grand passage",
             fontsize=13,fontweight="bold",color=C["ink"],loc="left",pad=12)
plt.savefig("/home/user/ella-caisse/chambre_design/plan_lit_actuel.png",dpi=145,facecolor="#faf6ef",bbox_inches="tight")
print("OK plan_lit_actuel.png")
