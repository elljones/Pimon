"""Constants for SSD1608 driver IC."""
DRIVER_CONTROL = 0x01
GATE_VOLTAGE = 0x03
SOURCE_VOLTAGE = 0x04
DISPLAY_CONTROL = 0x07
NON_OVERLAP = 0x0B
BOOSTER_SOFT_START = 0x0C
GATE_SCAN_START = 0x0F
DEEP_SLEEP = 0x10
DATA_MODE = 0x11
SW_RESET = 0x12
TEMP_WRITE = 0x1A
TEMP_READ = 0x1B
TEMP_CONTROL = 0x18
TEMP_LOAD = 0x1A
MASTER_ACTIVATE = 0x20
DISP_CTRL1 = 0x21
DISP_CTRL2 = 0x22
WRITE_RAM = 0x24
WRITE_ALTRAM = 0x26
READ_RAM = 0x25
VCOM_SENSE = 0x2B
VCOM_DURATION = 0x2C
WRITE_VCOM = 0x2C
READ_OTP = 0x2D
WRITE_LUT = 0x32
WRITE_DUMMY = 0x3A
WRITE_GATELINE = 0x3B
WRITE_BORDER = 0x3C
SET_RAMXPOS = 0x44
SET_RAMYPOS = 0x45
SET_RAMXCOUNT = 0x4E
SET_RAMYCOUNT = 0x4F
NOP = 0xFF
