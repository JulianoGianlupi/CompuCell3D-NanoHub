#!/bin/sh

# necessary to enforce standard convention for numeric values specification on non-English OS
export LC_NUMERIC="C.UTF-8"

# export PREFIX_CC3D=/apps/compucell3d/r7/CompuCell3D
export PREFIX_CC3D=$(readlink -f $(dirname $0))

PYTHON_EXEC=/usr/bin/python

CC3D_RUN_SCRIPT=${PREFIX_CC3D}/runScript.sh
OPTIMIZATIION_PYTHON_SCRIPT=${PREFIX_CC3D}/optimization/optimization.py

export PYTHON_MODULE_PATH=${PREFIX_CC3D}/pythonSetupScripts
export SWIG_LIB_INSTALL_DIR=${PREFIX_CC3D}/lib/python

export LD_LIBRARY_PATH=${PREFIX_CC3D}/lib/python:${PREFIX_CC3D}/lib/:${LD_LIBRARY_PATH}

${PYTHON_EXEC} ${OPTIMIZATIION_PYTHON_SCRIPT} $* --cc3d-run-script=${CC3D_RUN_SCRIPT} --clean-workdirs
