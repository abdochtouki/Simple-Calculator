Initial commit¨
please copy and past this in your hooks ---->prepare-commmit-msg and delete.sample
#!/bin/bash

# Ce script vérifie si le sujet d'un commit Git commence par un numéro de ticket JIRA selon un format spécifique.

# Fichier contenant le message de commit (passé en argument)
HOOK_FILE="$1"

# Récupérer le sujet du commit (première ligne du fichier)
COMMIT_MSG=$(head -n1 "$HOOK_FILE")

# Motif à rechercher dans le sujet du commit (ajustez selon vos besoins)
PATTERN="ASC+-[0-9]+"

# Vérifier si le sujet correspond au motif
if [[ ! $(COMMIT_MSG) =~ $PATTERN ]]; then
  echo
  echo "ERREUR ! Mauvais format de message de commit."
  echo "'$COMMIT_MSG' ne contient pas de numéro de ticket JIRA valide."
  echo "Exemple : 'ASC-1234 : mon commit'"
  echo
  exit 1
fi