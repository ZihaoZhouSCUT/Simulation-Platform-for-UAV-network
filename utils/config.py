import logging

# --------------------- simulation parameters --------------------- #
MAP_LENGTH = 1000  # m, length of the map
MAP_WIDTH = 1000  # m, width of the map
MAP_HEIGHT = 120  # m, height of the map
SIM_TIME = 30 * 1e6  # us, total simulation time (10s)
NUMBER_OF_DRONES = 20  # number of drones in the network
STATIC_CASE = 0
LOGGING_LEVEL = logging.ERROR

# ---------- hardware parameters of drone (rotary-wing) -----------#
PROFILE_DRAG_COEFFICIENT = 0.012
AIR_DENSITY = 1.225  # kg/m^3
ROTOR_SOLIDITY = 0.05  # defined as the ratio of the total blade area to disc area
ROTOR_DISC_AREA = 0.79  # m^2
BLADE_ANGULAR_VELOCITY = 400  # radians/second
ROTOR_RADIUS = 0.5  # m
INCREMENTAL_CORRECTION_FACTOR = 0.1
AIRCRAFT_WEIGHT = 100  # Newton
ROTOR_BLADE_TIP_SPEED = 500
MEAN_ROTOR_VELOCITY = 7.2  # mean rotor induced velocity in hover
FUSELAGE_DRAG_RATIO = 0.3

# ----------------------- radio parameters ----------------------- #
TRANSMITTING_POWER = 1  # Watt
LIGHT_SPEED = 3*1e8  # light speed (m/s)
CARRIER_FREQUENCY = 1*1e9  # carrier frequency (Hz)
NOISE_POWER = 4*1e-9  # noise power (Watt)
RADIO_SWITCHING_TIME = 100  # us, the switching time of the transceiver mode
SNR_THRESHOLD = 4  # dB
RADIO_SENSITIVITY = 1e-10  # power under which signal is not sensed

# ---------------------- packet parameters ----------------------- #
MAX_TTL = 15
PACKET_LIFETIME = 10*1e6
PACKET_HEADER_LENGTH = 128  # bit
DATA_PACKET_PAYLOAD_LENGTH = 1024*8  # bit
DATA_PACKET_LENGTH = PACKET_HEADER_LENGTH + DATA_PACKET_PAYLOAD_LENGTH

ACK_PACKET_LENGTH = 128  # bit

HELLO_PACKET_HEADER_LENGTH = 128  # bit
HELLO_PACKET_PAYLOAD_LENGTH = 256  # bit
HELLO_PACKET_LENGTH = HELLO_PACKET_HEADER_LENGTH + HELLO_PACKET_PAYLOAD_LENGTH

# ------------------ physical layer parameters ------------------- #
BIT_RATE = 54 * 1e6  # 54 Mbit/s, 802.11g 20 MHz channels
BIT_TRANSMISSION_TIME = 1/BIT_RATE * 1e6
NOISE_FLOOR = 1e-9
COMMUNICATION_RANGE = 250
SENSING_RANGE = 300

# --------------------- mac layer parameters --------------------- #
SLOT_DURATION = 50  # 50 microseconds, 802.11g 2.4 GHz
SIFS_DURATION = 28  # 28 microseconds, 802.11g 2.4 GHz
DIFS_DURATION = SIFS_DURATION + (2 * SLOT_DURATION)  # 128 microseconds
MAC_HEADER_LENGTH = 34*8  # 34 byte fixed fields of a mac packet
MAX_MAC_PAYLOAD_LENGTH = 2312*8
ACK_LENGTH = MAC_HEADER_LENGTH
CW_MIN = 16
CW_MAX = 1024
ACK_TIMEOUT = 1000  # maximum waiting time for ACK (0.1s)
MAX_RETRANSMISSION_ATTEMPT = 5

