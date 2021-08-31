%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rqt-plot
Version:        1.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_plot package

License:        BSD
URL:            http://wiki.ros.org/rqt_plot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       python%{python3_pkgversion}-matplotlib
Requires:       python%{python3_pkgversion}-numpy
Requires:       ros-rolling-python-qt-binding >= 0.2.19
Requires:       ros-rolling-qt-gui-py-common >= 0.2.25
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-rqt-gui
Requires:       ros-rolling-rqt-gui-py
Requires:       ros-rolling-rqt-py-common
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_plot provides a GUI plugin visualizing numeric values in a 2D plot using
different plotting backends.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Aug 31 2021 Mabel Zhang <mabel@openrobotics.org> - 1.1.0-1
- Autogenerated by Bloom

* Tue Apr 27 2021 Mabel Zhang <mabel@openrobotics.org> - 1.0.10-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Mabel Zhang <mabel@openrobotics.org> - 1.0.9-3
- Autogenerated by Bloom

