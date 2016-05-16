# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64_GA-4.3.30"

  config.vm.network "forwarded_port", guest: 5001, host: 8000

  config.vm.provider "virtualbox" do |v|
    v.name = "flask_api_sample"
    v.memory = "1024"
    v.cpus = "2"
  end

  config.vm.provision :chef_solo do |chef|

    chef.version = "12.6"
    chef.log_level = "warn"
    
    chef.environment = "development"
    chef.roles_path = "./roles"
    chef.environments_path = "./environments"
    
    chef.add_role "api"
    chef.add_role "web"

  end

end