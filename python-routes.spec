%define tarname Routes

Summary:	Routing recognition and generation tools for Python

Name:		python-routes
Version:	2.0
Release:	1
Source0:	http://pypi.python.org/packages/source/R/Routes/Routes-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://routes.groovie.org/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST
pushd docs
export PYTHONPATH=`dir -d ../build/lib*`
make html
rm -f _build/html/.buildinfo
popd docs

%files -f FILE_LIST
%doc CHANGELOG LICENSE README docs/_build/html




