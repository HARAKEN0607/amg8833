import subprocess
import os

raspi_folder = os.getcwd()

# print(raspi_folder)

folder_name = 'cubic_thermal'



subprocess.run('rclone sync ' + raspi_folder + '/' + folder_name + ' gcs:' + 'smart_security/' + folder_name, shell=True)


print('finished')

