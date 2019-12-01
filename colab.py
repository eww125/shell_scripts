from google.colab import drive
drive.mount('/content/drive')
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm, Inches, Pt
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import date
import jinja2
from jinja2.utils import Markup
import os, re, ast, glob, numpy, gspread, PyPDF2
from boxsdk import OAuth2, Client
from PyPDF2 import PdfFileReader
from os.path import expanduser
import pandas as pd
import geopandas as gpd
from shapely import wkt
pd.options.mode.chained_assignment = None
from gspread_dataframe import set_with_dataframe, get_as_dataframe
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())
