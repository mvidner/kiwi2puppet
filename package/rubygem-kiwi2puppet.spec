#
# spec file for package kiwi2puppet
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
Name:           rubygem-kiwi2puppet
Version:        0.1.0
Release:        0
%define mod_name kiwi2puppet
#
Group:          Development/Languages/Ruby
License:        GPL v2 only
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
Requires:       ruby >= 1.8.6
Requires:	rubygem-nokogiri
#BuildRequires:  ruby-devel >= 1.8.6
#
Url:            http://github.com/mvidner/kiwi2puppet
Source:         %{mod_name}-%{version}.gem
#
Summary:        Convert KIWI image descriptions to Puppet manifests
%description

%prep
%build
%install
%gem_install %{S:0}
%gem_cleanup

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{mod_name}
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/

%changelog
