Singularity Recipe for the AIT-WATCHMAN version of Rat-pac
==========================================================

[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/1886)

The recipe is split into two components. The first, Singularity.base,
contains the recipe to build Geant4 and ROOT into ubuntu. The second,
Singularity.ratpac, uses the base image and appends rat-pac onto that
image. This is done so that Geant4 and ROOT remain fixed while rat-pac
is ever changing.
