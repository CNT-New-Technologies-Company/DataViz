# diccionatios.py

orden_cols = [
    'Pozo', 'Etapa', 'Fecha Inicio', 'Fecha Fin', 'Hora Inicio', 'Hora Fin', 'desde',
    'hasta', 'Notas', 'Tipo Agujero', 'Actividad', 'Actividades', 'Actividad Programada', 
    'Sub Actividad', 'Descripción Actividad', 'Condicionante', 'Color', 'Color Est', 
    'Hora', 'ROT M', 'DESL M', 'ROT MIN', 'DESL MIN', 'CIRC MIN', 'H BBA', 'ROP',
    'Rebaja Cem', 'TipoTr', 'VelTR', 'Viajes M', 'Vel', 'Lingadas', 'Long Ling', 'TC', 
    'Tipo BHA', 'Profundidad Conexión', 'Pre', 'Pre Survey', 'Pre Comando', 'Repaso', 
    'Conexión', 'Pos', 'Pos Comando', 'Pos Survey', 'Orienta', 'Otros', 'Reducida', 
    'Baches', 'ProcMPD', 'Duración', 'Inc'
]

output_cols = [
    "Pozo", "Tipo de pozo", "Equipo", "Perforadora", "Etapa", "Fecha", "Inicia", 
    "Termina", "Semana", "Hora", "Turno", "Color est", "Actividad", "Actividades",
    "Actividad programada", "Sub actividad", "Descripción actividad", "Condicionante", 
    "Tipo agujero", "Desde", "Hasta", "Profundidad de pozo", "Tiempo (hr)", "Metros rotados", 
    "Metros deslizados", "Tiempo rotado (min)", "Tiempo deslizado (min)", 
    "Tiempo circulado (min)", "Tiempo de bombeo (hr)", "ROP", "Rebaja cemento", 
    "Pre-conexion", "Survey antes", "Comando antes", "Repaso", 
    "Conexion cuña a cuña", "Post-conexion", "Comando despues", 
    "Survey despues", "Orienta", "Otros", "Reducida", "Baches", 
    "Procedimiento MPD", "Conexion fondo a fondo", "Inclinacion", 
    "Profundidad de conexion", "Metros viajados", "Velocidad (m/h)", 
    "Cantidad de lingadas", "Longitud de lingada", "Tiempo de conexion", 
    "Diametro de TR", "Velocidad de introduccion TR", "Tipo de BHA", 
    "eficiencia", "estandar", "tnpi"
]

nombre_columnas = {
    'Hora': 'Tiempo (hr)', 
    'Rot m': 'Metros rotados', 
    'Desl m': 'Metros deslizados', 
    'Rot min': 'Tiempo rotado (min)', 
    'Desl min': 'Tiempo deslizado (min)', 
    'Circ min': 'Tiempo circulado (min)', 
    'H bba': 'Tiempo de bombeo (hr)', 
    'Rop': 'ROP', 
    'Rebaja cem': 'Rebaja cemento', 
    'Viajes m': 'Metros viajados', 
    'Vel': 'Velocidad (m/h)', 
    'Lingadas': 'Cantidad de lingadas', 
    'Tc': 'Tiempo de conexion', 
    'Tipo bha': 'Tipo de BHA', 
    'Profundidad conexión': 'Profundidad de conexion', 
    'Pre': 'Pre-conexion', 
    'Pre survey': 'Survey antes', 
    'Pre comando': 'Comando antes', 
    'Conexión': 'Conexion cuña a cuña', 
    'Pos': 'Post-conexion',
    'Pos comando': 'Comando despues', 
    'Pos survey': 'Survey despues', 
    'Procmpd': 'Procedimiento MPD', 
    'Duración': 'Conexion fondo a fondo', 
    'Tipotr': 'Diametro de TR', 
    'Veltr': 'Velocidad de introduccion TR', 
    'Long ling': 'Longitud de lingada', 
    'Inc': 'Inclinacion'
}

