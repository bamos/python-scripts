#!/usr/bin/env python3
#
# ScrapeCountriesTest.py
#
# Note: Because the website fluctuates, this is not up to date and
#   tests won't all pass. However, I'm leaving this for the HTMLParser
#   example rather than parsing accuracy.
#
# Brandon Amos
# 2013.05.01

import os # File removal.
import subprocess # Process creation.
import pickle # Pickling.

baseURL = "http://www.nationsonline.org/oneworld/"
urlDict = dict(
  arabic  = baseURL + "countrynames_arabic.htm",
  chinese = baseURL + "country_names_in_chinese.htm",
  codes   = baseURL + "country_code_list.htm",
  french  = baseURL + "countries_of_the_world.htm",
  german  = baseURL + "countrynames_german.htm",
  italian = baseURL + "countrynames_italian.htm",
  russian = baseURL + "countrynames_russian.htm",
  spanish = baseURL + "countrynames_spanish.htm"
)

# Helper function to count the number of lines in a file handle.
def countLines(fileHandle):
  count = 0
  for line in fileHandle:
    count += 1
  return count

# Helper functions to print sections and subsections.
def section(title):
  print(" + {0}".format(title))
def subsection(title):
  print("   + {0}".format(title))
def subsubsection(title):
  print("     + {0}".format(title))

# Helper function to safely delete a file, if it exists.
def safeDelete(name):
  try:
    os.remove(name)
  except OSError:
    pass

