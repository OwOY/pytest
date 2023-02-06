import sys
sys.path.append('../')
import pytest
from fastapi.responses import JSONResponse
from importlib import import_module
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.basemodel import Settings, init_db, drop_db
from service.equipmentService import SrvEquipment
from service.workStationService import SrvWorkStation



env = Settings().cfg_config
module = import_module(f'config.{env}')
base_url = getattr(module, 'DB_URL')
db_url = f'{base_url}/test'
engine = create_engine(url=db_url)
session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = session_factory()


class TestCase():
    def setup_class(self):
        init_db(engine)
        
    def teardown_class(self):
        session.close()
        drop_db(engine)
        logger.info('測試資料庫移除成功')
    
    def teardown_method(self):
        session.close()
    ###################################################################
    #                              設備                               #
    ###################################################################
    def test_get_equipment_by_id_list(self):
        result = SrvEquipment(session).get_equipment_by_id_list([])
        assert isinstance(result, list)
    
    def test_get_all_equipment(self):
        class Params:
            equipmentClassNumber='test'
        result = SrvEquipment(session).get_all_equipment(Params)
        assert isinstance(result, JSONResponse)
    
    ###################################################################
    #                              工站                               #
    ###################################################################
    def test_get_workstation_class_number(self):
        result = SrvWorkStation(session).get_workstation_class_number()
        assert isinstance(result, JSONResponse)
    
    def test_get_workstation_number(self):
        class Params:
            workStationClassNumber='test'
        result = SrvWorkStation(session).get_workstation_number(Params)
        assert isinstance(result, JSONResponse)
        
    def test_get_workstation(self):
        class Params:
            workStationNumber='test'
        result = SrvWorkStation(session).get_workstation(Params)
        assert isinstance(result, JSONResponse)
    
    def test_add_workstation(self):
        class AddWorkStation:
            workStationNumber='test'
            workStationName='test'
            workStationClassNumber='test'
            workStationDescription='test'
            availableMaterialClass='test'
            equipmentGroup=[1, 2]
        user_info = {'name':'test'}
        result = SrvWorkStation(session).add_workstation(AddWorkStation, user_info)
        assert isinstance(result, JSONResponse)
    
    def test_update_workstation(self):
        class UpdateWorkStation:
            workstationId=1
            workStationName='test'
            workStationClassNumber='test'
            workStationDescription='test'
            availableMaterialClass='test'
            equipmentGroup=[1, 2]
        user_info = {'name':'test'}
        result = SrvWorkStation(session).update_workstation(UpdateWorkStation, user_info)
        assert isinstance(result, JSONResponse)
        
        
if __name__ == '__main__':
    pytest.main(['-s', 'testMain.py'])