dtype_mapping = {
    'Pozo': 'str',
    'Etapa': 'str',
    'Fecha inicio': 'datetime',
    'Fecha fin': 'datetime',
    'Hora inicio': 'timedelta',
    'Hora fin': 'timedelta',
    'Desde': 'int64',
    'Hasta': 'int64',
    'Notas': 'str',
    'Tipo agujero': 'str',
    'Actividad': 'str',
    'Sub actividad': 'str',
    'Descripción actividad': 'str',
    'Condicionante': 'str',
    'Color': 'int64',
    'Color est': 'str',
    'Tiempo (hr)': 'int64',
    'Metros rotados': 'float64',
    'Metros deslizados': 'float64',
    'Tiempo rotado (min)': 'float64',
    'Tiempo deslizado (min)': 'float64',
    'Tiempo circulado (min)': 'float64',
    'Tiempo de bombeo (hr)': 'float64',
    'ROP': 'float64',
    'Rebaja cemento': 'float64',
    'Diametro de TR': 'str',
    'Velocidad de introduccion TR': 'int64',
    'Metros viajados': 'int64',
    'Velocidad (m/h)': 'int64',
    'Cantidad de lingadas': 'int64',
    'Longitud de lingada': 'float64',
    'Tiempo de conexion': 'float64',
    'Tipo de BHA': 'int64',
    'Profundidad de conexion': 'int64',
    'Pre-conexion': 'float64',
    'Survey antes': 'float64',
    'Comando antes': 'float64',
    'Repaso': 'float64',
    'Conexion cuña a cuña': 'float64',
    'Post-conexion': 'float64',
    'Comando despues': 'float64',
    'Survey despues': 'float64',
    'Orienta': 'float64',
    'Otros': 'float64',
    'Reducida': 'float64',
    'Baches': 'float64',
    'Procedimiento MPD': 'float64',
    'Conexion fondo a fondo': 'float64',
    'Inclinacion': 'float64',
    'Inicia': 'datetime',
    'Termina': 'datetime',
    'Fecha': 'datetime',
    'Año': 'int64',
    'Semana': 'int64',
    'Hora': 'int64',
    'Tipo de pozo': 'str',
    'Equipo': 'str',
    'Perforadora': 'str',
    'Turno': 'str',
    'Estandar viaje': 'int64',
    'Tiempo teorico (hr)': 'float64',
    'Ahorro en viajes (hr)': 'float64',
    'TNPI viajes (hr)': 'float64',
    'Puntaje viaje': 'float64',
    'Eficiencia viaje': 'float64',
    'Eventos Totales': 'int64',
    'Eventos Cumplidos': 'int64',
    'Consistencia viajes': 'float64',
    'Estandar cp': 'int64',
    'Ahorro cp (min)': 'float64',
    'Ahorro cp (hr)': 'float64',
    'TNPI cp (min)': 'float64',
    'TNPI (hr)': 'float64',
    'Eficiencia cp': 'float64',
    'Eventos Totales cp': 'int64',
    'Eventos Cumplidos cp': 'int64',
    'Consistencia cp': 'float64'
}

nombre_pozos = {
    'ACTUL-4': 'ACTUL 4',
    'ETKAL 2DES': 'ETKAL 2DES',
    'MADREFIL 101': 'MADREFIL 101-EXP',
    'MADREFIL 201': 'MADREFIL 201-EXP',
    'MADREFIL 101 1EXP': 'MADREFIL 101-EXP',
    'MADREFIL 201 1EXP': 'MADREFIL 201-EXP',
    'MULACH 14V': 'MULACH 14 VENTANA',
    "ATOYATL 1 DEL": "ATOYATL 1 DEL",
    "ATOYATL 1DEL": "ATOYATL 1 DEL",
    "BAKTE 1DEL": "BAKTE 1 DEL",
    "NANIK 1EXP": "NANIK 1 EXP",
    'PORKCHE 104': 'POKCHE 104',
    'IXACHI-31': 'IXACHI 31',
    'MULACH 31': 'MULACH 31 INY',
    'MULACH 32': 'MULACH 32 INY',
    'PLATAO 2 ': 'PLATAO 2',
    "Platao-2": "PLATAO 2",
    "PLATAO-2": "PLATAO 2",
    'CAMATL-2': 'CAMATL 2',
    'POKCHE-103': 'POKCHE 103',
    'ATOYATL  2': 'ATOYATL 2',
    'RACEMOSA 4 ': 'RACEMOSA 4',
    'RACEMOSA 4 RMA': 'RACEMOSA 4 VENTANA',
    'CAMALT 4': 'CAMATL 4',
    'QUESQUI-420': 'QUESQUI 420',
    'TENTOK  4': 'TENTOK 4',
    'TUPILCO 3011 VENT': 'TUPILCO 3011 VENTANA',
    'TUPILCO 3012 VENT': 'TUPILCO 3012 VENTANA',
    'TUPILCO 3004RMA': 'TUPILCO 3004',
    'Tupilco 3004RMA': 'TUPILCO 3004',
    'TENTOK 1DEL': 'TENTOK 1 DEL',
    'TENTOK 1 DEL': 'TENTOK 1 DEL',
    'CIBIX 401 EXP 3': 'CIBIX 3',
    'TUPILCO - 3022': 'TUPILCO 3022',
}

