Name:           ffmpeg2dirac
Version:        0.2.0
Release:        2%{?dist}
Summary:        Convert any file that ffmpeg can decode to dirac or theora

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://diracvideo.org
Source0:        http://downloads.sourceforge.net/dirac/ffmpeg2dirac-%{version}.tar.gz
Patch0:         ffmpeg2dirac-ffmpeg.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  scons

BuildRequires:  dirac-devel >= 1.0.2
BuildRequires:  ffmpeg-devel
BuildRequires:  libkate-devel >= 0.3.0
BuildRequires:  libtheora-devel
BuildRequires:  libogg-devel >= 1.1.0
BuildRequires:  libvorbis-devel
BuildRequires:  schroedinger-devel >= 1.0.6

%description
With ffmpeg2dirac, you can convert any file that ffmpeg can decode to Dirac or
Theora. right now the settings are hardcoded into the binary. the idea is to
provide ffmpeg2dirac as a binary along sites like diracvideo.org to enable as 
many people as possible to encode video clips with the same settings.


%prep
%setup -q
%patch0 -p1 -b .ff08

sed -i -e 's/1.0beta1/1.0/' SConstruct


%build
scons \
  prefix=%{_prefix} \
  mandir=PREFIX/share/man \
  APPEND_CCFLAGS="$RPM_OPT_FLAGS" \
  %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
scons \
  destdir=$RPM_BUILD_ROOT \
  prefix=%{_prefix} \
  mandir=PREFIX/share/man \
  APPEND_CCFLAGS="$RPM_OPT_FLAGS" \
  install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%doc subtitles.txt
%{_bindir}/ffmpeg2dirac
%{_mandir}/man1/ffmpeg2dirac.1.*


%changelog
* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

<<<<<<< ffmpeg2dirac.spec
* Sat Sep 03 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-1
- Update to 0.2.0

=======
* Thu Sep 22 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-1
- Update to 0.2.0
- Add Patch for FFmpeg-0.8

>>>>>>> 1.3
* Fri Oct 16 2009 kwizart <kwizart at gmail.com> - 0.1.0-4
- Rebuild for F-12

* Tue Apr 14 2009 kwizart < kwizart at gmail.com > - 0.1.0-3
- Better scons scheme
- Better description

* Mon Mar 23 2009 kwizart < kwizart at gmail.com > - 0.1.0-2
- Bump schroedinger-devel to 1.0.6

* Tue Mar 17 2009 kwizart < kwizart at gmail.com > - 0.1.0-1
- Initial Build

