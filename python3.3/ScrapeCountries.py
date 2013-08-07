#!/usr/bin/env python3.3
#
# ScrapeCountries.py
#
# Scrapes countries from http://www.nationsonline.org
#
# Note: Because the website fluctuates, this is not up to date and
#   tests won't all pass. However, I'm leaving this for the HTMLParser
#   example rather than parsing accuracy.
#
# Brandon Amos
# 2013.04.26

import argparse # Argument parsing.
import html.parser # HTML parsing.
import urllib.parse # URL retrieval.
import urllib.request # URL retrieval.
import re # Regular expressions.
import pickle # Pickling.

# Given a URL, this retrieves the content with a utf8 encoding
# and uses the CountryParser to extract the country names from
# the tables.
class URLParser():
  user_agent = ("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) "
    "AppleWebKit/525.13 (KHTML,     like Gecko)"
    "Chrome/0.2.149.29 Safari/525.13")

  def __init__(self, url, numCols, extractionMap, exceptions):
    # Request the html.
    request = urllib.request.Request(url)
    request.add_header("User-Agent",self.user_agent)
    try:
      response = urllib.request.urlopen(request)
    except:
      print("Error: Invalid URL. Exiting.")
      exit()
    htmlContent = response.read().decode("utf8")

    # Some files have <br> in the middle of a <td> tag,
    # and cause the parser to misinterpret the data.
    htmlContent = htmlContent.replace("<br>", "")

    # Parse the html.
    parser = CountryParser(numCols, extractionMap, exceptions, strict=False)
    htmlContent = parser.unescape(htmlContent) # Unescape HTML entities.
    parser.feed(htmlContent)
    parser.close()
    self.__countryData = parser.countryData

  @property
  def countryData(self):
    return self.__countryData

# CountryParser keeps track of the HTML tags and appends country
# names to a list.
class CountryParser(html.parser.HTMLParser):

  # Initialize the class variables.
  def __init__(self, numCols, extractionMap, exceptions, strict=False):
    super().__init__(strict=strict)

    self.__numCols = numCols
    self.__extractionMap = extractionMap
    self.__exceptions = exceptions
    
    # Maintain our position within tags.
    self.__in_tr = False
    self.__in_td = False

    # Within rows specifically, keep track of our index.
    # This helps because we know the country name always
    # occurs in the 0th position, and if we've exceeded
    # `numCols` positions, then the current row does not have
    # the data we want.
    self.__td_position = 0

    # Keep a record of possible data.
    self.__possible_data = []

    # The country names, successfully parsed.
    self.__countryData = []

  def handle_starttag(self, tag, attrs):
    if tag == "tr":
      self.__in_tr = True

      # Reset the possible data.
      self.__td_position = 0
      self.__possible_data = []
      for i in range(self.__numCols):
        self.__possible_data.append("")
    elif tag == "td":
      self.__in_td = True
    
  def handle_endtag(self, tag):
    if tag == "tr":
      self.__in_tr = False

      if self.__td_position == self.__numCols:
        # Extract the columns and clean them up.
        extractedData = [self.__possible_data[i] for i in self.__extractionMap]
        for i in range(len(extractedData)):
          if extractedData[i]:
            extractedData[i] = extractedData[i].replace('\n', ' ').strip()

        # Detect data with empty columns, unless it's an exception,
        # in which case we don't do this check.
        isIntersection = bool(set(extractedData) & set(self.__exceptions))
        if not isIntersection:
          for i in range(len(extractedData)):
            if not extractedData[i] or len(extractedData[i]) == 0:
              #print(extractedData)
              return

        self.__countryData.append(extractedData)
    elif tag == "td":
      self.__in_td = False
      self.__td_position += 1
      
  # If our criteria match, we know our position in the table.
  # Keep track of the data.
  def handle_data(self, data):
    if self.__in_tr:
      if self.__in_td:
        if self.__td_position < self.__numCols:
          self.__possible_data[self.__td_position] += data

  @property
  def countryData(self):
    return self.__countryData

