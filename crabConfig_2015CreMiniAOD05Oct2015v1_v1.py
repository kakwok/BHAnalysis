from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'BHnTuples_2015CreMiniAOD05Oct2015v1_Nov28'
config.General.workArea = 'crab_jobs_2015CreMiniAOD05Oct2015v1_Nov28'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'reMiniAOD05Oct2015v1-tuples_2015C_v1.py'
config.JobType.inputFiles=['Summer15_25nsV6_DATA.db','Summer15_25nsV6_DATA']

config.Data.inputDataset = '/JetHT/Run2015C_25ns-05Oct2015-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 35
config.Data.lumiMask='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'BHnTuples_2015CreMiniAOD05Oct2015v1_Nov28'

config.Site.storageSite = 'T3_US_Brown'
