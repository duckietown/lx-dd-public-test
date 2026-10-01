from setuptools import find_packages, setup


package_name = 'solution'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    package_data={'solution': ['z_pid.yaml']},
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='LX Sync Test',
    maintainer_email='sync@example.invalid',
    description='Mock learner package for LX sync testing',
    license='Unspecified',
)