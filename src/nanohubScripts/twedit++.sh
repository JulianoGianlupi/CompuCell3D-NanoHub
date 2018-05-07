#!/bin/sh

# necessary to enforce standard convention for numeric values specification on non-English OS
export LC_NUMERIC="C.UTF-8"

# export PREFIX_CC3D=/apps/compucell3d/r7/CompuCell3D
export PREFIX_CC3D=$(readlink -f $(dirname $0))

PYTHON_EXEC=/usr/bin/python

export PYTHON_MODULE_PATH=${PREFIX_CC3D}/pythonSetupScripts
export SWIG_LIB_INSTALL_DIR=${PREFIX_CC3D}/lib/python

export LD_LIBRARY_PATH=${PREFIX_CC3D}/lib/python:${PREFIX_CC3D}/lib/:${LD_LIBRARY_PATH}

${PYTHON_EXEC} ${PREFIX_CC3D}/Twedit++5/twedit_plus_plus_cc3d.py $*
