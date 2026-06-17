import os
_base = os.path.join(os.path.expanduser('~' + os.environ.get('SUDO_USER', '')), 'mse112-ws-student', 'MasterPi','CameraCalibration')

#The actual distance between two adjacent corner points, in cm
corners_length = 2.1

#The side length of the wooden block is 3cm
square_length = 3

#Calibrate chessboard size, columns, rows, refers to the number of inner corner points, not chessboard
calibration_size = (7, 7)

#Collect the calibration image storage path
save_path = os.path.join(_base, 'calibration_images') + '/'

#Calibration parameter storage path
calibration_param_path = os.path.join(_base, 'calibration_param')

#Mapping parameter storage path
map_param_path = os.path.join(_base, 'map_param')
