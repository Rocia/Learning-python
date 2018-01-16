from __future__ import print_function
import sys, re, csv
import time
from collections import OrderedDict, defaultdict
import psycopg2
import json
import codecs
from datetime import datetime
import os, shutil, glob
#import logging 


class CustomError(Exception):
	pass

#smb = smbclient.SambaClient(server='172.29.6.31', share='shared team', domain='LDL', username='rocia.fernandes',password='Aloy5iu$')

'''def crony(): 
    from crontab import CronTab
    cron = CronTab(user=True)
    job = cron.new(command='cd /root python /root/project/Projects/NoSQL/source/a.py', comment = 'test')
    job.minute.every(7)
    cron.write()'''

def pathsetup():
	rootDir='//172.29.254.171/RA_HOTFOLDER/'
	export_db_Path='E:/PostGresSQL_Export/Walmart_RA/'
	export_db_share='//172.1.254.182/Walmart_RA/'
	return rootDir, export_db_Path, export_db_share

def dev_pathsetup():
	rootDir='/root/project/RA_HOTFOLDER/'
	export_db_Path='E:/PostGresSQL_Export/Walmart_RA/'
	export_db_share='/root/project/WALMART_RA/'
	return rootDir, export_db_Path, export_db_share



def csv_reader(file_obj):
	try:
		reader = csv.DictReader(file_obj)
		for row in reader:
			sorted_row = OrderedDict(sorted(row.items(),key=lambda item: reader.fieldnames.index(item[0])))
			dict_list.append(sorted_row)
		return dict_list
	except csv.Error as e:
		move_back(data_path,kw_path,YTSpath,'Error in CSV file.')
		sys.exit('file {}, line {}: {}'.format(file_obj, reader.line_num, e))


def csv_counter(file_obj, count):
	try:
		with open(file_obj, 'rb') as f:
			reader = csv.reader(f)
		for row in reader:
			count += 1
		return count
	except:
		raise CustomError("Error in export")

def keyword_reader(obj):
	reader = csv.reader(obj)
	for row in reader:
		k_list.append(row)
	return k_list


def ValueFile_Reader(obj):
	reader = csv.reader(obj)
	for row in reader:
		av_list.append(row)
	return av_list
	
def remove_tags(text):
    return TAG_RE.sub('', text)


def query_format(query):	
	new = query.replace("''","\"")		
	return new


def Filename_format(query):
	new = query.replace(".","\.")	
	return new


def splitstring(obj):
	alpha = obj.split(' ')
	for a in alpha:
		b = a.title()
		alpha.append(b)
		return alpha
	

def filterText(a):
	a = a.replace('<br />',' ').replace('<b>',' ').replace('</b>',' ').replace('<br>',' ').replace('  ',' ').replace('  ',' ')
	b = re.sub('([\[\^$.?*+\(\)*"\'/,-<>])','',remove_tags(a))
	return b


def keys_of_value(dct, value):
    for k in dct:
        if isinstance(dct[k], list):
            if value in dct[k]:
                return k
        else:
            if value == dct[k]:
                return k
			

def removelist(string):
	string = str(string).replace("[",'').replace("]",'').replace("'",'')
	return string


def move_back(a,b,YTS,message,c, status):
	if not os.path.isfile(a.replace(WIPpath+'/',YTS)):
		shutil.move(a,YTS)
	if not os.path.isfile(b.replace(WIPpath+'/',YTS)):
		shutil.move(b,YTS)
	if status == True:
		if not os.path.isfile(c.replace(WIPpath+'/',YTS)):
			shutil.move(c,YTS)	
	with open(LOG_FILENAME,'w+') as f:
		f.write('Error : '+message)
	f.close()
	#sys.exit()
	#logging.basicConfig(filename=LOG_FILENAME)
	#logging.debug(message)
	
	
def move_to_wip(a,b,WIP,c, STATUS):
	shutil.move(a,WIP)
	shutil.move(b,WIP)
	if STATUS == True:
		shutil.move(c, WIP)
	
	
