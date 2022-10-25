import html_creater as hc
import xml_generator as xg
import data_provider as dp
import logger as log

# print(hc.create())
# print(xg.create())

hc.new_create(xg.new_create(dp.data_collection()))
log.temperature_logger(dp.get_temperature(-1))
log.pressure_logger(dp.get_preassure(-1))
log.wind_speed_logger(dp.get_wind_speed(-1))