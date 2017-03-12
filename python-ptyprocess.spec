#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests [require ptys support, so not on builders]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Run a subprocess in a pseudo terminal
Summary(pl.UTF-8):	Uruchamianie podprocesu w pseudoterminalu
Name:		python-ptyprocess
Version:	0.5.1
Release:	1
License:	ISC
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/ptyprocess/ptyprocess-%{version}.tar.gz
# Source0-md5:	94e537122914cc9ec9c1eadcd36e73a1
URL:		https://github.com/pexpect/ptyprocess
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%endif
%{?with_doc:BuildRequires:	sphinx-pdg}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 module to launch a subprocess in a pseudo terminal (pty), and
interact with both the process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a
password prompt that doesn't read from stdin, output that changes when
it's going to a pipe rather than a terminal, or curses-style
interfaces that rely on a terminal. If you need to automate these
things, running the process in a pseudo terminal (pty) is the answer.

%description -l pl.UTF-8
Moduł Pythona 2 do uruchamiania podprocesu w pseudoterminalu (pty) i
interakcji zarówno z procesem, jak i jego terminalem.

Czasem przekazywanie stdin i stdout przez potoki nie wystarcza. Może
tak być w przypadku zapytania o hasło nie czytającego ze standardowego
wejścia, a i wyjście czasem się zmienia, jeśli jest potokiem, a nie
terminalem, lub interfejsem w stylu curses zależnym od terminala.
Aby zautomatyzować takie sytuacje, rozwiązaniem jest uruchomienie
procesu w pseudoterminalu (pty).

%package -n python3-ptyprocess
Summary:	Run a subprocess in a pseudo terminal
Summary(pl.UTF-8):	Uruchamianie podprocesu w pseudoterminalu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-ptyprocess
Python 3 module to launch a subprocess in a pseudo terminal (pty), and
interact with both the process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a
password prompt that doesn't read from stdin, output that changes when
it's going to a pipe rather than a terminal, or curses-style
interfaces that rely on a terminal. If you need to automate these
things, running the process in a pseudo terminal (pty) is the answer.

%description -n python3-ptyprocess -l pl.UTF-8
Moduł Pythona 3 do uruchamiania podprocesu w pseudoterminalu (pty) i
interakcji zarówno z procesem, jak i jego terminalem.

Czasem przekazywanie stdin i stdout przez potoki nie wystarcza. Może
tak być w przypadku zapytania o hasło nie czytającego ze standardowego
wejścia, a i wyjście czasem się zmienia, jeśli jest potokiem, a nie
terminalem, lub interfejsem w stylu curses zależnym od terminala.
Aby zautomatyzować takie sytuacje, rozwiązaniem jest uruchomienie
procesu w pseudoterminalu (pty).

%package apidocs
Summary:	ptyprocess API documentation
Summary(pl.UTF-8):	Dokumentacja API ptyprocess
Group:		Documentation

%description apidocs
API documentation for ptyprocess.

%description apidocs -l pl.UTF-8
Dokumentacja API ptyprocess.

%prep
%setup -q -n ptyprocess-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:%{__python} -m unittest discover -s tests}
%endif

%if %{with python3}
%py3_build

%{?with_tests:%{__python3} -m unittest discover -s tests}
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/ptyprocess
%{py_sitescriptdir}/ptyprocess-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ptyprocess
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/ptyprocess
%{py3_sitescriptdir}/ptyprocess-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,*.html,*.js}
%endif
