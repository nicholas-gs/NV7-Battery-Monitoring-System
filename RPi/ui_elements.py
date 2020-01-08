# 2D array to keep track if a temperature sensor is working -- change value to 'False' if not working
# If True --> Temperature sensor is working
# Arranged in the 2D array according to [moduleID][SensorID]

# IMPORTANT:

# Modules are numbered -- 0,1,2,4,5,6. But can't tell which module ID corresponds to which physical module


class ValidTemps:

    validSensors = [[True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True],  # Module 0

                    [True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True],  # Module 1

                    [True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True],  # Module 2

                    [True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True],  # Module NULL

                    [True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True],  # Module 4

                    [True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True],  # Module 5

                    [True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True, True, True, True, True, True, True, True, True,
                     True, True]  # Module 6
                    ]
