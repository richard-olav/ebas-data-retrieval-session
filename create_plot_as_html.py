
# coding: utf-8

# <table style="float:left; border:none">
#    <tr style="border:none; background-color: #ffffff">
#        <td style="border:none">
#            <a href="http://www.nilu.no/">     
#            <img 
#                src="http://www.nilu.no/Portals/0/Logo_transparent.png" 
#                style="width:100%"
#            >
#            </a>    
#        </td>
# 
#    </tr>
# </table>
# <div style="float:right;"><h2>Retriving data from EBAS:</h2><h3>02. Basic data retrieval and plotting</h3></div>

# In[1]:

from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from netCDF4 import num2date
from pydap.client import open_dods


# In[2]:

#The bokeh plotting library useually outputs the content to html, therefore we must explicitly call the output to the notebook
#output_notebook()


# **Syntax of the OPeNDAP request**
# 
# FI_REF = Instrument reference
# 
# ME_REF = Method reference
# 
# Syntax:
# 
# *ST_STATION_CODE.FT_TYPE.RE_REGIME_CODE.MA_MATRIX_NAME.CO_COMP_NAME.DS_RESCODE.FI_REF.ME_REF.DL_DATA_LEVEL*
# 
# *Both could be found using the EBAS web, selecting the metadata tab for a selected dataset
# 
# Example (no data level):
# 
# *NO0042G.Hg_mon.IMG.air.mercury.1h.NO01L_tekran_42_dup.NO01L_afs..*
# 
# Ends up in the following request:
# http://dev-ebas-pydap.nilu.no/NO0042G.Hg_mon.IMG.air.mercury.1h.NO01L_tekran_42_dup.NO01L_afs..dods

# **We will do a quick example with mercury data from the Zeppelin station**
# 
# We access the data using the OPeNDAP protocol, we send a dods request and recieve binary data.
# 
# This is now parsed by the PyDAP library.

# In[4]:

mercury_ds = open_dods('http://dev-ebas-pydap.nilu.no/NO0042G.Hg_mon.IMG.air.mercury.1h.NO01L_tekran_42_dup.NO01L_afs..dods')

# We get the keys
keys = mercury_ds.keys()

print(keys)


# **Now we can append the data to some variables**

# In[5]:

mercury = mercury_ds['mercury']

# Let's have a quicklook at the data
print(mercury.keys())

print(mercury.mercury.data)

y = mercury.mercury.data


# **In EBAS we specify dates as days since a specified date** 
# 
# This is not very user friendly, so we must convert the dates
# In order to find the unit, we must actually check the metadata calling the Dataset Attribute Structure (DAS) which provides information about the variables themselves
# 
# http://dev-ebas-pydap.nilu.no/NO0042G.Hg_mon.IMG.air.mercury.1h.NO01L_tekran_42_dup.NO01L_afs..das
# 
# This is the same for all datasets using the OPeNDAP protocol

# In[6]:

x = num2date(mercury.time.data,units='days since 1900-01-01 00:00:00',calendar='gregorian')


# **Now that we have a x and y variable, we could plot the data**

# In[7]:


plot = figure(plot_width=800, plot_height=400, title="Mercury Zeppelin",x_axis_type="datetime")

plot.line(x, y, line_width=2)

plot.xaxis.axis_label = 'Date'
plot.yaxis.axis_label = ''


show(plot) # show the results


# **So how do we now figure out the unit of the mercury plotted above?**

# In[8]:

mercury_ds.mercury_ebasmetadata


# In[9]:

print len(mercury_ds.mercury_ebasmetadata.mercury_ebasmetadata.data)


# In[10]:

mercury_metadata = mercury_ds.mercury_ebasmetadata.mercury_ebasmetadata.data[0]

print(mercury_metadata)


# In[10]:

plot = figure(plot_width=800, plot_height=400, title="Mercury Zeppelin",x_axis_type="datetime")

plot.line(x, y, line_width=2)

plot.xaxis.axis_label = 'Date'
plot.yaxis.axis_label = 'ng/m3'


show(plot) # show the results


# In[ ]:



