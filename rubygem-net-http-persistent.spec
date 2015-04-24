#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-net-http-persistent
Version  : 2.9.4
Release  : 4
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
/usr/lib64/ruby/gems/2.2.0/cache/net-http-persistent-2.9.4.gem
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/BufferedIO/cdesc-BufferedIO.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/SSLReuse/cdesc-SSLReuse.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/ca_file%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/ca_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/can_retry%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/cdesc-Persistent.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/cert%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/cert-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/cert_store%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/cert_store-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/certificate%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/certificate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/connection_close%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/connection_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/connection_keep_alive%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/debug_output-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/detect_idle_timeout-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/error_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/escape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/expired%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/finish-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/http_version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/http_versions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/idempotent%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/idle_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/keep_alive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/key%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/max_requests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/no_proxy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/normalize_uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/open_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/override_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/pipeline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/private_key%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/private_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/proxy%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/proxy_bypass%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/proxy_from_env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/proxy_uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/read_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/reconnect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/reconnect_ssl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/retry_change_requests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/reuse_ssl_sessions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/shutdown-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/shutdown_in_all_threads-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/socket_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/ssl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/ssl_version%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/ssl_version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/unescape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/verify_callback%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/verify_callback-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/verify_mode%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/Persistent/verify_mode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/HTTP/cdesc-HTTP.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/Net/cdesc-Net.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/page-History_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/net-http-persistent-2.9.4/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/.gemtest
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/History.txt
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/lib/net/http/faster.rb
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/lib/net/http/persistent.rb
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/lib/net/http/persistent/ssl_reuse.rb
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/test/test_net_http_persistent.rb
/usr/lib64/ruby/gems/2.2.0/gems/net-http-persistent-2.9.4/test/test_net_http_persistent_ssl_reuse.rb
/usr/lib64/ruby/gems/2.2.0/specifications/net-http-persistent-2.9.4.gemspec
