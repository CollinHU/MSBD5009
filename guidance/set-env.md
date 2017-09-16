### attention

each user only have `100MB` for our home directory

you may need to put large files into `/tmp`, memory file system, but the data will be lost after reboot, which is done per day. you can make a directory to separate your files with others, e.g, `mkdir -p /tmp/yche`.

### add search path for executable

add `setenv PATH "${PATH}:/usr/local/software/openmpi/bin"` to your server file `~/.cshrc`, in order to let your shell environment able to find `mpicc` and `mpic++`

you can use `vim` to add this, or just echo and redirect(append `>>`, instead of override `>`) to your server file `~/.cshrc` as follows

```tcsh
echo setenv PATH "${PATH}:/usr/local/software/openmpi/bin" >> ~/.cshrc
```

after append, you can check as follows to see whether `/usr/local/software/openmpi/bin` is in your current shell environment searching path

```tcsh
echo $PATH
```

check if `mpicc` and `mpic++` work

```tcsh
mpicc
```

```tcsh
mpic++
```
