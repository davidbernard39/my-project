# VIM

## Configuration de base *.vimrc*

```
" Code
syntax on " Coloration syntaxique active

set expandtab " Remplace les tabs par des espaces (avec les 2 params suivants)
set shiftwidth=4 " Nombre d'espaces //Tab
set softtabstop=4 " Nombre d'espaces //Tab
set nobackup " Empeche de creer des fichiers ~
set noundofile " Empeche de creer des fichiers un~

" Indentation
set smartindent " Indente automatiquement en fonction du langage
set autoindent " Reproduit l'indentation de la ligne courante sur la suivante

" Encoding par defaut
set encoding=utf-8 " Encoding pour l'affichage
set fileencodings=utf-8 " Encoding a l'écriture du fichier
```

## Commandes utiles

- Supprimer la coloration syntaxique après une recherche : `:noh`
