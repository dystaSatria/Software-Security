
# Kali Linux Terminal 

#### Basic Navigation
- `pwd` - Prints the current directory.
- `ls` - Lists the contents of a directory.
- `cd` - Changes the directory.
- `cd ~` - Goes back to the home directory.
- `cd ..` - Moves up one level in the directory.

#### File and Directory Management
- `touch` - Creates a new file.
- `mkdir` - Creates a new directory.
- `rm` - Deletes a file.
- `rm -r` - Deletes a directory and its contents.
- `cp` - Copies files or directories.
- `mv` - Moves or renames files or directories.

#### File Permission
- `chmod` - Changes the file or directory permissions.
- `chown` - Changes the owner of a file or directory.

#### Package Management
- `apt update` - Updates the list of packages and their versions.
- `apt upgrade` - Upgrades all installed packages.
- `apt install [package_name]` - Installs a new package.
- `apt remove [package_name]` - Removes a package.

#### Networking
- `ifconfig` - Displays network configuration.
- `ping [ip_address]` - Tests connectivity to an IP address.
- `netstat -tuln` - Displays listening ports.

#### System
- `top` - Displays running processes.
- `df` - Displays disk usage.
- `free` - Displays memory usage.

#### Searching for Files
- `find / -name [file_name]` - Searches for a file in the system.
- `grep [text] [file]` - Searches for text within a file.

#### Security Tips
- Always use `sudo` to run commands that require root privileges.
- Regularly update your system with `apt update` and `apt upgrade`.
- Change the default password to a strong one using `passwd`.
- Disable services that are not being used to reduce attack vectors.

#### Miscellaneous
- `echo [text]` - Displays text.
- `|` (pipe) - Sends the output from one command to another command.
- `>` - Redirects output to a file.
- `nano [file]` / `vim [file]` - Opens a text editor to edit files.

### Conclusion
This cheatsheet only covers the basics of using the terminal in Kali Linux and is not meant to be a comprehensive guide. For more detailed information and advanced commands, referring to the official Kali Linux documentation and man pages (`man [command]`) is highly recommended.
