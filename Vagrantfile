# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "alvistack/ubuntu-22.04"

  # via 127.0.0.1 to disable public access
  config.vm.network "forwarded_port", guest: 5601, host: 5601, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 9200, host: 9200, host_ip: "127.0.0.1"

  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 2
    vb.memory = "8192"
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
  SHELL
end
