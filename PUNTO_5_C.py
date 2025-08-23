import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def LETRA(letra, x, y):
    if letra == 'A':
        ax.plot([x, x+0.5, x+1], [y, y+1, y], color="black")
        ax.plot([x+0.25, x+0.75], [y+0.5, y+0.5], color="black")
    elif letra == 'B':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y+1, y+0.75], color="black")
        ax.plot([x+0.5, x], [y+0.75, y+0.5], color="black")
        ax.plot([x, x+0.5], [y+0.5, y+0.25], color="black")
        ax.plot([x+0.5, x], [y+0.25, y], color="black")
    elif letra == 'C':
        ax.plot([x+0.5, x], [y+1, y+1], color="black")
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y, y], color="black")
    elif letra == 'D':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.8], [y+1, y+0.5], color="black")
        ax.plot([x+0.8, x], [y+0.5, y], color="black")
    elif letra == 'E':
        ax.plot([x+0.5, x], [y+1, y+1], color="black")
        ax.plot([x, x+0.5], [y, y], color="black")
        ax.plot([x, x+0.5], [y+0.5, y+0.5], color="black")
        ax.plot([x, x], [y, y+1], color="black")
    elif letra == 'F':
        ax.plot([x, x+0.5], [y+1, y+1], color="black")
        ax.plot([x, x+0.5], [y+0.5, y+0.5], color="black")
        ax.plot([x, x], [y, y+1], color="black")
    elif letra == 'G':
        ax.plot([x+0.5, x], [y+1, y+1], color="black")
        ax.plot([x, x], [y, y+0.5], color="black")
        ax.plot([x, x+0.5], [y, y], color="black")
        ax.plot([x+0.5, x+0.5], [y+0.25, y+0.5], color="black")
        ax.plot([x+0.5, x+0.25], [y+0.25, y+0.25], color="black")
    elif letra == 'H':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y+0.5, y+0.5], color="black")
    elif letra == 'I':
        ax.plot([x+0.25, x+0.75], [y+1, y+1], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+1], color="black")
        ax.plot([x+0.25, x+0.75], [y, y], color="black")
    elif letra == 'J':
        ax.plot([x+0.75, x+0.75], [y+0.25, y+1], color="black")
        ax.plot([x+0.25, x+0.75], [y, y], color="black")
        ax.plot([x+0.25, x], [y, y+0.25], color="black")
    elif letra == 'K':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y+0.5, y+1], color="black")
        ax.plot([x, x+0.5], [y+0.5, y], color="black")
    elif letra == 'L':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y, y], color="black")
    elif letra == 'M':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.25], [y+1, y], color="black")
        ax.plot([x+0.25, x+0.5], [y, y+1], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+1], color="black")
    elif letra == 'N':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y+1, y], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+1], color="black")
    elif letra == 'O':
        ax.plot([x+0.5, x], [y+1, y+1], color="black")
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y, y], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+1], color="black")
    elif letra == 'P':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y+1, y+0.75], color="black")
        ax.plot([x+0.5, x], [y+0.75, y+0.5], color="black")
    elif letra == 'Q':
        ax.plot([x+0.5, x], [y+1, y+1], color="black")
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y, y], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+1], color="black")
        ax.plot([x+0.25, x+0.5], [y+0.25, y], color="black")
    elif letra == 'R':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y+1, y+0.75], color="black")
        ax.plot([x+0.5, x], [y+0.75, y+0.5], color="black")
        ax.plot([x+0.25, x+0.5], [y+0.5, y], color="black")
    elif letra == 'S':
        ax.plot([x+0.5, x], [y+1, y+1], color="black")
        ax.plot([x, x], [y+0.5, y+1], color="black")
        ax.plot([x, x+0.5], [y+0.5, y+0.5], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+0.5], color="black")
        ax.plot([x+0.5, x], [y, y], color="black")
    elif letra == 'T':
        ax.plot([x+0.25, x+0.75], [y+1, y+1], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+1], color="black")
    elif letra == 'U':
        ax.plot([x, x], [y, y+1], color="black")
        ax.plot([x+0.5, x+0.5], [y, y+1], color="black")
        ax.plot([x, x+0.5], [y, y], color="black")
    elif letra == 'V':
        ax.plot([x, x+0.25], [y+1, y], color="black")
        ax.plot([x+0.25, x+0.5], [y, y+1], color="black")
    elif letra == 'W':
        ax.plot([x, x+0.25], [y+1, y], color="black")
        ax.plot([x+0.25, x+0.5], [y, y+1], color="black")
        ax.plot([x+0.5, x+0.75], [y+1, y], color="black")
        ax.plot([x+0.75, x+1], [y, y+1], color="black")
    elif letra == 'X':
        ax.plot([x, x+0.5], [y+1, y], color="black")
        ax.plot([x, x+0.5], [y, y+1], color="black")
    elif letra == 'Y':
        ax.plot([x, x+0.25], [y+1, y+0.5], color="black")
        ax.plot([x+0.5, x+0.25], [y+1, y+0.5], color="black")
        ax.plot([x+0.25, x+0.25], [y, y+0.5], color="black")
    elif letra == 'Z':
        ax.plot([x, x-0.5], [y+1, y+1], color="black")
        ax.plot([x-0.5, x], [y, y+1], color="black")
        ax.plot([x, x+-.5], [y, y], color="black")
    else:
        ax.text(x, y, letra, fontsize=10)

#RECORRER
def NOMBRE(nombre,x,y, spacing=1.5):
    for i, char in enumerate(nombre):
        LETRA(char, x + i * spacing, y)

# NOMBRE
nombres = ['DANIEL', 'VALENTINA', 'LUIS']

#RECORRER NOMBRE
for i, nombre in enumerate(nombres):
    NOMBRE(nombre,x=0,y=-i*2)

#plot
ax.set_aspect('equal')
ax.set_xlim(-1, 15)
ax.set_ylim(-6,6)
plt.axis('off')
plt.show()
