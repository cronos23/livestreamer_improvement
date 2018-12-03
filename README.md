# Streamlink Helper
Just a small script to pull followed online streams for opening in streamlink. Streamlink is a livestreamer fork, and can be found at https://github.com/streamlink/streamlink

## Installation

### With PIP
Install Python 3 (and Pip) if you don't have it, then run this in command prompt on Windows or the terminal in MacOS or Linux.
```bash
pip install streamlink_helper
```

### Manual
Make sure you have Python 3 and Git installed, then run this in git bash/command prompt on Windows or the terminal in MacOS or Linux.
```bash
git clone https://github.com/cronos23/streamlink_helper
cd streamlink_helper
python setup.py install
```
<b>Note</b>: On unix systems, the ```python``` command is usually assigned for python 2. In this case, you should run ```python3 setup.py install``` instead.

## Usage

In bash, cmd or powershell:
```
streamlink_helper
```
On first run you will be asked for your twitch.tv username and preferred stream quality. After this, these will be fetched from the configuration file. If you want to change your options, simply access the config file and change ask_on_startup to true, or configure the settings there.<br/><br/>
#### On Windows:
```
%APPDATA%\streamlink_helper\config.yml
```
#### On Linux/MacOS:
```
~/.config/streamlink_helper/config.yml
```
