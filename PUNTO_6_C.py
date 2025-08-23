import cv2
import matplotlib.pyplot as plt

def obtener_todos_contornos(ruta_imagen, umbral=120):
    img = cv2.imread(ruta_imagen)
    if img is None:
        print(f"⚠️ No se pudo cargar {ruta_imagen}")
        return None, []
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, umbral, 255, cv2.THRESH_BINARY_INV)
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return img, contornos

logos = ["chevrolet.png", "mazda.png"]
plt.figure(figsize=(12, 6))

for i, logo in enumerate(logos):
    img, contornos = obtener_todos_contornos(logo, umbral=120)
    if img is not None:
        plt.subplot(2, len(logos), i+1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(f"Logo {logo.split('.')[0].capitalize()}")
        plt.axis("off")

        plt.subplot(2, len(logos), i+1+len(logos))
        for c in contornos:
            coords = c.squeeze()
            if coords.ndim == 2:
                plt.plot(coords[:, 0], coords[:, 1], color='red', linewidth=0.8)
        plt.gca().invert_yaxis()
        plt.axis('equal')
        plt.axis("off")
        plt.title(f"Contornos {logo.split('.')[0].capitalize()}")

plt.tight_layout()
plt.show()
