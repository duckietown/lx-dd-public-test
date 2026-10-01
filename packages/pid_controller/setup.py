from setuptools import find_packages, setup


package_name = 'pid_controller'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='LX Sync Test',
    maintainer_email='sync@example.invalid',
    description='Mock controller package for LX sync testing',
    license='Unspecified',
    entry_points={'console_scripts': ['mock_altitude_node = pid_controller.pid_controller_node:main']},
)