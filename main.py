#import multiprocessing, time, pika, json, traceback, logging, sys, os, itertools, urllib, urllib2, cStringIO, mysql.connector, shutil, hashlib, socket, urllib2, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from PIL import Image
from os import listdir
from os.path import isfile, join
#from bs4 import BeautifulSoup
from pprint import pprint
import webdriver_class


wdc = webdriver_class
wdc.appointment_search()
