%define module	envisage
%define name 	python-%{module}
%define version 4.2.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Enthought Tool Suite - extensible application framework
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/envisage/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Obsoletes:	python-enthought-envisagecore
Obsoletes:	python-enthought-envisageplugins
Requires:	python-apptools >= 4.1.0
Requires:	python-traitsui >= 4.2.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx

%description
Envisage is a Python-based framework for building extensible
applications, that is, applications whose functionality can be
extended by adding "plug-ins". Envisage provides a standard mechanism
for features to be added to an application, whether by the original
developer or by someone else. In fact, when you build an application
using Envisage, the entire application consists primarily of
plug-ins. In this respect, it is similar to the Eclipse and Netbeans
frameworks for Java applications.

Each plug-in is able to:

* Advertise where and how it can be extended (its "extension points").
* Contribute extensions to the extension points offered by other plug-ins.
* Create and share the objects that perform the real work of the 
  application ("services").

The EnvisageCore project provides the basic machinery of the Envisage
framework. This project contains no plug-inn. You are free to use:

* plug-ins from the EnvisagePlugins project
* plug-ins from other ETS projects that expose their functionality as plug-ins
* plug-ins that you create yourself

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
%__python setup.py build_docs

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt *.rst examples/ build/docs/html/
%py_sitedir/%{module}*