#######
section("Testing Arabic.")
outName = "out-arabic.txt"
command = ["./ScrapeCountries.py", urlDict.get("arabic"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

subsection("Checking output.")
try:
  output = open(outName, encoding="utf8")

  # 1. Check number of lines.
  assert countLines(output) == 227, "Incorrect number of lines."

  # 2. Check the content of miscellaneous entries.
  output.seek(0)
  lines = [line.strip() for line in output]
  afghanistan = lines[0].split("\t")
  assert afghanistan[0] == "Afghanistan", "Incorrect content (1)."
  assert afghanistan[1] == "أفغانستان", "Incorrect content (2)."
  assert afghanistan[2] == "Afghanestan", "Incorrect content (3)."

  zimbabwe = lines[226].split("\t")
  assert zimbabwe[0] == "Zimbabwe", "Incorrect content (4)."
  assert zimbabwe[1] == "زمبابوي", "Incorrect content (5)."
  assert zimbabwe[2] == "Zimbabwe", "Incorrect content (6)."

  output.close()
  subsection("Complete.")
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)

# 3. Test the pickle.
subsection("Testing pickle.")
outName = "out-arabic.pickle"
command = ["./ScrapeCountries.py", "-p", urlDict.get("arabic"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

try:
  f = open(outName, "rb")
  countryData = pickle.load(f)

  afghanistan = countryData[0]
  assert afghanistan[0] == "Afghanistan", "Incorrect content (1)."
  assert afghanistan[1] == "أفغانستان", "Incorrect content (2)."
  assert afghanistan[2] == "Afghanestan", "Incorrect content (3)."

  zimbabwe = countryData[226]
  assert zimbabwe[0] == "Zimbabwe", "Incorrect content (4)."
  assert zimbabwe[1] == "زمبابوي", "Incorrect content (5)."
  assert zimbabwe[2] == "Zimbabwe", "Incorrect content (6)."

  subsection("Complete.")
  f.close()
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)

#######
section("Testing Chinese.")
outName = "out-chinese.txt"
command = ["./ScrapeCountries.py", urlDict.get("chinese"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

subsection("Checking output.")
try:
  output = open(outName, encoding="utf8")

  # 1. Check number of lines.
  assert countLines(output) == 205, "Incorrect number of lines."

  # 2. Check the content of miscellaneous entries.
  output.seek(0)
  lines = [line.strip() for line in output]

  #    Specifically, check São Tomé and Príncipe because of the
  #    ampersand character codes it originally contains.
  saoTome = lines[161].split("\t")
  assert saoTome[0] == "São Tomé and Príncipe", "Incorrect content (1)."
  assert saoTome[1] == "圣多美普林西比", "Incorrect content (2)."
  assert saoTome[2] == "sheng4 duo1 mei3  pu3 lin2 xi1 bi3", "Incorect content (3)."
  assert saoTome[3] == "São Tomé e Príncipe", "Incorrect content (4)."

  output.close()
  subsection("Complete.")
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)


#######
section("Testing country codes.")
outName = "out-codes.txt"
command = ["./ScrapeCountries.py", urlDict.get("codes"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

subsection("Checking output.")
try:
  output = open(outName, encoding="utf8")

  # 1. Check number of lines.
  assert countLines(output) == 247, "Incorrect number of lines."

  # 2. Check the content of the last entry.
  output.seek(0)
  lines = [line.strip() for line in output]

  zimbabwe = lines[246].split("\t")
  assert zimbabwe[0] == "Zimbabwe", "Incorrect content."
  assert zimbabwe[1] == "ZW", "Incorrect content (1)."
  assert zimbabwe[2] == "ZWE", "Incorrect content (2)."
  assert zimbabwe[3] == "716", "Incorrect content (3)."

  output.close()
  subsection("Complete.")
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)


#######
section("Testing French.")
outName = "out-french.txt"
command = ["./ScrapeCountries.py", urlDict.get("french"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

subsection("Checking output.")
try:
  output = open(outName, encoding="utf8")

  # 1. Check number of lines.
  assert countLines(output) == 237, "Incorrect number of lines."

  # 2. Check the content of miscellaneous entries.
  output.seek(0)
  lines = [line.strip() for line in output]

  zimbabwe = lines[236].split("\t")
  assert zimbabwe[0] == "Zimbabwe", "Incorrect content (1)."
  assert zimbabwe[1] == "Zimbabwe", "Incorrect content (2)."
  assert zimbabwe[2] == "Zimbabwe", "Incorrect content (3)."
  assert zimbabwe[3] == "Eastern Africa", "Incorrect content (4)."

  output.close()
  subsection("Complete.")
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)


#######
section("Testing German.")
outName = "out-german.txt"
command = ["./ScrapeCountries.py", urlDict.get("german"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

subsection("Checking output.")
try:
  output = open(outName, encoding="utf8")

  # 1. Check number of lines.
  assert countLines(output) == 250, "Incorrect number of lines."

  # 2. Check the content of the last entry.
  output.seek(0)
  lines = [line.strip() for line in output]

  zimbabwe = lines[249].split("\t")
  assert zimbabwe[0] == "Zimbabwe", "Incorrect content (1)."
  assert zimbabwe[1] == "Simbabwe", "Incorrect content (2)."
  assert zimbabwe[2] == "Zimbabwe", "Incorrect content (3)."

  output.close()
  subsection("Complete.")
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)

#######
section("Testing Italian.")
outName = "out-italian.txt"
command = ["./ScrapeCountries.py", urlDict.get("italian"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

subsection("Checking output.")
try:
  output = open(outName, encoding="utf8")

  # 1. Check number of lines.
  assert countLines(output) == 250, "Incorrect number of lines."

  # 2. Check the content of the last entry.
  output.seek(0)
  lines = [line.strip() for line in output]

  zimbabwe = lines[249].split("\t")
  assert zimbabwe[0] == "Zimbabwe", "Incorrect content (1)."
  assert zimbabwe[1] == "Zimbabwe", "Incorrect content (2)."
  assert zimbabwe[2] == "Zimbabwe", "Incorrect content (3)."

  output.close()
  subsection("Complete.")
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)


#######
section("Testing Russian.")
outName = "out-russian.txt"
command = ["./ScrapeCountries.py", urlDict.get("russian"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

subsection("Checking output.")
try:
  output = open(outName, encoding="utf8")

  # 1. Check number of lines.
  assert countLines(output) == 227, "Incorrect number of lines."

  # 2. Check the content of the last entry.
  output.seek(0)
  lines = [line.strip() for line in output]

  zimbabwe = lines[226].split("\t")
  assert zimbabwe[0] == "Zimbabwe", "Incorrect content (1)."
  assert zimbabwe[1] == "Зимбабве", "Incorrect content (2)."
  assert zimbabwe[2] == "Zimbabwe", "Incorrect content (3)."

  output.close()
  subsection("Complete.")
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)


#######
section("Testing Spanish.")
outName = "out-spanish.txt"
command = ["./ScrapeCountries.py", urlDict.get("spanish"), outName]
try:
  subprocess.call(command, stdout=subprocess.DEVNULL)
except Exception as err:
  subsection("Error: " + str(err))

subsection("Checking output.")
try:
  output = open(outName, encoding="utf8")

  # 1. Check number of lines.
  assert countLines(output) == 237, "Incorrect number of lines."

  # 2. Check the content of the last entry.
  output.seek(0)
  lines = [line.strip() for line in output]

  zimbabwe = lines[236].split("\t")
  assert zimbabwe[0] == "Zimbabwe", "Incorrect content (1)."
  assert zimbabwe[1] == "Zimbabwe", "Incorrect content (2)."
  assert zimbabwe[2] == "Zimbabwe", "Incorrect content (3)."
  assert zimbabwe[3] == "África Oriental", "Incorrect content (4)."

  output.close()
  subsection("Complete.")
except Exception as err:
  subsubsection("Error: " + str(err))
finally:
  safeDelete(outName)

#######
section("Finished testing.")
