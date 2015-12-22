Title: FAQs

### General Questions

#### How do you pronounce “bokeh”?
Either “boh-Kay” or “boh-Kuh”. For more information, you can consult Wikipedia or an actual Japanese person.

#### Why did you start writing a new plotting library?
There are a number of reasons why we wrote a new Python library, but they all hinge on maximizing flexibility for exploring new design spaces for achieving our long-term visualization goals. (Please see [Technical Vision](/pages/technical-vision.html) for details about those.)

The client-server nature of displaying for the web is reflected in the fundamental architecture of the library, and also has significant impact on the front-end interface. Additionally, the difficult task of coalescing large data sets for display on thin clients in a perceptually useful way demands different things of a graphics and rendering architecture than most of the readily-available libraries in Python today.

In the meantime, we would like to remain as compatible with the rest of the Scipy and PyData ecosystems of tools as possible. This means that we are very eager to get contributions that help us understanding configuration files from other libraries, provide API compatibility layers, and possibly create backends for other libraries on top of Bokeh’s low-level glyph API.

Please see [Contact](/pages/contact.html) and get in touch with the dev team if you have ideas along these lines.

#### Can I incorporate Bokeh into my proprietary app or platform?
We are happy for people to do this. We do appreciate an attribution, and we also would like to receive feedback about how it’s working out for your project.

#### What is the relationship between Bokeh and Chaco?
There is no direct active relationship between these two projects. Some of the design choices in Chaco are reflected in the architecture of Bokeh, and some snippets of code from Chaco have been ported to Javascript and placed in BokehJS. The goals of the two projects are quite different. If you have a Chaco project that you’d like to put on the web, there is a good chance that you can make it work with Bokeh (since the HTML5 Canvas API is fairly close to Kiva’s), but at this point, you will need to write Javascript if you want custom interactors. For rich client, customizable, interactive visualization in Python, Chaco is still a good tool.

#### How does Bokeh compare to mpld3?
For a lightweight, python-only library that exposes most of matplotlib to the browser, mpld3 could be a good choice. Bokeh also intends to fully support the MPL interface (and hence Seaborn, pandas, and ggplot.py), however the main goal of Bokeh is to provide approachable capability for novel interactive visualizations in the browser. If you would like to have the benefits of HTML canvas rendering, dynamic downsampling, abstract rendering, server plot hosting, and the possibility of interacting from languages besides python, please consider Bokeh for your project.

#### Does Bokeh implement R’s ggplot2?
No, Bokeh does not implement R’s ggplot2 interface. Bokeh was influenced by Wilkinson’s Grammar of Graphics (e.g. the idea of tight, well-defined, composable abstractions that can be tied directly to data). However, Bokeh does not implement a “GoG” system. Please see [Technical Vision](/pages/technical-vision.html) for more details.
An experimental ggplot interface was prototyped at early stages, (circa Bokeh 0.1), but it was never fully developed and has since been removed. At present there are no plans to implement R’s ggplot2 interface directly within Bokeh. However, since Bokeh provides some level of Matplotlib compatibility, it is often possible to convert plots created using the third-party python library ggplot.py into Bokeh plots very easily. There are several examples in the gallery; you can see one here.

### Technical Questions
#### Does Bokeh use D3.js?
No. D3 is very cool and its predecessor Protovis was one of the inspirations for Bokeh. However, we understand the goals of D3 to be about providing a Javascript-based data scripting layer for the DOM, and this is somewhat orthogonal (at this point) to the visualization challenges that Bokeh is trying to tackle. Please see [Technical Vision](/pages/technical-vision.html) for more details about the underlying goals and vision behind our project.
#### Why not use something like Vega?
We may very well end up using the Vega grammar. For now, we need to be able to specifically tag certain objects with UUIDs so that the object graph structure can be reconstituted on the JS side. Additionally, we use this JSON to reproduce Python object graphs when we load up a Python plot from the plot server - so we would need to make sure that Vega can fully encapsulate all the information we need here as well.
#### How do I get the sample data?
Some of the Bokeh examples rely on sample data that is not included in the Bokeh GitHub repository or released packages, due to their size. The sample data can be obtained by executing the following commands at a python prompt:

```
  >>> import bokeh.sampledata
  >>> bokeh.sampledata.download()
```

### Troubleshooting
#### Are the tools not working in Chrome/Cromium?
If you have a device with touchscreen capabilities, is possible that Chrome/Chromium is “flagged” to capture touch events which makes not possible to interact with the Bokeh tools with you mouse.
To solve this issue you need to configure Chrome/Cromium going to the url bar and pasting the following:
```
chrome://flags/#touch-events
```
then you will see something like:
```
Enable touch events Mac, Windows, Linux, Chrome OS Force touchscreen support to always be enabled or disabled,or to be enabled when a touchscreen is detected on startup (Automatic, the default). #touch-events
```
and a drop-down button that you have to set to ``Disabled``.