nombre_equipos = {
    'GW-901 ': 'GW 901',
    'GW-901': 'GW 901',
    'GW-903': 'GW 903',
    'PM-306': 'PM 306', 
    'PM-341': 'PM 341', 
    'PM-335': 'PM 335', 
    'PM -335': 'PM 335',
    'PM-2304': 'PM 2304',
    'PM-2305': 'PM 2305', 
    'PM-329': 'PM 329',
    'PM-339': 'PM 339',
    'PM-324': 'PM 324',
    'GW-902': 'GW 902', 
    'RIG-703': 'RIG 703',
    'PM-1283': 'PM 1283',
    'PM-1381': 'PM 1381',
    'CME 1': 'CME I',
    'CME LL': 'CME II',
    'PM-342': 'PM 342', 
    'PM-1603': 'PM 1603',
    'RIG-702': 'RIG 702', 
    'GW-905': 'GW 905',
    'RIG-48': 'RIG 48',
    'RIG-70': 'RIG 702',
    'RIG-702': 'RIG 702',
    ' RIG-702': 'RIG 702',
    'RIG-703': 'RIG 703',
    'ICMA-880': 'ICMA 880', 
    'PM-305': 'PM 305',
    ' GALAR': 'GALAR',
    'GERSERMI': 'GERSEMI',
    'GALAR ': 'GALAR',
    'CME-II': 'CME II',
    'SANTA MARIA': 'LA SANTA MARIA',
    'SANTA MARIA / 3000 HP': 'LA SANTA MARIA',
    'PM-338 / 2000 HP': 'PM 338',
    'PM-1381 /1500 HP': 'PM 1381',
    'GW-901/3000 HP': 'GW 901',
    'GW-902/ 3000 HP': 'GW 902',
    'PM-335 / 2000 HP ': 'PM 335',
    'PM-339 / 2000 HP': 'PM 339', 
    'PM-2305/3000 HP': 'PM 2305',
    'PM-1383/1500': 'PM 1383', 
    'PITSA-018 / 1500 HP': 'PITSA 018', 
    'GW-903/3000': 'GW 903', 
    'PM-2302/3000': 'PM 2302', 
    'PM-2305/3000': 'PM 2305', 
    'PM-0305/3000HP': 'PM 305', 
    'PM-342/2000': 'PM 342', 
    'ICMA-880 / 3000 HP': 'ICMA 880', 
    'PM-324 / 2000 HP': 'PM 324',
    'PM-329/2000 HP': 'PM 329',
    'PM 342/ 2000 HP': 'PM 342',
    'PM-1603/3000 HP': 'PM 1603',
    'ICMA-880/3000 HP': 'ICMA 880',
    'GW - 905 / 3000 HP': 'GW 905',
    'PM 1386 / 1500 HP': 'PM 1386',
    'PM - 338/2000HP': 'PM 338',
    'PM-335 / 2000 HP': 'PM 335',
    'PM - 1383/1500 HP': 'PM 1383',
}

