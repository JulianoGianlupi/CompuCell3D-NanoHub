.PHONY: all install clean distclean

all:
	. /etc/environ.sh; use -e -r pyqt5-5.10.1; use -e -r vtk-6.3.0; \
                      installHome=$$(readlink -f ../CompuCell3D); mkdir -p build; cd build; \
                      cmake -DCMAKE_INSTALL_PREFIX=$${installHome} \
                            -DCMAKE_BUILD_TYPE=Release \
                            -DPYTHON_EXECUTABLE=/usr/bin/python \
                            -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
                            -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
                            -DVTK_DIR=$${VTK_LIB_DIR} \
                            ../CompuCell3D ; \
                            make all

install: all
	. /etc/environ.sh; use -e -r pyqt5-5.10.1; use -e -r vtk-6.3.0; cd build; make install
	install --mode 0755 -D nanohubScripts/compucell3d.sh ../CompuCell3D
	install --mode 0755 -D nanohubScripts/optimization.sh ../CompuCell3D
	install --mode 0755 -D nanohubScripts/paramScan.sh ../CompuCell3D
	install --mode 0755 -D nanohubScripts/runScript.sh ../CompuCell3D
	install --mode 0755 -D nanohubScripts/twedit++.sh ../CompuCell3D

clean:
	rm -rf build

distclean: clean
	rm -rf ../CompuCell3D

