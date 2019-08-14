from pathlib import Path
import os
import logging
import csv
import chardet #　encodingのタイプを決めるために

# loggingの設定
# set logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger("Change Encoding")

# specify file type and encoding
# 転換したいファイル格式とencoding 
type_file = "*.csv"
encoding = "shift-jis"

# locate the directory
# フォルダーの設定
cwd = os.getcwd()
pathlist = Path(cwd).glob(type_file)

# iterate through every files
for path in pathlist:
	if path == None:
		log.error("File not found!")
		break

	path = str(path)

	with open(path, "rb") as rawdata:
		rawdata = rawdata.read()
		encoding_format = chardet.detect(rawdata).get("encoding")

	with open(path, 'r',encoding=encoding_format) as infile, open(path.replace(".csv","") + "_" + encoding + ".csv", encoding=encoding, mode="w") as outfile:
		inputs = csv.reader(infile)
		outputs = csv.writer(outfile)
		for index, row in enumerate(inputs):
			outputs.writerow(row)
		log.info(path + "Success!")