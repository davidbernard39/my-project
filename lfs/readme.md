# Notes sur l'installation de LFS sur Raspberry pi 1 b+ / Raspberry pi 2

## Sources

[http://www.intestinate.com/pilfs/guide.html](http://www.intestinate.com/pilfs/guide.html)
[http://www.linuxfromscratch.org/lfs/](http://www.linuxfromscratch.org/lfs/)

(LFS version 7.10 utilisée à la rédaction du document)

- 11/01/2017 : Tentative d'installation sur raspberry pi 1 b+ mais problème de compilation de gcc (certainement dû à un manque de RAM)
- 14/01/2017 : Passage de la sd sur un raspberry pi2 suppression des tools (binutils déjà compilé sur le pi1 avec architecture armv6) (autre solution non retenue : ajouter du swap sur le pi1)

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
- Installation de gcc 

patch pour tirer partie du fpu du raspberry pi: https://wiki.debian.org/ArmHardFloatPort/VfpComparison#FPU
```
--- gcc-5.3.0-orig/gcc/config.gcc	2016-03-15 12:42:09.000000000 -0700
+++ gcc-5.3.0/gcc/config.gcc	2016-03-15 12:46:31.000000000 -0700
@@ -1056,6 +1056,13 @@
 	    tmake_file="$tmake_file arm/t-linux-androideabi"
 	    ;;
 	esac
+	case ${target} in
+	arm*-*-*eabihf)
+	    with_cpu=${with_cpu:-cortex-a7}
+	    with_fpu=${with_fpu:-neon-vfpv4}
+	    with_float=${with_float:-hard}
+	    ;;
+	esac
 	# The EABI requires the use of __cxa_atexit.
 	default_use_cxa_atexit=yes
 	with_tls=${with_tls:-gnu}
```

patch pour le linker :
```
for file in \
 $(find gcc/config -name linux64.h -o -name linux.h -o -name sysv4.h -o -name linux-eabi.h -o -name linux-elf.h)
do
  cp -uv $file{,.orig}
  sed -e 's@/lib\(64\)\?\(32\)\?/ld@/tools&@g' \
      -e 's@/usr@/tools@g' $file.orig > $file
  echo '
#undef STANDARD_STARTFILE_PREFIX_1
#undef STANDARD_STARTFILE_PREFIX_2
#define STANDARD_STARTFILE_PREFIX_1 "/tools/lib/"
#define STANDARD_STARTFILE_PREFIX_2 ""' >> $file
  touch $file.orig
done
```

- Installation des headers linux (version de la raspberry foundation : wget https://github.com/raspberrypi/linux/archive/rpi-4.4.y.tar.gz)

- Installation de glibc

lien pour les ld-linux-armhf : `ln -sv ld-2.24.so $LFS/tools/lib/ld-linux.so.3`

- Installation de libstdc++
- Installation de binutils Pass #2
- Installation de gcc Pass #2
- Installation de tcl-core
- Installation de expect
- Installation de dejaGnu
- Installation de check
- Installation de ncurses
- Installation de bash
- Installation de bzip2
- Installation de coreutils
- Installation de diffutils
- Installation de file
- Installation de findutils
- Installation de gawk
- Installation de gettext
- Installation de grep
- Installation de gzip
- Installation de m4
- Installation de make
- Installation de patch
- Installation de perl
- Installation de sed
- Installation de tar
- Installation de texinfo
- Installation de util-linux
- Installtion de xz

Striping et suppression de de la doc :

```
strip --strip-debug /tools/lib/*
/usr/bin/strip --strip-unneeded /tools/{,s}bin/*
rm -rf /tools/{,share}/{info,man,doc}
```

Changement de /tools pour root : `chown -R root:root $LFS/tools`

Backup de /tools.

Création des répertoires et device nodes.

Montage des systemes de fichier virtuels du kernel.

Montage de la clé usb pour accès depuis l'environnement chroot : `mount -v --bind /cle/sources $LFS/sources/download`

Entrer dans l'environnement chroot : 
```
chroot "$LFS" /tools/bin/env -i \
    HOME=/root                  \
    TERM="$TERM"                \
    PS1='\u:\w\$ '              \
    PATH=/bin:/usr/bin:/sbin:/usr/sbin:/tools/bin \
    /tools/bin/bash --login +h
```

Création des répertoires FHS pour le système final.

Création de liens symbolique pour compatibilité de certains programmes.

Création des fichiers passwd, group

- Installation des headers Linux pour glibc
- Installation de man pages
- Installation de glibc

Lien symbolique pour arm : `ln -sv ld-2.24.so /lib/ld-linux.so.3`

Ajustement de la toolchain : utilisation de `$(gcc -dumpmachine)` au lieu de `$(uname -m)`

- Installation de zlib
- Installation de file
- Installation de binutils
- Installation de gmp 
- Installation de mpfr
- Installation de mpc
- Installation de gcc

## Notes suite à la lecture de LFS

### Standards LFS

LFS est compatible avec la norme [POSIX.1-2008](http://pubs.opengroup.org/onlinepubs/9699919799/) qui définit un système d'exploitation standard, son environnement incluant un interpréteur de commandes et tous les utilitaires nécessaires à la portabilité du code source (notamment fonctions et routines utilisées en C)

LFS est conforme à la hiérarchie des systèmes de fichiers (v 3.0) préconisée par le groupe de travail LSB de la Linux Foundation [http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html](http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

LFS remplit certaines conditions définies par la LSB (Linux Standard Base) version 5 [http://refspecs.linuxfoundation.org/lsb.shtml](http://refspecs.linuxfoundation.org/lsb.shtml) : définit les librairies qui doivent être présentes sur un système (librairies common, core, desktop, runtime language, imaging)

Voir [http://www.linuxfromscratch.org/lfs/view/stable/prologue/standards.html](http://www.linuxfromscratch.org/lfs/view/stable/prologue/standards.html) pour la liste des paquets remplissant les conditions (lfs et blfs)

### Les raisons de la présence des paquets 

Liste des paquets installés dans la LFS et pourquoi :
[http://www.linuxfromscratch.org/lfs/view/stable/prologue/package-choices.html](http://www.linuxfromscratch.org/lfs/view/stable/prologue/package-choices.html)