pozos_equipos = {
    'ACTUL 4': 'PM 1383',
    'ACTUL 5': 'PM 1383',
    'BAKTE 1 DEL': 'PM 2301',
    'BAKTE 2': 'GW 902',
    'BAKTE 3': 'PM 2005',
    'BAKTE 6': 'GW 168',
    'BAKTE 7': 'PM 2404',
    'CAMALT 51': 'ODIN',
    'CIBIX 3': 'PM 202',
    'CIBIX 34': 'PM 1386',
    'CIBIX 35': 'PM 1386',
    'CIBIX 37': 'PITSA 018',
    'CIBIX 40': 'PM 324',
    'CHUCOX 108': 'PM 338',
    'ETKAL 2DES': 'CME II',
    'ETKAL 5ADES': 'CME II',
    'ETKAL NE 202': 'CME II',
    'IXACHI 26': 'GW 903',
    'IXACHI 32': 'GW 901',
    'IXACHI 54': 'RIG 48',
    'IXACHI 60': 'PM 2302',
    'IXACHI 89': 'PM 2305',
    'MABALNAK 1EXP': 'GALAR',
    'NANIK 1 EXP': 'ODIN',
    'PLATAO 2': 'PM 335',
    'PLATAO 3': 'PM 335',
    'PLATAO 4': 'PM 305',
    'QUESQUI 181': 'PM 1503',
    'QUESQUI 28': 'GW 902',
    'QUESQUI 405': 'PM 1603',
    'QUESQUI 418': 'ICMA 882',
    'RACEMOSA 4': 'PM 342',
    'RACEMOSA 4 VENTANA': 'PM 342',
    'TECHIAKTLI 2': 'PM 9907',
    'TENTOK 1 DEL': 'GRID',
    'TLALKIVAK 2': 'NJORD',
    'TLALKIVAK 4': 'NJORD',
    'TUPILCO 3004': 'RIG 702',
    'TUPILCO 3011': 'GW 905',
    'TUPILCO 3012': 'ICMA 880',
    'TUPILCO 3015': 'RIG 703',
    'TUPILCO 3022': 'RIG 703',
    'VALERIANA 3': 'PM 339',
    'XANAB 58': 'GALAR',
    'XANAB 58A': 'GALAR'
}

pozo_perforadora = {
    'ACTUL 3': 'PEMEX',
    'ACTUL 4': 'PEMEX',
    'ACTUL 5': 'PEMEX',
    'AKAL 503': 'PEMEX',
    'AKAL 504': 'PEMEX',
    'ATOYATL 1 DEL': 'OPEX',
    'ATOYATL 2': 'OPEX',
    'ATOYATL 3': 'OPEX',
    'ATOYATL 3 RME': 'OPEX',
    'BAKTE 1 DEL': 'PEMEX',
    'BAKTE 2': 'PEMEX',
    'BAKTE 3': 'PEMEX',
    'BAKTE 6': 'PEMEX',
    'BAKTE 7': 'PEMEX',
    'CAMATL 2': 'OPEX',
    'CAMATL 4': 'OPEX',
    'CAMATL 5': 'OPEX',
    'CAMATL 51': 'OPEX',
    'CHUCOX 102': 'PEMEX',
    'CHUCOX 108': 'PEMEX',
    'CIBIX 3': 'PEMEX',
    'CIBIX 32': 'PEMEX',
    'CIBIX 34': 'PEMEX',
    'CIBIX 35': 'PEMEX',
    'CIBIX 36': 'PEMEX',
    'CIBIX 37': 'PEMEX',
    'CIBIX 40': 'PEMEX',
    'CIBIX 5': 'PEMEX',
    'ETKAL 2DES': 'OPEX',
    'ETKAL 5ADES': 'OPEX',
    'ETKAL NE 202': 'OPEX',
    'ITTA 69': 'OPEX',
    'ITTA 87': 'OPEX',
    'ITTA 88': 'OPEX',
    'ITTA 89': 'OPEX',
    'IXACHI 26': 'PEMEX',
    'IXACHI 27': 'PEMEX',
    'IXACHI 31': 'PEMEX',
    'IXACHI 32': 'PEMEX',
    'IXACHI 54': 'GSM',
    'IXACHI 60': 'PEMEX',
    'IXACHI 89': 'PEMEX',
    'MADREFIL 101-EXP': 'PEMEX',
    'MADREFIL 201-EXP': 'PEMEX',
    'MABALNAK 1EXP': 'OPEX',
    'MULACH 12': 'OPEX',
    'MULACH 13': 'OPEX',
    'MULACH 14': 'OPEX',
    'MULACH 14 VENTANA': 'OPEX',
    'MULACH 15': 'OPEX',
    'MULACH 16': 'OPEX',
    'MULACH 23': 'OPEX',
    'MULACH 31 INY': 'OPEX',
    'MULACH 32 INY': 'OPEX',
    'MULACH 32 VENTANA': 'OPEX',
    'NANIK 1 EXP': 'OPEX',
    'PLATAO 2': 'PEMEX',
    'PLATAO 3': 'PEMEX',
    'PLATAO 4': 'PEMEX',
    'POKCHE 102': 'OPEX',
    'POKCHE 103': 'OPEX',
    'POKCHE 104': 'OPEX',
    'POKCHE 15': 'OPEX',
    'QUESQUI 181': 'PEMEX',
    'QUESQUI 28': 'PEMEX',
    'QUESQUI 35': 'PEMEX',
    'QUESQUI 405': 'PEMEX',
    'QUESQUI 418': 'PEMEX',
    'QUESQUI 420': 'PEMEX',
    'RACEMOSA 4': 'PEMEX',
    'RACEMOSA 4 VENTANA': 'PEMEX',
    'TECA 43': 'OPEX',
    'TECA 51': 'OPEX',
    'TECA 71': 'OPEX',
    'TECHIAKTLI 2': 'PEMEX',
    'TEEKIT 12': 'OPEX',
    'TENTOK 1 DEL': 'OPEX',
    'TENTOK 2': 'OPEX',
    'TENTOK 3': 'OPEX',
    'TENTOK 4': 'OPEX',
    'TLACAME 51 INY': 'OPEX',
    'TLAKATI 2': 'OPEX',
    'TLAKATI 3': 'OPEX',
    'TLALKIVAK 2': 'OPEX',
    'TLALKIVAK 4': 'OPEX',
    'TUPILCO 3004': 'PEMEX',
    'TUPILCO 3009': 'PEMEX',
    'TUPILCO 3010': 'PEMEX',
    'TUPILCO 3011': 'PEMEX',
    'TUPILCO 3011 VENTANA': 'PEMEX',
    'TUPILCO 3012': 'PEMEX',
    'TUPILCO 3012 VENTANA': 'PEMEX',
    'TUPILCO 3015': 'OPEX',
    'TUPILCO 3016': 'PEMEX',
    'TUPILCO 3022': 'OPEX',
    'VALERIANA 3': 'PEMEX',
    'XANAB 58': 'PEMEX',
    'XANAB 58A': 'OPEX'
}