# Define usage when running this from the command line.
if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description='Scrape countries from http://www.nationsonline.org.')
  parser.add_argument('url', type=str, help='The URL to scrape.')
  parser.add_argument('output', type=str, help='The output file.')
  parser.add_argument('-p', '--pickle', dest='p', action='store_true',
      help='Generate a pickle.')
  args = parser.parse_args()

  genPickle = args.p
  url = args.url
  outputFile = args.output

  # Default values.
  numPops = 0 # The number of irrelavant data values at the top to ignore.
  exceptions = [] # Legitamet country rows marked as erroneous.
  numCols = 3 # The number of columns.
  extractionMap = (0, 1, 2) # The subset of columns to use as output.

  # Consider the different cases for each URL.
  baseUrl = ".*nationsonline.org/oneworld/"
  if re.match(baseUrl + "countrynames_arabic.htm", url):
    print("Parsing country names in Arabic.")
    numCols = 5
    extractionMap = (1, 2, 4)
    exceptions = ['Cayman Islands', 'Falkland Islands', 'Montenegro',
        'Saint Kitts and Nevis', 'Saint Vincent and the Grenadines',
        'Tokelau', 'Western Sahara']
  elif re.match(baseUrl + "country_names_in_chinese.htm", url):
    print("Parsing country names in Chinese.")
    numCols = 4
    extractionMap = (0, 1, 2, 3)
    exceptions = ['Tuvalu']
    numPops = 1
  elif re.match(baseUrl + "country_code_list.htm", url):
    print("Parsing country code list.")
    numCols = 5
    extractionMap = (1, 2, 3, 4)
  elif re.match(baseUrl + "countries_of_the_world.htm", url):
    print("Parsing countries of the world.")
    numCols = 5
    extractionMap = (1, 2, 3, 4)
    exceptions = ['Saint Kitts and Nevis',
      'Saint Vincent and the Grenadines', 'Virgin Islands (British)']
  elif re.match(baseUrl + "countrynames_german.htm", url):
    print("Parsing country names in German.")
    exceptions = ['Saint Kitts and Nevis',
      'Saint Vincent and the Grenadines',
      'South Georgia and South Sandwich Islands',
      'Virgin Islands (British)',
      'Western Sahara']
  elif re.match(baseUrl + "countrynames_italian.htm", url):
    print("Parsing country names in Italian.")
    exceptions = ['French Southern Territories',
        'Saint Kitts and Nevis',
        'Saint Vincent and the Grenadines',
        'South Georgia and South Sandwich Islands',
        'U.S. Minor Outlying Islands',
        'Virgin Islands (British)',
        'Western Sahara']
  elif re.match(baseUrl + "countrynames_russian.htm", url):
    print("Parsing country names in Russian.")
    exceptions = ['Saint Kitts and Nevis',
        'Saint Vincent and the Grenadines',
        'Western Sahara']
  elif re.match(baseUrl + "countrynames_spanish.htm", url):
    print("Parsing country names in Spanish.")
    numCols = 5
    extractionMap = (1, 2, 3, 4)
    exceptions = ['Saint Kitts and Nevis',
        'Saint Vincent and the Grenadines',
        'Virgin Islands (British)']
  else:
    print("Unrecognized url. Using default (and likely incorrect) values.")

  print("Using {0} columns overall and extracting columns {1}.".format(
    numCols, extractionMap))

  # Parse the HTML and pop the irrelevant values from the results.
  parsedURL = URLParser(url, numCols, extractionMap, exceptions)
  countryData = parsedURL.countryData
  for i in range(numPops):
    countryData.pop(0)

  # Write the data to disk.
  if genPickle:
    f = open(args.output, 'wb')
    pickle.dump(countryData, f, pickle.HIGHEST_PROTOCOL)
    f.close()
  else:
    f = open(args.output, 'w', encoding="utf8")
    for country in countryData:
      f.write('\t'.join(map(str,country)))
      f.write('\n')
    f.close()
  print("Finished extracting. Data written to '{0}'".format(outputFile))
