# dotfiles

Dotfiles setup for Fedora.

## Installation

### 3. Install dependencies in a venv
```bash
pip install -r requirements.txt
```

## Usage

### Deploy
Run the deployment to install VSCode (requires sudo):

```bash
pyinfra @local deploy.py
```

# TODO
- Flameshot asennus ja shortcut prntscrniin
- Miten swaybarissa saa nätiks ton akun latingin, esim. vihreellä kun lataa, punasella kun alle 50% tms.
- Neofetch korvike
- zsh

# Notes

Video issues in current machine fixed installing codecs and drivers (requires `rpmfusion-free` and `rpmfusion-nonfree`):

`sudo dnf install libva-intel-media-driver libavcodec-freeworld mesa-va-drivers-freeworld`
