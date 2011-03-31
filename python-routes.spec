%define tarname Routes
%define name	python-routes
%define version 1.12.3
%define release %mkrel 1

Summary:	Routing recognition and generation tools for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/R/%{tarname}/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://routes.groovie.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-pkg-resources
Requires:	python-webob
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx, python-webob

%description
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to application actions, and conversely to generate
URLs. Routes makes it easy to create pretty and concise URLs that are
RESTful with little effort.

Routes allows conditional matching based on domain, cookies, HTTP
method, or a custom function. Sub-domain support is built in. Routes
comes with an extensive unit test suite.

%prep
%setup -q -n %{tarname}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
export PYTHONPATH=`dir -d ../build/lib*`
make html
rm -f _build/html/.buildinfo
popd docs

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGELOG LICENSE README docs/_build/html

