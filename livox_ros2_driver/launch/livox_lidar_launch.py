from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterFile

configpath = PathJoinSubstitution([
                    FindPackageShare('livox_ros2_driver'),
                    "config",
                    "config.yaml"
                ])

file_params_arg = DeclareLaunchArgument(
        'params_file',
        default_value=configpath,
        description='Full path to the ROS2 parameters file to use.',
    )

def generate_launch_description():
      
    livox_driver = Node(
        package='livox_ros2_driver',
        executable='livox_ros2_driver_node',
        name='livox_lidar_publisher',
        output='screen',
        parameters=[ParameterFile(LaunchConfiguration('params_file'), allow_substs=True)]
        )

    return LaunchDescription([
        file_params_arg,
        livox_driver
    ])
