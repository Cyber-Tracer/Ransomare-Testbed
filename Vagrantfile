# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end

  config.vm.synced_folder ".", "/data/shared"
  config.vm.disk :disk, size: "50GB", name: "experiment_storage"

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
   config.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get install zfsutils-linux fastjar docker.io -y

     ls /dev > gg
     sleep 10
     ls /dev > gg2
     zpool create tank /dev/sdc
     zfs create -o mountpoint=/datasets tank/datasets
     

     cd /datasets
     for i in {000..030}; do
       curl https://digitalcorpora.s3.amazonaws.com/corpora/files/govdocs1/zipfiles/$i.zip | jar xv ;
     done

   SHELL
end
