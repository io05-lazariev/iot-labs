from csv import reader
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.parking import Parking
from domain.aggregated_data import AggregatedData
import config


class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
        parking_filename: str,
    ) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        self.parking_filename = parking_filename
        with open(self.accelerometer_filename) as file:
            lines = [line.rstrip() for line in file]
            lines = lines[1:]
            self.accelerometer_lines = lines
        with open(self.gps_filename) as file:
            lines = [line.rstrip() for line in file]
            lines = lines[1:]
            self.gps_lines = lines
        with open(self.parking_filename) as file:
            lines = [line.rstrip() for line in file]
            lines = lines[1:]
            self.parking_lines = lines

    def read(self) -> AggregatedData:
        """Метод повертає дані отримані з датчиків"""
        data = AggregatedData(
            Accelerometer(1, 2, 3),
            Gps(4, 5),
            Parking(25, Gps(4, 5)),
            datetime.now(),
            config.USER_ID,
        )
        
        if self.is_being_read == True:
            if (self.accelerometer_line_n > len(self.accelerometer_lines) - 1):
                self.accelerometer_line_n = 0
                
            if (self.gps_line_n > len(self.gps_lines) - 1):
                self.gps_line_n = 0
            
            if (self.parking_line_n > len(self.parking_lines) - 1):
                self.parking_line_n = 0

            acceleration = self.accelerometer_lines[self.accelerometer_line_n].split(',')
            gps = self.gps_lines[self.gps_line_n].split(',')
            parking = self.parking_lines[self.parking_line_n].split(',')
            
            x, y, z = acceleration
            data.accelerometer = Accelerometer(x, y, z)
            
            lat, long = gps
            data.gps = Gps(long, lat)
            
            long, lat, empty_count = parking
            data.parking = Parking(empty_count, Gps(long, lat))
            
            self.accelerometer_line_n += 1
            self.gps_line_n += 1
            self.parking_line_n +=1
        
        return data

    def startReading(self, *args, **kwargs):
        """Метод повинен викликатись перед початком читання даних"""
        self.is_being_read = True
        self.accelerometer_line_n = 0
        self.gps_line_n = 0
        self.parking_line_n = 0

    def stopReading(self, *args, **kwargs):
        """Метод повинен викликатись для закінчення читання даних"""
        self.is_being_read = False
