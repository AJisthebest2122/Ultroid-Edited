#!/usr/bin/env bash

# Ultroid Extended - Heroku Optimized Installer
# Based on Ultroid by TeamUltroid
# Modified for Heroku compatibility

echo "
            ┏┳┓╋┏┓╋╋╋╋┏┓┏┓
            ┃┃┣┓┃┗┳┳┳━╋╋┛┃
            ┃┃┃┗┫┏┫┏┫╋┃┃╋┃
            ┗━┻━┻━┻┛┗━┻┻━┛

      Ultroid Extended - Heroku Edition
      Installing dependencies...
"

# Install basic pip packages
pip3 install --no-cache-dir -r requirements.txt
pip3 install --no-cache-dir -r resources/startup/optional-requirements.txt

# Create necessary directories
if [ ! -d "pyUltroid/downloads" ]; then
    mkdir -p "pyUltroid/downloads"
fi

echo "
      Installation completed!
      Run the bot using 'bash startup'
"