tipo_de_pozos = {
    'ACTUL 3': 'TERRESTRE',
    'ACTUL 4': 'TERRESTRE',
    'ACTUL 5': 'TERRESTRE',
    'AKAL 503': 'MARINO',
    'AKAL 504': 'MARINO',
    'ATOYATL 1 DEL': 'MARINO',
    'ATOYATL 2': 'MARINO',
    'ATOYATL 3': 'MARINO',
    'ATOYATL 3 RME': 'MARINO',
    'BAKTE 1 DEL': 'TERRESTRE',
    'BAKTE 2': 'TERRESTRE',
    'BAKTE 3': 'TERRESTRE',
    'BAKTE 6': 'TERRESTRE',
    'BAKTE 7': 'TERRESTRE',
    'CAMATL 2': 'MARINO',
    'CAMATL 4': 'MARINO',
    'CAMATL 5': 'MARINO',
    'CAMATL 51': 'MARINO',
    'CHUCOX 102': 'TERRESTRE',
    'CHUCOX 108': 'TERRESTRE',
    'CIBIX 3': 'TERRESTRE',
    'CIBIX 32': 'TERRESTRE',
    'CIBIX 34': 'TERRESTRE',
    'CIBIX 35': 'TERRESTRE',
    'CIBIX 36': 'TERRESTRE',
    'CIBIX 37': 'TERRESTRE',
    'CIBIX 40': 'TERRESTRE',
    'CIBIX 5': 'TERRESTRE',
    'ETKAL 2DES': 'MARINO',
    'ETKAL 5ADES': 'MARINO',
    'ETKAL NE 202': 'MARINO',
    'ITTA 69': 'MARINO',
    'ITTA 87': 'MARINO',
    'ITTA 88': 'MARINO',
    'ITTA 89': 'MARINO',
    'IXACHI 26': 'TERRESTRE',
    'IXACHI 27': 'TERRESTRE',
    'IXACHI 31': 'TERRESTRE',
    'IXACHI 32': 'TERRESTRE',
    'IXACHI 54': 'TERRESTRE',
    'IXACHI 60': 'TERRESTRE',
    'IXACHI 89': 'TERRESTRE',
    'MADREFIL 101-EXP': 'TERRESTRE',
    'MADREFIL 201-EXP': 'TERRESTRE',
    'MABALNAK 1EXP': 'TERRESTRE',
    'MULACH 12': 'MARINO',
    'MULACH 13': 'MARINO',
    'MULACH 14': 'MARINO',
    'MULACH 14 VENTANA': 'MARINO',
    'MULACH 15': 'MARINO',
    'MULACH 16': 'MARINO',
    'MULACH 23': 'MARINO',
    'MULACH 31 INY': 'MARINO',
    'MULACH 32 INY': 'MARINO',
    'MULACH 32 VENTANA': 'MARINO',
    'NANIK 1 EXP': 'MARINO',
    'PLATAO 2': 'TERRESTRE',
    'PLATAO 3': 'TERRESTRE',
    'PLATAO 4': 'TERRESTRE',
    'POKCHE 102': 'MARINO',
    'POKCHE 103': 'MARINO',
    'POKCHE 104': 'MARINO',
    'POKCHE 15': 'MARINO',
    'QUESQUI 181': 'TERRESTRE',
    'QUESQUI 28': 'TERRESTRE',
    'QUESQUI 35': 'TERRESTRE',
    'QUESQUI 405': 'TERRESTRE',
    'QUESQUI 418': 'TERRESTRE',
    'QUESQUI 420': 'TERRESTRE',
    'RACEMOSA 4': 'TERRESTRE',
    'RACEMOSA 4 VENTANA': 'TERRESTRE',
    'TECA 43': 'MARINO',
    'TECA 51': 'MARINO',
    'TECA 71': 'MARINO',
    'TECHIAKTLI 2': 'TERRESTRE',
    'TEEKIT 12': 'MARINO',
    'TENTOK 1 DEL': 'MARINO',
    'TENTOK 2': 'MARINO',
    'TENTOK 3': 'MARINO',
    'TENTOK 4': 'MARINO',
    'TLACAME 51 INY': 'MARINO',
    'TLAKATI 2': 'MARINO',
    'TLAKATI 3': 'MARINO',
    'TLALKIVAK 2': 'MARINO',
    'TLALKIVAK 4': 'MARINO',
    'TUPILCO 3004': 'TERRESTRE',
    'TUPILCO 3009': 'TERRESTRE',
    'TUPILCO 3010': 'TERRESTRE',
    'TUPILCO 3011': 'TERRESTRE',
    'TUPILCO 3011 VENTANA': 'TERRESTRE',
    'TUPILCO 3012': 'TERRESTRE',
    'TUPILCO 3012 VENTANA': 'TERRESTRE',
    'TUPILCO 3015': 'TERRESTRE',
    'TUPILCO 3016': 'TERRESTRE',
    'TUPILCO 3022': 'TERRESTRE',
    'VALERIANA 3': 'TERRESTRE',
    'XANAB 58': 'MARINO',
    'XANAB 58A': 'MARINO'
}

