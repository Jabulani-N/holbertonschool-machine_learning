# holbertonschool-machine_learning
A Repository Implementing Machine Learning Techniques

# Using Vagrant on your personal computer

## Mac

[Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) and install it.

[Download Vagrant](https://developer.hashicorp.com/vagrant/downloads) and install it.

Open Terminal

* `$ vagrant box add ubuntu/focal64`
* * this may be slow
  * [other image options](https://app.vagrantup.com/boxes/search)
* create your first virtual machine: `$ vagrant init ubuntu/focal64`
  * it will generate a Vagrantfile with `base = "ubuntu/focal64"` - you don’t have to execute this command line everyday, only once, to create a new virtual machine
 
image 1 goes here

* start your virtual machine: `$ vagrant up`

image 2 goes here

* Enter your virtual machine: `$ vagrant ssh`

image 3 goes here

## Windows

[Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) and install it.

[Download Vagrant](https://developer.hashicorp.com/vagrant/downloads) and install it.

open command prompt

Add the Ubuntu 20.04 (Focal) image to your box list via:

* `vagrant box add ubuntu/focal64`
  * slow
  * 
image 4 goes ehre

create your first vm: `vagrant init ubuntu/focal64`

*  it will generate a Vagrantfile with base = "ubuntu/focal64" -you don’t have to execute this command line everyday, only once, to create a new virtual machine

  image 5 goese here

  do `vagrant plugin install vagrant-vbguest` -> to avoid issue with the last version of Vagrant (2.2.4 or latest)

start your vm: `vagrant up`

image 6 goes here

enter your vm: `vagrant ssh`

image 7 goes here

## Ubuntu

open terminal

Install VirtualBox: `$ sudo apt-get install virtualbox`
Install Vagrant: `$ sudo apt-get install vagrant`
Add the Ubuntu 20.04 (Focal) image to your box list: `$ vagrant box add ubuntu/focal64` Warning: this step can take time

Create your first virtual machine:
`$ vagrant init ubuntu/focal64` -> it will generate a Vagrantfile with `base = "ubuntu/focal64"` - you don’t have to execute this command line everyday, only once, to create a new virtual machine
`$ vagrant up` -> it will start your virtual machine
`$ vagrant ssh` -> now you are inside your virtual machine.
