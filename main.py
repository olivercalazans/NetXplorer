import os, platform
import pyfiglet
from strategy import *

class Main:
    DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    if platform.system() == 'Windows': DIRECTORY += '\\wfiles\\'
    elif platform.system() == 'Linux': DIRECTORY += '/wfiles/'


    STRATEGY_DICTIONARY = {
        "help":  Command_List_Strategy(),
        "pscan": Portscan_Strategy(),
        "ip":    IP_Strategy()
    }


    def __init__(self) -> None:
        self._stop_flag = False
        self._create_directory()


    @staticmethod
    def _create_directory(_directory:str) -> None:
        try:   os.mkdir(_directory)
        except FileExistsError: print('The directory already exists')
        except Exception as error: print(f'Error creating directory: {error}')
        else:  print('Directory created')


    @classmethod
    def _get_directory(cls) -> str:
        return cls.DIRECTORY
    

    @classmethod
    def _get_strategy_dictionary(cls) -> dict:
        return cls.STRATEGY_DICTIONARY


    @property
    def stop(self) -> None:
        self._stop_flag = True


    def _handle_client(self) -> None:
        print(pyfiglet.figlet_format("watcher"))
        while not self._stop_flag:
            ...


    @staticmethod
    def _separate_function_from_arguments(string:str) -> tuple[str, str]:
        ...


    def _check_if_the_method_exists(self) -> tuple[str, str]:
        ...


    def _get_result(self) -> tuple[str, str]:
       ...



if __name__ == '__main__':
    server = Main()
    server.receive_client()
