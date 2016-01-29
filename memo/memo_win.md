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
