import os
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

os.system('clear')

try:
	import rich
except ImportError:
	sup='# module rich belum terinstall...'
	suo=mark(sup,style='red')
	sol().print(suo,style='cyan')
	os.system('pip install rich')
	lol='# succes install module rich...'
	loi=mark(lol,style='green')
	sol().print(loi,style='cyan')
	
try:
	import mechanize
except ImportError:
	suq='# module mechanize belum terinstall...'
	suh=mark(suq,style='red')
	sol().print(suh,style='cyan')
	os.system('pip install mechanize')
	dog='# succes install module mechanize...'
	dof=mark(dog,style='green')
	sol().print(dof,style='cyan')
	
try:
	import bs4
except ImportError:
	suq='# module bs4 belum terinstall...'
	suh=mark(suq,style='red')
	sol().print(suh,style='cyan')
	os.system('pip install bs4')
	dog='# succes install module bs4...'
	dof=mark(dog,style='green')
	sol().print(dof,style='cyan')
	
try:
	import bash
except ImportError:
	suq='# module bash belum terinstall...'
	suh=mark(suq,style='red')
	sol().print(suh,style='cyan')
	os.system('pip install bash')
	dog='# succes install module bash...'
	dof=mark(dog,style='green')
	sol().print(dof,style='cyan')
	
try:
	import requests
except ImportError:
	suq='# module requests belum terinstall...'
	suh=mark(suq,style='red')
	sol().print(suh,style='cyan')
	os.system('pip install requests')
	dog='# succes install module requests...'
	dof=mark(dog,style='green')
	sol().print(dof,style='cyan')
	
os.system('clear')

from src import Data
