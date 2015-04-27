#!/bin/bash
VASM_SPEC=vasm.spec
VASM_ARCHIVE=vasm.tar.gz
VASM_DAILY_URL=http://sun.hasenbraten.de/vasm/daily/${VASM_ARCHIVE}
# VLINK_ARCHIVE, VBCC_ARCHIVE, etc.
SOURCE_DIR=~/rpmbuild/SOURCES/
SPEC_DIR=~/rpmbuild/SPECS/

MYDIR=`pwd`

if [ -z "`which rpm`" ] ; then
	echo This script will work only on RPM-based distributions.
	exit 1
fi

if [ `id -u` -eq 0 ] ; then
	echo Please run this script as unprivileged user.
fi

if [ -z "`which wget`" ] ; then
	prereqs
	exit 2 
fi

mkdir -p $SOURCE_DIR 
cd $SOURCE_DIR
rm -f $VASM_ARCHIVE 
wget $VASM_DAILY_URL

mkdir -p $SPEC_DIR
cd $SPEC_DIR

cp -v $MYDIR/SPECS/$VASM_SPEC . 
rpmbuild -bb $VASM_SPEC

function prereqs() {
	echo Please install the following packages:
	echo wget tar gzip rpmbuild glibc-devel ...
}

