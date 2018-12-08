# Notes sur l'installation de manjaro

## Création d'une clé bootable 

- Téléchargement de l'iso sur [Manjaro](http://manjaro.github.io/download/) : manjaro-kde-16.06.1-x86_64.iso
- Vérification du sha : `sha1sum -b manjaro-kde-16.06.1-x86_64.iso`
- Ecriture sur la clé :
  - `fdisk -l` : pour identifier le montage de la clé : *Disque /dev/sdc*
  - `dd bs=4M if=manjaro-kde-16.06.1-x86_64.iso of=/dev/sdc`

## Boot

- Dans le BIOS (F2), désactiver le Fast-Boot et le Secure-Boot
- Redémarrer avec la clé USB et retourner dans le BIOS, la clé doit être visible dans les options de boot : passer en priorité 1

## Installation 

- Sur l'écran d'accueil : *Installer en utilisant thus*
- Choix de la langue et de la localisation
- Dans type d'installation : choisir le partitionnement (mode avancé) 
  - Créer une partition /boot/efi en fat32 (250 MB)
  - Créer une partition /
- Choix du fuseau horaire, disposition du clavier
- Création du user avec mot de passe
- Installation.

## Post installation

- Log in
- Réglage des paramètres d'affichage (écran hidpi : ajuster la mise à l'échelle coeff 2 ; augmenter la taille des polices ; règler les dpi des polices à 150...)
- Mise à jour pacman :
  - Mettre à jour la liste des miroirs triés par ping : `pacman-mirrors -g`
  - Synchroniser la base pacman : `pacman -Syy`
  - Mettre à jour le système : `pacman -Syu`
- Installer vi : 
  - `pacman -S vim`
  - Créer un lien vi vers vim : `ln -s vim /usr/bin/vi`
- Edition du fichier `~/.bashrc`
  - Ajouter les alias :
    - `alias ls = ls --color`
    - `alias ll = ls -l`
- Installer powerline

## Packages 

### Pacman

- eclipse-java
- git
- gimp
- inkscape
- blender

### AUR

- brackets (nodejs+npm)
- arduino
