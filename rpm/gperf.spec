Name:       gperf
Summary:    A perfect hash function generator
Version:    3.1
Release:    1
License:    GPLv3+
URL:        http://www.gnu.org/software/gperf/
Source0:    %{name}-%{version}.tar.bz2
Patch0:     no-doc-creation.patch
BuildRequires: autoconf

%description
Gperf is a perfect hash function generator written in C++. Simply stated,
a perfect hash function is a hash function and a data structure that allows
recognition of a key word in a set of words using exactly one probe into
the data structure.
For a given list of strings, it produces a hash function and hash table,
in form of C or C++ code, for looking up a value depending on the input string.
The hash function is perfect, which means that the hash table has no collisions,
and the hash table lookup needs a single string comparison only.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
# autogen.sh calls gnulib-tool which checks for AC_PREREQ() existence in configure.ac,
# doesn't find it and fails.
# So do all these actions instead of the autogen.sh:
for file in build-aux/install-sh build-aux/mkinstalldirs \
            build-aux/compile build-aux/ar-lib; do
  cp ../gnulib/$file $file
done
chmod a+x build-aux/install-sh build-aux/mkinstalldirs \
          build-aux/compile build-aux/ar-lib

make -f Makefile.devel totally-clean all

%configure --disable-static
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
