# ebas-data-retrieval-session
Notebooks used for demonstrating retrieval of data in EBAS using OPeNDAP

**In order to successfully run the notebooks, you need to install the following python modules:**

pydap.handlers.cdms==0.2.0.1

bokeh==0.12.10

numpy==1.13.3

pandas==0.20.1

matplotlib==1.5.1

netCDF4==1.3.0

pydap==3.2.2

# All relevant URLs for Zeppelin is available in the all_urls_zeppelin.txt
**Note that the URLs generated are in .dds format, this you could paste into the browser, and it will give you information regarding the availbale variables for each link. If you want the actual data, you must change .dds to .dods, e.g:** 
> http://dev-ebas-pydap.nilu.no/NO0042G.uv_abs.IMG.air.ozone.1h.NO01L_uv_abs_uk_0042.NO01L_uv_abs..dds                                                                                                                                                        


To

> http://dev-ebas-pydap.nilu.no/NO0042G.uv_abs.IMG.air.ozone.1h.NO01L_uv_abs_uk_0042.NO01L_uv_abs..dods                                                                                                          


# Generate Plots as html

**You can generate Bokeh plots as html. In order to do this you must download the notebook as a python file (.py). And you must comment out the following content:**
> output_notebook()

**See the create_plot_as_html.py example:**
> python create_plot_as_html.py

