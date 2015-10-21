from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'BHnTuples_2015DreMiniAOD05Oct2015v1_oct22'
config.General.workArea = 'crab_jobs_2015DreMiniAOD05Oct2015v1_oct22'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'reMiniAOD05Oct2015v1-tuples_2015D.py'

config.Data.inputDataset = '/JetHT/Run2015D-05Oct2015-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 35
config.Data.lumiMask='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.publishDataName = 'BHnTuples_2015DreMiniAOD05Oct2015v1_oct22'

config.Site.storageSite = 'T3_US_Brown'
