FOLDERS=BUILD SRPMS
SPEC=wise-2.4.1.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}
	rpm -qplv ./RPMS/x86_64/*.rpm 

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
