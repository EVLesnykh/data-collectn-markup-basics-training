from clickhouse_driver import Client
import json

# Подключение к серверу ClickHouse
client = Client('localhost')

# Создание базы данных (если она не существует)
client.execute('CREATE DATABASE IF NOT EXISTS town_cary')

# Создание таблицы
# Создание основной таблицы 'crashes'
client.execute('''
CREATE TABLE IF NOT EXISTS town_cary.crashes (
    id UInt64,
    location_description String,
    rdfeature String,
    rdsurface String,
    rdcondition String,
    lightcond String,
    weather String,
    crash_date Int64,
    year String,
    fatalities String,
    injuries String,
    month String
) ENGINE = MergeTree()
ORDER BY id
''')

print("Таблица создана успешно.")

with open('crash-data.json', 'r') as file:
    data = json.load(file)

data = data['features']

# Вставка данных в таблицу
for feature in data:
    properties = feature['properties']

    # Определение crash_id
    crash_id = properties['tamainid']

    # Вставка данных о ДТП
    client.execute("""
    INSERT INTO town_cary.crashes (
        id, location_description, rdfeature,
        rdsurface, rdcondition, lightcond,
        weather, crash_date, year,
        fatalities, injuries, month
    ) VALUES""",
    [(crash_id,
      properties['location_description'] or "",
      properties['rdfeature'] or "",
      properties['rdsurface'] or "",
      properties['rdcondition'] or "",
      properties['lightcond'] or "",
      properties['weather'] or "",
      properties['crash_date'],
      properties['year'],
      properties['fatalities'] or "",
      properties['injuries'] or "",
      properties['month'])])

print("Данные введены успешно.")

# Проверка успешности вставки
result = client.execute("SELECT * FROM town_cary.crashes")
print("Вставленная запись:", result[0])