def move_to_done(a,b,DONE,c, STATUS):
	shutil.move(a,DONE)
	shutil.move(b,DONE)
	if STATUS == True:
		shutil.move(c, DONE)
		
	

def error_log(FILENAME, message):
	FILENAME = FILENAME.replace('.csv','_NAME_ERROR.log')
	with open(FILENAME.replace(),'w+') as f:
		f.write('Error : '+message)
		
cnx = psycopg2.connect("dbname='ReAttribution_Dev' user='ePublishing_Studio' host='172.1.254.182' password='opmstech$123'")
dict_list, alpha, k_list, keywords, antikeywords, KEYWORDS , ANTIKEYWORDS ,mstList, transList, UOM, UOMs =  [], defaultdict(list), [], [], [],{},{},[],[],[],{}
TAG_RE = re.compile(r'<[^>]+>')
count, counter, fileList, av_list = 0, 0, [], []
dir=pathsetup()

#dir = dev_pathsetup()
rootDir=dir[0]
export_db_path=dir[1]
export_db_share=dir[2]
YTSpath = rootDir + '01_YTS'
WIPpath = rootDir + '02_WIP'
donepath = rootDir + '03_DONE'
ExportRootDir = rootDir + '04_TAGGED'

types = (YTSpath+'/*_input_*.csv', YTSpath+'/*_INPUT_*.csv', YTSpath+'/*_Input_*.csv')

for files in types:
	try:
		fileList.extend(glob.glob(files))
	except Exception as e:
		raise CustomError(e,"Network Error")
		sys.exit()
		
		
for file in fileList:
	if file.find("'") != -1:
		error_log(file, 'Invalid File Naming: A file name cannot include invalid charachters. Only 0-9, a-z, A_Z, (_) , (-) and (.) are valid charachters')
		
status, VF1 , VF2= False, False, False
AttributeValuePresent = False
#print(fileList)

