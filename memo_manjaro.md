# Notes sur l'installation de manjaro

## Création d'une clé bootable 

- Téléchargement de l'iso sur [Manjaro](http://manjaro.github.io/download/) : manjaro-kde-16.06.1-x86_64.iso
- Vérification du sha : `sha1sum -b manjaro-kde-16.06.1-x86_64.iso`
- Ecriture sur la clé :
  - `fdisk -l` : pour identifier le montage de la clé : *Disque /dev/sdc*
  - `dd bs=4M if=manjaro-kde-16.06.1-x86_64.iso of=/dev/sdc`

## Boot
