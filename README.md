# bokehplots.com
Source code for bokeh landing site.

# Getting setup

  $ conda env create
  $ source activate bokehplots_com
  $ npm install

# Running locally

  $ ./node_modules/grunt-cli/bin/grunt serve

Grunt is then watching for changes.

**Edit the scss files not the css.**

# To deploy

Requires s3cmd (http://s3tools.org/s3cmd-howto) to be installed and in a conda-env called s3cmd.

  $ ./node_modules/grunt-cli/bin/grunt deploy 
  $ source activate s3cmd
  $ s3cmd put -r --force output/* s3://bokehplots.com
