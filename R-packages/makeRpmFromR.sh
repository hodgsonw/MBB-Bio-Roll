#!/bin/env bash

function deleteIfExists {
    echo ""
}

function deleteIfExistsAndRecreate {
    echo ""
}

function makeSources {
    mkdir -p rpmbuild/${PACKAGE_NAME}/SOURCES/${PACKAGE_NAME}
    R CMD INSTALL $TGZ --library=rpmbuild/${PACKAGE_NAME}/SOURCES
    tar czvf rpmbuild/${PACKAGE_NAME}/SOURCES/${PACKAGE_NAME}_${VERSION}.tgz rpmbuild/${PACKAGE_NAME}/SOURCES/${PACKAGE_NAME}
    rm -rf rpmbuild/${PACKAGE_NAME}/SOURCES/${PACKAGE_NAME}
}

function makeSpec {
    mkdir -p rpmbuild/${PACKAGE_NAME}/{SPECS,SOURCES,RPMS}
    SOURCEDIR="rpmbuild/${PACKAGE_NAME}/SOURCES"
    makeSources

    OUT="rpmbuild/${PACKAGE_NAME}/SPECS/${PACKAGE_NAME}.spec"


    
DATETIME=`date`
cat >$OUT <<EOF
# R package: ${PACKAGE_NAME} SPEC file
# Generated ${DATETIME} by makeSpecFromR
%define name		${PACKAGE_NAME}
%define release		1
%define version 	${VERSION}
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	${TITLE}
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	${NAME}_${VERSION}.tgz
Packager:	makeSpecFromR
URL:            ${URL}
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        ${LICENSE}
AutoReq:	yes

%description
${DESCRIPTION}

%prep 
%setup -q -n ${NAME}_${VERSION}

%build

%install

EOF
}

function main {
    if  [[ $# -eq 0 ]]; then
	echo "Error: need R package tgz filename"
	exit 42
    fi
    export R_LIB_INSTALL_DIR=$1
    export TGZ=$2
    PACKAGE_NAME=`echo $TGZ | cut -c 5-| sed 's/ *_.*//'`

    if [[ -d tmp && ! -L tmp ]] || [[ ! -e tmp ]]; then
	rm -rf tmp
	mkdir tmp
    fi

    if [[ ! -e tmp ]]; then
    	mkdir tmp
    fi

    cd tmp
    gunzip -c ../$TGZ |tar xvf - ${PACKAGE_NAME}/DESCRIPTION
    # Use sed to deal with multi-line key:values
    sed ':a;N;$!ba;s/\n\+\([a-z,\ ]\)/ \1/g;' ${PACKAGE_NAME}/DESCRIPTION>${PACKAGE_NAME}/DESCRIPTION.s
    export NAME=`grep -h "^Package:" ${PACKAGE_NAME}/DESCRIPTION.s|sed 's/^[^:]*: //'`
    export URL=`grep -h "^URL:" ${PACKAGE_NAME}/DESCRIPTION.s|sed 's/^[^:]*: //'`
    export DESCRIPTION=`grep -h "^Description:" ${PACKAGE_NAME}/DESCRIPTION.s|sed 's/^[^:]*: //'`
    export LICENSE=`grep -h "^License:" ${PACKAGE_NAME}/DESCRIPTION.s|sed 's/^[^:]*: //'`
    export VERSION=`grep -h "^Version:" ${PACKAGE_NAME}/DESCRIPTION.s|sed 's/^[^:]*: //'`
    export TITLE=`grep -h "^Title:" ${PACKAGE_NAME}/DESCRIPTION.s|sed 's/^[^:]*: //'`
    rm -rf ${PACKAGE_NAME}
    cd ..

    makeSpec

    rm -rf tmp
}




################
main $@
################
