#!/bin/sh

# necessary to enforce standard convention for numeric values specification on non-English OS
export LC_NUMERIC="C.UTF-8"

export PREFIX_CC3D=$(readlink -f $(dirname $0))

export PYTHON_EXEC=/usr/bin/python

export MAX_NUMBER_OF_CONSECUTIVE_RUNS=50

cd $PREFIX_CC3D

export COMPUCELL3D_PLUGIN_PATH=${PREFIX_CC3D}/lib/CompuCell3DPlugins
export COMPUCELL3D_STEPPABLE_PATH=${PREFIX_CC3D}/lib/CompuCell3DSteppables
export VTK_INSTALL_PATH=/home/nanohub/anshaikh/VTK_INSTALL

export LD_LIBRARY_PATH=${COMPUCELL3D_STEPPABLE_PATH}:${COMPUCELL3D_PLUGIN_PATH}:${PREFIX_CC3D}/lib/python:${VTK_INSTALL_PATH}/lib:${PREFIX_CC3D}/lib/:$LD_LIBRARY_PATH

export SWIG_LIB_INSTALL_DIR=${PREFIX_CC3D}/lib/python
export PYTHON_MODULE_PATH=${PREFIX_CC3D}/pythonSetupScripts
export PYTHONPATH=${VTK_INSTALL_PATH}/lib/python2.7/site-packages:${PYTHONPATH}

export COMPUCELL3D_MAJOR_VERSION=3
export COMPUCELL3D_MINOR_VERSION=7
export COMPUCELL3D_BUILD_VERSION=7

export SOSLIB_PATH=${PREFIX_CC3D}/examplesSoslib

echo "CompuCell3D - version $COMPUCELL3D_MAJOR_VERSION.$COMPUCELL3D_MINOR_VERSION.$COMPUCELL3D_BUILD_VERSION"

export exit_code=0
${PYTHON_EXEC} ${PREFIX_CC3D}/../cc3d/player5/compucell3d.pyw $* --currentDir=${current_directory}
exit_code=$?

exit ${exit_code}
