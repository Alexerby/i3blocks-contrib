# Disk size
Bash script for fetching available storage of a mount point.

## Configuration
```ini
[disk]
label=🖴 
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-disksize/i3blocks-disksize <mount_point>
interval=100
```

For mount points use ``df -a`` on command line (last column). 

### Example configuration
```ini
[disk]
label=🖴 
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-disksize/i3blocks-disksize /
interval=100

[Onedrive]
label=󰅟 
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-disksize/i3blocks-disksize ~/OneDrive
interval=100

[Dropbox]
label=󰇣 
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-disksize/i3blocks-disksize ~/Dropbox
interval=100
```

> Note that label may not be visible in this README markdown.
