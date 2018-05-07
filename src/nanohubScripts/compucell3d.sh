#!/bin/sh

# necessary to enforce standard convention for numeric values specification on non-English OS
export LC_NUMERIC="C.UTF-8"

# export PREFIX_CC3D=/apps/compucell3d/r7/CompuCell3D
export PREFIX_CC3D=$(readlink -f $(dirname $0))

PYTHON_EXEC=/usr/bin/python

export MAX_NUMBER_OF_CONSECUTIVE_RUNS=50

COMPUCELL3D_PLUGIN_PATH=${PREFIX_CC3D}/lib/CompuCell3DPlugins
COMPUCELL3D_STEPPABLE_PATH=${PREFIX_CC3D}/lib/CompuCell3DSteppables

export LD_LIBRARY_PATH=${COMPUCELL3D_STEPPABLE_PATH}:${COMPUCELL3D_PLUGIN_PATH}:${PREFIX_CC3D}/lib/python:${PREFIX_CC3D}/lib:${VTK_LIB_DIR}:${LD_LIBRARY_PATH}
export SWIG_LIB_INSTALL_DIR=${PREFIX_CC3D}/lib/python
export PYTHON_MODULE_PATH=${PREFIX_CC3D}/pythonSetupScripts

COMPUCELL3D_MAJOR_VERSION=3
COMPUCELL3D_MINOR_VERSION=7
COMPUCELL3D_BUILD_VERSION=7

export SOSLIB_PATH=${PREFIX_CC3D}/examplesSoslib

echo "CompuCell3D - version $COMPUCELL3D_MAJOR_VERSION.$COMPUCELL3D_MINOR_VERSION.$COMPUCELL3D_BUILD_VERSION"

${PYTHON_EXEC} ${PREFIX_CC3D}/player5/compucell3d.pyw $* --currentDir=${PWD}
exit_code=$?

exit ${exit_code}
