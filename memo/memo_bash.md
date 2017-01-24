# Memo bash

## Move Running process to background & Nohup 
* Into background :
	1. Ctrl-z
	2. jobs
	3. bg %jobnum (or bg)

* Into Nohup:
	1. Ctrl-z
	2. bg to run it in background
	3. disown -h (to mark job so that SIGHUP is not send to the job)
	4. exit

## Rename all filenames in $PWD with "TXT" suffix to a "txt" suffix. 
For example, "file1.TXT" becomes "file1.txt" . . .                  
```
SUFF=TXT
suff=txt
 
for i in $(ls *.$SUFF)
do
	mv -f $i ${i%.$SUFF}.$suff 
done 
```
> ${string%substring} Deletes shortest match of $substring from back of $string.

## ~/.vimrc File Example 
```
set nocp
syn on
set encoding=utf8
set autoindent
set expandtab
set tabstop=3
```

## Tableaux 
```
tab=( "el1" "el2")
for el in ${tab[*]}
do 
  echo $el
done
```

## Echanges de clés entre serveur  
** sur la machine cliente **
```
ssh-keygen -t dsa -b 1024
ssh-copy-id -i ~/.ssh/id_dsa.pub user@host \#fichier.pub généré par la cmd précédente 
```

Pour passer par un alias Editer / Créer le fichier ~/.ssh/config :
``` 
Host alias-remote
    User user-remote
    HostName host-remote
``` 
Pour se loguer : `ssh alias-remote`


** Generer une clé privée pour ssh ** 
`ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key`

Vérifier que le fichier /etc/ssh/sshd_config est configuré pour pointer vers cette clé dsa (HostKey ...)

Si modif du fichier redémarrer le service : `service sshd restart`

## Manipuler les dates 
```
date +%Y%m%d%H%M%S
date +%Y%m%d -d "yesterday"
date +%Y%m%d -d "next week"
date +%Y%m%d -d "next tuesday"
date +%Y%m%d -d "6 days ago"
```

## Générer des fichiers delta vides  
```
for i in {0..7} 
do 
	NOM_FIC="DELTAQ$(date +%Y%m%d -d "$i days ago")$(date +%Y%m%d%H%M%S -d "$i days ago")"; echo "$NOM_FIC;;0" > $NOM_FIC 
done
```

## Remplacer une chaine de caractere dans un fichier

`sed -i -e "s/chaines1/chaine2/g" fichier`

ex:
```
sed -i -e "s/;musicien;/;/g" RESULT_DRAK_SANS_EC_15422.txt
```

## Afficher la ligne X d'un fichier

`head -X fichier | tail -1`

ex: Afficher la ligne 72954
```
head -72954 RESULT_DRAK_SANS_EC_15422.txt | tail -1
```
