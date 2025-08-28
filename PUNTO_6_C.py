import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGEN_1 = "porshe.png"
IMAGEN_2 = "maserati.png"

def auto_canny(gray, sigma=0.33):
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    v = np.median(blur)
    lower, upper = int(max(0, (1.0 - sigma) * v)), int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(blur, lower, upper)

def contornos_detallados(img_bgr):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    edges = auto_canny(gray)
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=1)
    conts, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    return conts, edges.shape

def dibujar_contornos(ax, conts, shape, titulo):
    h, w = shape[:2]
    for c in conts:
        x, y = c[:, 0, 0], c[:, 0, 1]
        ax.plot(x, y, linewidth=1)          # un solo color para todos
    ax.set_title(titulo)
    ax.invert_yaxis()
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(0, w); ax.set_ylim(h, 0)
    ax.set_xlabel("X (px)"); ax.set_ylabel("Y (px)")
    ax.grid(True, linewidth=0.3, alpha=0.5)

def main():
    img1 = cv2.imread(IMAGEN_1);  img2 = cv2.imread(IMAGEN_2)
    if img1 is None or img2 is None:
        raise FileNotFoundError("No se pudieron cargar las imágenes. Verifica nombres/rutas.")

    c1, sh1 = contornos_detallados(img1)
    c2, sh2 = contornos_detallados(img2)

    fig = plt.figure(figsize=(14, 8))
    ax1 = fig.add_subplot(2, 2, 1); ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3); ax4 = fig.add_subplot(2, 2, 4)

    ax1.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)); ax1.set_title(f"Original: {IMAGEN_1}"); ax1.axis("off")
    ax2.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)); ax2.set_title(f"Original: {IMAGEN_2}"); ax2.axis("off")

    dibujar_contornos(ax3, c1, sh1, f"Contornos: {IMAGEN_1}")
    dibujar_contornos(ax4, c2, sh2, f"Contornos: {IMAGEN_2}")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
