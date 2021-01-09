#!/bin/sh

##
# Run the whole process in sequence
# Eg. sh ./start.sh /home/youruser/path/to/virtualenv

set -e

ENVPATH=${1}

# Activate env
. ${ENVPATH}/bin/activate

# Update deps
(pip3 install -r ./requirements.txt) || true

# Load up .env
export $(egrep -v '^#' .env | xargs)

# Exec
python3 ./ir.py --do check_environment_variables

echo "Env OK"

python3 ./ir.py --do busca_trades_e_faz_merge_operacoes

echo "Busca OK"

python3 ./ir.py --do calculo_ir

echo "Calculo OK"
