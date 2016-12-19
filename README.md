[![GPL
Licence](https://badges.frapsoft.com/os/gpl/gpl.svg?v=103)](https://opensource.org/licenses/GPL-3.0/)

## Overview
Simulate population growth, spatial dispersion, and robustness to environment.

## Vision
It wants to be a full fledged package simulating interactions between
artificial and naturally observed organisms, their environments, and economic
pressures (like consumption, shipping, anthropogenic climate change). Could be
used to show potential ramifications of different energy, consumption, etc.
policies. Could be used to generate different stories of life on earth under
different geoclimactic conditions. Originally just for seeing how plants will
rediversify as extinction events pass and for looking at economy as an
evolutionary force acting on climate and agricultural genetics and crop
productivity.

## TODO
* simulate categorical alleles
* simulate QTL-esque alleles
* write unittests for utilities
* Give each allele or combination morphological meaning
   e.g.  
  1. just higher number is higher fitness. Trivial but functional.
  2. LES, drought tollerance, etc. all parameterized ecophysiologically.
  3. tolerance to pests, diseases, and eaters who all have their own  
   evolutionary path.
  4. maybe find a way to grow new adaptive morphological traits rather than just
   strategies of movement, reproduction, and potentially social order (fish swim
   in schools) and trait parameterization.
* Allow for input from better climate models, crop models, economic models.
* Allow for multiple generation life spans, fitness based probabilistic life
   spans
* Allow for variable population size dependent on climate state e.g. true
   polynomial range over x domain proportional to sustainable population size -
   if the range gets too small, world e.g. gets too hot and nothing survives
* Track inheritance of genes
