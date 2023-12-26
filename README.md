# SpotiGTA

A simple script to play Spotify music (or any other audio source) in GTA V.

It works by using the play/pause media key to play/pause the music in the background. Because of this, the program may
work in reverse, however pausing the music will resolve such an issue.

## Install

You must have [Python 3](https://www.python.org/downloads/) installed.

Then, download SpotiGTA from GitHub and unzip it.

Open command prompt and enter the directory where SpotiGTA is downloaded.

To change directories, use the `cd` command. See below example:

```bash
cd C:\Users\%USERNAME%\Downloads\SpotiGTA
```

Install requirements.

```bash
py -m pip install -r requirements.txt
```

Also, move all four files found in the `music` directory to the `User Music` directory in GTA V. (This is usually found
in `C:\Users\%USERNAME%\Documents\Rockstar Games\GTA V\User Music`.)

## Usage

Open command prompt and enter the directory where SpotiGTA is downloaded.

Run the program.

```bash
py spotigta.py
```

In GTA V, use the "Self Radio" station to play the music.

## Help

Open an issue or message me on Discord: `ucyt5040`.