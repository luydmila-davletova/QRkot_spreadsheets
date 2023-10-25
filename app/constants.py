MAX_CHARITY_PROJECT_NAME = 100
MIN_CHARITY_PROJECT_NAME_DESCRIPTION = 1
REPRESENTATION_STR_LENGTH = 20
ZERO_INVESTMENT = 0

DEFAULT_DB_URL = 'sqlite+aiosqlite:///./QRKot.db'
DEFAULT_TITLE = 'Сервис QRKot'
DEFAULT_SECRET = 'SECRET'

DATE_FORMAT_FOR_SHEETS = "%Y/%m/%d %H:%M:%S"

SHEETS_BODY = {
    'properties': {'title': '', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 100,
                                                  'columnCount': 5}}}]
}
