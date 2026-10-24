import requests
import matplotlib
import numpy as np
import pandas as pd
import pydicom

import os
import sys

if sys.version_info[:3] == (3,12,10) and os.path.join(os.getcwd(), '.venv') in sys.executable:
    print('Wszystko ustawione!')
else:
    print(f'Używasz wersji pythona {sys.version_info[:3]}, z lokalizacji {sys.executable}. Sprawdź to :)')


