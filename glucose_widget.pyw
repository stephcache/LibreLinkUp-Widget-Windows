import tkinter as tk
from pylibrelinkup import PyLibreLinkUp
import threading

# --- CONFIGURATION ---
EMAIL = "VOTRE_EMAIL"
PASSWORD = "VOTRE_MOT_DE_PASSE"
REGION = "EU"  # "EU", "US", etc.
REFRESH_RATE = 60

class GlucoseWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Glycémie")
        self.root.geometry("150x80")
        self.root.overrideredirect(True) # Supprime les bordures Windows
        self.root.attributes("-topmost", True) # Toujours au premier plan
        self.root.configure(bg='black')

        # --- AJOUT DU BOUTON FERMER (X) ---
        self.btn_close = tk.Button(root, text="×", command=self.root.destroy,
                                  bg="black", fg="#666666", font=("Arial", 12, "bold"),
                                  bd=0, highlightthickness=0, activebackground="red", 
                                  activeforeground="white", cursor="hand2")
        self.btn_close.place(x=125, y=0, width=25, height=25)
        
        # Effet au survol du bouton
        self.btn_close.bind("<Enter>", lambda e: self.btn_close.config(fg="white"))
        self.btn_close.bind("<Leave>", lambda e: self.btn_close.config(fg="#666666"))

        # --- ÉLÉMENTS VISUELS ---
        self.label_val = tk.Label(root, text="--", font=("Arial", 28, "bold"), fg="white", bg="black")
        self.label_val.pack(pady=(10, 0))

        self.label_trend = tk.Label(root, text="Chargement...", font=("Arial", 10), fg="gray", bg="black")
        self.label_trend.pack()

        # Permet de déplacer la fenêtre avec la souris
        self.x = 0
        self.y = 0
        self.root.bind("<Button-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.do_move)

        # --- LOGIQUE API / VPN ---
        self.client = PyLibreLinkUp(email=EMAIL, password=PASSWORD)
        
        # Correctif Headers pour contourner les blocages VPN
        self.client.headers = {
            "User-Agent": "LibreLinkUp/4.12.0 (iPhone; iOS 15.5; Scale/3.00)",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "product": "llp.ios",
            "version": "4.12.0",
            "Accept": "application/json",
            "Accept-Language": "fr-FR",
            "culture": "fr-FR"
        }

        # Lancement de la première mise à jour
        self.update_data()

    # --- FONCTIONS DE DÉPLACEMENT ---
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    # --- RÉCUPÉRATION DES DONNÉES ---
    def update_data(self):
        def fetch():
            try:
                # Forcer l'URL France
                self.client.base_url = "https://api-fr.libreview.io"

                self.client.authenticate()
                patients = self.client.get_patients()
                if patients:
                    p = patients[0]
                    data = self.client.read(p.patient_id)
                    val = data.current.value
                    trend_arrow = self.get_trend_arrow(data.current.trend)

                    # Mise à jour de l'interface (depuis le thread)
                    self.label_val.config(text=str(val), fg=self.get_color(val))
                    self.label_trend.config(text=f"{trend_arrow}", fg="gray")
                else:
                    self.label_trend.config(text="Aucun patient", fg="orange")
            except Exception as e:
                print(f"Erreur API : {e}")
                self.label_trend.config(text="Erreur VPN/API", fg="red")

            # Programmer la prochaine mise à jour
            self.root.after(REFRESH_RATE * 1000, self.update_data)

        # Lancer la requête dans un thread pour ne pas figer la fenêtre
        threading.Thread(target=fetch, daemon=True).start()

    def get_trend_arrow(self, trend):
        # 1: forte baisse, 2: baisse, 3: stable, 4: hausse, 5: forte hausse
        arrows = {1: "↓ Forte", 2: "↓", 3: "→", 4: "↑", 5: "↑ Forte"}
        return arrows.get(trend, "→")

    def get_color(self, val):
        if val < 70: return "#ff4d4d"  # Rouge (Hypo)
        if val > 180: return "#ffcc00" # Jaune (Hyper)
        return "#00ff00"                # Vert (OK)

if __name__ == "__main__":
    root = tk.Tk()
    app = GlucoseWidget(root)
    root.mainloop()