estado_de_pozos = {
    'ACTUL 3': 'ENTREGADO',
    'ACTUL 4': 'PERFORANDO',
    'ACTUL 5': 'PERFORANDO',
    'AKAL 503': 'ENTREGADO',
    'AKAL 504': 'ENTREGADO',
    'ATOYATL 1 DEL': 'ENTREGADO',
    'ATOYATL 2': 'ENTREGADO',
    'ATOYATL 3': 'ENTREGADO',
    'ATOYATL 3 RME': 'ENTREGADO',
    'BAKTE 1 DEL': 'PERFORANDO',
    'BAKTE 2': 'PERFORANDO',
    'BAKTE 3': 'PERFORANDO',
    'BAKTE 6': 'PERFORANDO',
    'BAKTE 7': 'PERFORANDO',
    'CAMATL 2': 'ENTREGADO',
    'CAMATL 4': 'ENTREGADO',
    'CAMATL 5': 'ENTREGADO',
    'CAMATL 51': 'ENTREGADO',
    'CHUCOX 102': 'ENTREGADO',
    'CHUCOX 108': 'PERFORANDO',
    'CIBIX 3': 'PERFORANDO',
    'CIBIX 32': 'ENTREGADO',
    'CIBIX 34': 'ENTREGADO',
    'CIBIX 35': 'PERFORANDO',
    'CIBIX 36': 'ENTREGADO',
    'CIBIX 37': 'ENTREGADO',
    'CIBIX 40': 'ENTREGADO',
    'CIBIX 5': 'ENTREGADO',
    'ETKAL 2DES': 'PERFORANDO',
    'ETKAL 5ADES': 'PERFORANDO',
    'ETKAL NE 202': 'PERFORANDO',
    'ITTA 69': 'ENTREGADO',
    'ITTA 87': 'ENTREGADO',
    'ITTA 88': 'ENTREGADO',
    'ITTA 89': 'ENTREGADO',
    'IXACHI 26': 'PERFORANDO',
    'IXACHI 27': 'ENTREGADO',
    'IXACHI 31': 'ENTREGADO',
    'IXACHI 32': 'PERFORANDO',
    'IXACHI 54': 'PERFORANDO',
    'IXACHI 60': 'PERFORANDO',
    'IXACHI 89': 'ENTREGADO',
    'MADREFIL 101-EXP': 'ENTREGADO',
    'MADREFIL 201-EXP': 'ENTREGADO',
    'MABALNAK 1EXP': 'PERFORANDO',
    'MULACH 12': 'ENTREGADO',
    'MULACH 13': 'ENTREGADO',
    'MULACH 14': 'ENTREGADO',
    'MULACH 14 VENTANA': 'ENTREGADO',
    'MULACH 15': 'ENTREGADO',
    'MULACH 16': 'ENTREGADO',
    'MULACH 23': 'ENTREGADO',
    'MULACH 31 INY': 'ENTREGADO',
    'MULACH 32 INY': 'ENTREGADO',
    'MULACH 32 VENTANA': 'ENTREGADO',
    'NANIK 1 EXP': 'PERFORANDO',
    'PLATAO 2': 'PERFORANDO',
    'PLATAO 3': 'PERFORANDO',
    'PLATAO 4': 'PERFORANDO',
    'POKCHE 102': 'ENTREGADO',
    'POKCHE 103': 'ENTREGADO',
    'POKCHE 104': 'ENTREGADO',
    'POKCHE 15': 'ENTREGADO',
    'QUESQUI 181': 'PERFORANDO',
    'QUESQUI 28': 'TERMINACION',
    'QUESQUI 35': 'ENTREGADO',
    'QUESQUI 405': 'PERFORANDO',
    'QUESQUI 418': 'PERFORANDO',
    'QUESQUI 420': 'ENTREGADO',
    'RACEMOSA 4': 'ENTREGADO',
    'RACEMOSA 4 VENTANA': 'REPARACION MENOR',
    'TECA 43': 'ENTREGADO',
    'TECA 51': 'ENTREGADO',
    'TECA 71': 'ENTREGADO',
    'TECHIAKTLI 2': 'PERFORANDO',
    'TEEKIT 12': 'ENTREGADO',
    'TENTOK 1 DEL': 'PERFORANDO',
    'TENTOK 2': 'ENTREGADO',
    'TENTOK 3': 'ENTREGADO',
    'TENTOK 4': 'ENTREGADO',
    'TLACAME 51 INY': 'ENTREGADO',
    'TLAKATI 2': 'ENTREGADO',
    'TLAKATI 3': 'ENTREGADO',
    'TLALKIVAK 2': 'PERFORANDO',
    'TLALKIVAK 4': 'PERFORANDO',
    'TUPILCO 3004': 'ENTREGADO',
    'TUPILCO 3009': 'ENTREGADO',
    'TUPILCO 3010': 'ENTREGADO',
    'TUPILCO 3011': 'ENTREGADO',
    'TUPILCO 3011 VENTANA': 'REPARACION MAYOR',
    'TUPILCO 3012': 'PERFORANDO',
    'TUPILCO 3012 VENTANA': 'REPARACION MAYOR',
    'TUPILCO 3015': 'PERFORANDO',
    'TUPILCO 3016': 'ENTREGADO',
    'TUPILCO 3022': 'PERFORANDO',
    'VALERIANA 3': 'PERFORANDO',
    'XANAB 58': 'PERFORANDO',
    'XANAB 58A': 'PERFORANDO',
}

