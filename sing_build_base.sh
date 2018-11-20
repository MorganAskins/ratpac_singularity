SINGULARITY_TMPDIR=$(pwd)/tmp
SINGULARITY_CACHEDIR=$(pwd)/.singularity
SINGULARITY_LOCALCACHEDIR=$(pwd)/tmp
TMPDIR=$(pwd)/tmp

mkdir -p $SINGULARITY_TMPDIR
mkdir -p $SINGULARITY_CACHEDIR

echo $SINGULARITY_TMPDIR
echo $SINGULARITY_CACHEDIR

export SINGULARITY_TMPDIR
export SINGULARITY_CACHEDIR
export TMPDIR

if [[ $EUID -ne 0 ]]; then
  echo "Run as root"
  exit 1
fi

singularity build wmbase.sif Singularity.base
