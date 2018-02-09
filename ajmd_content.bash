# ajmd_content bash initialization script for dev instances.
#
# Usage (I think .bash_profile is the correct place for this if you want
# it in all your shells.  It's important to use the source command instead
# of executing it directly):
#   source ~/path/to/ajmd_content/script/ajmd_content.bash
#
# Support for non-bash shells is left as an exercise for the reader.

# Get the root of the hg checkout.
ROOT=$(dirname $(dirname ${BASH_SOURCE[0]}))

# Convert to absolute path
ROOT=$(cd $ROOT; pwd)
echo $ROOT

# AJMD_HOME is used to set the later variables and also in .hgrc
export AJMD_HOME=$ROOT

# Python environment.
# export PATH=~/envs/ajmd_content-dev/bin:$PATH
export PYTHONPATH=$AJMD_HOME
echo $PYTHONPATH

# Additional scripts.  Optional but convenient.
export PATH=$AJMD_HOME/script:$PATH

echo $PATH