etapas = {
    "10 58 x 12 14": "10 5/8\" X 12 1/4\"",
    "12  14": "12 1/4\"",
    "12 14": "12 1/4\"",
    "12 14 x 13 12": "12 1/4\" X 13 1/2\"",
    "12 14 x 14 12": "12 1/4\" X 14 1/2\"",
    "12 14 x 14 34": "12 1/4\" X 14 3/4\"",
    "12 14”": "12 1/4\"",
    "12 ¼”": "12 1/4\"",
    "12.250in": "12 1/4\"",
    "14  12": "14 1/2\"",
    "14 12": "14 1/2\"",
    "14 12 x 16": "14 1/2\" X 16\"",
    "14 12 x 16 12": "14 1/2\" X 16 1/2\"",
    "16": "16\"",
    "16in": "16\"",
    "16”": "16\"",
    "17 12": "17 1/2\"",
    "17 12”": "17 1/2\"",
    "18 12": "18 1/2\"",
    "18 12”": "18 1/2\"",
    "18 14": "18 1/4\"",
    "18 14”": "18 1/4\"",
    "26": "26\"",
    "26in": "26\"",
    "36": "36\"",
    "36”": "36\"",
    "4": "4\"",
    "4 18": "4 1/8\"",
    "4 8": "4 1/8\"",
    "5 58": "5 5/8\"",
    "5 78": "5 7/8\"",
    "6 12": "6 1/2\"",
    "6 18": "6 1/8\"",
    "6.50in": "6 1/2\"",
    "8 12": "8 1/2\"",
    "8 12 - LN 7": "8 1/2\"",
    "8 12 ventana": "8 1/2\" Ventana",
    "8 12- LN 7": "8 1/2\"",
    "8 12”": "8 1/2\"",
    "8.50in": "8 1/2\"",
    "8 12”": "8 1/2\"",
    "14 12 x 16": "14 1/2\" x 16\"",
    "36": "36\"",
    "5 78": "5 7/8\"",
    "12 14 x 14 34": "12 1/4\" x 14 3/4\"",
    "12 14”": "12 1/4\"",
    "8 12 ventana": "8 1/2\" Ventana",
    "12 ¼”": "12 1/4\"",
    "Desconocido": "Terminación",
    "Terminacion": "Terminacion",
    "Terminación": "Terminacion"
}

