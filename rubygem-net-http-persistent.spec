#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-net-http-persistent
Version  : 2.9.4
Release  : 7
URL      : https://rubygems.org/downloads/net-http-persistent-2.9.4.gem
Source0  : https://rubygems.org/downloads/net-http-persistent-2.9.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rdoc

%description
= net-http-persistent
* http://docs.seattlerb.org/net-http-persistent
* https://github.com/drbrain/net-http-persistent

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n net-http-persistent-2.9.4
gem spec %{SOURCE0} -l --ruby > rubygem-net-http-persistent.gemspec

%build
gem build rubygem-net-http-persistent.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
net-http-persistent-2.9.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/net-http-persistent-2.9.4
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/net-http-persistent-2.9.4.gem
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/.autotest
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/History.txt
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/lib/net/http/faster.rb
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/lib/net/http/persistent.rb
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/lib/net/http/persistent/ssl_reuse.rb
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/test/test_net_http_persistent.rb
/usr/lib64/ruby/gems/2.3.0/gems/net-http-persistent-2.9.4/test/test_net_http_persistent_ssl_reuse.rb
/usr/lib64/ruby/gems/2.3.0/specifications/net-http-persistent-2.9.4.gemspec
