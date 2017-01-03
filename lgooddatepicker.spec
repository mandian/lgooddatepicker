%define oname LGoodDatePicker
%define lname %(echo %oname | tr [:upper:] [:lower:])

Summary:	Java Swing Date Picker
Name:		%{lname}
Version:	8.3.0
Release:	0
License:	MIT
Group:		Development/Java
URL:		https://github.com/%{oname}/%{oname}
Source0:	https://github.com/%{oname}/%{oname}/archive/v%{version}-Standard/%{name}-%{version}.tar.gz
#https://github.com/LGoodDatePicker/LGoodDatePicker/archive/v8.3.0-Standard.tar.gz
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	beansbinding

Requires:	java-headless >= 1.8
Requires:	jpackage-utils

%description
An Easy to use, good looking, nice features, and localized data picker written
in Java according to the JSR-310 standard.

%files -f .mfiles
%doc README.md
%doc LICENSE

#----------------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for %{name}
Requires:	jpackage-utils

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}-Standard
# Delete all prebuild binaries
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Remove failing depsnednry (use only for demo)
%pom_remove_dep :beansbinding ./Project

%build
%mvn_build -d -- -f ./Project

%install
%mvn install -- -f ./Project
