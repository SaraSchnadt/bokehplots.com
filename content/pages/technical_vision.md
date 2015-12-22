Title: Technical Vision

Photographers use the Japanese word “bokeh” to describe the blurring of the
out-of-focus parts of an image. Its aesthetic quality can greatly enhance a
photograph, and photographers artfully use focus to draw attention to subjects
of interest. “Good bokeh” contributes visual interest to a photograph and
places its subjects in context.

In this vein of focusing on high-impact subjects while always maintaining a
relationship to the data background, the Bokeh project attempts to address
fundamental challenges of large dataset visualization:

##### How do we look at all the data?

  * What are the best perceptual approaches to honestly and accurately represent the data to domain experts and SMEs so they can apply their intuition to the data?
  * Are there automated approaches to accurately reduce large datasets so that outliers and anomalies are still visible, while we meaningfully represent baselines and backgrounds? How can we do this without “washing away” all the interesting bits during a naive downsampling?
  * If we treat the pixels and topology of pixels on a screen as a bottleneck in the I/O channel between hard drives and an analyst’s visual cortex, what are the best compression techniques at all levels of the data transformation pipeline?

##### How can scientists and data analysts be empowered to use visualization fluidly, not merely as an output facility or one stage of a pipeline, but as an entire mode of engagement with data and models?

  * Are language-based approaches for expressing mathematical modeling and data transformations the best way to compose novel interactive graphics?
  * What data-oriented interactions (besides mere linked brushing/selection) are useful for fluid, visually-enable analysis?

Some of the core ideas for the backend processing in bokeh-server are currently
implemented as a standalone library, and are being developed under the term
“Abstract Rendering”, which we will be presenting at VDA 2014. For more
information, you can visit the [Abstract Rendering GitHub page](//github.com/JosephCottam/AbstractRendering).

Bokeh is one of several open-source components of the broader technical vision
of [Continuum Analytics](//continuum.io). By providing powerful data description and vector
computing on remote and distributed data via [Blaze](//blaze.pydata.org/) and [Numba](//numba.pydata.org), and providing
interactive visualizations of them via Bokeh, we enable teams to
collaboratively perform rich analysis, share them with others (potentially
non-technical members of their team or business), and rapidly create analytical
dashboards and monitoring interfaces.

One guiding principle for the development of Bokeh is to provide useful
software for people, while incorporating novel ideas from the academic world of
visualization research. Additionally, as a modular and open-source project, we
hope that Bokeh will enable many other projects to build a rich suite of
domain-specific applications that change existing, legacy paradigms of data
processing workflow.
