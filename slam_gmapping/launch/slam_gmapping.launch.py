from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    rviz2_config = os.path.join(
      get_package_share_directory('slam_gmapping'),
      'rviz',
      'gmapping.rviz'
    )

    rviz2_node = Node(
      package='rviz2',
      executable='rviz2',
      name='rviz2_gmapping',
      arguments=['-d', rviz2_config],
      output='screen'
    )

    slam_gmapping_node = Node(
        package='slam_gmapping',
        executable='slam_gmapping',
        name='slam_gmapping',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}]
    )

    ld = LaunchDescription([
        SetEnvironmentVariable('RCUTILS_LOGGING_BUFFERED_STREAM', '1'),
        rviz2_node,
        slam_gmapping_node,
    ])

    return ld
