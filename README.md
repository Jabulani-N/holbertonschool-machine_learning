# holbertonschool-machine_learning
A Repository Implementing Machine Learning Techniques.

It is recommended to complete the projects in this repository via virtual environment. As such, instructions on installing vagrant (virtual machine) are included below.

- [holbertonschool-machine\_learning](#holbertonschool-machine_learning)
- [Using Vagrant on your personal computer](#using-vagrant-on-your-personal-computer)
  - [Mac](#mac)
  - [Windows](#windows)
  - [Ubuntu](#ubuntu)
- [Other Resources](#other-resources)

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

<p align="left">
    <details>
        <summary>Visual</summary>
        <img src="visual aid images/virtualbox%20visual%20aid%20images/image%201.jpg" width="600\"/><br>
    </details>
<br>
</p>
* start your virtual machine: `$ vagrant up`

image 2 goes here
<p align="left">
    <details>
        <summary>Visual</summary>
        <img src="visual aid images/virtualbox%20visual%20aid%20images/image%202.jpg" width="600\"/><br>
    </details>
<br>
</p>
* Enter your virtual machine: `$ vagrant ssh`

image 3 goes here
<p align="left">
    <details>
        <summary>Visual</summary>
        <img src="visual aid images/virtualbox%20visual%20aid%20images/image%203.jpg" width="600\"/><br>
    </details>
<br>
</p>

## Windows

[Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) and install it.

[Download Vagrant](https://developer.hashicorp.com/vagrant/downloads) and install it.

open command prompt

Add the Ubuntu 20.04 (Focal) image to your box list via:

* `vagrant box add ubuntu/focal64`
  * slow
  * [other image options](https://app.vagrantup.com/boxes/search)
image 4 goes here
<p align="left">
    <details>
        <summary>Visual</summary>
        <img src="visual aid images/virtualbox%20visual%20aid%20images/image%204.jpg" width="600\"/><br>
    </details>
<br>
</p>

create your first vm: `vagrant init ubuntu/focal64`

*  it will generate a Vagrantfile with base = "ubuntu/focal64" -you don’t have to execute this command line everyday, only once, to create a new virtual machine

  image 5 goese here
  <p align="left">
    <details>
        <summary>Visual</summary>
        <img src="visual aid images/virtualbox%20visual%20aid%20images/image%205.jpg" width="600\"/><br>
    </details>
<br>
</p>

  do `vagrant plugin install vagrant-vbguest` -> to avoid issue with the last version of Vagrant (2.2.4 or latest)

start your vm: `vagrant up`

image 6 goes here
<p align="left">
    <details>
        <summary>Visual</summary>
        <img src="visual aid images/virtualbox%20visual%20aid%20images/image%206.jpg" width="600\"/><br>
    </details>
<br>
</p>

enter your vm: `vagrant ssh`

image 7 goes here
<p align="left">
    <details>
        <summary>Visual</summary>
        <img src="visual aid images/virtualbox%20visual%20aid%20images/image%207.jpg" width="600\"/><br>
    </details>
<br>
</p>

## Ubuntu

open terminal

Install VirtualBox: `$ sudo apt-get install virtualbox`
Install Vagrant: `$ sudo apt-get install vagrant`
Add the Ubuntu 20.04 (Focal) image to your box list: `$ vagrant box add ubuntu/focal64` Warning: this step can take time

  * [other image options](https://app.vagrantup.com/boxes/search)
Create your first virtual machine:
`$ vagrant init ubuntu/focal64` -> it will generate a Vagrantfile with `base = "ubuntu/focal64"` - you don’t have to execute this command line everyday, only once, to create a new virtual machine
`$ vagrant up` -> it will start your virtual machine
`$ vagrant ssh` -> now you are inside your virtual machine.

# Other Resources

* [NumPy User Guide](https://numpy.org/doc/stable/user/quickstart.html)
