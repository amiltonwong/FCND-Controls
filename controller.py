"""
PID Controller

components:
    follow attitude commands
    gps commands and yaw
    waypoint following
"""
import numpy as np

class NonlinearController(object):

    def __init__(self):
        pass    
    
    def trajectory_control(self,position_trajectory,yaw_trajectory,time_trajectory,current_time):
        """Generate a commanded position, velocity and yaw based on the trajectory
        
        Args:
            position_trajectory: list of 3-element numpy arrays, NED positions
            yaw_trajectory: list yaw commands in radians
            time_trajectory: list of times (in seconds) that correspond to the position and yaw commands
            current_time: float corresponding to the current time in seconds
            
        Returns: tuple (commanded position, commanded velocity, commanded yaw)
                
        """
        pass
    
    def position_control(self, local_position_cmd, local_velocity_cmd, local_position, local_velocity,
                               acceleration_ff = np.array([0.0,0.0])):
        """Generate horizontal acceleration commands for the vehicle in the local frame

        Args:
            local_position_cmd: desired 2D position in local frame [north, east]
            local_velocity_cmd: desired 2D velocity in local frame [north_velocity, east_velocity]
            local_position: vehicle position in the local frame [north, east]
            local_velocity: vehicle velocity in the local frame [north_velocity, east_velocity]
            acceleration_cmd: feedforward acceleration command
            
        Returns: desired vehicle 2D acceleration in the local frame [north, east]
        """
        pass
    
    def altitude_control(self,altitude_cmd,vertical_velocity_cmd,altitude,vertical_velocity,attitude,acceleration_ff=0.0):
        """Generate vertical acceleration (thrust) command

        Args:
            altitude_cmd: desired vertical position (+up)
            vertical_velocity_cmd: desired vertical velocity (+up)
            altitude: vehicle vertical position (+up)
            vertical_velocity: vehicle vertical velocity (+up)
            acceleration_ff: feedforward acceleration command (+up)
            
        Returns: 2-element numpy array, desired vehicle 2D acceleration in the local frame [north, east]
        """
        
        pass
    
    def roll_pitch_controller(self,acceleration_cmd,attitude,thrust_cmd):
        """ Generate the rollrate and pitchrate commands in the body frame
        
        Args:
            target_acceleration: 2-element numpy array (north_acceleration_cmd,east_acceleration_cmd) in m/s^2
            attitude: 3-element numpy array (roll,pitch,yaw) in radians
            thrust_cmd: vehicle thruts command in Newton
            
        Returns: 2-element numpy array, desired rollrate (p) and pitchrate (q) commands in radians/s
        """
        pass
    
    def body_rate_control(self,body_rate_cmd,body_rate):
        """ Generate the roll, pitch, yaw moment commands in the body frame
        
        Args:
            body_rate_cmd: 3-element numpy array (p_cmd,q_cmd,r_cmd) in radians/second^2
            attitude: 3-element numpy array (p,q,r) in radians/second^2
            
        Returns: 3-element numpy array, desired roll moment, pitch moment, and yaw moment commands in Newtons*meters
        """
        pass
    
    def yaw_control(self,yaw_cmd,yaw):
        """ Generate the target yawrate
        
        Args:
            yaw_cmd: desired vehicle yaw in radians
            yaw: vehicle yaw in radians
        
        Returns: target yawrate in radians/sec
        """
        pass
    
