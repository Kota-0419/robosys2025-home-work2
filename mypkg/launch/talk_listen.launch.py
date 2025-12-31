import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    sensor = launch_ros.actions.Node(
        package='mypkg',
        executable='sensor',
    )
    monitor = launch_ros.actions.Node(
        package='mypkg',
        executable='monitor',
    )

    return launch.LaunchDescription([
        sensor,
        monitor,
    ])
