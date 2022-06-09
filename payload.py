import json
from system.operation_system import OperationSystem
from exceptions.exception_events import Logger

class Payload:
    
    def __init__(self) -> None:
        self.__mock = self.__open_mock()
    
    @property
    def get(self):
        return self.__mock
    
    def __open_mock(self):
        if OperationSystem().env.mock_task.value == 'true':
            Logger().info("Mock ativo, iniciando tarefa mocada")
            try:
                with open(OperationSystem().directory.mock.value) as task_mock:
                    mock_task = json.load(task_mock)
                    return mock_task
            except Exception as err:
                raise err
