lib_LTLIBRARIES = armory.la

armory_la_SOURCES = armory.cpp
armory_la_CPPFLAGS= -I$(top_srcdir)/include -I$(top_srcdir)/plugins/plugin_utils
armory_la_LDFLAGS = -module -avoid-version -shared
armory_la_LIBADD = $(top_builddir)/plugins/plugin_utils/libplugin_utils.la

AM_CPPFLAGS = $(CONF_CPPFLAGS)
AM_CFLAGS = $(CONF_CFLAGS)
AM_CXXFLAGS = $(CONF_CXXFLAGS)

EXTRA_DIST = \
	README.armory.txt \
	armory.def \
	armory.sln \
	armory.vcxproj

MAINTAINERCLEANFILES =	\
	Makefile.in
