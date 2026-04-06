# 🩸 Widget Glycémie Windows (LibreLinkUp - VPN Friendly)

Un widget léger et discret pour Windows 10/11 qui affiche votre glycémie en temps réel. 

Ce projet est né d'un besoin spécifique : faire fonctionner le suivi de glycémie même lorsqu'un **VPN** est actif, ce qui bloque normalement les requêtes vers les serveurs LibreLinkUp.

## ✨ Points forts
- **Compatible VPN** : Utilise des réglages spécifiques (User-Agent iPhone et serveurs FR) pour éviter les erreurs de connexion.
- **Toujours visible** : Reste au-dessus des autres fenêtres (Always-on-top).
- **Design discret** : Pas de bordures, fond noir, texte coloré selon le taux.
- **Interactions** : Déplacez-le à la souris et fermez-le d'un clic.

## 🔴 Alertes Couleurs
- **Rouge** : Glycémie basse (< 70 mg/dL)
- **Jaune** : Glycémie haute (> 180 mg/dL)
- **Vert** : Glycémie dans la cible (80-170 mg/dL)

## 🚀 Installation rapide

1. **Installer Python** : 
   - Téléchargez Python sur [python.org](https://www.python.org/downloads/).
   - **Important** : Cochez la case **"Add Python to PATH"** lors de l'installation.

2. **Installer la bibliothèque nécessaire** :
   - Ouvrez votre terminal (tapez `cmd` dans la barre de recherche Windows).
   - Copiez-collez cette commande et appuyez sur Entrée :
     ```bash
     pip install pylibrelinkup
     ```

3. **Configurer le script** :
   - Téléchargez le fichier `glycemie_widget.pyw` de ce dépôt.
   - Faites un clic droit sur le fichier > **Ouvrir avec le bloc-notes**.
   - Remplacez `VOTRE_EMAIL` et `VOTRE_MOT_DE_PASSE` par vos vrais identifiants LibreLinkUp.
   - Enregistrez le fichier.

4. **Lancement** :
   - Double-cliquez sur `glycemie_widget.pyw`. Le widget apparaît sur votre bureau !

## 🖱️ Utilisation
- **Déplacer** : Cliquez n'importe où sur le widget avec le bouton gauche et glissez.
- **Quitter** : Cliquez sur la petite croix `×` en haut à droite.

## 📜 Crédits & Remerciements
- **[pajonp/pylibrelinkup](https://github.com/pajonp/pylibrelinkup)** : Pour la bibliothèque Python qui gère l'API LibreLinkUp.
- **Assistance IA** : Ce widget a été développé avec l'aide de ChatGPT pour la correction des erreurs VPN et l'interface Tkinter.

## ⚖️ Licence
Ce projet est distribué sous la licence **MIT**. Vous pouvez l'utiliser, le modifier et le partager librement.

---
*Note : Ce projet n'est pas affilié à Abbott. Utilisez-le uniquement à titre informatif.*