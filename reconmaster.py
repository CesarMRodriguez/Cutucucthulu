import globals
import ConfigParser
from database_management import DatabaseConnection
from stages.generic_stage import GenericStage
from stages.stage_db import StageDB

def print_flag():
    print('--- CUTUCUCTHULU ---')

def initialize():
    globals.configParser = ConfigParser.ConfigParser()
    globals.configParser.read('configuration.properties')
    globals.db = DatabaseConnection(globals.configParser.get('Database Connection','DB_HOST'),
                            int(globals.configParser.get('Database Connection','DB_PORT')))
    globals.db.initDatabase()

print_flag()
initialize()

genStage = GenericStage()
genStage.fillOption(StageDB())
genStage.executeStage()
