### see https://www.gnu.org/software/make/manual/make.html#Static-Pattern

# R repo to use
BASE=http://cran.r-project.org/src/contrib/

# Install dir to be used in RPM SPEC
R_INSTALL_DIR=/opt/R/R3/3.1.0/lib64/R/library

# Uncomment following line to use proxy server
export http_proxy=http://biocluster.agr.gc.ca:3128

##################################################################
## Do not edit below this line ###################################
##################################################################

.SUFFIXES: .tgz .spec

default: specs rpms

TGZ = tgz/maptools_0.8-30.tgz tgz/BoolNet_2.0.1.tgz
RPMS = tgz/maptools_0.8-30.rpm tgz/BoolNet_2.0.1.rpm
SPECS = tgz/maptools_0.8-30.spec tgz/BoolNet_2.0.1.spec

# $(TGZ):
# 	cd tgz; echo "${BASE}${*}.tar.gz" | sed 's/\/tgz\//\//' | wget -nc -i - 
# 	mv ${*}.tar.gz ${*}.tgz

# .tgz: $(TGZ)
# 	cd tgz; echo "${BASE}${*}.tar.gz" | sed 's/\/tgz\//\//' | wget -nc -i - 
# 	mv ${*}.tar.gz ${*}.tgz

.tgz.spec:
	cd tgz; echo "${BASE}${*}.tar.gz" | sed 's/\/tgz\//\//' | wget -nc -i - 
	mv ${*}.tar.gz ${*}.tgz
	./makeRpmFromR.sh ${R_INSTALL_DIR} ${*}.tgz
	touch ${*}.spec

.spec.rpm:
	touch ${*}.rpm

specs: $(TGZ:.tgz=.spec)

rpms: $(RPMS:.spec=.rpm)




