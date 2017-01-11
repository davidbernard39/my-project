# Notes sur l'installation de LFS sur raspberrypi 1 b+

## Sources

[http://www.intestinate.com/pilfs/guide.html](http://www.intestinate.com/pilfs/guide.html)
[http://www.linuxfromscratch.org/lfs/](http://www.linuxfromscratch.org/lfs/)

(LFS version 7.10 utilisée à la rédaction du document)

## Manips

Configuration de la mémoire max pour le build : édition du /boot/config.txt
ajout de gpu_mem=16
`sudo reboot`

Définition d'un password pour le compte root
sudo passwd root
log en root : `su`

Vérification des prérequis [http://www.linuxfromscratch.org/lfs/view/stable/chapter02/hostreqs.html](http://www.linuxfromscratch.org/lfs/view/stable/chapter02/hostreqs.html)

```
$ bash version-check.sh
bash, version 4.3.30(1)-release
/bin/sh -> /bin/bash
Binutils: (GNU Binutils for Raspbian) 2.25
version-check.sh: line 11: bison: command not found
yacc not found
bzip2,  Version 1.0.6, 6-Sept-2010.
Coreutils:  8.23
diff (GNU diffutils) 3.3
find (GNU findutils) 4.4.2
version-check.sh: line 25: gawk: command not found
/usr/bin/awk -> /usr/bin/mawk
gcc (Raspbian 4.9.2-10) 4.9.2
g++ (Raspbian 4.9.2-10) 4.9.2
(Debian GLIBC 2.19-18+deb8u6) 2.19
grep (GNU grep) 2.20
gzip 1.6
Linux version 4.4.26+ (dc4@dc4-XPS13-9333) (gcc version 4.9.3 (crosstool-NG crosstool-ng-1.22.0-88-g8460611) ) #915 Thu Oct 20 17:02:14 BST 2016
version-check.sh: line 41: m4: command not found
GNU Make 4.0
GNU patch 2.7.5
Perl version='5.20.2';
sed (GNU sed) 4.2.2
tar (GNU tar) 1.27.1
version-check.sh: line 47: makeinfo: command not found
xz (XZ Utils) 5.1.0alpha
g++ compilation OK
```

Installation des outils manquants : `apt-get install bison gawk m4 texinfo`

Vérification des libs :

```
/home/pi# bash library-check.sh
libgmp.la: not found
libmpfr.la: not found
libmpc.la: not found
```

§2.4 Pas de nouvelle partition, le système est installé dans un répertoire de la partition existante /lfs

dans .profile on ajoute `export LFS=/lfs` puis `$ source ~/.profile`

dans /lfs créer un répertoire sources

Changer les droits du répertoire sources : sticky et writable `chmod -v a+wt $LFS/sources` (sticky permet de dire que les fichiers ne peuvent être supprimés que par le propriétaire même si plusieurs utilisateurs ont le droit d'écriture dessus)

dans /lfs/sources on récupère la liste des paquets à récupérer : `$ wget http://www.linuxfromscratch.org/lfs/view/stable/wget-list` et la liste de leur md5sums : `wget http://www.linuxfromscratch.org/lfs/view/stable/md5sums`

Ajout des paquets raspberry pi (pilfs) :
- http://www.intestinate.com/pilfs/patches/gcc-5.3.0-rpi1-cpu-default.patch
- http://www.intestinate.com/pilfs/patches/gcc-5.3.0-rpi2-cpu-default.patch
- http://www.intestinate.com/pilfs/patches/gcc-5.3.0-rpi3-cpu-default.patch
- http://www.intestinate.com/pilfs/scripts/ch5-build.sh
- http://www.intestinate.com/pilfs/scripts/ch6-build.sh
- http://www.intestinate.com/pilfs/scripts/pilfs-bootscripts-20160219.tar.xz
- https://github.com/raspberrypi/linux/archive/rpi-4.4.y.tar.gz
- https://github.com/raspberrypi/firmware/archive/master.tar.gz

Créer le répertoire qui va contenir les outils temporaires nécessaire à la construction de la LFS finale :

```
mkdir -v $LFS/tools
ln -sv $LFS/tools /
```

Créer un nouvel utilisateur et un nouveau groupe pour construire les outils :

```
groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs
```

`-m` permet de créer le home de l'utilisateur
`-k /dev/null` permet d'éviter la copie de fichiers skeleton dans le home du nouvel utilisateur

Donner un mdp à lfs : `passwd lfs`

fichier .bashrc spécifique pi :

```
set +h
umask 022
LFS=/lfs
LC_ALL=POSIX
LFS_TGT=$(uname -m)-lfs-linux-gnueabihf
PATH=/tools/bin:/bin:/usr/bin
export LFS LC_ALL LFS_TGT PATH
```

- Installation de binutils

## Notes suite à la lecture de LFS

### Standards LFS

LFS est compatible avec la norme [POSIX.1-2008](http://pubs.opengroup.org/onlinepubs/9699919799/) qui définit un système d'exploitation standard, son environnement incluant un interpréteur de commandes et tous les utilitaires nécessaires à la portabilité du code source (notamment fonctions et routines utilisées en C)

LFS est conforme à la hiérarchie des systèmes de fichiers (v 3.0) préconisée par le groupe de travail LSB de la Linux Foundation [http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html](http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

LFS remplit certaines conditions définies par la LSB (Linux Standard Base) version 5 [http://refspecs.linuxfoundation.org/lsb.shtml](http://refspecs.linuxfoundation.org/lsb.shtml) : définit les librairies qui doivent être présentes sur un système (librairies common, core, desktop, runtime language, imaging)

Voir [http://www.linuxfromscratch.org/lfs/view/stable/prologue/standards.html](http://www.linuxfromscratch.org/lfs/view/stable/prologue/standards.html) pour la liste des paquets remplissant les conditions (lfs et blfs)

### Les raisons de la présence des paquets 

Liste des paquets installés dans la LFS et pourquoi :
[http://www.linuxfromscratch.org/lfs/view/stable/prologue/package-choices.html](http://www.linuxfromscratch.org/lfs/view/stable/prologue/package-choices.html)