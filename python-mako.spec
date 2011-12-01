%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: python-mako
Version: 0.3.4
Release: 1%{?dist}
Summary: Mako template library for Python

Group: Development/Languages
License: MIT
URL: http://www.makotemplates.org/
Source0: http://www.makotemplates.org/downloads/Mako-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: python-setuptools-devel
BuildRequires: python-nose
BuildRequires: python-markupsafe

Requires: python-beaker
Requires: python-markupsafe

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.


%prep
%setup -q -n Mako-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%check
PYTHONPATH=$(pwd) nosetests
 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README doc examples
%{_bindir}/mako-render
%{python_sitelib}/*


%changelog
* Wed Jul 14 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.4-1
- rebase to 0.3.4; add requirement on python-markupsafe
Resolves: rhbz#608155
- add %%check section, adding build-time requirements on python-nose and
python-markupsafe

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.10-3
- Rebuild for Python 2.6

* Sun May 11 2008 Kyle VanderBeek <kylev@kylev.com> - 0.1.10-2
- Fix rpmlint warnings.
- Add docs and examples.

* Wed Apr  9 2008 Kyle VanderBeek <kylev@kylev.com> - 0.1.10-1
- Initial version.
