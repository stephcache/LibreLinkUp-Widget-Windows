# Widget Glycémie LibreLinkUp pour Windows 🩸

Ce petit widget discret permet d'afficher votre glycémie en temps réel directement sur votre bureau Windows 10 ou 11.

Il a été spécialement optimisé pour fonctionner en France et même si vous utilisez un **VPN** (correction des erreurs de connexion 401/919).

## ✨ Caractéristiques
- **Anti-blocage VPN** : Configuration spécifique pour éviter les rejets des serveurs d'Abbott.
- **Toujours visible** : Reste au-dessus des autres fenêtres (Always on top).
- **Interface discrète** : Sans bordures, fond noir, déplaçable à la souris.
- **Alertes couleurs** : 
  - 🔴 Rouge : < 70 mg/dL (Hypo)
  - 🟡 Jaune : > 180 mg/dL (Hyper)
  - 🟢 Vert : Glycémie normale
- **Mode discret** : Se lance sans fenêtre de commande (format `.pyw`).

## 🚀 Installation

1. **Installer Python** : Téléchargez-le sur [python.org](https://www.python.org/) (cochez bien "Add Python to PATH").
2. **Installer la bibliothèque** : Ouvrez un terminal (CMD) et tapez :
   ```bash
   pip install pylibrelinkup