# -*- encoding: utf-8 -*-
from datetime import datetime
TODAY = datetime.now()
LOG_PATH = './log/'
MODULE_LOG = {
	"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
	"filename": LOG_PATH+"module/"+str(TODAY.year)+"/module_"+str(datetime.now().date())+".log",
	"error" : {
		"filename": LOG_PATH+"module/"+str(TODAY.year)+"/error_"+str(datetime.now().date())+".log",
		"maxBytes": 0,
        "backupCount": 20,
        "encoding": "utf8"
	},
	"info" : {
		"filename": LOG_PATH+"module/"+str(TODAY.year)+"/info_"+str(datetime.now().date())+".log",
		"maxBytes": 0,
        "backupCount": 20,
        "encoding": "utf8"
	}
}

MODEL_LOG = {
	"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
	"filename": LOG_PATH+"model/"+str(TODAY.year)+"/model_"+str(datetime.now().date())+".log",
	"error" : {
		"filename": LOG_PATH+"model/"+str(TODAY.year)+"/error_"+str(datetime.now().date())+".log",
		"maxBytes": 0,
        "backupCount": 20,
        "encoding": "utf8"
	},
	"info" : {
		"filename": LOG_PATH+"model/"+str(TODAY.year)+"/info_"+str(datetime.now().date())+".log",
		"maxBytes": 0,
        "backupCount": 20,
        "encoding": "utf8"
	}
}
