from setuptools import setup
from glob import glob


package_name = 'jmu_turtlebot3_bringup'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch/',  glob('launch/*.launch.py')),
        ('share/' + package_name + '/param/',  glob('param/*.yaml')),
        ('share/' + package_name + '/rviz/',  glob('rviz/*.rviz'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='spragunr',
    maintainer_email='nathan.r.sprague@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'safe_cmd_vel = jmu_turtlebot3_bringup.safe_cmd_vel:main'
        ],
    },
)
