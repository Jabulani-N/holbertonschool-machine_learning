# Linear Algebra

**Be sure you give your python files appropriate permissions**

 * [icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)

Installing Ubuntu 16.04 and Python 3.5

* Follow the instructions listed in `Using Vagrant on your personal computer`, with the caveat that you should be using `ubuntu/xenial64` instead of `ubuntu/trusty64`.

* Python 3.5 comes pre-installed on Ubuntu 16.04. How convenient! You can confirm this with `python3 -V`

Installing pip 19.1

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3 get-pip.py
    rm get-pip.py

To check that pip has been successfully downloaded, use pip -V. Your output should look like:

    $ pip -V
    pip 19.1.1 from /usr/local/lib/python3.5/dist-packages/pip (python 3.5)

Installing numpy 1.15, scipy 1.3, and pycodestyle 2.5

    $ pip install --user numpy==1.15
    $ pip install --user scipy==1.3
    $ pip install --user pycodestyle==2.5

To check that all have been successfully downloaded, use `pip list`.


## Tasks

### Task0

array slicing: https://numpy.org/doc/stable/user/basics.indexing.html

* indexes with negative numbers mean "from end"
  * for example, -2 means "number 2 from end." **-1 means "number at end."**
  * `[-3:-1]` means "number 3 from end until number 1 from end(last number)"

