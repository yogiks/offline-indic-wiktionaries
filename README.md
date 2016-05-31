# offline-kn-wiktionary
Offline Kannada(ಕನ್ನಡ) wiktionary compiled sources from wikimedia XML dumps with aard-tools for aard dictionary.

## Download
Generated Aard file(.aar) can be downloaded from this [link](http://goo.gl/8RIy2V). After downloading, open the file in [Aard](http://aarddict.org/). Current stable version of Aard for Ubuntu can be downloaded [here](http://dl.aarddict.org/1dlemAz).

For [Aard 2](http://aarddict.org/), download the dictionary in new slob format from this [link](http://goo.gl/nVweNJ).

## Produce your own Aard file
Below are the instructions which can help you to generate your own Kannada wiktionary aard file to use it in Aard from Wikimedia xml dumps. I used Ubuntu 14.04 64-bit.

* Get the latest Kannada wiktionary xml dump [here](https://dumps.wikimedia.org/knwiktionary/latest/knwiktionary-latest-pages-articles.xml.bz2) which has all the pages/articles of [Kannada wiktionary](http://kn.wiktionary.org/).
```bash
wget https://dumps.wikimedia.org/knwiktionary/latest/knwiktionary-latest-pages-articles.xml.bz2
```
* Install the pre-requisites
```bash
sudo apt-get install libicu-dev

sudo dpkg -i aarddict_0.9.3-1_all.deb 

sudo apt-get install build-essential

sudo apt-get install python-dev

sudo apt-get install python-virtualenv

sudo apt-get install libevent-dev libxml2-dev libxslt1-dev
```
* Create Python virtual environment:
```bash
virtualenv env-aard
```
* Activate it:
```bash
source env-aard/bin/activate
```
* Install _Aard_ Tools:
```bash
sudo pip install -e git+git://github.com/aarddict/tools.git#egg=aardtools
```
* Get Kannada wiktionary site info:
```bash
sudo aard-siteinfo kn.wiktionary.org > knwiktionary.json
```
* Build mwlib article database:
```bash
sudo mw-buildcdb --input knwiktionary-latest-pages-articles.xml.bz2 --output knwiktionary-latest.cdb
```
* Since Kannada wiktionary is being compiled, make sure your system has Kannada(kn) locale:
```bash
sudo locale-gen kn
```
* Compile Kannada dictionary from the wiktionary article database:
```bash
sudo aardc wiki knwiktionary-latest.cdb knwiktionary.json
```
Verify that resulting dictionary has good metadata (description, license, source url), that “View Online” action works by opening it in Aard dictionary. For more detailed instructions on using Aard tools, have a look at [this](http://aarddict.org/aardtools/doc/aardtools.html) awesome documentation in Aard site. I've referred the same to write this.
