%w{ python-pip python-dev screen }.each do |p|
	package p
end

bash "install-requirements" do
	cwd "/vagrant"
	code <<-EOH
		pip install -r requirements.txt
	EOH
	user "root"
	action :run
end