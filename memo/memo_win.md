# Memo Windows

## Ajouter un équivalent de .bashrc a cmd

Dans la base de registre `regedit`, dans HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor :
Ajouter la "Valeur chaine" AutoRun=C:\path\to\file\bashrc.cmd

ex de bashrc.cmd :
```
@echo off
doskey ll=ls -l $*
doskey vi=vim $*
``` 

## Ajouter un menu contextuel à un répertoire pour l'ouvrir dans cmd

1. Dans la base de registre `regedit`, dans HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell : Clic droit sur shell > New Key "Command Prompt"

2. Modifier la valeur par défaut avec le texte à afficher dans le menu contextuel : "Ouvrir dans cmd"

3. Clic droit sur Command Prompt > New Key "Command"

4. Modifier la valeur par défaut Cmd.exe /k pushd %L 