if __name__ == "__main__":
   for name in fileList:
		   name = name.replace("\\","/").replace('_Input_','_input_').replace('_INPUT_','_input_')    
		   #print("File found: ",name)
		   #dfile = re.compile("((([\w_/[\s]*]+/([\S+]+_([\d]+)_[\S+]+))_[iI][nN][pP][uU][tT]_([_\S+]+))(.csv|.CSV))")
		   try:
			   vi = name.split('_input_')
		   except:
			   break
		   
		   dfile = re.compile("([^$]+)/([^$]+_([\d]+)_[\S+]+)")
		   
		   InPutFileWithPath=vi[0]
		   DataFile = dfile.findall(InPutFileWithPath)
		   DataFile=DataFile[0]
		   #print(DataFile[2])
		   if len(DataFile)!= 0:
				   eKFname1 = InPutFileWithPath +'_keywords.csv'
				   eKFname2 = InPutFileWithPath +'_Keywords.csv'
				   errorFname = InPutFileWithPath +'_error.log'
				   ValueFname10 = InPutFileWithPath +'_multiselect.csv'
				   ValueFname11 = InPutFileWithPath +'_Multiselect.csv'
				   ValueFname12 = InPutFileWithPath +'_MultiSelect.csv'
				   ValueFname20 = InPutFileWithPath +'_singleselect.csv'
				   ValueFname21 = InPutFileWithPath +'_Singleselect.csv'
				   ValueFname22 = InPutFileWithPath +'_SingleSelect.csv'
				   
				   LOG_FILENAME = errorFname
				   #print(eKFname,errorFname)
				   
				   if not os.path.isfile(errorFname):
					   #print(eKFname2, os.path.isfile(eKFname2))
					   if os.path.isfile(eKFname1) or os.path.isfile(eKFname2):
						   #print(2)
						   if os.path.isfile(eKFname1):
							   eKFname = eKFname1
						   elif os.path.isfile(eKFname2):
							   eKFname = eKFname2
							   
						   exported_csv_name=DataFile[1]+'_export.csv'
						   export_path = export_db_path+exported_csv_name
						   copy_csv_from=export_db_share+exported_csv_name
						   copy_csv_to=ExportRootDir+"/"+exported_csv_name
						   #print("Export Path: ", export_path)
						   DataFileName = DataFile[1]
						   ShelfId = DataFile[2]
						   alpha = vi[1].split('.')
						   Attribute = alpha[0]
						   

						   data_path = name.replace(YTSpath,WIPpath)
						   kw_path = eKFname.replace(YTSpath,WIPpath)
						   

						   status = True
						   if os.path.isfile(ValueFname10):
							   ValueFname1 = ValueFname10
							   VF1 = True
						   elif os.path.isfile(ValueFname11):
							   ValueFname1 = ValueFname11
							   VF1 = True
						   elif os.path.isfile(ValueFname12):
							   ValueFname1 = ValueFname12
							   VF1 = True
						   if VF1 == True:					   
						      with codecs.open(ValueFname1, "r",encoding='utf-8', errors='ignore') as f_obj:
								       AValueFiledata = ValueFile_Reader(f_obj)
								       AttributeValuePresent = True
								       avfilename = ValueFname1
								       av_path = avfilename.replace(YTSpath,WIPpath)
									         
						   if os.path.isfile(ValueFname20):
							   ValueFname2 = ValueFname20
							   VF2 = True
						   elif os.path.isfile(ValueFname21):
							   ValueFname2 = ValueFname21
							   VF2 = True
						   elif os.path.isfile(ValueFname22):
							   ValueFname2 = ValueFname22
							   VF2 = True
						   
						   if VF2 == True:			
						      with codecs.open(ValueFname2, "r",encoding='utf-8', errors='ignore') as f_obj:
								       AValueFiledata = ValueFile_Reader(f_obj)
								       AttributeValuePresent = True
								       avfilename = ValueFname2
								       av_path = avfilename.replace(YTSpath,WIPpath)
   
						   
						   if AttributeValuePresent and status == True:
							   move_to_wip(name, eKFname,WIPpath,avfilename,AttributeValuePresent)
						   elif status == True:
							   move_to_wip(name, eKFname,WIPpath,'xyz',False)
						          
						   if status == True:
							   #print(data_path,kw_path, YTSpath, av_path)
							   t = time.time()
							   KeywordFileName = kw_path.replace(WIPpath,'')
							   
							   Status = 'YTP'
							   CreatedOn = datetime.date(datetime.now())
							   cursor = cnx.cursor()
							
							   keyworddetailsExist = query_format("Select ''KeywordDetailsID'' from ''KeywordDetails'' where ''ProductName'' = '"+DataFileName+"' and ''Attribute'' = '"+Attribute+"'")
							
							   cursor.execute(keyworddetailsExist)
							   rowcount = cursor.rowcount;
							   
							   if rowcount != 0:
								   if AttributeValuePresent:
									   move_back(data_path,kw_path,YTSpath,'File already processed. If you want to run again, please rename the file.',av_path, AttributeValuePresent)
									   break
								   else:
									   move_back(data_path,kw_path,YTSpath,'File already processed. If you want to run again, please rename the file.','xyz',False)
									   break
								
							   Masterselect = query_format("SELECT ''ItemID_Attribute_ShelfID'', ''AttributeValue'' from ''mstFileDetails'' where ''ItemID_Attribute_ShelfID'' like '%"+Attribute+str(ShelfId)+"'")   
							   cursor.execute(Masterselect)
							   
							   for row in cursor:
								   mstList.append(row)
							   mstList = dict(mstList)
							   #print(mstList)
							   
							   TransSelect = query_format("SELECT ''ItemID_Attribute_ShelfID'', ''TaggingStatus'' from ''FileTransaction'' where ''ItemID_Attribute_ShelfID'' like '%"+Attribute+str(ShelfId)+"' and ''FileTransactionStatus'' = 'DISPATCHED'")
							   cursor.execute(TransSelect)
							   
							   for row in cursor:
								   transList.append(row)
							   transList = dict(transList) 
							   #print(transList)  
							   Attribute_VAL = query_format("Insert into ''closelist_values''(''clvalues'', ''filename'') values (%s, %s)")
							   if AttributeValuePresent == True:
								      AValueFiledata = AValueFiledata[1:]
								      AValueFiledict = {'closelist_values': removelist(AValueFiledata)}
								      AttributeValueData = (json.dumps(AValueFiledict), avfilename.replace(YTSpath+'/', ''))
								      cursor.execute(Attribute_VAL, AttributeValueData)	
									  
										     
							   print('Reading keywords file',time.strftime("%H:%M:%S", time.gmtime(time.time())))
							
							   with codecs.open(kw_path, "r",encoding='utf-8', errors='ignore') as f_obj:
							      kdata = keyword_reader(f_obj)
								  
							   
							   if len(kdata[0]) == 3:
								      UnitOfM = True
							   elif len(kdata[0]) == 1:	
								   
								   if AttributeValuePresent:
									   move_back(data_path,kw_path,YTSpath,'Incorrect Keywords file format',av_path, AttributeValuePresent)
								   else:
									   move_back(data_path,kw_path,YTSpath,'Incorrect Keywords file format','xyz',False)
								   
								   raise CustomError ("Incorrect Keywords file format")
								   break

								     
							   else:
								   UnitOfM = False
							   keyword = kdata[0][0]
							   Antikeyword = kdata[0][1]
							   if UnitOfM:
								   Unit = kdata[0][2]


						   
							   for i in kdata:
								   if i[0] != '':
									   keywords.append(i[0])
								   if i[1] != '':
									   antikeywords.append(i[1])
								   if UnitOfM:
									   if i[2] != '':
										   UOM.append(i[2])
										
							   keywords = keywords[1:]
							   antikeywords = antikeywords[1:]
							   UOM = UOM[1:]
							
							   for i in range(0,len(keywords)):
								   KEYWORDS[i+1] = keywords[i]
							   for i in range(0, len(antikeywords)):
								   ANTIKEYWORDS[i+1] = antikeywords[i]
							   if UnitOfM:
								   for i in range(0, len(UOM)):
									   UOMs[i+1] = UOM[i]
								   
							   c = KEYWORDS.values()
							   d = ANTIKEYWORDS.values()
							   UOMlist = '\\b|'.join(UOMs.values())
							   UOMlist = UOMlist + '\\b'
							   UOMregex = '([.\d]+[\s_-]*('+UOMlist+'){1,2})'
							   UOMreg = re.compile(UOMregex, re.IGNORECASE)
							   #for a in UOMlist:
								#	UOMPDlist.append(a[0])
								#UOMPDlist = list(set(UOMPDlist))
							
							
							   keyworddetails = query_format("INSERT INTO ''KeywordDetails''(''Attribute'', ''ProductShelfID'', ''Keywords'', ''AntiKeywords'',''ProductName'')VALUES (%s, %s, %s, %s, %s);")   
							   keyworddetails_data = (Attribute, ShelfId, json.dumps(KEYWORDS) ,json.dumps(ANTIKEYWORDS),DataFileName)
							   keyworddetail = query_format("Select ''KeywordDetailsID'' from ''KeywordDetails'' where ''ProductShelfID''='"+ShelfId+"' and ''Attribute'' = '"+Attribute+"'" )
							
							   dataUpload = query_format("INSERT INTO ''FileUpload'' (''DataFileName'', ''KeywordsFileName'', ''ShelfID'', ''Attribute'', ''Status'', ''CreatedOn'', ''KeywordDetailsID'')VALUES (%s, %s, %s, %s, %s, %s, %s);")
							   FileUpload = query_format("Select ''FileUploadID'' from ''FileUpload'' where ''DataFileName'' = '"+DataFileName+ "'AND ''KeywordsFileName'' = '"+KeywordFileName+"'")
							   
							   #transDetails = query_format("Insert into ''FileTransaction''(''FileUploadID'', ''ItemID'', ''ProductID'', ''ProductName'',  ''PrimaryAssetUrl'', ''OfferLifecycleStatus'', ''ProductShortDescription'',  ''ProductLongDescription'', ''PrimaryShelfId'', ''PrimaryShelf'', ''AllShelvesId'',  ''AllShelves'', ''PchId'', ''Category'', ''ProductType'', ''AbstractProductId'',  ''ProductClassType'', ''ItemID_Attribute_ShelfID'', ''FileData'', ''ProductNameFilteredText'',  ''ProductLongDescriptionFilteredText'', ''KeywordTags'', ''AntikeywordTags'',  ''ProductNameKeywords'', ''ProductNameAntiKeywords'', ''ProductLongDescKeywords'',  ''ProductLongDescAntiKeywords'', ''ProductShortDescKeywords'', ''ProductShortDescAntiKeywords'', ''TaggingStatus'',   ''Attribute'', ''DistinctKeywords'') values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
							   if UnitOfM:
								   transDetails = query_format("Insert into ''FileTransaction''(''FileUploadID'', ''ItemID'', ''ProductID'', ''ProductName'',  ''PrimaryAssetUrl'', ''OfferLifecycleStatus'', ''ProductShortDescription'',  ''ProductLongDescription'', ''PrimaryShelfId'', ''PrimaryShelf'', ''AllShelvesId'',  ''AllShelves'', ''PchId'', ''Category'', ''ProductType'', ''AbstractProductId'',  ''ProductClassType'', ''ItemID_Attribute_ShelfID'', ''FileData'', ''ProductNameFilteredText'',  ''ProductLongDescriptionFilteredText'', ''ProductNameKeywords'', ''ProductNameAntiKeywords'', ''ProductDescKeywords'', ''ProductDescAntiKeywords'', ''TaggingStatus'',''FileTransactionStatus'',   ''Attribute'', ''DistinctKeywords'', ''ProductNameUOM'', ''ProductDescUOM'') values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
							   else:
								   transDetails = query_format("Insert into ''FileTransaction''(''FileUploadID'', ''ItemID'', ''ProductID'', ''ProductName'',  ''PrimaryAssetUrl'', ''OfferLifecycleStatus'', ''ProductShortDescription'',  ''ProductLongDescription'', ''PrimaryShelfId'', ''PrimaryShelf'', ''AllShelvesId'',  ''AllShelves'', ''PchId'', ''Category'', ''ProductType'', ''AbstractProductId'',  ''ProductClassType'', ''ItemID_Attribute_ShelfID'', ''FileData'', ''ProductNameFilteredText'',  ''ProductLongDescriptionFilteredText'', ''ProductNameKeywords'', ''ProductNameAntiKeywords'', ''ProductDescKeywords'', ''ProductDescAntiKeywords'', ''TaggingStatus'',''FileTransactionStatus'',    ''Attribute'', ''DistinctKeywords'') values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
							
							   try:
								   cursor.execute(keyworddetails, keyworddetails_data)					   
								   cnx.commit()
								   cursor.execute(keyworddetail)
								   row = cursor.fetchone()
								   keyworddetailsID =row[0]
	  
								   
								   dataUpload_data = (DataFileName, KeywordFileName, str(ShelfId), Attribute, Status, str(CreatedOn) ,str(keyworddetailsID))
							   
								   try:
									   cursor.execute(dataUpload, dataUpload_data)
									   cnx.commit()
									   print("FileUpload Table generated",time.strftime("%H:%M:%S", time.gmtime(time.time())),'\n ......Reading Data File......\n')
									   with codecs.open(data_path, "r",encoding='utf-8', errors='ignore') as f_obj:
										   data = csv_reader(f_obj)
									   #cursor.execute(dataUpload, dataUpload_data)
								
									   print("Excel Data Read",time.strftime("%H:%M:%S", time.gmtime(time.time())))
								
								      
									   try:
										   cursor.execute(FileUpload) # test select from FileUploadID
										   row = cursor.fetchone() 
										   FileUploadID = row [0]
										   print("Start reading rows")
							   		         
								
										   for i in range(0,len(data)):				#for i in range(0,len(data)):
											   PNkeys, PLDkeys, PNAkeys, PLDAkeys, UOMPDlist = [],[],[],[],[]
											   a = list(data[i].items())
											   ProductID = a[1][1]
											   ItemID = a[2][1]
											   ProductName = a[3][1]
											   ProductNameFilteredText = filterText(ProductName)
											   PrimaryAssetUrl = a[4][1]
											   OfferLifecycleStatus = a[5][1]
											   ProductShortDescription = a[6][1]
											   ProductLongDescription = a[7][1]
											   PrimaryShelfId = a[8][1]
											   PrimaryShelf = a[9][1]
											   AllShelvesId = a[10][1]
											   AllShelves = a[11][1]
											   PchId = a[12][1]
											   Category = a[13][1]
											   ProductType = a[14][1]
											   AbstractProductId = a[15][1]
											   ProductClassType  = a[16][1]
											   ProductNameFilteredText = filterText(ProductName)
											   ProductLongDescriptionFilteredText = filterText(ProductLongDescription)
											   ProductShortDescriptionFilteredText = filterText(ProductShortDescription)
											   PNKeywords = list(set(splitstring(re.sub('([\[\^$.?*+\(\)<>*"\'/,-])','',remove_tags(ProductName)))).intersection(keywords))
											   PLDKeywords = list(set(splitstring(re.sub('([\[\^$.?*+\(\)<>*"\'/,-])','',remove_tags(ProductLongDescription)))).intersection(keywords))
											   PSDKeywords = list(set(splitstring(re.sub('([\[\^$.?*+\(\)<>*"\'/,-])','',remove_tags(ProductShortDescription)))).intersection(keywords))
											   PNAntikeywords = list(set(splitstring(re.sub('([\[\^$.?*+\(\)<>*"\'/,-])','',remove_tags(ProductName)))).intersection(antikeywords))
											   PLDAntikeywords = list(set(splitstring(re.sub('([\[\^$.?*+\(\)<>*"\'/,-])','',remove_tags(ProductLongDescription)))).intersection(antikeywords))
											   PSDAntikeywords = list(set(splitstring(re.sub('([\[\^$.?*+\(\)<>*"\'/,-])','',remove_tags(ProductShortDescription)))).intersection(antikeywords))
											   PDKeywords = list(set(PLDKeywords).union(PSDKeywords))
											   PDAntikeywords = list(set(PLDAntikeywords).union(PSDAntikeywords))
											   #Keywords = {'PN': PNKeywords, 'PLD': PLDKeywords, 'PSD':PSDKeywords}
											   #Antikeywords = {'PN': PNAntikeywords, 'PLD': PLDAntikeywords, 'PSD':PSDAntikeywords}
											   #FileDetails = query_format("Insert into ''FileDetails'' (''FileUploadID'' , ''ShelfID'' , ''Attribute'' , ''ItemID'' , ''ProductID'' , ''ProductName'' , ''PrimaryAssetUrl'' , ''OfferLifecycleStatus'' , ''ProductShortDescription'' , ''ProductLongDescription'' , ''PrimaryShelfId'' , ''PrimaryShelf'' , ''AllShelvesId'' , ''AllShelves'' , ''PchId'' , ''Category'' , ''ProductType'' , ''AbstractProductId'' , ''ProductClassType'' , ''ItemID_Attribute_ShelfID'' , ''FileData'' , ''ProductNameFilteredText'' , ''ProductLongDescriptionFilteredText'' , ''ProductNameTags'' , ''ProductLongDescriptionTags'' , ''ProductNameKeywords'' , ''ProductNameAntiKeywords'' , ''ProductLongDescKeywords'' , ''ProductLongDescAntiKeywords'') values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
											   #FileDetails_data = (str(FileUploadID), str(ShelfId) , Attribute , str(ItemID) , ProductID , ProductName , PrimaryAssetUrl , OfferLifecycleStatus , ProductShortDescription , ProductLongDescription , str(PrimaryShelfId) , PrimaryShelf , str(AllShelvesId) , AllShelves , PchId , Category , ProductType , AbstractProductId , ProductClassType,str(ItemID)+Attribute+str(ShelfId),json.dumps(dict(a[17:len(a)+1])),ProductNameFilteredText, ProductLongDescriptionFilteredText, json.dumps(Keywords), json.dumps(Antikeywords),removelist(PNKeywords),removelist(PNAntikeywords),removelist(PLDKeywords),removelist(PLDAntikeywords))
											   if UnitOfM:
												   UOMPNlist = UOMreg.findall(ProductName)
												   if len(UOMPNlist) != 0:
													   UOMPNlist = list(UOMPNlist[0][:-1])
												   if len(UOMreg.findall(ProductShortDescription+ProductLongDescription)) != 0:   
													   for a in UOMreg.findall(ProductShortDescription+ProductLongDescription):
														      UOMPDlist.append(a[0])
												   UOMPDlist = list(set(UOMPDlist))
											   Jsondata = dict(a[17:len(a)+1])
											   AttributeValue = Jsondata.get(Attribute)
											   ItemID_Attribute_ShelfID = str(ItemID)+Attribute+str(ShelfId)
											   if ItemID_Attribute_ShelfID in mstList:
												   if AttributeValue == mstList.get(mstList):
													   TaggingStatus = 'ITEM_CONFLICT'
												   elif TaggingStatus != mstList.get(mstList):
													   TaggingStatus = 'VALUE_CONFLICT'
											   elif ItemID_Attribute_ShelfID in transList:
												   TaggingStatus = 'ITEM_CONFLICT'
											   else:
												   TaggingStatus = 'NEW'
											   DistinctKeywords = list(set(PNKeywords).union(PDKeywords))
											   if UnitOfM:
												   transDetails_data = (str(FileUploadID) , str(ItemID) , ProductID , ProductName , PrimaryAssetUrl , OfferLifecycleStatus , ProductShortDescription , ProductLongDescription , str(PrimaryShelfId) , PrimaryShelf , str(AllShelvesId) , AllShelves , PchId , Category , ProductType , AbstractProductId , ProductClassType, ItemID_Attribute_ShelfID, json.dumps(Jsondata), ProductNameFilteredText, ProductLongDescriptionFilteredText, removelist(PNKeywords), removelist(PNAntikeywords), removelist(PDKeywords), removelist(PDAntikeywords), TaggingStatus,TaggingStatus, AttributeValue, removelist(DistinctKeywords),removelist(UOMPNlist),removelist(UOMPDlist))
											   else:
												   transDetails_data = (str(FileUploadID) , str(ItemID) , ProductID , ProductName , PrimaryAssetUrl , OfferLifecycleStatus , ProductShortDescription , ProductLongDescription , str(PrimaryShelfId) , PrimaryShelf , str(AllShelvesId) , AllShelves , PchId , Category , ProductType , AbstractProductId , ProductClassType, ItemID_Attribute_ShelfID, json.dumps(Jsondata), ProductNameFilteredText, ProductLongDescriptionFilteredText, removelist(PNKeywords), removelist(PNAntikeywords), removelist(PDKeywords), removelist(PDAntikeywords), TaggingStatus,TaggingStatus, AttributeValue, removelist(DistinctKeywords))
											   #print(transDetails_data)
											   try:  
												   '''if i == 500:
													   cnx.commit()'''
												   cursor.execute(transDetails, transDetails_data)
												   print(i)
												   
											   except:
												   if AttributeValuePresent:
													   move_back(data_path,kw_path,YTSpath,'Failure in update to table FileDetails',av_path,AttributeValuePresent)
												   else:
													   move_back(data_path,kw_path,YTSpath,'Failure in update to table FileDetails','xyz',False)
												   raise CustomError ('Failure in update to table FileDetails')
									   except:
										   if AttributeValuePresent:
											   move_back(data_path,kw_path,YTSpath,'Failure in Select from Table FileDetails',av_path,AttributeValuePresent)
										   else:
											   move_back(data_path,kw_path,YTSpath,'Failure in Select from Table FileDetails','xyz',False)
										   raise CustomError ('Failure in Select from Table FileDetails')         
								   except:
										   if AttributeValuePresent:
											   move_back(data_path,kw_path,YTSpath,'Insert into table FileUploads failed',av_path,AttributeValuePresent)
										   else:
											   move_back(data_path,kw_path,YTSpath,'Insert into table FileUploads failed','xyz',False)

										   raise CustomError ("Insert into table FileUploads failed")

							   except(FileNotFoundError):
								   raise CustomError("File with same name present in the database. Try Renaming.")

							   except:
								   if AttributeValuePresent:
									   move_back(data_path,kw_path,YTSpath,'Insert into table FileUploads failed',av_path, AttributeValuePresent)
								   else:
									   move_back(data_path,kw_path,YTSpath,'Insert into table FileUploads failed','xyz',False)
								   
								   raise CustomError ("Insert into table KeywordDetails failed")
							   
								   
							   
							   print("Commit start",time.strftime("%H:%M:%S", time.gmtime(time.time())))
							   cnx.commit()
							   
							   if AttributeValuePresent == True:
								   move_to_done(data_path,kw_path,donepath,av_path,AttributeValuePresent)
							   else:
								   move_to_done(data_path,kw_path,donepath,'xyz',False)
							   JsonString = ''
							   
							   print('Start Time:',time.strftime("%H:%M:%S", time.gmtime(t)),'Finish time:',time.strftime("%H:%M:%S", time.gmtime(time.time())),'Total time:',time.strftime("%H:%M:%S", time.gmtime(time.time()-t)))
							   t2 = time.time()		   
							   
							   Jsonfields = list(Jsondata.keys())
							   for a in Jsonfields:
								   JsonString = JsonString + "''FileData''->> '"+ a +"' AS "+a+", "
							   #print(JsonString)
							   
							   fetchToCsv = query_format("COPY (SELECT ''FileUploadID'' ,  ''ItemID'' ,  ''ProductID'' ,  ''ProductName'' ,  ''PrimaryAssetUrl'' ,  ''OfferLifecycleStatus'' ,  ''ProductShortDescription'' ,  ''ProductLongDescription'' ,  ''PrimaryShelfId'' ,  ''PrimaryShelf'' ,  ''AllShelvesId'' ,  ''AllShelves'' ,  ''PchId'' ,  ''Category'' ,  ''ProductType'' ,  ''AbstractProductId'' ,  ''ProductClassType'' ,  ''ItemID_Attribute_ShelfID'' ,  "+JsonString+"  ''ProductNameFilteredText'' ,  ''ProductLongDescriptionFilteredText'' ,  ''ProductNameKeywords'' ,  ''ProductNameAntiKeywords'' ,  ''ProductLongDescKeywords'' ,  ''ProductLongDescAntiKeywords'' ,  ''ProductShortDescKeywords'' ,  ''ProductShortDescAntiKeywords'' ,  ''TaggingStatus'', ''Attribute'' ,  ''DistinctKeywords'' , ''ProductNameUOM'' , ''ProductDescUOM'' FROM ''FileTransaction'' WHERE ''FileUploadID'' = "+str(FileUploadID)+") TO '"+export_path+"' DELIMITER ',' CSV HEADER;")
							#copy(
							   #print(fetchToCsv)
							   try:
								   cursor.execute(fetchToCsv)
								   #print("From: ",copy_csv_from,"\nTo: ",copy_csv_to)
								   shutil.move(copy_csv_from,copy_csv_to)
							
								   print("Export completed:",time.strftime("%H:%M:%S", time.gmtime(time.time())))
							   except Exception as e:
								   print('Export Failed',e)
							   
							   #outputquery = query_format("COPY ({0}) TO STDOUT WITH CSV HEADER")
   
if status != True:  
	print("Status = ", status,"Error: No files present or file naming format is incorrect")	
	