etapa_tr_mapping = {
'36"':'30"',
'26"':'20"',
'18 1/2"':'16"',
'18 1/4"':'16"',
'17 1/2"':'16"',
'17 1/2" ST':'16"',
'16"': '13 3/8"',
'14 1/2" X 16"': '13 3/8"',
'12 1/4" X 14 3/4"': '13 3/8"',
'12 1/4" X 14 1/2"': '13 3/8"',
'12 1/4"': '9 7/8"',
'10 5/8" X 12 1/4"': '9 7/8"',
'10 5/8"': '9 7/8"',
'8 1/2"': '7"',
'6 1/2"': '5"'
}

armado_bha_mapping = {
1: 4, 
2: 6.5, 
3: 6, 
4: 7, 
5: 8.5, 
6: 3.5, 
7: 4.5, 
8: 10.5
}

desarmado_bha_mapping = {
1: 3, 
2: 5, 
3: 4.5, 
4: 5.5, 
5: 6.5, 
6: 2.5, 
7: 2.5, 
8: 7.5
}

casing_conexion_std = {
'30"': 8,
'20"': 5.5,
'16"': 5,
'13 3/8"': 4.5,
'9 7/8"': 4,
'7"': 4,
'5"': 4
}

casing_velocidad_std = {
    'Tr 20"': 110,
    'Tr 16"': 112,
    'Liner/tr 13 3/8" txt': 120,
    'Liner/tr 9 7/8" txt': 140,
    'Liner/tr 9 5/8" txt': 140,
    'Liner/tr 11 3/4" txt': 140,
    'Liner 11 3/4" lingadas': 242,
    'Liner 7 3/4" txt': 140,
    'Liner 7 3/4" lingadas': 242,
    'Liner 7" txt': 140,
    'Liner 7" lingadas': 242,
    'Liner 5 1/2" txt': 140,
    'Liner 5 1/2" lingadas': 242,
    'Liner 5" txt': 140,
    'Liner 5" lingadas': 242
}

# casing_velocidad_std = {
# '30"': 48,
# '20"': 110,
# '16"': 112,
# '13 3/8"': 120,
# '9 7/8"': 140,
# '7"': 140,
# '5"': 140
# }