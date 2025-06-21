#!/bin/bash

# Navega para o diretório onde este script está (pasta raiz do projeto)
cd "$(dirname "$0")"

# Ativa o ambiente virtual
source venv/bin/activate

# Executa o seu script Python principal
# Verifique se o nome do arquivo está correto e qual é o seu script principal
python batalhaVerificada.py

# Opcional: Desativa o ambiente virtual no final, se você quiser que seu terminal volte ao normal
# remove o '#' abaixo se quiser desativar automaticamente
# deactivate